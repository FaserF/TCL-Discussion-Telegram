# Administration Guide

This page is for community administrators and moderators. It explains how to manage the dynamic parts of the TCL Firmware Hub, such as the announcement banner.

## :material-bullhorn: Managing the Announcement Banner

We use a GitHub Actions workflow to update the news banner without touching the code. This ensures even non-developers can push critical updates.

### 1. Triggering the Update

1.  Go to the **[GitHub Actions Tab](https://github.com/FaserF/TCL-Discussion-Telegram/actions/workflows/update-news.yml)**.

2.  Click the **"Run workflow"** button on the right.

3.  Fill in the fields:
    *   **Show Banner?**: Uncheck to hide the banner.
    *   **Banner Text**: The message to display. (e.g., "New V562 Firmware is out!")
    *   **Link URL**: Optional. Link to the Telegram post or download.
    *   **Date Override**: Use `YYYY-MM-DD` if you want to push a message with a specific timestamp.

### 2. How it works

- When you click "Run", the workflow updates `docs/assets/news.json`.

- The website fetches this file instantly for every visitor.

- **Persistence:** If a user clicks "Close" on the banner, they won't see it again until you change the **Date**. The modern `banner.js` uses `localStorage` to remember the dismissal status based on the date string.

---

## :material-database-edit: Maintaining Chipsets

If a new TV model or chipset is released:

1.  Open `docs/chipsets.md` in the GitHub editor.

2.  Add the new entry to the **Mapping Table**.

3.  Commit the changes. The site will rebuild automatically in ~2 minutes.

---

## :material-security: Safety & Community Reports

- **Scam Alerts:** If a new Telegram scam and targeting the group is reported, use the **Banner** (see above) to push a warning immediately.
- **Broken Links:** If the `@FirmwareTCLbot` is down or links are broken, update the banner to inform users while the dev team works on a fix.

---

## :material-robot-confused: Rose Bot Administration

The **Rose Bot** (@MissRose_bot) is our primary automation tool for moderation, filters, and welcome messages. This section explains how admins can interact with and configure the bot.

### 1. Connecting to the Bot
To manage group settings privately or via the web dashboard, you must first connect your account:

1.  **Start the Bot:** Message [@MissRose_bot](https://t.me/MissRose_bot) and press `/start`.
2.  **Request Connection:** In the **TCL Discussion Group**, type `/connect`.
3.  **Confirm:** Rose will send you a PM with a button to confirm the connection. Once connected, you can send commands to her PM instead of the group, keeping the chat clean.

### 2. Management via Web Dashboard
For complex tasks like editing rules or configuring advanced settings, we recommend the web interface:

- **Dashboard Link:** [missrose.org/dashboard](https://missrose.org/dashboard/)
- **Setup:** After logging in with Telegram, select the TCL Discussion Group from your list.

### 3. Core Admin Commands
While most things are in the dashboard, you can use these common commands in the group (or PM if connected):

| Command | Purpose | Official Guide |
| :--- | :--- | :--- |
| `/rules` | View or edit the group rules. | [Rules Guide](https://missrose.org/guide/rules/) |
| `/setwelcome` | Update the randomized welcome msg. | [Notes/Welcome](https://missrose.org/guide/notes/) |
| `/filter` | Add a new keyword trigger. | [Filters Guide](https://missrose.org/guide/filters/) |
| `/config` | Access the general bot configuration. | [General Setup](https://missrose.org/guide/getting-started/) |
| `/adminlist` | See all authorized group admins. | — |

> [!IMPORTANT]
> **Avoid Chat Spam:** Whenever possible, use the **Web Dashboard** or **Private Messages** to Rose for configuration. Only use commands in the main group for testing or immediate moderation actions.

---

## :material-robot: Telegram Welcome Message (Randomized)
Copy this entire block. The `%%%` markers allow the bot to pick a random variation each time a new member joins.

```text
/setwelcome
Welcome to {chatname}, {username}! 🚀✨

Ready to supercharge your TCL TV? We've built a **brand new Documentation Hub** just for you! It's packed with step-by-step guides, chipset data, and the latest firmware links.

📍 **Your Journey Starts Here:**
- 🛠 [Installation Guides](https://FaserF.github.io/TCL-Discussion-Telegram/guides)
- 🧠 [Chipset & Platform Database](https://FaserF.github.io/TCL-Discussion-Telegram/chipsets)
- 🔓 [Rooting & Custom ROMs](https://FaserF.github.io/TCL-Discussion-Telegram/rooting)

🛡 **STAY SAFE:** Admins and Mods will **NEVER** PM you to sell anything. Protect yourself by reading our [Safety Guide](https://FaserF.github.io/TCL-Discussion-Telegram/safety).

⚠️ **English Only** | 🔍 **Search Before Asking**

[Open Documentation Hub](buttonurl://https://FaserF.github.io/TCL-Discussion-Telegram/)
[Firmware Updates](buttonurl://https://t.me/tclupdates)
[Firmware Bot](buttonurl://@FirmwareTCLbot)
%%%
Hey {username}, welcome aboard {chatname}! 👋🏻

We're glad to have you here! To help you get started, we've launched the **Official TCL Documentation Hub**. It’s your one-stop shop for firmware updates, installation guides, and platform mapping.

Before you dive in:
- 📖 [Help & FAQ](https://FaserF.github.io/TCL-Discussion-Telegram/faq/)
- ⚙️ [Update Notes](https://FaserF.github.io/TCL-Discussion-Telegram/guides)

🗣 **Note:** This group is English-only.
🔍 **Pro Tip:** Millions of questions have been answered—use the search button first!

[Documentation Hub & FAQ](buttonurl://https://FaserF.github.io/TCL-Discussion-Telegram/faq/)
[Check Updates](buttonurl://https://t.me/tclupdates)
[Firmware Bot](buttonurl://@FirmwareTCLbot)
%%%
Greetings {username}! Welcome to {chatname}. 🎉

Looking for the latest firmware or technical support? Our internal **Documentation Hub** is now live and is the primary source for all TCL information.

🌟 **Quick Links:**
- [Firmware Installation Masterclass](https://FaserF.github.io/TCL-Discussion-Telegram/guides)
- [Official Safety & Anti-Scam Guide](https://FaserF.github.io/TCL-Discussion-Telegram/safety)

Remember: This is an English-only community. Please use the search function before posting new questions.

[Visit Documentation Hub](buttonurl://https://FaserF.github.io/TCL-Discussion-Telegram/)
[Join Channel](buttonurl://https://t.me/tclupdates)
[Firmware Bot](buttonurl://@FirmwareTCLbot)
```

---

---

## :material-filter-variant: Rose Bot Filters
Use these commands to set up automatic responses for common questions. We use Rose's multi-trigger syntax to keep the group clean.

**How to use:** Copy and paste these blocks directly into the Telegram group.

### 1. Firmware & Update Assistance
Triggers when people ask about versions, changelogs, where to find software, or "can I update" questions.
```text
/filter ("is my tv software outdated?", "where to look for firmware", "where to look for software", "where i can download", "software update for", "latest firmware", "latest version", "latest update", "what changes", "last update", "patch notes", "what is new", "change log", "what's new", changelog, "can i update", "any new update", "soft update", "new sw", "sw version", "firmware link", "google tv update", "android tv update")
Looking for the latest firmware or wondering if your TV is up to date? 🚀

Check our **Firmware Database** for all chipsets and current versions. Also, keep an eye on the **Updates Channel** for real-time notifications.

[Open Firmware Database](buttonurl://https://FaserF.github.io/TCL-Discussion-Telegram/chipsets/)
[Join Updates Channel](buttonurl://https://t.me/tclupdates)
[Use Firmware Bot](buttonurl://@FirmwareTCLbot)
```

### 2. Installation & USB Troubleshooting
Triggers for flashing, upgrading, and common USB recognition issues.
```text
/filter ("how to install", "how to upgrade", "issues installing", "no file on usb", "how to flash", "flash firmware", "update via usb", "usb update", "install firmware", "how to update", "usb not found", "file not found")
Need help installing a firmware update? 🛠

Whether you are using a local update or an IMG file, our **Installation Masterclass** covers all steps and common pitfalls (like "no file found").

[Installation Guide](buttonurl://https://FaserF.github.io/TCL-Discussion-Telegram/guides/)
[Troubleshooting FAQ](buttonurl://https://FaserF.github.io/TCL-Discussion-Telegram/faq/)
```

### 3. Downgrading & Shop Reset
Triggers for safety-critical operations like rolling back or resetting specialized modes.
```text
/filter (downgrade, "down grade", "reset shop", "shop reset", "go back to old", "roll back", "rollback", "previous version")
Thinking about downgrading your software? ⚠️

Downgrading can be tricky and might require a **factory reset** or a **Shop Reset**. Please read our guide on how to safely return to an older version.

[Downgrade Guide](buttonurl://https://FaserF.github.io/TCL-Discussion-Telegram/faq/#how-to-downgrade)
[Shop Reset Guide](buttonurl://https://FaserF.github.io/TCL-Discussion-Telegram/reset-shop/)
```

### 4. Root, Bootloader & Custom ROMs
```text
/filter (root, "unlock bootloader", "custom rom", "rooting")
Interested in rooting your TCL TV? 🔓

Rooting allows for deeper customization but carries risks. Check our dedicated section for verified methods and warnings.

[Rooting & ROMs Guide](buttonurl://https://FaserF.github.io/TCL-Discussion-Telegram/rooting/)
```

### 5. Technical Optimizations & Features
Triggers for Performance, Gamebar, 5G Wi-Fi, and Play Store issues.
```text
/filter ("speed up", country, gamebar, 5g, "play store shortcut", "playstore", "tv slow", "tv lagging", "high ping", "factory reset", "hard reset")
Looking for specific features or optimizations? ⚡️

We have sections covering Wi-Fi issues (5G), the Gamebar feature, and tips on how to speed up your Android TV experience.

[Optimization & FAQ](buttonurl://https://FaserF.github.io/TCL-Discussion-Telegram/faq/)
```

---

### Internal Links
- [View news.json](assets/news.json)
- [Workflow Code](https://github.com/FaserF/TCL-Discussion-Telegram/blob/main/.github/workflows/update-news.yml)
