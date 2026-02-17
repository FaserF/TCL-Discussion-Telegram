# TCL Frequently Asked Questions

Common technical questions and troubleshooting steps for TCL Android/Google TVs.

??? question "How do I find my Project ID or Panel ID?"
    The **Project ID** is a 4-digit number specific to your TV's screen size and panel type.

    1.  Look at the sticker on the back of the TV.
    2.  Check the **Service Menu** (see [Guides](guides.md#advanced-service-menus)).
    3.  Ask in the [TCL Discussion Telegram](https://t.me/tclupdates_discussion) with a photo of your model sticker.

??? question "What is the difference between Google TV and Android TV?"
    TCL models from 2021+ mostly use **Google TV** (a layer on top of Android). Legacy or budget models use **Android TV**.

    - You can often switch a GTV to "Apps Only" mode in settings to get a cleaner, more ATV-like experience.

??? question "Why can't my TV see my 5GHz Wi-Fi?"
    TCL TVs often have specific requirements for 5GHz networks:

    1.  **Lower Channels:** Most models only support "Lower" 5GHz channels. Set your router to **Channels 36, 40, 44, or 48**. Higher channels (DFS) are often invisible to the TV.
    2.  **Hardware Support:** Some budget/legacy models only support 2.4GHz Wi-Fi. Check your detailed specs or the Telegram group to verify 5G support for your specific ID.

??? question "Is my firmware version outdated?"
    Firmware versions are usually in the format `VXXX` (e.g., `V560`).

    *   **Higher is newer:** `V560` is newer than `V509`.
    *   **Prefixes:** `V` = Release, `R` = Test, `M` = Pre-production.
    *   Check **[@FirmwareTCLbot](https://t.me/FirmwareTCLbot)** to see the absolute latest official version for your Platform ID.

??? question "My TV is slow. How do I speed it up?"
    Android TVs can become sluggish over time. Try these steps:

    1.  **Reduce Animations:** Go to Developer Options and set all "Animation scale" settings to `0.5x` or `Off`.
    2.  **Background Process Limit:** In Developer Options, set limit to `At most 2 processes`.
    3.  **Apps Only Mode:** (GTV only) Enable this in Accounts/Settings to remove heavy content recommendations.
    4.  **Reset Shop:** (Last resort) Use code `6425` in the Service Menu to perform a clean system wipe.

??? question "Where can I find the Play Store?"
    Since Google TV (v11+) prioritizes content, the Play Store icon might be hidden.

    *   **Voice Search:** Say "Open Play Store" to the remote.
    *   **Settings:** Go to Settings > Apps > See all apps > Show system apps > Google Play Store > Open.

??? question "What are Changelogs/Patch Notes?"
    TCL rarely provides official changelogs for firmware updates. Community members often track changes manually.

    - Follow the [News Channel](https://t.me/tclupdates) for major update reports.
    - Check the [Firmware History](https://t.me/FirmwareTCLbot) in the bot for version numbers.

??? question "What is the Game Bar?"
    The **Game Bar** is a featureset for 2022+ models (Pentonic/T615) that allows real-time viewing of Refresh Rate (Hz), VRR status, and HDR settings during gaming.

    *   **Access:** Long-press the **Settings** (gear) or **Menu** (three lines) button on the remote while an HDMI source is active.
