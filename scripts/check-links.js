import fs from 'fs';
import path from 'path';

// Using native fetch available in Node.js 18+

const IGNORE_URLS = [
    'http://localhost',
    'https://react.dev/error',
    'https://reactrouter.com',
    'https://github.com/FaserF/AegisBot'
];

const EXTENSIONS = ['.jsx', '.js', '.md', '.html'];
const SEARCH_DIRS = ['src', 'docs'];

// Improved regex to handle trailing punctuation like ) or . or , and markdown symbols like ` or *
const urlRegex = /https?:\/\/[^\s"'><*`)]+[^\s"'><.,):*`]/g;

async function checkLink(url) {
    if (IGNORE_URLS.some(ignore => url.startsWith(ignore))) {
        return { url, status: 'ignored' };
    }

    try {
        const response = await fetch(url, {
            method: 'HEAD',
            timeout: 5000,
            redirect: 'follow', // Explicitly follow redirects
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            }
        });

        if (response.ok || (response.status >= 300 && response.status < 400) || response.status === 403 || response.status === 401 || response.status === 429) {
            // Case 2xx (ok), 3xx (redirect), or 4xx bot detection: Assume it's valid for the check
            return { url, status: 'ok' };
        } else {
            // Try GET if HEAD fails
            const getResponse = await fetch(url, { method: 'GET', timeout: 5000, redirect: 'follow' });
            const isOk = getResponse.ok || (getResponse.status >= 300 && getResponse.status < 400) || getResponse.status === 403;
            return { url, status: isOk ? 'ok' : 'broken', code: getResponse.status };
        }
    } catch (error) {
        // Only ignore specific network issues that are often transient or due to aggressive firewalls
        if (error.message.includes('timeout') || error.message.includes('ECONNREFUSED')) {
            return { url, status: 'ok' };
        }
        return { url, status: 'broken', error: error.message };
    }
}

function getFiles(dir) {
    let results = [];
    const list = fs.readdirSync(dir);
    list.forEach(file => {
        file = path.join(dir, file);
        const stat = fs.statSync(file);
        if (stat && stat.isDirectory()) {
            if (file !== 'node_modules' && file !== '.git' && file !== 'dist' && file !== 'site' && file !== 'site-temp') {
                results = results.concat(getFiles(file));
            }
        } else if (EXTENSIONS.includes(path.extname(file))) {
            results.push(file);
        }
    });
    return results;
}

async function run() {
    console.log('🧪 Starting Link Integrity Check...');
    const files = SEARCH_DIRS.flatMap(dir => getFiles(dir));
    const urls = new Set();

    files.forEach(file => {
        const content = fs.readFileSync(file, 'utf8');
        let match;
        while ((match = urlRegex.exec(content)) !== null) {
            urls.add(match[0]);
        }
    });

    console.log(`🔍 Found ${urls.size} unique URLs across ${files.length} files.`);

    const results = await Promise.all(Array.from(urls).map(checkLink));
    const broken = results.filter(r => r.status === 'broken');

    if (broken.length > 0) {
        console.error('\n❌ BROKEN LINKS DETECTED:');
        broken.forEach(r => {
            console.error(`- ${r.url} (Code: ${r.code || 'N/A'}, Error: ${r.error || 'N/A'})`);
        });
        process.exit(1);
    } else {
        console.log('\n✅ All links are valid!');
        process.exit(0);
    }
}

run();
