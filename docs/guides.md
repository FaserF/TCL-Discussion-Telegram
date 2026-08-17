This page details the standard methods for updating, recovering, and configuring TCL television hardware.

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
*   **Version:** the digits following the "V" (`V474`).

### 3. Modern Platform Naming (2025/2026 Format)
Starting in recent firmware versions, TCL simplified the Platform part of the firmware name displayed in the TV menu. Use the table below to cross-reference TV menu IDs with their traditional platform names:

| TV Menu ID | Traditional Platform | Chassis / SoC Family |
| :--- | :--- | :--- |
| **0016T01** | 0016T01 | G15 (AP & LATAM models) |
| **0015T01** | T655T01 | Pentonic 800 (MT55) |
| **0012T01** | T653T01 | Pentonic 700 (MT53 / EU & Global) |
| **0012T02** | T653T02 | Pentonic 700 (G08 / NA & LATAM) |
| **0012T03** | T653T03 | Pentonic 700 (G16 / QM9K) |
| **0013T02** | T800T02 | T800 / AMLT963D4 (G09) |
| **0008T01** | R75PT01 | Realtek RT75 (G10) |
| **0003T05..T09** | T221T05..T09 | MediaTek MT21 (2K / FHD) |

!!! tip "Verification"
    If your ID is not listed, search for the **full firmware string** in the [TCL Telegram Group](https://t.me/tclupdates_discussion) or use the [Firmware Bot](https://t.me/FirmwareTCLbot) for verification.

---

## :material-usb: Flashing Methods Overview

There are two primary ways to update or recover a TCL TV. Choosing the right one depends on your goal (upgrade vs. recovery/downgrade).

### 1. Local Update (OTA) Update
**Best for:** Standard version upgrades where you want to keep your data.

*   **File Format:** `.zip`
*   **Data Loss:** None. Apps, accounts, and settings are preserved.
*   **Process:** Performed via the **System Update > Local Update** menu.

### 2. IMG / PKG Flash
**Best for:** Downgrading, unbricking, recovering from bootloops, or performing a clean system reset.

*   **File Format:** `.img`, `.pkg`, or unzipped recovery package.
*   **Data Loss:** **Total.** All user data, apps, and accounts are erased.
*   **Process:** Performed by holding the hardware power button during cold boot.

!!! warning "Downgrade Rules"
    Normally, a **downgrade** should only be done using **IMG/PKG** firmware.
    
    *   **Project ID Whitelist:** Never flash an IMG/PKG firmware older than your TV model's release or factory version. Doing so will result in a **black screen** because the older firmware lacks your model's Project ID.
    *   **Realtek Exception:** On older **Realtek** hardware running **Android 11 or earlier**, forced OTA zip installation via the power button method was possible, but on Android 12 and 14 all downgrades require full IMG/PKG files.

---

## :material-cog: Step-By-Step Instructions

### Preparation Checklist

*   **USB Drive Format:** Format a USB flash drive (8GB–32GB recommended) to **FAT32** with an **MBR** (Master Boot Record) partition table on a Windows or Linux PC. (Avoid macOS formatting or ensure Safari auto-unzip is turned off).
*   **Single File:** Ensure **only one** firmware file is placed in the root directory of the USB drive.
*   **Port Selection:** For most TVs, use the **USB 2.0** port (black/white). Certain Pentonic 700 / T653 models may require the **USB 3.0** (blue) port.
*   **Disable Developer Options:** If Local Update validation fails, turn off Developer Options in Android Settings before trying again.

### How to Install Local Update (OTA) (.zip)

1. Download the correct firmware `.zip` file for your platform.
2. **Do not unzip.** Copy the `.zip` file directly to the root of the FAT32 USB drive.
3. Plug the USB drive into the TV.
4. Navigate to **Settings** > **System** > **About** > **System Update** > **Local Update**.
5. Wait for the TV to validate the package and follow the on-screen prompts.

### How to Flash IMG / PKG (Recovery / Downgrade)

1. Download the IMG/PKG firmware package and extract the archive on your PC.
2. Copy the resulting `.pkg` or `.img` file (e.g., `V8-T653T01-...pkg` or `Update.pkg`) to the root of your FAT32 USB drive.
3. Plug the USB drive into the TV.
4. Unplug the TV's power cord from the wall outlet.
5. **Press and hold the physical Power Button** on the TV:
    - Located directly under the front TCL logo, or on the rear/side as a button or joystick.
6. While continuing to hold the power button, plug the TV back into power.
7. Keep holding the button for 10–15 seconds until the flashing blue "Software Update" screen appears, then release.
8. Allow the flashing process to reach 100% and restart automatically.

---

## :material-console: Advanced: Service Menus & Secret Codes

Service menus allow access to hardware-level parameters, total running time, panel calibration, and system toggle options.

| Code | Name | Primary Use Cases |
| :--- | :--- | :--- |
| **`6425`** | **Quick Access & Maintenance** | Check **Total Running Time**, execute **Reset All** or **Reset Shop**, and toggle **Shutdown Config** (restores long-press Power button shutdown menu). |
| **`1950`** | **Design / General Service Menu** | View Panel Type, White Balance calibration, PQ parameters, and general hardware configuration. |
| **`9735`** | **Factory Menu** | Disable **9-Sita P mode** and **Factory Hotkey** if red "P" or "M" factory mode appears on screen. |
| **`6428`** | **Factory Menu (Alternative)** | Alternative entry to Factory settings. |
| **`9705`** | **Subsystem Service Menu** | Deep subsystem and hardware revision diagnostics. |
| **`6405`** | **Hotel Menu** | Hotel / commercial display restrictions mode. |

### How to Enter a Service Menu:

1. Open TV **Settings** (gear icon on remote).
2. Navigate to **Display & Sound** (or **Picture**) > **Advanced Settings** > **Brightness Settings**.
3. Highlight **Contrast** (do **not** press OK or enter the adjustment slider).
4. Type the **4-digit code** (e.g., `6425`, `1950`, or `9735`) quickly on the remote keypad.
5. If your remote does not have physical numeric buttons, press the **`123`** virtual keypad button on your remote to bring up the on-screen number pad, or use a mobile remote app (Google Home or TCL Home).

!!! danger "Service Menu Warning"
    Do not alter unknown values in the Service Menus (especially NVM or White Balance presets) unless you have noted down original values. Incorrect settings can cause color distortion or brick your TV.

---

## :material-remote: Re-Enabling the "Shutdown" Option (Android 14 / GTV)

On newer Google TV builds (including Android 14), long-pressing the remote power button may only offer a "Restart" option by default. You can re-enable the complete Shutdown option:

1. Go to **Settings** > **Picture** > **Advanced** > **Brightness** and highlight **Contrast**.
2. Type **`6425`** on your remote.
3. In the service menu overlay, look for **Shutdown Config** (or **Shutdown**).
4. Change the setting from `OFF` to **`ON`**.
5. Press **Back** or **Home** to exit. Long-pressing the remote power button will now show **Shut down**, **Restart**, and **Cancel**.

---

## :material-shield-refresh: Blind Project ID Recovery Method

If your screen remains black after a mainboard replacement or accidental Project ID modification, but the TV is powered on and the status LED responds to the remote:

1. Turn the TV **ON**.
2. On your remote control, sequentially dial:
   ```text
   0 6 2 5 9 8
   ```
3. Press **`MENU`** (or **`OK`** on some remotes).
4. Type your TV's original **`Project ID`** (1 to 6 digits, e.g., `10188` or `5456`).
5. Wait 5–10 seconds; the TV will automatically reinitialize the display panel and reboot with the correct screen configuration.

---

## :material-help-circle-outline: Troubleshooting Flashing & USB

*   **"No file found" or "Validation failed":**
    1. Ensure the USB is formatted to **FAT32** with **MBR** partition scheme.
    2. Try another USB flash drive (USB 2.0 drives with 8GB–16GB capacity are the most reliable).
    3. Ensure the file is at the root of the USB drive (no nested folders).
    4. **Cold restart trick:** With the USB plugged into the TV, hold the power button on the remote for 5 seconds to select Shutdown (or unplug from the wall for 1 minute), then power the TV back on so the OS mounts the USB storage upon boot.
*   **Stuck on Logo / Bootloop:**
    - Perform a forced IMG/PKG flash using the hardware power button cold boot procedure described above. OTA files cannot recover a bootloop.
