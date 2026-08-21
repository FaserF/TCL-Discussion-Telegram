# TCL Firmware Discussion Hub 🚀

![TCL Firmware Logo](docs/assets/logo.png)

A modern, community-driven documentation site and automated firmware tracking platform for TCL Smart TV enthusiasts. Built with **MkDocs Material** for speed, simplicity, and ease of contribution.

---

## ⚡ Automated TCL Firmware Tracker & API

This repository features a **100% dynamic, automated TCL TV Firmware Tracking Engine** powered by official TCL FOTA upgrade servers (`huan.tv`) and official Content Delivery Networks (`cedock.com`).

- 📊 **[Live Firmware Catalog](docs/firmwares.md)**: Real-time table covering 42+ TCL TV SoC platforms with latest verified OTA releases, package sizes, compilation dates, changelogs, and direct CDN download links.
- 📡 **[FOTA API & Protocol Documentation](docs/update_mechanisms.md)**: Reverse-engineered specification of official TCL TV update endpoints, XML payloads, and `HUAN-Sign` MD5 cryptographic signatures.
- 🤖 **[Firmware Tracking Engine (`scripts/fetch_firmwares.py`)](scripts/fetch_firmwares.py)**: Python automation script that queries official TCL FOTA endpoints, performs sequential package extraction, and triggers Telegram community broadcasts.
- 🗄️ **[Structured JSON Dataset (`docs/assets/firmwares.json`)](docs/assets/firmwares.json)**: Machine-readable API dataset providing verified firmware details, hardware specifications, and deep Android build metadata.

---

## 📢 Telegram Channel Broadcast Integration

When a new TV platform is discovered or a new firmware update is released, the GitHub Actions CI workflow ([`.github/workflows/firmware-tracker.yml`](.github/workflows/firmware-tracker.yml)) automatically broadcasts formatted announcement messages to the Telegram community channel.

### Configuration via GitHub Secrets:
To activate automated Telegram notifications for your fork or channel, configure the following secrets in **Settings -> Secrets and variables -> Actions**:
- `TELEGRAM_BOT_TOKEN`: The bot token obtained from `@BotFather`.
- `TELEGRAM_CHANNEL_ID`: The target Telegram channel or group ID (e.g. `@your_channel` or `-100xxxxxxxxxx`).

---

## 📖 Key Features
- **Automated Firmware Tracking**: Runs daily at 04:00 UTC (06:00 German Time) to detect new OTA updates across all platforms.
- **Deep Firmware Extraction**: Extracts authentic Android OS versions, Google TV vs. Android TV UI flavors, Security Patch dates, and build fingerprints.
- **Premium Documentation**: Step-by-step flashing guides, unbricking tutorials, and secret service menu codes.
- **Hardware Explorer**: Comprehensive [Chipset & SoC Matrix](docs/chipsets.md) matching TV models to chassis platforms.
- **Safety Centric**: Integrated anti-scam warnings and official community links.
- **Community Driven**: Direct integration with Telegram (50K+ members).

---

## 🛠 Tech Stack
- **Engine**: [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) (Static Site Generator)
- **Tracker**: Python 3 Standard Library (`hashlib`, `urllib`, `xml.etree.ElementTree`, `zipfile`)
- **CI/CD**: GitHub Actions & GitHub Pages
- **Styling**: Custom CSS variables (Slate & Red Theme)

---

## 💻 Local Development
To preview the website locally on Windows, you can use the provided PowerShell script:

1. Open PowerShell in the project root.
2. Run the following command:
   ```powershell
   ./dev.ps1
   ```
   *This will automatically check for Python, install dependencies, and start the server.*

3. Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

To manually run the firmware tracker locally:
```bash
python scripts/fetch_firmwares.py
```

---

## 🤝 Contributing
We welcome contributions! The easiest way to help is to use the **"Edit this page"** button (:pencil2:) directly on the website.

If you are a developer:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/amazing-guide`).
3. Commit your changes.
4. Open a Pull Request.

---

## ⚖️ Legal Disclaimer
This project is community-run and not affiliated with **TCL Electronics**. Use all firmware at your own risk.

---
*Visit us on Telegram: [@tclupdates](https://t.me/tclupdates)*
