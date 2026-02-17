export const searchData = [
    // Chipsets
    { id: 'mt9615', title: 'MT9615 (T615T03)', category: 'Chipset', content: 'High-End Google TV, C735, C835, C935. Platform: V8-T615T03.', link: '/guides' },
    { id: 'rt51', title: 'RT51 (R51MT05)', category: 'Chipset', content: 'Google TV, C725, C825, P725. Platform: V8-R51MT05.', link: '/guides' },
    { id: 'nt72671', title: 'NT72671 (T615T01)', category: 'Chipset', content: 'Basic/Mid Google TV, P635, P735. Platform: V8-T615T01.', link: '/guides' },
    { id: 'mt5889', title: 'MT5889 (V8-T658T01)', category: 'Chipset', content: 'Legacy Android TV, P815, C715. Platform: V8-T658T01.', link: '/guides' },

    // Troubleshooting
    { id: 'verif-failed', title: 'Verification Failed', category: 'Error', content: 'Corrupted ZIP or incompatible USB filesystem. Re-format to FAT32 MBR.', link: '/faq' },
    { id: 'no-file', title: 'No File Found', category: 'Error', content: 'File hidden in folder or renamed incorrectly. Ensure root directory placement.', link: '/faq' },
    { id: 'stuck-logo', title: 'TV Stuck on Logo', category: 'Error', content: 'Soft-brick recovery. Use IMG/PKG method to force low-level format.', link: '/faq' },

    // Guides
    { id: 'ota-guide', title: 'OTA (Local Update)', category: 'Guide', content: 'Safe - Keeps Data. File: .zip. Trigger via TV Menu Update.', link: '/guides' },
    { id: 'img-guide', title: 'IMG / PKG (Flash)', category: 'Guide', content: 'Wipe - Factory Reset. File: .img/.pkg/.bin. Trigger via Power Button.', link: '/guides' },
    { id: 'usb-prep', title: 'USB Media Preparation', category: 'Guide', content: 'Format: FAT32. Root Directory only. Use USB 2.0 port for stability.', link: '/guides' },

    // General FAQ
    { id: 'lang-rule', title: 'Language (English)', category: 'FAQ', content: 'English only allows international experts to help. Common bridge for 100+ countries.', link: '/faq' },
    { id: 'bot-safety', title: '@FirmwareTCLbot', category: 'FAQ', content: 'Safe community tool. Identifies TV by Serial Number to prevent wrong chipset downloads.', link: '/faq' },
    { id: 'sn-lookup', title: 'Find Serial Number', category: 'FAQ', content: 'Check back sticker or Settings -> About -> Status.', link: '/faq' },
    { id: 'service-menu', title: 'Service Menu (6425)', category: 'FAQ', content: 'Code: 6425. Use for Panel ID checking and Shop Mode resets.', link: '/faq' },

    // Community & Telegram (New)
    { id: 'tg-group', title: 'Telegram Discussion Group', category: 'Community', content: 'Join 50k members for live help, chat, and support. Search terms: Telegram, Group, Chat, Help, Support.', link: 'https://t.me/tclupdates_discussion' },
    { id: 'tg-channel', title: 'Telegram Firmware Channel', category: 'Community', content: 'Official-source for new firmware releases and announcements. Search terms: Telegram, Channel, Feed, Updates.', link: 'https://t.me/tclupdates' },
    { id: 'tg-bot', title: '@FirmwareTCLbot (Telegram Bot)', category: 'Community', content: 'Request firmwares directly via the bot. Search terms: Telegram, Bot, Download, Firmware Bot.', link: 'https://t.me/FirmwareTCLbot' },

    // Contribution
    { id: 'contribute-how', title: 'How to Contribute', category: 'Guide', content: 'Learn how to edit the site, add chipsets, and submit PRs.', link: '/contribute' },
    { id: 'local-dev', title: 'Local Development', category: 'Guide', content: 'Use dev.ps1 to start the site locally and test your changes.', link: '/contribute' },
];
