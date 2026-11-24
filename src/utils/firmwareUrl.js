const OFFICIAL_CDN_EXACT_HOSTS = new Set([
    'update.cedock.com',
    'celesw.tcl.com',
    'file-fota-tv.api.leiniao.com',
]);

const OFFICIAL_CDN_SUFFIXES = ['.cedock.com', '.api.leiniao.com'];

const FW_FILENAME_RE = /^(V8-([A-Z0-9]+)-[A-Z0-9]+)(?:\.(\d{4,8}))?(?:_(PKG|IMG))?\.(zip|pkg|img|bin)$/i;
const LEINIAO_PATH_RE = /^\/(\d{4})\/(\d{2})\/(\d{2})\/(full|inc|incr|diff|ota|pkg|img)\/[0-9a-fA-F]+\/[0-9a-fA-F]+\//i;

export const CN_KNOWN_MODELS = [
    {
        platform: 'T653T11',
        model: 'FF-CN-MT9653-R675C (R675C)',
        codename: 'tcl_mt5879_cn',
        projectId: '12061',
        region: 'CN',
        latestVersion: 'V8-T653T11-LF1V751',
        downloadUrl: 'https://file-fota-tv.api.leiniao.com/2026/10/12/full/ab/d61e1b75fb/V8-T653T11-LF1V751.zip',
    },
];

export function isOfficialCdnHost(host) {
    const clean = (host || '').trim().toLowerCase().split(':')[0];
    if (!clean) return false;
    if (OFFICIAL_CDN_EXACT_HOSTS.has(clean)) return true;
    return OFFICIAL_CDN_SUFFIXES.some((sfx) => clean.endsWith(sfx));
}

export function parseFirmwareUrl(rawUrl) {
    const trimmed = (rawUrl || '').trim();
    if (!trimmed) return null;

    let parsed;
    try {
        parsed = new URL(trimmed);
    } catch {
        return null;
    }

    if (parsed.protocol !== 'http:' && parsed.protocol !== 'https:') {
        return null;
    }
    if (!isOfficialCdnHost(parsed.hostname)) {
        return null;
    }

    const host = parsed.hostname.toLowerCase();
    const filename = parsed.pathname.split('/').pop() || '';
    const match = FW_FILENAME_RE.exec(filename);
    if (!match) {
        return null;
    }

    const version = match[1].toUpperCase();
    const platform = match[2].toUpperCase();
    const buildNumber = match[3] || '';
    const pkgTag = (match[4] || '').toUpperCase();
    const ext = match[5].toLowerCase();

    let region = 'EU';
    let releaseDate = '—';
    let releaseType = ext === 'pkg' || ext === 'img' || ext === 'bin' || pkgTag
        ? 'IMG / PKG Recovery'
        : 'Full OTA (ZIP)';

    if (host.endsWith('.api.leiniao.com')) {
        region = 'CN';
        const cnMatch = LEINIAO_PATH_RE.exec(parsed.pathname);
        if (cnMatch) {
            releaseDate = `${cnMatch[1]}-${cnMatch[2]}-${cnMatch[3]}`;
            const kind = cnMatch[4].toLowerCase();
            if (kind === 'inc' || kind === 'incr' || kind === 'diff') {
                releaseType = 'Incremental OTA';
            } else if (kind === 'pkg' || kind === 'img') {
                releaseType = 'IMG / PKG Recovery';
            }
        }
    } else if (host.startsWith('na-') || host.startsWith('na.')) {
        region = 'NA';
    } else if (host.startsWith('as-') || host.startsWith('as.')) {
        region = 'AS';
    }

    return {
        url: parsed.href,
        host,
        region,
        platform,
        version,
        buildNumber,
        filename,
        releaseDate,
        releaseType,
    };
}
