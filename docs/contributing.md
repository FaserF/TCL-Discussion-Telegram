# Contributing to TCL Firmware Hub

Thank you for your interest in contributing! Whether you are an experienced developer or a complete beginner, this guide will help you set up the project locally, test your changes, and submit your improvements.

## :material-rocket: Getting Started (Local Setup)

This project uses **MkDocs** with the **Material** theme. Follow these steps to get it running on your machine.

### 1. Prerequisites
You need **Python** installed on your computer.
- [Download Python](https://www.python.org/downloads/) (Ensure you check "Add Python to PATH" during installation).

### 2. Clone the Repository
Open your terminal (PowerShell or Command Prompt on Windows) and run:
```bash
git clone https://github.com/FaserF/TCL-Discussion-Telegram.git
cd TCL-Discussion-Telegram
```

### 3. Setup the Environment
We use a simple script to handle all dependencies for you. Just run:
```powershell
.\dev.ps1
```
This script will:
- Check for Python.
- Install required libraries (`mkdocs-material`, `pymdown-extensions`).
- Start a local development server.

## :material-console: How to Test Locally

Once you run `.\dev.ps1`, your local version of the site will be available at: http://127.0.0.1:8000/

### Live Reloading
The best part is **Live Reloading**. Whenever you save a file in the `docs/` folder, the browser will automatically refresh to show your changes. You don't need to restart the script!

### Manual Build Test
To ensure your changes don't have any broken links or errors, run the strict build command:
```bash
python -m mkdocs build --strict
```

## :material-file-tree: Project Structure

Knowing where files are located makes contributing easier:

- `mkdocs.yml`: The main configuration file. You can change the site name, navigation, and theme settings here.
- `docs/`: This is where all the content lives.
    - `index.md`: The homepage.
    - `guides.md`: Detailed installation guides.
    - `faq.md`: Safety information and FAQs.
    - `stylesheets/extra.css`: The custom "Premium" design styles.
- `site/`: This folder is generated automatically when you build the site. **Do not edit files here directly.**

## :material-pencil: Making Changes

1.  **Edit Content:** Most of the content is in Markdown (`.md`). It's a simple text format. You can use any text editor (like Notepad++, VS Code, or even standard Notepad).
2.  **Add Images:** Place new images in `docs/assets/` and link to them using `![Alt text](assets/image.png)`.
3.  **Submit your work:** Once you are happy with your changes, commit them to your fork and create a **Pull Request** on GitHub.

### Beginner Tip: Using GitHub Desktop
If you aren't comfortable with the command line, we recommend using [GitHub Desktop](https://desktop.github.com/). It provides a simple visual interface for cloning, committing, and pushing changes.

---

## :material-scale-balance: Contribution Rules

-   **Be Helpful:** Our goal is to make firmware flashing safe for everyone.
-   **Verify Info:** If you are adding technical details about a chipset or firmware version, please ensure it has been verified in the Telegram group.
-   **No Spam:** Only content related to TCL firmware and community utilities is allowed.

---

### Need Help?
If you get stuck, feel free to ask in the [Community Group](https://t.me/tclupdates_discussion). We are always happy to help new contributors!
