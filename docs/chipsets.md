# Hardware Architecture & Platforms

Identifying your TV's hardware platform (SoC) is the most critical step before downloading any firmware. Installing a file for the wrong platform will fail at best and brick your TV at worst.

## :material-timeline: Platform Mapping (2026 Sync)

TCL platforms are generally grouped by the year of the model release. Use this table as a reference, but always verify your specific Project ID.

### 2024 - 2026 (Modern Era)

| Platform Family | Specific IDs | Featured Models | Notes |
| :--- | :--- | :--- | :--- |
| **Pentonic 800** | T800T02 | X955 Max, C965 | Hyper-Premium (2025/26) |
| **T655 / T653** | T655T01, T653T01, T653T02, T653T03 | C655, C655 PRO, C765, P755, T8B | 2024/25 Performance Class |
| **T615** | T615T01, T615T02, T615T03 | C645 (Late), P745 | 2024 Entry-Mid range |
| **T221** | T221T01..T07, T221T09 | S55H, S5200 (Late) | 2025 Entry/Monitor Class |

### 2022 - 2023 (Google TV Era)

| Platform Family | Specific IDs | Featured Models | OS Version |
| :--- | :--- | :--- | :--- |
| **Pentonic 700** | MT9653 | X955, C955, C855, C805, C755 | Google TV 11/12 |
| **R51M / R851** | R51MT01..T08, R851T02, R851T03, R851T10 | C645, C635, P745, P735 | Google TV 11 |
| **MT9615** | MT9615 | C845, C835, C735, C825, C728 | Google TV 11 |

### Legacy & Specialist

| Platform ID | Chipset (SoC) | Featured Models | Status |
| :--- | :--- | :--- | :--- |
| **R41K** | R41KT01 | S6500 Series | Legacy Android TV |
| **R75P** | R75PT01 (0008T01) | Specialist Display | Hardware Revision |
| **RT51 / AT51** | R51AT01 | P725, C725 | Transition Era |

---

## :material-earth: Regional Rosetta Stone (NA vs. Global)

TCL uses significantly different marketing names in North America compared to Europe and the rest of the world (Global). The firmware platforms, however, are often identical.

| North America (NA) | Global / EU Equivalent | Platform ID (Common) |
| :--- | :--- | :--- |
| **QM8 (2024)** | **X955 / C955** | **Pentonic 700 (MT9653)** |
| **QM7 (2024)** | **C855 / C805** | **Pentonic 700 (MT9653)** |
| **Q7 (2023)** | **C745 / C755** | **MT9615 / Pentonic 700** |
| **R646 (2021)** | **C825** | **MT9615** |
| **S546 (2021)** | **C725** | **RT51** |

!!! important "Verify Project ID"
    Always verify your **Project ID** before flashing. Even if the platform matches, a mismatched Project ID can lead to inverted screens or disabled features.

---

## :material-form-textbox-password: Decoding Firmware Names

Firmware files follow a strict naming convention:

### Example: `V8-R51MT05-LF1V615`

1.  **Release Type**:
    *   **`V`**: Release Version (Stable/Public)
    *   **`R`**: Test Version (Community/Beta)
    *   **`M`**: Pre-production Version (Initial Launch)
2.  **`V8`**: Standard prefix for Smart TV firmware.
3.  **`R51MT05`**: The **Platform ID**. This must match your device exactly.
4.  **`LF1`**: Region / Language indicator.
5.  **`V615`**: The version number.

---

## :material-settings-helper: How to find your Platform ID

### Method 1: The "Contact Us" Menu

1.  Navigate to **Settings** > **System** > **About** > **Contact Us**.
2.  Look for the **Project ID** or **Firmware Version**.
3.  The string will start with something like `V8-R51...` or `V8-T61...`.

### Method 2: System Version String

1.  Navigate to **Settings** > **System** > **About** > **Software Version**.
2.  The full string contains the platform name.

!!! tip "Identify Chipset"
    If your Project ID doesn't appear in the timeline above, please visit the **[@FirmwareTCLbot](https://t.me/FirmwareTCLbot)**. Send your Model Number to the bot for an instant identification.
