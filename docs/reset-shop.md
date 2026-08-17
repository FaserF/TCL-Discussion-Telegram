# Reset All & Reset Shop Guide

This technical guide explains how to perform deep system resets using the TCL Service Menu. These methods are more thorough than a standard Factory Reset and are often used to resolve persistent software bugs, cache corruption after major Android updates, or "Shop Mode" issues.

!!! warning "Data Loss"
    Both reset procedures will erase all user data, installed apps, and settings. Ensure any important personal data is backed up before proceeding. (Your TV's Platform and Project ID are preserved in hardware NVM).

---

## :material-cog-box: Accessing the Service Menu

Before performing a reset, you must first enter the hidden Service Menu:

1.  Press the **Settings** (gear) button on your remote.
2.  Select **Display & Sound** (or **Picture**) and press `OK`.
3.  Navigate to **Advanced Settings** > **Brightness Settings**.
4.  Highlight the **Contrast** option (do not enter the adjustment slider).
5.  While **Contrast** is highlighted, type the following code on your remote:
    ```text
    6 4 2 5
    ```
6.  The **Service Menu** overlay will appear on the left side of your screen.

!!! tip "No Number Buttons?"
    If your remote lacks number buttons, press the **`123`** virtual keyboard button on the remote to display the on-screen keypad, or use a mobile remote app (like Google Home or TCL Home).

---

## :material-refresh: Service Menu 6425 Features

The `6425` Service Menu provides several key diagnostics and maintenance functions:

### 1. TV Running Time
Displays the lifetime operating hours of the TV panel and motherboard. Useful for verifying whether a display was a store floor model.

### 2. Reset All
A comprehensive system-wide data wipe. Recommended if your TV is sluggish or apps crash following a firmware update:
- **Effect:** Erases user apps, accounts, and system caches.
- **Procedure:** Highlight **Reset All** > press **Right Arrow** > confirm **OK**. The TV will wipe user data and restart.

### 3. Reset Shop
A deep factory re-initialization that returns the TV to its out-of-the-box state:
- **Effect:** Completely reinitializes the system storage partitions. **Mandatory** if your TV is stuck in "Retail / Shop Demo Mode".
- **Procedure:** Highlight **Reset Shop** > press **Right Arrow** > confirm **OK**. The TV will shut down and reboot directly to the initial setup wizard.

### 4. Shutdown Config (Power Menu Toggle)
Enables the full **Shut Down** choice when long-pressing the remote power button on Google TV (Android 14). Toggle this setting from `OFF` to **`ON`**.

---

## :material-help-circle: Troubleshooting & Related Codes

- **Code doesn't work?** Ensure you are highlighting the **Contrast** menu item and typing without long pauses. If needed, exit to TV home screen and try again.
- **Red "P" or "M" in screen corner (Factory Mode)?** Enter code **`9735`** on Contrast, then select **9-Sita P mode** and set to **OFF**, and set **Factory Hotkey** to **Disable**.
- **Post-Update Maintenance:** After updating across major Android versions (e.g., from Android 12 `V5xx` to Android 14 `V6xx`), performing a **Reset All** is highly recommended to eliminate legacy cache conflicts.
