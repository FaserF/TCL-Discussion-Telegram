# Reset All & Reset Shop Guide

This technical guide explains how to performing deep system resets using the TCL Service Menu. These methods are more thorough than a standard Factory Reset and are often used to resolve persistent software bugs or "Shop Mode" issues.

!!! warning "Data Loss"
    Both procedures will erase all user data, installed apps, and settings. Ensure any important data or identifiers (like Project ID) are noted before proceeding.

---

## :material-cog-box: Accessing the Service Menu

Before performing a reset, you must first enter the hidden Service Menu:

1.  Press the **Settings** (gear) button on your remote.
2.  Select **Picture** and press `OK`.
3.  Navigate down to **Advanced Settings** and press `OK`.
4.  Navigate down to **Brightness Settings** and press `OK`.
5.  Highlight the **Contrast** option (do not change it).
6.  While **Contrast** is highlighted, type the following code on your remote:
    ```text
    6 4 2 5
    ```
7.  The **Service Menu** overlay should appear on the left side of your screen.

!!! tip "No Number Buttons?"
    If your remote lacks number buttons, you can use the **on-screen keyboard** (Gboard) or a **smartphone remote app** (like Google Home or the TCL app) to type the code.

---

## :material-refresh: Reset All vs. Reset Shop

The Service Menu provides two distinct reset options. Depending on your issue, you may need one or both.

### 1. Reset All
This is a standard system-wide data wipe. Use this if your TV is lagging or apps are crashing frequently.

- **Effect:** Erases apps and system settings.
- **Procedure:**
    - Within the Service Menu, navigate to **Reset All**.
    - Press the **Right Arrow** on your remote.
    - Confirm the prompt by selecting **OK**.
    - The TV will process the reset and may reboot.

### 2. Reset Shop
This is a more intensive reset that returns the TV to its "Out-of-the-Box" state (First Time Installation).

- **Effect:** Completely reinitializes the system storage. **Mandatory** if your TV is stuck in "Retail/Shop Demo Mode".
- **Procedure:**
    - Within the Service Menu, navigate to **Reset Shop**.
    - Press the **Right Arrow** on your remote.
    - Confirm the prompt by selecting **OK**.
    - The TV will turn off and then restart at the initial language/region setup screen.

---

## :material-help-circle: Troubleshooting

- **Code doesn't work?** Ensure you are on the **Contrast** menu item and typing fairly quickly. If it fails, exit the settings menu and try again.
- **Stuck in Shop Mode?** If a standard "Reset All" does not fix the demo mode, the **Reset Shop** procedure is required.
- **Missing Project ID?** Resetting does not typically erase the Project ID (Model Mapping), but it is always good practice to [verify it](chipsets.md) after a reset.

!!! tip "Post-Update Maintenance"
    After any major firmware update (e.g., from V500 to V600), we highly recommend performing a **Reset All** to ensure no legacy cache files cause performance issues.
