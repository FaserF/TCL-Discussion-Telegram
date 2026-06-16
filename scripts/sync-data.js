import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');

const CHIPSET_MD_PATH = path.join(rootDir, 'docs', 'chipsets.md');
const FAQ_MD_PATH = path.join(rootDir, 'docs', 'faq.md');

const CHIPSETS_JSON_PATH = path.join(rootDir, 'src', 'data', 'chipsets.json');
const FAQS_JSON_PATH = path.join(rootDir, 'src', 'data', 'faqs.json');
const SEARCH_DATA_JS_PATH = path.join(rootDir, 'src', 'data', 'searchData.js');

function parseChipsets() {
    console.log('📖 Parsing chipsets.md...');
    const content = fs.readFileSync(CHIPSET_MD_PATH, 'utf8').replace(/\r/g, '');
    const lines = content.split('\n');
    const chipsets = [];

    let insideTable = false;

    for (const line of lines) {
        if (line.includes('| Platform Family | Specific IDs |')) {
            insideTable = true;
            continue;
        }

        if (insideTable) {
            if (line.trim() === '' || (!line.trim().startsWith('|') && !line.trim().startsWith('---'))) {
                insideTable = false;
                continue;
            }

            const parts = line.split('|').map(p => p.trim());
            if (parts.length >= 5 && parts[1] && !parts[1].startsWith(':') && !parts[1].toLowerCase().includes('platform family') && !parts[1].startsWith('---')) {
                const family = parts[1].replace(/\*\*/g, '').trim();
                const ids = parts[2].trim();
                const models = parts[3].trim();
                const notes = parts[4].replace(/\*\*/g, '').trim();

                chipsets.push({
                    name: `${family} (${ids})`,
                    models: models || '—',
                    type: notes
                });
            }
        }
    }

    console.log(`✓ Found ${chipsets.length} chipset families.`);
    return chipsets;
}

function parseFaqs() {
    console.log('📖 Parsing faq.md...');
    const content = fs.readFileSync(FAQ_MD_PATH, 'utf8').replace(/\r/g, '');
    const lines = content.split('\n');
    const faqs = [];
    let currentFaq = null;

    for (const line of lines) {
        const questionMatch = line.match(/^\?\?\?\s+question\s+"([^"]+)"/);
        if (questionMatch) {
            if (currentFaq) {
                faqs.push({
                    q: currentFaq.q,
                    a: currentFaq.a.join('\n').trim()
                });
            }
            currentFaq = { q: questionMatch[1], a: [] };
        } else if (currentFaq) {
            if (line.startsWith('    ') || line.trim() === '') {
                currentFaq.a.push(line.replace(/^    /, ''));
            } else {
                faqs.push({
                    q: currentFaq.q,
                    a: currentFaq.a.join('\n').trim()
                });
                currentFaq = null;
            }
        }
    }

    if (currentFaq) {
        faqs.push({
            q: currentFaq.q,
            a: currentFaq.a.join('\n').trim()
        });
    }

    console.log(`✓ Found ${faqs.length} FAQ questions.`);
    return faqs;
}

function generateSearchData(chipsets, faqs) {
    console.log('✍ Generating searchData.js...');

    const searchItems = [];

    // Add parsed chipsets
    chipsets.forEach(c => {
        const id = c.name.toLowerCase().replace(/[^a-z0-9]/g, '-').replace(/-+/g, '-').replace(/^-|-$/g, '');
        searchItems.push({
            id,
            title: c.name,
            category: 'Chipset',
            content: `Featured Models: ${c.models}. Notes: ${c.type}.`,
            link: '/guides'
        });
    });

    // Add Troubleshooting static items (as these are custom styled in UI)
    const troubleshooting = [
        { id: 'verif-failed', title: 'Verification Failed', category: 'Error', content: 'Corrupted ZIP or incompatible USB filesystem. Re-format to FAT32 MBR.', link: '/faq' },
        { id: 'no-file', title: 'No File Found', category: 'Error', content: 'File hidden in folder or renamed incorrectly. Ensure root directory placement.', link: '/faq' },
        { id: 'stuck-logo', title: 'TV Stuck on Logo', category: 'Error', content: 'Soft-brick recovery. Use IMG/PKG method to force low-level format.', link: '/faq' }
    ];
    searchItems.push(...troubleshooting);

    // Add Guides static items
    const guides = [
        { id: 'ota-guide', title: 'OTA (Local Update)', category: 'Guide', content: 'Safe - Keeps Data. File: .zip. Trigger via TV Menu Update.', link: '/guides' },
        { id: 'img-guide', title: 'IMG / PKG (Flash)', category: 'Guide', content: 'Wipe - Factory Reset. File: .img/.pkg/.bin. Trigger via Power Button.', link: '/guides' },
        { id: 'usb-prep', title: 'USB Media Preparation', category: 'Guide', content: 'Format: FAT32. Root Directory only. Use USB 2.0 port for stability.', link: '/guides' }
    ];
    searchItems.push(...guides);

    // Add parsed FAQs
    faqs.forEach(faq => {
        const id = faq.q.toLowerCase().replace(/[^a-z0-9]/g, '-').replace(/-+/g, '-').replace(/^-|-$/g, '').substring(0, 30);
        
        // Clean markdown links and formatting cleanly
        const cleanContent = faq.a
            .replace(/\[([^\]]+)\]\([^\)]+\)/g, '$1') // Extract link text
            .replace(/[\*\`]/g, '')                   // Remove formatting
            .replace(/\s+/g, ' ')                     // Normalize spacing
            .trim();
            
        const truncated = cleanContent.length > 150 
            ? cleanContent.substring(0, 150) + '...' 
            : cleanContent;

        searchItems.push({
            id,
            title: faq.q,
            category: 'FAQ',
            content: truncated,
            link: '/faq'
        });
    });

    // Add static community/links
    const community = [
        { id: 'tg-group', title: 'Telegram Discussion Group', category: 'Community', content: 'Join 50k members for live help, chat, and support. Search terms: Telegram, Group, Chat, Help, Support.', link: 'https://t.me/tclupdates_discussion' },
        { id: 'tg-channel', title: 'Telegram Firmware Channel', category: 'Community', content: 'Official-source for new firmware releases and announcements. Search terms: Telegram, Channel, Feed, Updates.', link: 'https://t.me/tclupdates' },
        { id: 'tg-bot', title: '@FirmwareTCLbot (Telegram Bot)', category: 'Community', content: 'Request firmwares directly via the bot. Search terms: Telegram, Bot, Download, Firmware Bot.', link: 'https://t.me/FirmwareTCLbot' },
        { id: 'contribute-how', title: 'How to Contribute', category: 'Guide', content: 'Learn how to edit the site, add chipsets, and submit PRs.', link: '/contribute' },
        { id: 'local-dev', title: 'Local Development', category: 'Guide', content: 'Use dev.ps1 to start the site locally and test your changes.', link: '/contribute' }
    ];
    searchItems.push(...community);

    const outputContent = `// Automatically generated by scripts/sync-data.js
// Do not edit this file directly.

export const searchData = ${JSON.stringify(searchItems, null, 4)};
`;

    fs.writeFileSync(SEARCH_DATA_JS_PATH, outputContent, 'utf8');
}

function run() {
    console.log('🔄 Syncing Markdown Docs to React Web App Data...');
    try {
        const chipsets = parseChipsets();
        const faqs = parseFaqs();

        fs.writeFileSync(CHIPSETS_JSON_PATH, JSON.stringify(chipsets, null, 4), 'utf8');
        fs.writeFileSync(FAQS_JSON_PATH, JSON.stringify(faqs, null, 4), 'utf8');

        generateSearchData(chipsets, faqs);

        console.log('✨ Data Sync completed successfully!');
    } catch (error) {
        console.error('❌ Data Sync failed:', error);
        process.exit(1);
    }
}

run();
