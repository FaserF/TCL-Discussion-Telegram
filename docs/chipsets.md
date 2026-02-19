# Platforms & Chipsets

Identifying your TV's hardware **Platform** (SoC) is the most critical step before downloading any firmware. Installing a file for the wrong platform will fail at best and brick your TV at worst.

## :material-timeline: Platform Mapping (2026 Sync)

TCL platforms are generally grouped by the year of the model release. Use this table as a reference, but always verify your specific **Platform**.

!!! warning "Platform Verification"
    Installing firmware that is too old for your model, even if the platform seems to match, can brick your TV if the firmware doesn't recognize your specific model or Project ID. Always use the latest verified firmware from the bot or community.

### 2024 - 2026 (Modern Era)

### Modern & Legacy Platforms

| Platform Family | Specific IDs | Featured Models | Notes / 2025 ID |
| :--- | :--- | :--- | :--- |
| **Pentonic 800** | — | — | **0015T01** (Upcoming) |
| **T800 / Pentonic 700** | T800T02, MT9653 | X955 Max, C965, C855 | **0013T02** |
| **T655 / T653** | T655T01, T653T01..T03 | C655, C655 PRO, C765, P755, R75P | **0012T01..T03**, **0008T01** |
| **T615** | T615T01..T03 | C645 (Late), P745 | 2024 Entry-Mid range |
| **T221** | T221T01..T07, T221T09 | S55H, S5200 (Late) | **0003T05..T09** |
| **RT51 / AT51** | R51AT01 | P725, C725 | Legacy Android |
| **R51M / R851** | R51MT01..T10 | C645, C635, P745 | Legacy GTV |
| **MT9615** | MT9615 | C845, C835, C735 | High-end Legacy |
| **R41K** | R41KT01 | S6500 Series | Entry Legacy |

---

## :material-earth: Regional Platform Mapping (NA vs. Global)

TCL uses significantly different marketing names in North America compared to Europe and the rest of the world (Global). The firmware platforms, however, are often identical.

| North America (NA) | Global / EU Equivalent | Platform ID (Common) |
| :--- | :--- | :--- |
| **QM8 (2024)** | **X955 / C955** | **Pentonic 700 (MT9653)** |
| **QM7 (2024)** | **C855 / C805** | **Pentonic 700 (MT9653)** |
| **Q7 (2023)** | **C745 / C755** | **MT9615 / Pentonic 700** |
| **R646 (2021)** | **C825** | **MT9615** |
| **S546 (2021)** | **C725** | **RT51** |

!!! important "Verify Platform"
    Always verify your **Platform** before flashing. Even if the platform family matches, installing firmware not designed for your specific regional hardware can lead to failures.

!!! note "What is a 'Platform'?"
    The Platform (e.g., T653, RT51) refers to the underlying System-on-Chip (SoC) and hardware architecture of your TV. It is distinct from the **Project ID**, which identifies specific panel and model configurations.

---

## :material-form-textbox-password: Decoding Firmware Names

Firmware files follow a strict naming convention:

### Example: `V8-R51MT05-LF1V615`

1.  **Release Type**:
    *   **`V`**: Release Version (Stable/Public)
    *   **`R`**: Test Version (Community/Beta)
    *   **`M`**: Pre-production Version (Initial Launch)
2.  **`V8`**: Standard prefix for Smart TV firmware.
3.  **`R51MT05`**: The **Platform**. This must match your device exactly.
4.  **`LF1`**: Region / Language indicator.
5.  **`V615`**: The version number.

---

## :material-settings-helper: Locating your Platform information

For detailed instructions on how to locate your **Platform Name** and **Version** (including 2025 formats), please refer to our **[Firmware Identification Guide](guides.md#identify-your-firmware-platform)**.

### About Project IDs
The **Project ID** is an internal identifier that can be any positive integer (typically 1 to 6 digits). While important for advanced configuration, your primary focus for firmware selection must always be the **Platform**.

!!! tip "Full ID Search"
    If your specific information is not listed in the tables above, use the **[@FirmwareTCLbot](https://t.me/FirmwareTCLbot)**. You can search by **Platform String** for instant results and verification of compatible models.
