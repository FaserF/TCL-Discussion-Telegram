# TCL Frequently Asked Questions

Common technical questions, troubleshooting steps, and verified solutions for TCL Android and Google TVs.

??? question "How do I find my Project ID or Panel ID?"
    The **Project ID** is an internal identifier (typically 1 to 6 digits) that maps the TV motherboard firmware to your specific panel type, tuner region, and backlight configuration.

    1.  **TV Settings:** Navigate to **Settings** > **System** > **About** > **Product Information** and look for the **Project ID** field.
    2.  **Service Menu:** Enter code `1950` or `6425` on the **Contrast** menu (see [Guides](guides.md#advanced-service-menus-secret-codes)).
    3.  **Hardware Sticker:** Check the small white barcode sticker located on the physical motherboard inside the TV chassis.

??? question "How do I re-enable the 'Shutdown / Power Off' option on the remote (Google TV / Android 14)?"
    On recent Google TV firmware builds, long-pressing the remote power button may only display "Restart". To bring back the full shutdown dialog:

    1. Go to **Settings** > **Display & Sound** (or **Picture**) > **Advanced Settings** > **Brightness**.
    2. Highlight **Contrast** (do not click into it).
    3. Type **`6425`** on your remote keypad (or use the `123` virtual keypad button).
    4. In the service menu, find **Shutdown Config** (or **Shutdown**) and toggle it to **`ON`**.
    5. Press **Back** or **Home** to exit. Long-pressing the remote power button will now offer **Shut down**, **Restart**, and **Cancel**.

??? question "How do I exit Factory Mode / P-Mode (Red 'P' or 'M' on screen)?"
    If your TV displays a red letter "P" or "M" in the corner (Factory / Warm-up mode):

    1. Go to **Settings** > **Picture** > **Advanced** > **Brightness** > highlight **Contrast**.
    2. Type **`9735`** on your remote to open the Factory Menu.
    3. Select **9-Sita P mode** and toggle it to **`OFF`**.
    4. Also check **Factory Hotkey** and set it to **`Disable / OFF`**.
    5. Exit the menu and restart your TV.

??? question "Why is my screen black after flashing or changing Project ID?"
    A black screen occurs when the installed firmware lacks your specific TV's **Project ID** in its internal whitelist (e.g. flashing older firmware or China market firmware on a Global TV), or when the Project ID was accidentally changed:

    *   **Blind Recovery Method:** With the TV turned **ON** (status LED responds to remote), type `0 6 2 5 9 8` followed by `MENU` (or `OK`), then type your original **`[Project ID]`** and wait 10 seconds for the TV to reboot.
    *   **Recovery Flash:** Flash a recent verified **IMG / PKG** recovery file for your platform using the physical TV power button cold-boot method.

??? question "Why does my soundbar lose connection or have audio delay / echo with eARC?"
    HDMI eARC handshake issues can occur across various soundbars (Samsung, Sonos, Klipsch, TCL):

    1.  **Audio Output Mode:** In TV Settings > Sound > Advanced > Digital Audio Out, switch from **Auto** to **Pass-Through** (or PCM for standard stereo).
    2.  **Full Power Cycle:** Unplug the power cables of **both** the TV and the soundbar from the wall for at least 1 minute to clear the HDMI CEC/eARC handshake cache, then reconnect.
    3.  **Update Soundbar:** Ensure your soundbar is updated to its latest vendor firmware.
    4.  **Tutti Choral Mode:** On models supporting simultaneous TV + Soundbar audio (Tutti Choral), if an echo occurs, set audio output to dedicated **eARC** instead.

??? question "Why is my TV's Ethernet speed limited to ~100 Mbps?"
    All TCL TV motherboards (as with almost all modern smart TVs across all brands) are equipped with a physical **100 Mbps Fast Ethernet** LAN port:

    *   For speeds above 100 Mbps (200–400+ Mbps), use **5GHz Wi-Fi (802.11ac / Wi-Fi 6)**.
    *   Alternatively, connect a compatible **USB 3.0 to Gigabit Ethernet adapter** to the TV's USB 3.0 port.
    *   **Important:** When using Wi-Fi, always ensure the physical LAN cable is unplugged from the TV.

??? question "Why can't my TV see my 5GHz Wi-Fi network?"
    TCL Wi-Fi controllers prioritize standard non-DFS channels:

    1.  **Lower 5GHz Channels:** In your router settings, set the 5GHz Wi-Fi channel manually to **Channel 36, 40, 44, or 48** (or channel 149+). High DFS channels (52–144) are frequently not recognized.
    2.  **Unplug Ethernet:** If a LAN cable is plugged into the TV, the TV may disable Wi-Fi discovery until disconnected.

??? question "How do I pair my Bluetooth remote control?"
    If your voice remote loses Bluetooth connection or you replaced the remote:

    1. Bring the remote within **1 meter** of the TV.
    2. Press and hold the **`OK` + `Home`** buttons simultaneously (or on some remotes **`Home` + `Back`**) for 5–7 seconds until the remote's LED flashes.
    3. Follow the pairing prompt on screen or verify under **Settings** > **Remotes & Accessories**.

??? question "How do I enter Service Menu codes if my remote has no number buttons?"
    1.  Press the **`123`** virtual keyboard button on the TCL remote to open the on-screen numeric keypad.
    2.  Alternatively, use a mobile remote app such as **Google Home** or **TCL Home / MagiConnect** to type the 4-digit code.

??? question "Is my firmware version outdated?"
    Firmware versions follow the `VXXX` scheme (e.g., `V560`, `V643`, `V655`).

    *   **Higher number indicates newer build:** `V655` is newer than `V643` and `V560`.
    *   **Prefixes:** `V` = Release / Stable, `R` = Test / Release Candidate, `M` = Pre-production.
    *   Check **[@FirmwareTCLbot](https://t.me/FirmwareTCLbot)** to query the latest verified official OTA and IMG files for your platform.

??? question "My TV is sluggish. How do I speed it up?"
    1.  **Apps Only Mode (GTV):** Go to **Settings** > **Accounts & Sign-in** > select your profile > enable **Apps only mode** to disable heavy background home screen recommendation feeds.
    2.  **Animation Scales:** In **Developer Options**, set *Window animation scale*, *Transition animation scale*, and *Animator duration scale* to **0.5x** or **Off**.
    3.  **Safety Guard / Device Manager:** Use the built-in **Quick Speedup** tool and clear system cache regularly.
    4.  **Shop Reset:** If persistent lag occurs after a major Android OS version upgrade (e.g. Android 12 to 14), perform a **Reset All / Reset Shop** via service code `6425`.

??? question "What is the Game Bar / Game Master?"
    The **Game Bar** (available on Pentonic 700 / T653 / T615 models) provides real-time information and quick settings for Refresh Rate (Hz), VRR status, ALLM, and HDR during gaming over HDMI 2.1:

    *   **Access:** Long-press the **Settings** (gear) or **Menu** (three horizontal lines) button on the remote while an active game console or PC HDMI source is selected.

??? question "How do I downgrade my firmware?"
    <a id="how-to-downgrade"></a>
    Downgrading is possible but requires strict adherence to safety rules:

    *   **Requirement:** You **must** use a full **IMG / PKG** file. (OTA `.zip` files cannot be used for downgrading).
    *   **Data Loss:** An IMG/PKG flash performs a complete low-level storage wipe.
    *   **Project ID Safety:** Never downgrade to a firmware version older than the initial release of your TV model, or the TV will boot to a black screen due to missing panel whitelists.
    *   **Instructions:** Follow our detailed [IMG / PKG Flashing Guide](guides.md#how-to-flash-img-pkg-recovery-downgrade).
