# Platforms & Chipsets

Identifying your TV's hardware **Platform** (SoC) is the most critical step before downloading any firmware. Installing a file for the wrong platform will fail at best and brick your TV at worst.

## :material-timeline: Platform Mapping (2026 Sync)

TCL platforms are grouped by System-on-Chip (SoC) hardware families and year of release. Always verify your specific **Platform** from the TV menu before downloading.

!!! warning "Platform & Project ID Verification"
    Installing firmware that is older than your TV's factory version, or installing firmware that does not include your model's **Project ID** in its whitelist, can result in a **black screen** or bootloop. Always use verified firmware compatible with your platform and region.

### Modern & Legacy Platforms

| Platform Family | Specific IDs / TV Menu ID | Featured Models | Hardware / SoC Specs |
| :--- | :--- | :--- | :--- |
| **Pentonic 800** | **0015T01** (`T655T01`, `0015T02`) | X11L, C8L, RM9L, QM8L (2026) | MediaTek MT9655 (MT55), Flagship 4K Mini-LED |
| **Pentonic 700 (Global/EU)** | **0012T01** (`T653T01`) | X955, X955 Max (115"), C955, C855, C805, C765, C755, C745X2, C845X2, C7L, C6L, RM7L, X11K, C9K, C8K, C7K, C6K, P8K, T8C, 98C655, 85C655Pro, 98P745, 98P755 | MediaTek MT9653 / MT9618 (MT53), 4K 144Hz VRR |
| **Pentonic 700 (NA/LA)** | **0012T02** (`T653T02`) | QM891G, QM851G, QM751G, Q651G, Q750G, S551G, RM7L, QM7L, Q77L, X11K, QM8K, QM7K, Q77K, QM6K, QM67K | MediaTek Pentonic 700 (G08 / N. America & LATAM) |
| **Pentonic 700 (Flagship)** | **0012T03** (`T653T03`) | QM9K Series | MediaTek Pentonic 700 (G16) |
| **Pentonic 600** | **0014T01** (`T658T01`) | C655 (Selected AP/LA Releases) | MediaTek MT9658 (Pentonic 600) |
| **G15 Platform** | **0016T01** | P8L, P8LS, U75/A/85A, A400/M/U/PRO (AP & LA), P8K, C6K (AP) | 4K Google TV (G15 Platform) |
| **Next-Gen G17** | **0017T01** | Upcoming 2026/2027 Lineup | 4K Flagship Google TV (G17 Platform) |
| **Next-Gen G18** | **0018T01** | Upcoming Future Lineup | 4K Flagship Google TV (G18 Platform) |
| **T800 (Amlogic G09)** | **0013T02** (`T800T02`, `0013T01`, `0013T03`) | C655, C655 Pro, P755, T7B, P7K, C6KS, 55P755 | Amlogic AMLT963D4 (G09, 5-Core A55 @ 1.5GHz / 1.9GHz DVFS, Mali-G57 MC1, 2GB DDR4-3200) |
| **T615 / MT9615 (Global/EU)** | **T615T01** | C845, C835, C735, C825, C728, C645 (Late), P745 | MediaTek MT9615 (4K 120/144Hz) |
| **T615 / MT9615 (NA)** | **T615T02** | Q7 (2023 NA Series) | MediaTek MT9615 (4K 120/144Hz NA) |
| **T615 / MT9615 (R646)** | **T615T03** | R646 (2021 Flagship Mini-LED) | MediaTek MT9615 (4K 120/144Hz Mini-LED) |
| **R75P / RT75 (Global/EU)** | **0008T01** (`R75PT01`, `0008T02`) | P8LS, P7L, V6D, T6D, U65A, P6K, P7K, V6C, T6C, C6KS, C6CS, U65/75, MQLED70K, P755, C655, C655 Pro, T7B, V6B, QLED780/810, QM51L, QM5K, Q51K, Q63K, S551G, Q651G | Realtek RT75 (G10 Platform, Entry-Mid 4K GTV) |
| **T221 / MT21 (Google TV)** | **0003T05** (`T221T01`) | S350G, S55H, 32S5400, S5400A (Google TV) | MediaTek MT21 (2K / FHD Google TV) |
| **T221 / MT21 (Android TV)** | **0003T06** (`T221T02`) | S5200 (Late), 32S5400 (Android TV) | MediaTek MT21 (2K / FHD Android TV) |
| **R51M (Google TV)** | **R51MT05** | C645, C635, P745 (Google TV) | Realtek RTD2851 / R51M (4K Google TV) |
| **R851 (Google TV)** | **R851T02** | C728, C825, C735 (Early Google TV) | Realtek RTD2851 / R851 (4K Google TV) |
| **R51M (Android TV)** | **R51MT02** (`R51MT06`, `R51MT10`) | C715, C815, P715 (Android TV) | Realtek RTD2851 / R51M (4K Android TV) |
| **R851 (Android TV)** | **R851T10** | C715, C815 (Android TV) | Realtek RTD2851 / R851 (4K Android TV) |
| **RT51 / AT51** | **R51AT01** | P725, C725, P615, P635 | Realtek RT51 (Legacy Android TV) |
| **R41K** | **R41KT01** | S6500 Series, 32S60AI, ES560 | Realtek RTD2841K Entry Legacy (Android TV 9/11) |
| **MS6886 (MS88)** | **MS6886T02** (`MS6886T01`, `MS6886`) | EC780, X815, C815 (Early), EP680 | MStar MSD6886 (4K Android TV 9/11) |
| **MS6586 (MS86)** | **MS6586T02** (`MS6586T01`, `MS6586`) | C2, P2, P6, C4, C6, DP660, EP640, EP660 | MStar MSD6586 (4K Android TV 7/8/9) |
| **MS6488 (MS84)** | **MS6488T01** (`MS6488`, `MS84`) | C1, P1 Series | MStar MSD6488 (4K Legacy Android TV 7/8) |
| **MS48ES (MS48)** | **MS48EST01** (`MS48ES`, `MS48`) | S6000, S6800, F40, F50 | MStar MS48 (2K FHD Legacy Android TV 7/8) |
| **Novatek NT67** | **NT67T01** (`NT67`) | Thomson / TCL Regional Android TV Series | Novatek NT72671 / NT72673 (Android TV) |

---

## :material-earth: Regional Platform Mapping (NA vs. Global / EU)

TCL uses different marketing names across North America, Europe, Latin America, and Asia-Pacific. The internal platforms and firmware families, however, are shared:

| North America (NA) | Global / EU / AP Equivalent | Platform ID | Chassis / SoC |
| :--- | :--- | :--- | :--- |
| **QM8L (2026)** | **C8L / X11L** | **T655T01 (`0015T01`)** | Pentonic 800 (MT55) |
| **QM7L / QM6L (2026)** | **C7L / C6L / RM7L** | **T653T01 / T02 (`0012T01 / T02`)** | Pentonic 700 (MT53 / G08) |
| **QM8 (2024) / QM851G / QM891G** | **X955 / X955 Max / C955** | **T653T01 / T02 (`0012T01 / T02`)** | Pentonic 700 (MT9653 / MT9618) |
| **QM7 (2024) / QM751G** | **C855 / C805 / C755** | **T653T01 / T02 (`0012T01 / T02`)** | Pentonic 700 (MT9653) |
| **Q7 (2023) / Q750G** | **C745 / C755** | **MT9615 / T653** | MT9615 / Pentonic 700 |
| **Q651G / S551G** | **C655 / P755** | **R75PT01 (`0008T01`) / T800T02 (`0013T02`)** | RT75 (G10) / Amlogic (G09) |
| **R646 (2021)** | **C825** | **T615T03** | MT9615 |
| **S546 (2021)** | **C725** | **R51AT01** | RT51 |

!!! important "Verify Platform & Region Restrictions"
    Firmware is compiled for specific platform architectures and regional Project ID tables. Chinese market (CN) firmware and Global/EU firmware cannot be cross-installed (doing so results in a black screen or recovery loop due to missing Project IDs).

---

## :material-form-textbox-password: Decoding Firmware Names

Firmware files follow a standardized naming syntax:

### Example: `V8-0012T01-LF1V655.003254` (or `V8-T653T01-LF1V655`)

1. **`V8`**: Standard prefix identifier for TCL Smart TV software.
2. **`0012T01` / `T653T01`**: The **Platform**. Must match your TV's SoC platform.
3. **`LF1`**: Region / Language configuration package (e.g., `LF1`, `LF2`, `LA`, `AU`).
4. **Release Type & Version (`V655`)**:
    * **`V`**: Release / Production version (Stable public OTA/IMG).
    * **`R`**: Test / Release candidate build.
    * **`M`**: Early manufacturing / pre-production test build.
5. **`.003254`**: Internal revision build number (higher indicates newer compilation).

---

## :material-identifier: Platform vs. Project ID vs. Panel ID

Understanding the hierarchy of identifiers prevents flashing mistakes:

1. **Platform (SoC):** The processor and system motherboard family (e.g. `T653T01`, `0012T01`, `T800T02`). Firmware must match this exactly.
2. **Project ID (Panel ID / Configuration ID):** A 1-to-6 digit number stored in non-volatile memory (NVM). It configures the panel timing, backlight zones, color matrix, tuner frequencies (DVB-T2/S2/ATSC), and regional update channels.
3. **Firmware Version:** The software build version (e.g. `V560`, `V643`, `V655`).

!!! tip "Searching via Firmware Bot"
    You can query the **[@FirmwareTCLbot](https://t.me/FirmwareTCLbot)** using your **Platform String** (e.g. `T653T01`, `0012T01`, `T800T02`, `R75PT01`) to view the latest verified OTA and IMG/PKG downloads.
