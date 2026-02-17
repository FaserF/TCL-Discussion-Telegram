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
| **0003T05** | T221T05 | R51M |
| **0003T09** | T221T09 | R51M |
| **0008T01** | R75PT01 | RT51 |
| **0012T01** | T653T01 | T653 |
| **0012T02** | T653T02 | T653 |
| **0012T03** | T653T03 | T653 |
| **0013T02** | T800T02 | T800 (Pentonic 700) |
| **0015T01** | — | Pentonic 800 (Upcoming) |

> [!TIP]
> If your ID is not listed, search for the **full firmware string** in the [TCL Telegram Group](https://t.me/tclupdates_discussion) or use the [Firmware Bot](https://t.me/FirmwareTCLbot) for verification.

---

## :material-usb: Flashing Methods Overview

There are two primary ways to update or recover a TCL TV. Choosing the right one depends on your goal (upgrade vs. recovery).

### 1. Local Update (.zip)
**Best for:** Standard version upgrades where you want to keep your data.

*   **File Format:** `.zip`
*   **Data Loss:** None. Apps and settings are preserved.
*   **Process:** Performed via the **System Update > Local Update** menu.

### 2. IMG / PKG Flash
**Best for:** Downgrading, unbricking, or performing a clean system reset.

*   **File Format:** `.img`, `.pkg`, or `.bin`.
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
*   **Slot:** For TVs with multiple ports, use the **USB 2.0** slot (usually white/black) for the best compatibility.

### How to install OTA (.zip)

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

| Code | Access Path | Primary Use Case |
| :--- | :--- | :--- |
| **6425** | Settings > Picture > Brightness > Contrast | Standard (GTV/ATV). Used for uptime & version. |
| **1950** | Settings > Picture > Brightness > Contrast | Common on newer Google TV models. |
| **9735** | Settings > Picture > Advanced (Highlight Contrast) | Alternative code for older Android TV models. |
| **9705** | Settings > Picture > Brightness > Contrast | Used for factory debug and internal testing. |

### How to enter:

1.  Navigate to **Settings** > **Display & Sound** > **Picture**.
2.  Go to **Advanced Settings** > **Brightness**.
3.  Highlight **Contrast** (do not click).
4.  Type the **4-digit code** quickly on the remote.

---

## :material-monitor-edit: Master Class: Project ID & Panel Fixes

If you flash the correct platform but the **wrong model revision**, you might experience an **inverted screen**, scrambled colors, or a black panel (no backlight).

### Fixing an Inverted Screen
This usually means the software is expecting a different physical panel orientation (LVDS mapping).

1.  Enter the **Service Menu** (using code above).
2.  Find the **Project ID** or **Panel ID** entry.
3.  Input the **correct Project ID** for your specific model size (found on the sticker on the back or in the community telegram).
4.  Alternatively, look for an **LVDS Option** or **Rotate Flag** (rare on newer models).

### Changing Project ID (Screen is Black)
If the screen is black but the TV is "on" (status light reacts), you can sometimes blind-type a Project ID:

1.  Turn on the TV and wait 30 seconds.
2.  Type **062598 + Menu + [XXX]** where `XXX` is your 3-digit Project ID.
3.  The TV should reboot automatically with the new ID applied.

!!! danger "High Risk"
    Incorrectly changing Project IDs can lead to a "hard brick" if the bootloader becomes incompatible with the panel. Always verify the ID with a moderator before performing this.

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
2.  **Filesystem Check:** Re-format to FAT32 on a Windows PC.
3.  **No Subfolders:** The `.img` or `.pkg` file must be at the very root of the drive.
