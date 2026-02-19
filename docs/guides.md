This page details the standard methods for updating and recovering TCL television hardware.

---

## :material-identifier: Identify Your Firmware & Platform

Before downloading any firmware, you **must** know your TV's Platform and Version. Installing firmware for the wrong platform can result in a non-functional TV.

### 1. Where to look
On your TV, navigate to:
**Settings** > **System** > **About** > **Product Information**.

### 2. Traditional Naming Convention
Most TCL firmwares follow a long-string format. Take this example:
`V8-T615T03-LF1V474.000418`

*   **Platform:** the second part (`T615T03`). This identifies your hardware.
*   **Version:** the 3 digits following the "V" (`V474`).

### 3. New 2025 Platform Naming
Starting in 2025, TCL has simplified the Platform part of the firmware name displayed in the TV menu. Use the table below to cross-reference new IDs with their traditional platform names:

| New ID (TV Menu) | Traditional Platform | Chassis / SoC |
| :--- | :--- | :--- |
| **0003T05** | T221T05 | MT21 |
| **0003T09** | T221T09 | MT21 |
| **0008T01** | R75PT01 | RT75 |
| **0012T01** | T653T01 | MT53 |
| **0012T02** | T653T02 | MT53 |
| **0012T03** | T653T03 | MT53 |
| **0013T02** | T800T02 | T800 |
| **0015T01** | — | MT55 |

!!! tip "Verification"
    If your ID is not listed, search for the **full firmware string** in the [TCL Telegram Group](https://t.me/tclupdates_discussion) or use the [Firmware Bot](https://t.me/FirmwareTCLbot) for verification.

---

## :material-usb: Flashing Methods Overview

There are two primary ways to update or recover a TCL TV. Choosing the right one depends on your goal (upgrade vs. recovery).

### 1. OTA (Over-The-Air Update)
**Best for:** Standard version upgrades where you want to keep your data.

*   **File Format:** `.zip` or `.bin`
*   **Data Loss:** None. Apps and settings are preserved.
*   **Process:** Performed via the **System Update > Local Update** menu.

### 2. IMG / PKG Flash (Recommended for newer models)
**Best for:** Downgrading, unbricking, or performing a clean system reset.

*   **File Format:** `.img`, `.pkg`, or `.zip`.
*   **Data Loss:** **Total.** All user data is wiped.
*   **Process:** Performed by holding the hardware power button during cold boot.

!!! warning "Downgrade Logic"
    Normally, a **downgrade** should only be done using **IMG/PKG** firmware. This process will erase all your apps and data.

    *   **Exception:** If your TV uses **Realtek** hardware with **Android 11 or earlier**, you can also use an **OTA file** for downgrade by following the IMG installation instructions (holding the power button).

---

## :material-cog: Step-By-Step Instructions

### Preparation (Required)

*   **Format USB:** Use a Windows PC to format a USB drive (8GB-32GB) to **FAT32**.
*   **Single File:** Ensure **only one** firmware file is on the root directory of the USB.
*   **Slot:** For most TVs, use the **USB 2.0** slot (white/black). **Note:** T653 firmware may require a **USB 3.0** (blue) port.

### How to install OTA (.zip) / Local Update

1.  Download the correct firmware ZIP file.
2.  **Do not unzip.** Copy the ZIP file directly to the USB drive.
3.  Plug the USB into the TV.
4.  Navigate to **Settings** > **System** > **About** > **System Update** > **Local Update**.
5.  Wait for the validation to finish and follow on-screen prompts.

### How to Flash IMG / PKG

1.  Download the firmware and extract it.
2.  Copy the main file (e.g., `Update.pkg`) to the root of your USB drive.
3.  Plug the USB into the TV.
4.  Unplug the TV from power.
5.  **Press and hold the Power Button** on the TV. Location varies:
    - **Physical button:** Usually directly under the TCL logo or on the back/side.
    - **Toggle:** Some models use a small joystick; press it straight in.
6.  While holding, plug the TV back in.
7.  Release once the "Software Update" screen appears.


---

## :material-console: Advanced: Service Menus

Service menus allow access to hardware-level parameters, total runtime, and panel calibration.

| Code | Description |
| :--- | :--- |
| **1950** | General Service Menu (Design Menu) - Standard for GTV/ATV. |
| **6425** | Running Time & Quick access (Reset All / Reset Shop). |
| **9735** | Subsection: Factory Menu. |
| **6428** | Subsection: Factory Menu (Alternative). |
| **9705** | Subsection: Service Menu. |
| **6405** | Subsection: Hotel Menu. |

### How to enter:

1.  Navigate to **Settings** > **Display & Sound** > **Picture**.
2.  Go to **Advanced Settings** > **Brightness**.
3.  Highlight **Contrast** (do not click).
4.  Type the **4-digit code** quickly on the remote. **Note:** If your remote lacks number buttons, use the on-screen keyboard or a smartphone remote app.

!!! danger "Service Menu Warning"
    Do not change anything in the Service Menus unless you know exactly what you are doing. Incorrect settings can cause hardware malfunctions or "soft-brick" your device.

---



## :material-refresh: Reset & Maintenance

If you encounter bugs after an update, or if your TV is stuck in a specific mode, use these procedures.

### Factory Reset
Navigation: **Settings** > **System** > **About** > **Reset**.

*   **IMG / PKG Flash:** A factory reset is **not required** because the flashing process already performs a full system wipe.
*   **OTA Update:** Since OTA preserves your apps, we only recommend a manual factory reset if you encounter strange bugs or performance issues after the update.

### Shop Mode / Store Mode
If your TV constantly displays feature banners and resets settings:

1.  Navigate to **Settings** > **System** > **Environment**.
2.  Change from **Shop/Store** to **Home**.
3.  Alternatively, you can force-reset this flag through the **Service Menu**.

---

## :material-help-circle-outline: Troubleshooting

If the TV says "No file found" or fails verification:

1.  **Switch USB Drive:** Try an older USB 2.0 drive.
2.  **Filesystem Check:** Re-format to FAT32 on any PC (Windows/Linux) or directly on the TV in the storage settings.
3.  **No Subfolders:** The `.img` or `.pkg` file must be at the very root of the drive.
