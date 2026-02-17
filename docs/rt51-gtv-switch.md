# Switching R51MT02 (ATV) to Google TV

Users with the **R51MT02** platform (traditionally running Android TV) have the unique option to switch their operating system to **Google TV** by using the firmware designed for the **R51MT05** platform.

### :material-swap-horizontal: The Concept
The hardware in R51MT02 and R51MT05 models is compatible enough that the R51MT05 Google TV firmware can be run on R51MT02 devices. This allows legacy Android TV users to enjoy the modern Google TV interface.

---

### :material-alert: Critical Requirements

1.  **IMG Method ONLY:** You **cannot** perform this switch using a `.zip` (OTA) file. Because you are changing the underlying OS structure, a full [IMG Flashing Procedure](guides.md#how-to-flash-img-pkg) is mandatory.
2.  **Full Data Wipe:** Flashing an IMG file will **erase all your apps, accounts, and settings**. Ensure you have backed up any necessary information.
3.  **Platform Check:** Verify your current [Platform ID](guides.md#identify-your-firmware-platform) before proceeding. This guide is specifically for **R51MT02** hardware.

---

### :material-step-forward: How to Switch

1.  **Download:** Obtain a stable **R51MT05** IMG firmware file (e.g., V5xx or newer).
2.  **Prepare USB:** Format a USB drive to FAT32 and copy the `.pkg` or `.img` file to the root.
3.  **Flash:** Follow the **[IMG / PKG Flashing Guide](guides.md#how-to-flash-img-pkg)**:
    - Unplug the TV.
    - Press and hold the power button.
    - Plug the TV back in while holding.
    - Release when the update screen appears.
4.  **Setup:** Once the flash is complete, the TV will boot into the **Google TV** initial setup screen.

!!! tip "Going Back"
    If you decide you prefer the original Android TV interface, you can switch back at any time by flashing an original **R51MT02 IMG** file using the same procedure.

---

### Related Links
- [Installation Guides](guides.md)
- [Chipset Database](chipsets.md)
- [Safety FAQ](faq.md)
