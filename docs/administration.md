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

### Internal Links
- [View news.json](assets/news.json)
- [Workflow Code](https://github.com/FaserF/TCL-Discussion-Telegram/blob/main/.github/workflows/update-news.yml)
