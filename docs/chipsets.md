# Hardware Architecture & Platforms

Identifying your TV's hardware platform (SoC) is the most critical step before downloading any firmware. Installing a file for the wrong platform will fail at best and brick your TV at worst.

## :material-timeline: Platform Mapping (2026 Sync)

TCL platforms are generally grouped by the year of the model release. Use this table as a reference, but always verify your specific Project ID.

### 2024 - 2026 (Modern Era)

| Platform Family | Specific IDs | Featured Models | Notes / 2025 ID |
| :--- | :--- | :--- | :--- |
| **Pentonic 800** | — | — | **0015T01** (Upcoming) |
| **T800 / Pentonic 700** | T800T02, MT9653 | X955 Max, C965, C855 | **0013T02** |
| **T655 / T653** | T655T01, T653T01..T03 | C655, C655 PRO, C765, P755 | **0012T01..T03** |
| **T615** | T615T01..T03 | C645 (Late), P745 | 2024 Entry-Mid range |
| **T221** | T221T01..T07, T221T09 | S55H, S5200 (Late) | **0003T05..T09** |

### Legacy & Specialist

| Platform ID | Traditional Name | Featured Models | 2025 ID (if any) |
| :--- | :--- | :--- | :--- |
| **R75P** | R75PT01 | Specialist Display | **0008T01** |
| **RT51 / AT51** | R51AT01 | P725, C725 | — |
| **R51M / R851** | R51MT01..T10 | C645, C635, P745 | — |
| **MT9615** | MT9615 | C845, C835, C735 | — |
| **R41K** | R41KT01 | S6500 Series | — |

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
## :material-settings-helper: Finding your Platform ID

For detailed instructions on how to locate your Project ID, Platform Name, and Version (including 2025 formats), please refer to our **[Firmware Identification Guide](guides.md#identify-your-firmware-platform)**.

!!! tip "Full ID Search"
    If your specific ID is not listed in the tables above, use the **[@FirmwareTCLbot](https://t.me/FirmwareTCLbot)**. You can search by Model Number or Platform String for instant results.
