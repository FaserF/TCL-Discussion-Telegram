# :material-cloud-upload: Community Local Update (OTA) Extraction Guide

Help the community by capturing and sharing official Local Update (OTA) download links.

!!! info "Target Group: TCL T653T01 2025 Users"
    If your TV is offering the **V538** (or more recent) Local Update (OTA) update, you can help everyone by extracting the download link before installing it.

### Prerequisites

*   **PC & TV** connected to the same local network.
*   **ADB AppControl** installed on your PC ([Download Here](https://adbappcontrol.com/download)).
*   **WiFi** enabled on the TV.

### Step-by-Step Process

#### 1. Enable Developer Mode & USB Debugging
1.  On your TV: Go to **Settings** > **System** > **About**.
2.  Highlight **Android TV OS build** (or Version) and press the `OK` button **7-8 times** until a message says "You are now a developer".
3.  Go to **Settings** > **System** > **Developer options**.
4.  Enable **USB debugging**.

#### 2. Connect via ADB AppControl
1.  Open **ADB AppControl** on your PC.
2.  Enter your **TV's IP address** (find it in Settings > Network) in the top right corner.
3.  Click the **Connection** button.
4.  **Confirm the authorization** on your TV screen (check "Always allow from this computer").

#### 3. Start LogCat Capturing
1.  In ADB AppControl, go to the **Console** tab.
2.  Select **LogCat** on the right side.
3.  Check the box for **Debug & Save log to file**.
4.  Click **Start logcat**.

#### 4. Trigger the Update
1.  On your TV: Go to **Settings** > **System** > **About** > **System Update**.
2.  Click **Check for Update** and wait for it to find the update.
3.  Let it start the download process (you don't need to finish it).

#### 5. Save and Share
1.  On your PC: Click **Stop logcat** in ADB AppControl.
2.  Locate the saved log file.
3.  Send the file to **stasiof** on Telegram for extraction of the official Local Update (OTA) link.

---

### Important Notes
*   **Don't have the update yet?** If you are on an older version (like V509) and want to help, you can capture the log while checking for the update.
*   **Already updated?** You can still help if you downgrade (using PKG) and then capture the Local Update (OTA) update log during the re-update process.
