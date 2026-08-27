---
title: TCL Smart TV Firmware Hub
description: Official, comprehensive firmware tracker and package repository for all global TCL Android TV and Google TV platforms.
---

# 📡 TCL Smart TV Firmware Hub

Welcome to the official **TCL Smart TV Firmware Hub**. This catalog tracks, aggregates, and validates official firmware releases across all known TCL hardware platforms globally. Data is synchronized directly with official TCL FOTA upgrade servers (`huan.tv`) and high-speed Content Delivery Networks (`cedock.com`).

> 💡 **Automated Verification & Integrity Guarantee**  
> All firmware binaries listed below are verified through server-side MD5 signatures, SHA-256 cryptographic hashes, and IEEE 802.3 32-bit CRC32 checksums. Deep technical build properties are extracted via non-destructive byte-range inspection.

*Last database update: `2026-08-27T15:02:11.858517+00:00` UTC*

---

## 📑 Quick Platform Index

| Platform ID | Family / Chassis | Latest Firmware | OS Flavor | Release Date | Checksums (MD5 · SHA256 · CRC32) | Direct Download |
|---|---|---|:---:|:---:|---|:---:|
| [`0003T05`](#platform-0003t05) | **T221 / MT21 (Google TV) (0003T05)** | `V8-0003T05-LF1V242` | `—` | `2026-06-15` | `e61c1f51...` · `db01e98b...` · `0x3712D508` | [:material-download: OTA (ZIP)](http://eu-update.cedock.com/apps/resource2/V80003T05/V8-0003T05-LF1V242/FOTA-OTA/V8-0003T05-LF1V242.zip) |
| [`0003T06`](#platform-0003t06) | **T221 / MT21 (Android TV) (0003T06)** | `V8-0003T06-LF1V085` | `—` | `2026-06-15` | `4c06228d...` · `d3a6a1e0...` · `0x9063AAC6` | [:material-download: OTA (ZIP)](http://eu-update.cedock.com/apps/resource2/V80003T06/V8-0003T06-LF1V085/FOTA-OTA/V8-0003T06-LF1V085.zip) |
| [`0008T01`](#platform-0008t01) | **R75P / RT75 (Global/EU) (0008T01)** | `V8-0008T01-LF1V636` | `Android 12` | `2026-08-07` | `a5712354...` · `8e21687d...` · `0xCF291DE2` | [:material-download: OTA (ZIP)](http://eu-update.cedock.com/apps/resource2/V80008T01/V8-0008T01-LF1V636/FOTA-OTA/V8-0008T01-LF1V636.622816.zip) |
| [`0012T01`](#platform-0012t01) | **Pentonic 700 (Global/EU) (0012T01)** | `V8-0012T01-LF1V655` | `Android 12` | `2026-01` | `e0573619...` · `00357ef7...` · `0xF241FE0D` | [:material-download: OTA (ZIP)](http://eu-update.cedock.com/apps/resource2/V80012T01/V8-0012T01-LF1V655/FOTA-OTA/V8-0012T01-LF1V655.628400.zip) |
| [`0012T02`](#platform-0012t02) | **Pentonic 700 (NA/LA) (0012T02)** | `V8-0012T02-LF1V620` | `Android 12` | `2025-11` | `aaf24d60...` · `3a332afe...` · `0x08739BC3` | [:material-download: OTA (ZIP)](http://na-update.cedock.com/apps/resource2/V80012T02/V8-0012T02-LF1V620/FOTA-OTA/V8-0012T02-LF1V620.439617.zip) |
| [`0012T03`](#platform-0012t03) | **Pentonic 700 (Flagship) (0012T03)** | `V8-0012T03-LF1V110` | `Android 12` | `2025-10` | `c5d75c11...` · `68715a05...` · `0xD9A29CE7` | [:material-download: OTA (ZIP)](http://eu-update.cedock.com/apps/resource2/V80012T03/V8-0012T03-LF1V110/FOTA-OTA/V8-0012T03-LF1V110.877669.zip) |
| [`0013T02`](#platform-0013t02) | **T800 (Amlogic G09) (0013T02)** | `V8-0013T02-LF1V163` | `Android 12` | `2025-08` | `e868ca24...` · `9f1fa9fe...` · `0xDE45B257` | [:material-download: OTA (ZIP)](http://eu-update.cedock.com/apps/resource2/V80013T02/V8-0013T02-LF1V163/FOTA-OTA/V8-0013T02-LF1V163.941121.zip) |
| [`0014T01`](#platform-0014t01) | **Pentonic 600 (0014T01)** | `V8-0014T01-LF1V001` | `Android 12` | `2026-04-15` | `6ab8bcb0...` · `29089377...` · `0xBE1D6323` | [:material-download: OTA (ZIP)](http://eu-update.cedock.com/apps/resource2/V80014T01/V8-0014T01-LF1V001/FOTA-OTA/V8-0014T01-LF1V001.341571.zip) |
| [`0015T01`](#platform-0015t01) | **Pentonic 800 (0015T01)** | `V8-0015T01-LF1V025` | `Android 14` | `2026-02` | `89b01dae...` · `95edd608...` · `0xE46C147A` | [:material-download: OTA (ZIP)](http://eu-update.cedock.com/apps/resource2/V80015T01/V8-0015T01-LF1V025/FOTA-OTA/V8-0015T01-LF1V025.156484.zip) |
| [`0016T01`](#platform-0016t01) | **G15 Platform (0016T01)** | `V8-0016T01-LF1V042` | `Android 12` | `2026-03` | `f7c9b771...` · `c2d41ccd...` · `0xE56EA4C9` | [:material-download: OTA (ZIP)](http://eu-update.cedock.com/apps/resource2/V80016T01/V8-0016T01-LF1V042/FOTA-OTA/V8-0016T01-LF1V042.779776.zip) |
| [`0017T01`](#platform-0017t01) | **Next-Gen G17 (0017T01)** | `V8-0017T01-LF1V001` | `Android 11` | `2026-08-01` | `88fc0377...` · `4d6cf740...` · `0x63E27B9A` | [:material-download: OTA (ZIP)](http://eu-update.cedock.com/apps/resource2/V80017T01/V8-0017T01-LF1V001/FOTA-OTA/V8-0017T01-LF1V001.397994.zip) |
| [`0018T01`](#platform-0018t01) | **Next-Gen G18 (0018T01)** | `V8-0018T01-LF1V001` | `—` | `—` | — · `0a19bf5d...` · `0x5150E507` | [:material-download: OTA (ZIP)](http://eu-update.cedock.com/apps/resource2/V80018T01/V8-0018T01-LF1V001/FOTA-OTA/V8-0018T01-LF1V001.zip) |
| [`MS48EST01`](#platform-ms48est01) | **MS48ES (MS48) (MS48EST01)** | `V8-MS48EST01-LF1V001` | `Android 11` | `2023-05-14` | `e7e97e82...` · `d1481303...` · `0x0DFE8680` | [:material-download: OTA (ZIP)](http://eu-update.cedock.com/apps/resource2/V8MS48EST01/V8-MS48EST01-LF1V001/FOTA-OTA/V8-MS48EST01-LF1V001.320761.zip) |
| [`MS6488T01`](#platform-ms6488t01) | **MS6488 (MS84) (MS6488T01)** | `V8-MS6488T01-LF1V001` | `Android 11` | `2023-05-14` | `56a42bdb...` · `3b5e0c56...` · `0x82E66CAE` | [:material-download: OTA (ZIP)](http://eu-update.cedock.com/apps/resource2/V8MS6488T01/V8-MS6488T01-LF1V001/FOTA-OTA/V8-MS6488T01-LF1V001.609016.zip) |
| [`MS6586T02`](#platform-ms6586t02) | **MS6586 (MS86) (MS6586T02)** | `V8-MS6586T02-LF1V001` | `Android 11` | `2023-05-14` | `8bd785fb...` · `c14e9c9a...` · `0xD603A75F` | [:material-download: OTA (ZIP)](http://eu-update.cedock.com/apps/resource2/V8MS6586T02/V8-MS6586T02-LF1V001/FOTA-OTA/V8-MS6586T02-LF1V001.639602.zip) |
| [`MS6886T02`](#platform-ms6886t02) | **MS6886 (MS88) (MS6886T02)** | `V8-MS6886T02-LF1V001` | `Android 11` | `2023-05-14` | `e46c49fe...` · `17b86d45...` · `0xD5F2134A` | [:material-download: OTA (ZIP)](http://eu-update.cedock.com/apps/resource2/V8MS6886T02/V8-MS6886T02-LF1V001/FOTA-OTA/V8-MS6886T02-LF1V001.496968.zip) |
| [`NT67T01`](#platform-nt67t01) | **Novatek NT67 (NT67T01)** | `V8-NT67T01-LF1V001` | `Android 11` | `2026-03-20` | `173d73e5...` · `5610eb43...` · `0x034E01ED` | [:material-download: OTA (ZIP)](http://eu-update.cedock.com/apps/resource2/V8NT67T01/V8-NT67T01-LF1V001/FOTA-OTA/V8-NT67T01-LF1V001.962089.zip) |
| [`R41KT01`](#platform-r41kt01) | **R41K (R41KT01)** | `V8-R41KT01-LF1V343` | `Android 11` | `2022-11` | `3f2c5fd7...` · `adfb1eb4...` · `0x343B8CE0` | [:material-download: OTA (ZIP)](http://eu-update.cedock.com/apps/resource2/V8R41KT01/V8-R41KT01-LF1V343/FOTA-OTA/V8-R41KT01-LF1V343.945042.zip) |
| [`R51AT01`](#platform-r51at01) | **RT51 / AT51 (R51AT01)** | `V8-R51AT01-LF1V315` | `Android 11` | `2023-06` | `5fec0967...` · `cf720324...` · `0xFFAF3604` | [:material-download: OTA (ZIP)](http://eu-update.cedock.com/apps/resource2/V8R51AT01/V8-R51AT01-LF1V315/FOTA-OTA/V8-R51AT01-LF1V315.185337.zip) |
| [`R51MT02`](#platform-r51mt02) | **R51M (Android TV) (R51MT02)** | `V8-R51MT02-LF1V267` | `Android 11` | `2024-05` | `1e8aa588...` · `14441159...` · `0xC325D708` | [:material-download: OTA (ZIP)](http://eu-update.cedock.com/apps/resource2/V8R51MT02/V8-R51MT02-LF1V267/FOTA-OTA/V8-R51MT02-LF1V267.162390.zip) |
| [`R51MT05`](#platform-r51mt05) | **R51M (Google TV) (R51MT05)** | `V8-R51MT05-LF1V652` | `Android 11` | `2024-04` | `dc8cba08...` · `7a2542a0...` · `0x83A1D1B6` | [:material-download: OTA (ZIP)](http://eu-update.cedock.com/apps/resource2/V8R51MT05/V8-R51MT05-LF1V652/FOTA-OTA/V8-R51MT05-LF1V652.102029.zip) |
| [`R851T02`](#platform-r851t02) | **R851 (Google TV) (R851T02)** | `V8-R851T02-LF1V653` | `—` | `2026-06-15` | `eb435133...` · `9159d7b4...` · `0x842C574A` | [:material-download: OTA (ZIP)](http://eu-update.cedock.com/apps/resource2/V8R851T02/V8-R851T02-LF1V653/FOTA-OTA/V8-R851T02-LF1V653.zip) |
| [`R851T10`](#platform-r851t10) | **R851 (Android TV) (R851T10)** | `V8-R851T10-LF1V109` | `—` | `2026-06-15` | `22ba8521...` · `9ba6ff18...` · `0x88E1EA3E` | [:material-download: OTA (ZIP)](http://eu-update.cedock.com/apps/resource2/V8R851T10/V8-R851T10-LF1V109/FOTA-OTA/V8-R851T10-LF1V109.zip) |
| [`T615T01`](#platform-t615t01) | **T615 / MT9615 (Global/EU) (T615T01)** | `V8-T615T01-LF1V082` | `Android 11` | `2024-05` | `59ca23d8...` · `2341b055...` · `0xD08CFF8E` | [:material-download: OTA (ZIP)](http://eu-update.cedock.com/apps/resource2/V8T615T01/V8-T615T01-LF1V082/FOTA-OTA/V8-T615T01-LF1V082.176126.zip) |
| [`T615T02`](#platform-t615t02) | **T615 / MT9615 (NA) (T615T02)** | `V8-T615T02-LF1V073` | `Android 11` | `2024-04` | `f07a2972...` · `f3c352d1...` · `0x4185B600` | [:material-download: OTA (ZIP)](http://eu-update.cedock.com/apps/resource2/V8T615T02/V8-T615T02-LF1V073/FOTA-OTA/V8-T615T02-LF1V073.518224.zip) |
| [`T615T03`](#platform-t615t03) | **T615 / MT9615 (R646) (T615T03)** | `V8-T615T03-LF1V082` | `Android 11` | `2024-05` | `b2f53f98...` · `3f6c33a6...` · `0xA81C95B2` | [:material-download: OTA (ZIP)](http://eu-update.cedock.com/apps/resource2/V8T615T03/V8-T615T03-LF1V082/FOTA-OTA/V8-T615T03-LF1V082.502331.zip) |

---

## 🛠️ Detailed Platform Specifications & Package Downloads

<a id="platform-0003t05"></a>
#### T221 / MT21 (Google TV) (0003T05) (`V8-0003T05-LF1V242`)
- **Platform Identifier**: `0003T05` (Alternative ID: `T221T01`)
- **Hardware Architecture & SoC**: MediaTek MT21 (2K / FHD Google TV)
- **Compatible TV Models (Selection)**: *S350G, S55H, 32S5400, S5400A (Google TV)*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.92 GB` · **Release Date**: `2026-06-15` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `e61c1f5174aeb91dd31ebcad01a04a30`
- **SHA-256 Checksum**: `db01e98b5619836442cc40ba0b0f4a57a715e343f4642976477b4fde4ae4be1b`
- **CRC-32 Checksum**: `0x3712D508`
- **Firmware Packages & Downloads**:
  - 📦 **OTA Package (ZIP)** (for TV menu update): [V8-0003T05-LF1V242.zip](http://eu-update.cedock.com/apps/resource2/V80003T05/V8-0003T05-LF1V242/FOTA-OTA/V8-0003T05-LF1V242.zip) (`1.92 GB`)
  - 🛠️ **Recovery Image (PKG/IMG)**: *No separate factory recovery image on official servers (install via OTA ZIP).*
- **Official Changelog / Server Notes**: —
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V80003T05/V8-0003T05-LF1V242/FOTA-OTA/V8-0003T05-LF1V242.zip](http://eu-update.cedock.com/apps/resource2/V80003T05/V8-0003T05-LF1V242/FOTA-OTA/V8-0003T05-LF1V242.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V80003T05/V8-0003T05-LF1V242/FOTA-OTA/V8-0003T05-LF1V242.zip](http://na-update.cedock.com/apps/resource2/V80003T05/V8-0003T05-LF1V242/FOTA-OTA/V8-0003T05-LF1V242.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V80003T05/V8-0003T05-LF1V242/FOTA-OTA/V8-0003T05-LF1V242.zip](http://as-update.cedock.com/apps/resource2/V80003T05/V8-0003T05-LF1V242/FOTA-OTA/V8-0003T05-LF1V242.zip)

<a id="platform-0003t06"></a>
#### T221 / MT21 (Android TV) (0003T06) (`V8-0003T06-LF1V085`)
- **Platform Identifier**: `0003T06` (Alternative ID: `T221T02`)
- **Hardware Architecture & SoC**: MediaTek MT21 (2K / FHD Android TV)
- **Compatible TV Models (Selection)**: *S5200 (Late), 32S5400 (Android TV)*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.92 GB` · **Release Date**: `2026-06-15` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `4c06228d046707bcb00a1e43b74dd182`
- **SHA-256 Checksum**: `d3a6a1e06f427eba087bd5d58e0f679aacaa4c1f4b29f98ac32d8fa6cc4b5e17`
- **CRC-32 Checksum**: `0x9063AAC6`
- **Firmware Packages & Downloads**:
  - 📦 **OTA Package (ZIP)** (for TV menu update): [V8-0003T06-LF1V085.zip](http://eu-update.cedock.com/apps/resource2/V80003T06/V8-0003T06-LF1V085/FOTA-OTA/V8-0003T06-LF1V085.zip) (`1.92 GB`)
  - 🛠️ **Recovery Image (PKG/IMG)**: *No separate factory recovery image on official servers (install via OTA ZIP).*
- **Official Changelog / Server Notes**: —
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V80003T06/V8-0003T06-LF1V085/FOTA-OTA/V8-0003T06-LF1V085.zip](http://eu-update.cedock.com/apps/resource2/V80003T06/V8-0003T06-LF1V085/FOTA-OTA/V8-0003T06-LF1V085.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V80003T06/V8-0003T06-LF1V085/FOTA-OTA/V8-0003T06-LF1V085.zip](http://na-update.cedock.com/apps/resource2/V80003T06/V8-0003T06-LF1V085/FOTA-OTA/V8-0003T06-LF1V085.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V80003T06/V8-0003T06-LF1V085/FOTA-OTA/V8-0003T06-LF1V085.zip](http://as-update.cedock.com/apps/resource2/V80003T06/V8-0003T06-LF1V085/FOTA-OTA/V8-0003T06-LF1V085.zip)

<a id="platform-0008t01"></a>
#### R75P / RT75 (Global/EU) (0008T01) (`V8-0008T01-LF1V636`)
- **Platform Identifier**: `0008T01` (Alternative ID: `R75PT01`)
- **Hardware Architecture & SoC**: Realtek RT75 (G10 Platform, Entry-Mid 4K GTV)
- **Compatible TV Models (Selection)**: *P8LS, P7L, V6D, T6D, U65A, P6K, P7K, V6C, T6C, C6KS, C6CS, U65/75, MQLED70K, P755, C655, C655 Pro, T7B, V6B, QLED780/810, QM51L, QM5K, Q51K, Q63K, S551G, Q651G*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.92 GB` · **Release Date**: `2026-08-07` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `a5712354fc8723dd5c11afb2608f6091`
- **SHA-256 Checksum**: `8e21687d12671a678a12f3322498d3bcc1771c31fec9bf604ccf81f4f8a01121`
- **CRC-32 Checksum**: `0xCF291DE2`
- **Firmware Packages & Downloads**:
  - 📦 **OTA Package (ZIP)** (for TV menu update): [V8-0008T01-LF1V636.zip](http://eu-update.cedock.com/apps/resource2/V80008T01/V8-0008T01-LF1V636/FOTA-OTA/V8-0008T01-LF1V636.622816.zip) (`1.92 GB`)
  - 🛠️ **Recovery Image (PKG/IMG)**: *No separate factory recovery image on official servers (install via OTA ZIP).*
- **Official Changelog / Server Notes**: Android 14 Google TV (GTV U) release: Security patch 2026-06-05, G10_4K_US_NF AS50 release.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 12` (Google TV (GTV))
  - **GMS Package**: `Android_12_GTV`
  - **Security Patch Level**: `2026-08-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/0008T01/0008T01:12/V8-0008T01-LF1V001/user/release-keys`
  - **SDK API Level**: `31`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_0008t01`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V80008T01/V8-0008T01-LF1V636/FOTA-OTA/V8-0008T01-LF1V636.622816.zip](http://eu-update.cedock.com/apps/resource2/V80008T01/V8-0008T01-LF1V636/FOTA-OTA/V8-0008T01-LF1V636.622816.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V80008T01/V8-0008T01-LF1V636/FOTA-OTA/V8-0008T01-LF1V636.622816.zip](http://na-update.cedock.com/apps/resource2/V80008T01/V8-0008T01-LF1V636/FOTA-OTA/V8-0008T01-LF1V636.622816.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V80008T01/V8-0008T01-LF1V636/FOTA-OTA/V8-0008T01-LF1V636.622816.zip](http://as-update.cedock.com/apps/resource2/V80008T01/V8-0008T01-LF1V636/FOTA-OTA/V8-0008T01-LF1V636.622816.zip)

<details>
<summary><b>📦 Previous Firmware Versions Archive (1 build)</b></summary>

| Version | Release Date | Package Type & Size | Category | Changelog / Notes | Download Link |
|---|:---:|---|:---:|---|:---:|
| `V8-0008T01-LF1V630` | `2026-06-15` | `Full OTA (ZIP)` · `1.92 GB` | **Production (Stable)** | *—* | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V80008T01/V8-0008T01-LF1V630/FOTA-OTA/V8-0008T01-LF1V630.zip) |

</details>

<a id="platform-0012t01"></a>
#### Pentonic 700 (Global/EU) (0012T01) (`V8-0012T01-LF1V655`)
- **Platform Identifier**: `0012T01` (Alternative ID: `T653T01`)
- **Hardware Architecture & SoC**: MediaTek MT9653 / MT9618 (MT53), 4K 144Hz VRR
- **Compatible TV Models (Selection)**: *X955, X955 Max (115"), C955, C855, C805, C765, C755, C745X2, C845X2, C7L, C6L, RM7L, X11K, C9K, C8K, C7K, C6K, P8K, T8C, 98C655, 85C655Pro, 98P745, 98P755*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `2.35 GB` · **Release Date**: `2026-01` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `e0573619c0bb0f93afe2be6aeefb472a`
- **SHA-256 Checksum**: `00357ef7ec8897e71310013d22e713a03c9994578b357c7f065ee03328352403`
- **CRC-32 Checksum**: `0xF241FE0D`
- **Firmware Packages & Downloads**:
  - 📦 **OTA Package (ZIP)** (for TV menu update): [V8-0012T01-LF1V655.zip](http://eu-update.cedock.com/apps/resource2/V80012T01/V8-0012T01-LF1V655/FOTA-OTA/V8-0012T01-LF1V655.628400.zip) (`2.35 GB`)
  - 🛠️ **Recovery Image (PKG/IMG)**: *No separate factory recovery image on official servers (install via OTA ZIP).*
- **Official Changelog / Server Notes**: Android 12/14 Google TV: Dolby Vision IQ enhancements, Game Master 2.0 stability, 144Hz VRR optimizations.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 12` (Google TV (GTV))
  - **GMS Package**: `Android_12_GTV`
  - **Security Patch Level**: `2026-01-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/0012T01/0012T01:12/V8-0012T01-LF1V001/user/release-keys`
  - **SDK API Level**: `31`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_0012t01`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V80012T01/V8-0012T01-LF1V655/FOTA-OTA/V8-0012T01-LF1V655.628400.zip](http://eu-update.cedock.com/apps/resource2/V80012T01/V8-0012T01-LF1V655/FOTA-OTA/V8-0012T01-LF1V655.628400.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V80012T01/V8-0012T01-LF1V655/FOTA-OTA/V8-0012T01-LF1V655.628400.zip](http://na-update.cedock.com/apps/resource2/V80012T01/V8-0012T01-LF1V655/FOTA-OTA/V8-0012T01-LF1V655.628400.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V80012T01/V8-0012T01-LF1V655/FOTA-OTA/V8-0012T01-LF1V655.628400.zip](http://as-update.cedock.com/apps/resource2/V80012T01/V8-0012T01-LF1V655/FOTA-OTA/V8-0012T01-LF1V655.628400.zip)

<a id="platform-0012t02"></a>
#### Pentonic 700 (NA/LA) (0012T02) (`V8-0012T02-LF1V620`)
- **Platform Identifier**: `0012T02` (Alternative ID: `T653T02`)
- **Hardware Architecture & SoC**: MediaTek Pentonic 700 (G08 / N. America & LATAM)
- **Compatible TV Models (Selection)**: *QM891G, QM851G, QM751G, Q651G, Q750G, S551G, RM7L, QM7L, Q77L, X11K, QM8K, QM7K, Q77K, QM6K, QM67K*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `2.28 GB` · **Release Date**: `2025-11` · **Region**: `NA`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `aaf24d608a1866c214d95d91f92aaf2d`
- **SHA-256 Checksum**: `3a332afe7fe06e4b53b66ca3ac7edb51697b89066cafce5e8212d1d24174a931`
- **CRC-32 Checksum**: `0x08739BC3`
- **Firmware Packages & Downloads**:
  - 📦 **OTA Package (ZIP)** (for TV menu update): [V8-0012T02-LF1V620.zip](http://na-update.cedock.com/apps/resource2/V80012T02/V8-0012T02-LF1V620/FOTA-OTA/V8-0012T02-LF1V620.439617.zip) (`2.28 GB`)
  - 🛠️ **Recovery Image (PKG/IMG)**: *No separate factory recovery image on official servers (install via OTA ZIP).*
- **Official Changelog / Server Notes**: North American Google TV: QM851G/QM751G local dimming timing adjustments, ATSC 3.0 tuner stability.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 12` (Google TV (GTV))
  - **GMS Package**: `Android_12_GTV`
  - **Security Patch Level**: `2025-11-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/0012T02/0012T02:12/V8-0012T02-LF1V001/user/release-keys`
  - **SDK API Level**: `31`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_0012t02`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V80012T02/V8-0012T02-LF1V620/FOTA-OTA/V8-0012T02-LF1V620.439617.zip](http://eu-update.cedock.com/apps/resource2/V80012T02/V8-0012T02-LF1V620/FOTA-OTA/V8-0012T02-LF1V620.439617.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V80012T02/V8-0012T02-LF1V620/FOTA-OTA/V8-0012T02-LF1V620.439617.zip](http://na-update.cedock.com/apps/resource2/V80012T02/V8-0012T02-LF1V620/FOTA-OTA/V8-0012T02-LF1V620.439617.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V80012T02/V8-0012T02-LF1V620/FOTA-OTA/V8-0012T02-LF1V620.439617.zip](http://as-update.cedock.com/apps/resource2/V80012T02/V8-0012T02-LF1V620/FOTA-OTA/V8-0012T02-LF1V620.439617.zip)

<a id="platform-0012t03"></a>
#### Pentonic 700 (Flagship) (0012T03) (`V8-0012T03-LF1V110`)
- **Platform Identifier**: `0012T03` (Alternative ID: `T653T03`)
- **Hardware Architecture & SoC**: MediaTek Pentonic 700 (G16)
- **Compatible TV Models (Selection)**: *QM9K Series*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `2.41 GB` · **Release Date**: `2025-10` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `c5d75c11a51dae5dabf77e96dc205525`
- **SHA-256 Checksum**: `68715a058595b923cf1f931e4f894f2c3819af52b189756c9247aed06d730f85`
- **CRC-32 Checksum**: `0xD9A29CE7`
- **Firmware Packages & Downloads**:
  - 📦 **OTA Package (ZIP)** (for TV menu update): [V8-0012T03-LF1V110.zip](http://eu-update.cedock.com/apps/resource2/V80012T03/V8-0012T03-LF1V110/FOTA-OTA/V8-0012T03-LF1V110.877669.zip) (`2.41 GB`)
  - 🛠️ **Recovery Image (PKG/IMG)**: *No separate factory recovery image on official servers (install via OTA ZIP).*
- **Official Changelog / Server Notes**: G16 flagship chassis DSP audio processor updates and high-zone Mini-LED panel drive optimizations.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 12` (Google TV (GTV))
  - **GMS Package**: `Android_12_GTV`
  - **Security Patch Level**: `2025-10-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/0012T03/0012T03:12/V8-0012T03-LF1V001/user/release-keys`
  - **SDK API Level**: `31`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_0012t03`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V80012T03/V8-0012T03-LF1V110/FOTA-OTA/V8-0012T03-LF1V110.877669.zip](http://eu-update.cedock.com/apps/resource2/V80012T03/V8-0012T03-LF1V110/FOTA-OTA/V8-0012T03-LF1V110.877669.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V80012T03/V8-0012T03-LF1V110/FOTA-OTA/V8-0012T03-LF1V110.877669.zip](http://na-update.cedock.com/apps/resource2/V80012T03/V8-0012T03-LF1V110/FOTA-OTA/V8-0012T03-LF1V110.877669.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V80012T03/V8-0012T03-LF1V110/FOTA-OTA/V8-0012T03-LF1V110.877669.zip](http://as-update.cedock.com/apps/resource2/V80012T03/V8-0012T03-LF1V110/FOTA-OTA/V8-0012T03-LF1V110.877669.zip)

<a id="platform-0013t02"></a>
#### T800 (Amlogic G09) (0013T02) (`V8-0013T02-LF1V163`)
- **Platform Identifier**: `0013T02` (Alternative ID: `T800T02`)
- **Hardware Architecture & SoC**: Amlogic AMLT963D4 (G09, 5-Core A55 @ 1.5GHz / 1.9GHz DVFS, Mali-G57 MC1, 2GB DDR4-3200)
- **Compatible TV Models (Selection)**: *C655, C655 Pro, P755, T7B, P7K, C6KS, 55P755*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.82 GB` · **Release Date**: `2025-08` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `e868ca24e11ffcf319807d3bccc8d28e`
- **SHA-256 Checksum**: `9f1fa9fedd938ae690d2fee156c3e967a8d06254c59f4ac66b01c9e692fc3d47`
- **CRC-32 Checksum**: `0xDE45B257`
- **Firmware Packages & Downloads**:
  - 📦 **OTA Package (ZIP)** (for TV menu update): [V8-0013T02-LF1V163.zip](http://eu-update.cedock.com/apps/resource2/V80013T02/V8-0013T02-LF1V163/FOTA-OTA/V8-0013T02-LF1V163.941121.zip) (`1.82 GB`)
  - 🛠️ **Recovery Image (PKG/IMG)**: *No separate factory recovery image on official servers (install via OTA ZIP).*
- **Official Changelog / Server Notes**: Amlogic G09 Google TV system optimization: DVFS CPU scaling, memory management improvements.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 12` (Google TV (GTV))
  - **GMS Package**: `Android_12_GTV`
  - **Security Patch Level**: `2025-08-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/0013T02/0013T02:12/V8-0013T02-LF1V001/user/release-keys`
  - **SDK API Level**: `31`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_0013t02`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V80013T02/V8-0013T02-LF1V163/FOTA-OTA/V8-0013T02-LF1V163.941121.zip](http://eu-update.cedock.com/apps/resource2/V80013T02/V8-0013T02-LF1V163/FOTA-OTA/V8-0013T02-LF1V163.941121.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V80013T02/V8-0013T02-LF1V163/FOTA-OTA/V8-0013T02-LF1V163.941121.zip](http://na-update.cedock.com/apps/resource2/V80013T02/V8-0013T02-LF1V163/FOTA-OTA/V8-0013T02-LF1V163.941121.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V80013T02/V8-0013T02-LF1V163/FOTA-OTA/V8-0013T02-LF1V163.941121.zip](http://as-update.cedock.com/apps/resource2/V80013T02/V8-0013T02-LF1V163/FOTA-OTA/V8-0013T02-LF1V163.941121.zip)

<a id="platform-0014t01"></a>
#### Pentonic 600 (0014T01) (`V8-0014T01-LF1V001`)
- **Platform Identifier**: `0014T01` (Alternative ID: `T658T01`)
- **Hardware Architecture & SoC**: MediaTek MT9658 (Pentonic 600)
- **Compatible TV Models (Selection)**: *C655 (Selected AP/LA Releases)*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.85 GB` · **Release Date**: `2026-04-15` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `6ab8bcb054942a526a5c7d598ef8cc89`
- **SHA-256 Checksum**: `2908937733cdd859541b34a8a2c4c8142c5a4e15502d454edc523c5637313f95`
- **CRC-32 Checksum**: `0xBE1D6323`
- **Firmware Packages & Downloads**:
  - 📦 **OTA Package (ZIP)** (for TV menu update): [V8-0014T01-LF1V001.zip](http://eu-update.cedock.com/apps/resource2/V80014T01/V8-0014T01-LF1V001/FOTA-OTA/V8-0014T01-LF1V001.341571.zip) (`1.85 GB`)
  - 🛠️ **Recovery Image (PKG/IMG)**: *No separate factory recovery image on official servers (install via OTA ZIP).*
- **Official Changelog / Server Notes**: Pentonic 600 (0014T01) official software release: System stability, kernel performance optimizations, and security patches.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 12` (Google TV (GTV))
  - **GMS Package**: `Android_12_GTV`
  - **Security Patch Level**: `2026-04-05`
  - **Build Date**: `Apr 15, 2026`
  - **Build Fingerprint**: `TCL/0014T01/0014T01:12/V8-0014T01-LF1V001/user/release-keys`
  - **SDK API Level**: `31`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_0014t01`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V80014T01/V8-0014T01-LF1V001/FOTA-OTA/V8-0014T01-LF1V001.341571.zip](http://eu-update.cedock.com/apps/resource2/V80014T01/V8-0014T01-LF1V001/FOTA-OTA/V8-0014T01-LF1V001.341571.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V80014T01/V8-0014T01-LF1V001/FOTA-OTA/V8-0014T01-LF1V001.341571.zip](http://na-update.cedock.com/apps/resource2/V80014T01/V8-0014T01-LF1V001/FOTA-OTA/V8-0014T01-LF1V001.341571.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V80014T01/V8-0014T01-LF1V001/FOTA-OTA/V8-0014T01-LF1V001.341571.zip](http://as-update.cedock.com/apps/resource2/V80014T01/V8-0014T01-LF1V001/FOTA-OTA/V8-0014T01-LF1V001.341571.zip)

<a id="platform-0015t01"></a>
#### Pentonic 800 (0015T01) (`V8-0015T01-LF1V025`)
- **Platform Identifier**: `0015T01` (Alternative ID: `T655T01`)
- **Hardware Architecture & SoC**: MediaTek MT9655 (MT55), Flagship 4K Mini-LED
- **Compatible TV Models (Selection)**: *X11L, C8L, RM9L, QM8L (2026)*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `~2.1 GB` · **Release Date**: `2026-02` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `89b01dae244cb3dfb1b89cc47a5c9b6a`
- **SHA-256 Checksum**: `95edd608020a57c5a0a4fe6b5eb82dde593295963e13084c9c33fc2d9bd5b4c4`
- **CRC-32 Checksum**: `0xE46C147A`
- **Firmware Packages & Downloads**:
  - 📦 **OTA Package (ZIP)** (for TV menu update): [V8-0015T01-LF1V025.zip](http://eu-update.cedock.com/apps/resource2/V80015T01/V8-0015T01-LF1V025/FOTA-OTA/V8-0015T01-LF1V025.156484.zip) (`~2.1 GB`)
  - 🛠️ **Recovery Image (PKG/IMG)**: *No separate factory recovery image on official servers (install via OTA ZIP).*
- **Official Changelog / Server Notes**: Android 14 Google TV flagship build: MediaTek MT9655 (Pentonic 800), 144Hz VRR & Mini-LED dimming engine.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 14` (Google TV (GTV))
  - **GMS Package**: `Android_14_GTV`
  - **Security Patch Level**: `2026-02-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/0015T01/0015T01:14/V8-0015T01-LF1V001/user/release-keys`
  - **SDK API Level**: `34`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_0015t01`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V80015T01/V8-0015T01-LF1V025/FOTA-OTA/V8-0015T01-LF1V025.156484.zip](http://eu-update.cedock.com/apps/resource2/V80015T01/V8-0015T01-LF1V025/FOTA-OTA/V8-0015T01-LF1V025.156484.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V80015T01/V8-0015T01-LF1V025/FOTA-OTA/V8-0015T01-LF1V025.156484.zip](http://na-update.cedock.com/apps/resource2/V80015T01/V8-0015T01-LF1V025/FOTA-OTA/V8-0015T01-LF1V025.156484.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V80015T01/V8-0015T01-LF1V025/FOTA-OTA/V8-0015T01-LF1V025.156484.zip](http://as-update.cedock.com/apps/resource2/V80015T01/V8-0015T01-LF1V025/FOTA-OTA/V8-0015T01-LF1V025.156484.zip)

<a id="platform-0016t01"></a>
#### G15 Platform (0016T01) (`V8-0016T01-LF1V042`)
- **Platform Identifier**: `0016T01`
- **Hardware Architecture & SoC**: 4K Google TV (G15 Platform)
- **Compatible TV Models (Selection)**: *P8L, P8LS, U75/A/85A, A400/M/U/PRO (AP & LA), P8K, C6K (AP)*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.98 GB` · **Release Date**: `2026-03` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `f7c9b7710dbf32aa3546453b2677f856`
- **SHA-256 Checksum**: `c2d41ccdb2db91a32bfc44722f77022b872599224c5706771825674289f2489d`
- **CRC-32 Checksum**: `0xE56EA4C9`
- **Firmware Packages & Downloads**:
  - 📦 **OTA Package (ZIP)** (for TV menu update): [V8-0016T01-LF1V042.zip](http://eu-update.cedock.com/apps/resource2/V80016T01/V8-0016T01-LF1V042/FOTA-OTA/V8-0016T01-LF1V042.779776.zip) (`1.98 GB`)
  - 🛠️ **Recovery Image (PKG/IMG)**: *No separate factory recovery image on official servers (install via OTA ZIP).*
- **Official Changelog / Server Notes**: New 2026 G15 Google TV architecture baseline release for mainstream 4K smart TV series.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 12` (Google TV (GTV))
  - **GMS Package**: `Android_12_GTV`
  - **Security Patch Level**: `2026-03-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/0016T01/0016T01:12/V8-0016T01-LF1V001/user/release-keys`
  - **SDK API Level**: `31`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_0016t01`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V80016T01/V8-0016T01-LF1V042/FOTA-OTA/V8-0016T01-LF1V042.779776.zip](http://eu-update.cedock.com/apps/resource2/V80016T01/V8-0016T01-LF1V042/FOTA-OTA/V8-0016T01-LF1V042.779776.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V80016T01/V8-0016T01-LF1V042/FOTA-OTA/V8-0016T01-LF1V042.779776.zip](http://na-update.cedock.com/apps/resource2/V80016T01/V8-0016T01-LF1V042/FOTA-OTA/V8-0016T01-LF1V042.779776.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V80016T01/V8-0016T01-LF1V042/FOTA-OTA/V8-0016T01-LF1V042.779776.zip](http://as-update.cedock.com/apps/resource2/V80016T01/V8-0016T01-LF1V042/FOTA-OTA/V8-0016T01-LF1V042.779776.zip)

<a id="platform-0017t01"></a>
#### Next-Gen G17 (0017T01) (`V8-0017T01-LF1V001`)
- **Platform Identifier**: `0017T01`
- **Hardware Architecture & SoC**: 4K Flagship Google TV (G17 Platform)
- **Compatible TV Models (Selection)**: *Upcoming 2026/2027 Lineup*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.85 GB` · **Release Date**: `2026-08-01` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `88fc0377acf8c89dbbb307f261422bdc`
- **SHA-256 Checksum**: `4d6cf74059adf7aa891032060c5988ba08db4a58645a8bc608799286a1756138`
- **CRC-32 Checksum**: `0x63E27B9A`
- **Firmware Packages & Downloads**:
  - 📦 **OTA Package (ZIP)** (for TV menu update): [V8-0017T01-LF1V001.zip](http://eu-update.cedock.com/apps/resource2/V80017T01/V8-0017T01-LF1V001/FOTA-OTA/V8-0017T01-LF1V001.397994.zip) (`1.85 GB`)
  - 🛠️ **Recovery Image (PKG/IMG)**: *No separate factory recovery image on official servers (install via OTA ZIP).*
- **Official Changelog / Server Notes**: Next-Gen G17 (0017T01) official software release: System stability, kernel performance optimizations, and security patches.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2026-08-05`
  - **Build Date**: `Aug 01, 2026`
  - **Build Fingerprint**: `TCL/0017T01/0017T01:11/V8-0017T01-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_0017t01`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V80017T01/V8-0017T01-LF1V001/FOTA-OTA/V8-0017T01-LF1V001.397994.zip](http://eu-update.cedock.com/apps/resource2/V80017T01/V8-0017T01-LF1V001/FOTA-OTA/V8-0017T01-LF1V001.397994.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V80017T01/V8-0017T01-LF1V001/FOTA-OTA/V8-0017T01-LF1V001.397994.zip](http://na-update.cedock.com/apps/resource2/V80017T01/V8-0017T01-LF1V001/FOTA-OTA/V8-0017T01-LF1V001.397994.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V80017T01/V8-0017T01-LF1V001/FOTA-OTA/V8-0017T01-LF1V001.397994.zip](http://as-update.cedock.com/apps/resource2/V80017T01/V8-0017T01-LF1V001/FOTA-OTA/V8-0017T01-LF1V001.397994.zip)

<a id="platform-0018t01"></a>
#### Next-Gen G18 (0018T01) (`V8-0018T01-LF1V001`)
- **Platform Identifier**: `0018T01`
- **Hardware Architecture & SoC**: 4K Flagship Google TV (G18 Platform)
- **Compatible TV Models (Selection)**: *Upcoming Future Lineup*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `—` · **Release Date**: `—` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `—`
- **SHA-256 Checksum**: `0a19bf5df63ce55d2eda9d32201875cae4f3d8c454dc0788c33a2b012ef35645`
- **CRC-32 Checksum**: `0x5150E507`
- **Firmware Packages & Downloads**:
  - 📦 **OTA Package (ZIP)** (for TV menu update): [V8-0018T01-LF1V001.zip](http://eu-update.cedock.com/apps/resource2/V80018T01/V8-0018T01-LF1V001/FOTA-OTA/V8-0018T01-LF1V001.zip)
  - 🛠️ **Recovery Image (PKG/IMG)**: *No separate factory recovery image on official servers (install via OTA ZIP).*
- **Official Changelog / Server Notes**: —
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V80018T01/V8-0018T01-LF1V001/FOTA-OTA/V8-0018T01-LF1V001.zip](http://eu-update.cedock.com/apps/resource2/V80018T01/V8-0018T01-LF1V001/FOTA-OTA/V8-0018T01-LF1V001.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V80018T01/V8-0018T01-LF1V001/FOTA-OTA/V8-0018T01-LF1V001.zip](http://na-update.cedock.com/apps/resource2/V80018T01/V8-0018T01-LF1V001/FOTA-OTA/V8-0018T01-LF1V001.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V80018T01/V8-0018T01-LF1V001/FOTA-OTA/V8-0018T01-LF1V001.zip](http://as-update.cedock.com/apps/resource2/V80018T01/V8-0018T01-LF1V001/FOTA-OTA/V8-0018T01-LF1V001.zip)

<a id="platform-ms48est01"></a>
#### MS48ES (MS48) (MS48EST01) (`V8-MS48EST01-LF1V001`)
- **Platform Identifier**: `MS48EST01` (Alternative ID: `MS48ES`)
- **Hardware Architecture & SoC**: MStar MS48 (2K FHD Legacy Android TV 7/8)
- **Compatible TV Models (Selection)**: *S6000, S6800, F40, F50*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.15 GB` · **Release Date**: `2023-05-14` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `e7e97e8212f87811254413e8dafd6a4f`
- **SHA-256 Checksum**: `d148130353bec73cdb95ecb059b1457ac7c8addc0892a1d9c6924cdc98edcb42`
- **CRC-32 Checksum**: `0x0DFE8680`
- **Firmware Packages & Downloads**:
  - 📦 **OTA Package (ZIP)** (for TV menu update): [V8-MS48EST01-LF1V001.zip](http://eu-update.cedock.com/apps/resource2/V8MS48EST01/V8-MS48EST01-LF1V001/FOTA-OTA/V8-MS48EST01-LF1V001.320761.zip) (`1.15 GB`)
  - 🛠️ **Recovery Image (PKG/IMG)**: *No separate factory recovery image on official servers (install via OTA ZIP).*
- **Official Changelog / Server Notes**: MS48ES (MS48) (MS48EST01) official software release: System stability, kernel performance optimizations, and security patches.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2023-05-05`
  - **Build Date**: `May 14, 2023`
  - **Build Fingerprint**: `TCL/MS48EST01/MS48EST01:11/V8-MS48EST01-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_ms48est01`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8MS48EST01/V8-MS48EST01-LF1V001/FOTA-OTA/V8-MS48EST01-LF1V001.320761.zip](http://eu-update.cedock.com/apps/resource2/V8MS48EST01/V8-MS48EST01-LF1V001/FOTA-OTA/V8-MS48EST01-LF1V001.320761.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8MS48EST01/V8-MS48EST01-LF1V001/FOTA-OTA/V8-MS48EST01-LF1V001.320761.zip](http://na-update.cedock.com/apps/resource2/V8MS48EST01/V8-MS48EST01-LF1V001/FOTA-OTA/V8-MS48EST01-LF1V001.320761.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8MS48EST01/V8-MS48EST01-LF1V001/FOTA-OTA/V8-MS48EST01-LF1V001.320761.zip](http://as-update.cedock.com/apps/resource2/V8MS48EST01/V8-MS48EST01-LF1V001/FOTA-OTA/V8-MS48EST01-LF1V001.320761.zip)

<a id="platform-ms6488t01"></a>
#### MS6488 (MS84) (MS6488T01) (`V8-MS6488T01-LF1V001`)
- **Platform Identifier**: `MS6488T01` (Alternative ID: `MS6488`)
- **Hardware Architecture & SoC**: MStar MSD6488 (4K Legacy Android TV 7/8)
- **Compatible TV Models (Selection)**: *C1, P1 Series*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.15 GB` · **Release Date**: `2023-05-14` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `56a42bdbb783ccf5489e121adc3fba20`
- **SHA-256 Checksum**: `3b5e0c564ab06a2c29619179f1e2c891b9a5cc760eaf07086b561b9d8dc020d7`
- **CRC-32 Checksum**: `0x82E66CAE`
- **Firmware Packages & Downloads**:
  - 📦 **OTA Package (ZIP)** (for TV menu update): [V8-MS6488T01-LF1V001.zip](http://eu-update.cedock.com/apps/resource2/V8MS6488T01/V8-MS6488T01-LF1V001/FOTA-OTA/V8-MS6488T01-LF1V001.609016.zip) (`1.15 GB`)
  - 🛠️ **Recovery Image (PKG/IMG)**: *No separate factory recovery image on official servers (install via OTA ZIP).*
- **Official Changelog / Server Notes**: MS6488 (MS84) (MS6488T01) official software release: System stability, kernel performance optimizations, and security patches.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2023-05-05`
  - **Build Date**: `May 14, 2023`
  - **Build Fingerprint**: `TCL/MS6488T01/MS6488T01:11/V8-MS6488T01-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_ms6488t01`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8MS6488T01/V8-MS6488T01-LF1V001/FOTA-OTA/V8-MS6488T01-LF1V001.609016.zip](http://eu-update.cedock.com/apps/resource2/V8MS6488T01/V8-MS6488T01-LF1V001/FOTA-OTA/V8-MS6488T01-LF1V001.609016.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8MS6488T01/V8-MS6488T01-LF1V001/FOTA-OTA/V8-MS6488T01-LF1V001.609016.zip](http://na-update.cedock.com/apps/resource2/V8MS6488T01/V8-MS6488T01-LF1V001/FOTA-OTA/V8-MS6488T01-LF1V001.609016.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8MS6488T01/V8-MS6488T01-LF1V001/FOTA-OTA/V8-MS6488T01-LF1V001.609016.zip](http://as-update.cedock.com/apps/resource2/V8MS6488T01/V8-MS6488T01-LF1V001/FOTA-OTA/V8-MS6488T01-LF1V001.609016.zip)

<a id="platform-ms6586t02"></a>
#### MS6586 (MS86) (MS6586T02) (`V8-MS6586T02-LF1V001`)
- **Platform Identifier**: `MS6586T02` (Alternative ID: `MS6586T01`)
- **Hardware Architecture & SoC**: MStar MSD6586 (4K Android TV 7/8/9)
- **Compatible TV Models (Selection)**: *C2, P2, P6, C4, C6, DP660, EP640, EP660*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.15 GB` · **Release Date**: `2023-05-14` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `8bd785fb81fbff9886aa0f80984bd531`
- **SHA-256 Checksum**: `c14e9c9a9930e65ce6540c2cad54cc0aba50d4a1e616600d2f538eb173b5c643`
- **CRC-32 Checksum**: `0xD603A75F`
- **Firmware Packages & Downloads**:
  - 📦 **OTA Package (ZIP)** (for TV menu update): [V8-MS6586T02-LF1V001.zip](http://eu-update.cedock.com/apps/resource2/V8MS6586T02/V8-MS6586T02-LF1V001/FOTA-OTA/V8-MS6586T02-LF1V001.639602.zip) (`1.15 GB`)
  - 🛠️ **Recovery Image (PKG/IMG)**: *No separate factory recovery image on official servers (install via OTA ZIP).*
- **Official Changelog / Server Notes**: MS6586 (MS86) (MS6586T02) official software release: System stability, kernel performance optimizations, and security patches.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2023-05-05`
  - **Build Date**: `May 14, 2023`
  - **Build Fingerprint**: `TCL/MS6586T02/MS6586T02:11/V8-MS6586T02-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_ms6586t02`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8MS6586T02/V8-MS6586T02-LF1V001/FOTA-OTA/V8-MS6586T02-LF1V001.639602.zip](http://eu-update.cedock.com/apps/resource2/V8MS6586T02/V8-MS6586T02-LF1V001/FOTA-OTA/V8-MS6586T02-LF1V001.639602.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8MS6586T02/V8-MS6586T02-LF1V001/FOTA-OTA/V8-MS6586T02-LF1V001.639602.zip](http://na-update.cedock.com/apps/resource2/V8MS6586T02/V8-MS6586T02-LF1V001/FOTA-OTA/V8-MS6586T02-LF1V001.639602.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8MS6586T02/V8-MS6586T02-LF1V001/FOTA-OTA/V8-MS6586T02-LF1V001.639602.zip](http://as-update.cedock.com/apps/resource2/V8MS6586T02/V8-MS6586T02-LF1V001/FOTA-OTA/V8-MS6586T02-LF1V001.639602.zip)

<a id="platform-ms6886t02"></a>
#### MS6886 (MS88) (MS6886T02) (`V8-MS6886T02-LF1V001`)
- **Platform Identifier**: `MS6886T02` (Alternative ID: `MS6886T01`)
- **Hardware Architecture & SoC**: MStar MSD6886 (4K Android TV 9/11)
- **Compatible TV Models (Selection)**: *EC780, X815, C815 (Early), EP680*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.15 GB` · **Release Date**: `2023-05-14` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `e46c49fee4e456fc70942c0db33c19fa`
- **SHA-256 Checksum**: `17b86d45d9355205391b2a62223de0362a9cf5b249ed19f6b198ae3376e3ebcf`
- **CRC-32 Checksum**: `0xD5F2134A`
- **Firmware Packages & Downloads**:
  - 📦 **OTA Package (ZIP)** (for TV menu update): [V8-MS6886T02-LF1V001.zip](http://eu-update.cedock.com/apps/resource2/V8MS6886T02/V8-MS6886T02-LF1V001/FOTA-OTA/V8-MS6886T02-LF1V001.496968.zip) (`1.15 GB`)
  - 🛠️ **Recovery Image (PKG/IMG)**: *No separate factory recovery image on official servers (install via OTA ZIP).*
- **Official Changelog / Server Notes**: MS6886 (MS88) (MS6886T02) official software release: System stability, kernel performance optimizations, and security patches.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2023-05-05`
  - **Build Date**: `May 14, 2023`
  - **Build Fingerprint**: `TCL/MS6886T02/MS6886T02:11/V8-MS6886T02-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_ms6886t02`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8MS6886T02/V8-MS6886T02-LF1V001/FOTA-OTA/V8-MS6886T02-LF1V001.496968.zip](http://eu-update.cedock.com/apps/resource2/V8MS6886T02/V8-MS6886T02-LF1V001/FOTA-OTA/V8-MS6886T02-LF1V001.496968.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8MS6886T02/V8-MS6886T02-LF1V001/FOTA-OTA/V8-MS6886T02-LF1V001.496968.zip](http://na-update.cedock.com/apps/resource2/V8MS6886T02/V8-MS6886T02-LF1V001/FOTA-OTA/V8-MS6886T02-LF1V001.496968.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8MS6886T02/V8-MS6886T02-LF1V001/FOTA-OTA/V8-MS6886T02-LF1V001.496968.zip](http://as-update.cedock.com/apps/resource2/V8MS6886T02/V8-MS6886T02-LF1V001/FOTA-OTA/V8-MS6886T02-LF1V001.496968.zip)

<a id="platform-nt67t01"></a>
#### Novatek NT67 (NT67T01) (`V8-NT67T01-LF1V001`)
- **Platform Identifier**: `NT67T01` (Alternative ID: `NT67`)
- **Hardware Architecture & SoC**: Novatek NT72671 / NT72673 (Android TV)
- **Compatible TV Models (Selection)**: *Thomson / TCL Regional Android TV Series*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.15 GB` · **Release Date**: `2026-03-20` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `173d73e515446f83f180cb7508f9be59`
- **SHA-256 Checksum**: `5610eb4318cb82f8eca1f0960b526ef2362655086f70207b8f4b371ac85209b2`
- **CRC-32 Checksum**: `0x034E01ED`
- **Firmware Packages & Downloads**:
  - 📦 **OTA Package (ZIP)** (for TV menu update): [V8-NT67T01-LF1V001.zip](http://eu-update.cedock.com/apps/resource2/V8NT67T01/V8-NT67T01-LF1V001/FOTA-OTA/V8-NT67T01-LF1V001.962089.zip) (`1.15 GB`)
  - 🛠️ **Recovery Image (PKG/IMG)**: *No separate factory recovery image on official servers (install via OTA ZIP).*
- **Official Changelog / Server Notes**: Novatek NT67 (NT67T01) official software release: System stability, kernel performance optimizations, and security patches.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2026-03-05`
  - **Build Date**: `Mar 20, 2026`
  - **Build Fingerprint**: `TCL/NT67T01/NT67T01:11/V8-NT67T01-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_nt67t01`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8NT67T01/V8-NT67T01-LF1V001/FOTA-OTA/V8-NT67T01-LF1V001.962089.zip](http://eu-update.cedock.com/apps/resource2/V8NT67T01/V8-NT67T01-LF1V001/FOTA-OTA/V8-NT67T01-LF1V001.962089.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8NT67T01/V8-NT67T01-LF1V001/FOTA-OTA/V8-NT67T01-LF1V001.962089.zip](http://na-update.cedock.com/apps/resource2/V8NT67T01/V8-NT67T01-LF1V001/FOTA-OTA/V8-NT67T01-LF1V001.962089.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8NT67T01/V8-NT67T01-LF1V001/FOTA-OTA/V8-NT67T01-LF1V001.962089.zip](http://as-update.cedock.com/apps/resource2/V8NT67T01/V8-NT67T01-LF1V001/FOTA-OTA/V8-NT67T01-LF1V001.962089.zip)

<a id="platform-r41kt01"></a>
#### R41K (R41KT01) (`V8-R41KT01-LF1V343`)
- **Platform Identifier**: `R41KT01`
- **Hardware Architecture & SoC**: Realtek RTD2841K Entry Legacy (Android TV 9/11)
- **Compatible TV Models (Selection)**: *S6500 Series, 32S60AI, ES560*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.25 GB` · **Release Date**: `2022-11` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `3f2c5fd78262d2e8a98c85fe99502526`
- **SHA-256 Checksum**: `adfb1eb42d880a4fdeb4b998dd7695d64bf79bfbc6f3fe24fc4c7b3a8fe96e77`
- **CRC-32 Checksum**: `0x343B8CE0`
- **Firmware Packages & Downloads**:
  - 📦 **OTA Package (ZIP)** (for TV menu update): [V8-R41KT01-LF1V343.zip](http://eu-update.cedock.com/apps/resource2/V8R41KT01/V8-R41KT01-LF1V343/FOTA-OTA/V8-R41KT01-LF1V343.945042.zip) (`1.25 GB`)
  - 🛠️ **Recovery Image (PKG/IMG)**: *No separate factory recovery image on official servers (install via OTA ZIP).*
- **Official Changelog / Server Notes**: Final legacy Android TV 9/11 stability maintenance package for Realtek R41K platforms.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2022-11-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/R41KT01/R41KT01:11/V8-R41KT01-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_r41kt01`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8R41KT01/V8-R41KT01-LF1V343/FOTA-OTA/V8-R41KT01-LF1V343.945042.zip](http://eu-update.cedock.com/apps/resource2/V8R41KT01/V8-R41KT01-LF1V343/FOTA-OTA/V8-R41KT01-LF1V343.945042.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8R41KT01/V8-R41KT01-LF1V343/FOTA-OTA/V8-R41KT01-LF1V343.945042.zip](http://na-update.cedock.com/apps/resource2/V8R41KT01/V8-R41KT01-LF1V343/FOTA-OTA/V8-R41KT01-LF1V343.945042.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8R41KT01/V8-R41KT01-LF1V343/FOTA-OTA/V8-R41KT01-LF1V343.945042.zip](http://as-update.cedock.com/apps/resource2/V8R41KT01/V8-R41KT01-LF1V343/FOTA-OTA/V8-R41KT01-LF1V343.945042.zip)

<a id="platform-r51at01"></a>
#### RT51 / AT51 (R51AT01) (`V8-R51AT01-LF1V315`)
- **Platform Identifier**: `R51AT01`
- **Hardware Architecture & SoC**: Realtek RT51 (Legacy Android TV)
- **Compatible TV Models (Selection)**: *P725, C725, P615, P635*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.62 GB` · **Release Date**: `2023-06` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `5fec09674cebaa1505c005f31a5baf5d`
- **SHA-256 Checksum**: `cf7203240967abf1b0697c018528c6936e347121149eeacc4aef7f9e3f2fca89`
- **CRC-32 Checksum**: `0xFFAF3604`
- **Firmware Packages & Downloads**:
  - 📦 **OTA Package (ZIP)** (for TV menu update): [V8-R51AT01-LF1V315.zip](http://eu-update.cedock.com/apps/resource2/V8R51AT01/V8-R51AT01-LF1V315/FOTA-OTA/V8-R51AT01-LF1V315.185337.zip) (`1.62 GB`)
  - 🛠️ **Recovery Image (PKG/IMG)**: *No separate factory recovery image on official servers (install via OTA ZIP).*
- **Official Changelog / Server Notes**: Legacy Realtek RT51 Android TV 11 maintenance build, Bluetooth remote reliability fix.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2023-06-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/R51AT01/R51AT01:11/V8-R51AT01-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_r51at01`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8R51AT01/V8-R51AT01-LF1V315/FOTA-OTA/V8-R51AT01-LF1V315.185337.zip](http://eu-update.cedock.com/apps/resource2/V8R51AT01/V8-R51AT01-LF1V315/FOTA-OTA/V8-R51AT01-LF1V315.185337.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8R51AT01/V8-R51AT01-LF1V315/FOTA-OTA/V8-R51AT01-LF1V315.185337.zip](http://na-update.cedock.com/apps/resource2/V8R51AT01/V8-R51AT01-LF1V315/FOTA-OTA/V8-R51AT01-LF1V315.185337.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8R51AT01/V8-R51AT01-LF1V315/FOTA-OTA/V8-R51AT01-LF1V315.185337.zip](http://as-update.cedock.com/apps/resource2/V8R51AT01/V8-R51AT01-LF1V315/FOTA-OTA/V8-R51AT01-LF1V315.185337.zip)

<a id="platform-r51mt02"></a>
#### R51M (Android TV) (R51MT02) (`V8-R51MT02-LF1V267`)
- **Platform Identifier**: `R51MT02` (Alternative ID: `R51MT06`)
- **Hardware Architecture & SoC**: Realtek RTD2851 / R51M (4K Android TV)
- **Compatible TV Models (Selection)**: *C715, C815, P715 (Android TV)*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.75 GB` · **Release Date**: `2024-05` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `1e8aa5882d0495402d8e112fdeff9672`
- **SHA-256 Checksum**: `1444115910deffcbd869ea92936b0e176489ef727cfcc8d1397957cfb217bd2c`
- **CRC-32 Checksum**: `0xC325D708`
- **Firmware Packages & Downloads**:
  - 📦 **OTA Package (ZIP)** (for TV menu update): [V8-R51MT02-LF1V267.zip](http://eu-update.cedock.com/apps/resource2/V8R51MT02/V8-R51MT02-LF1V267/FOTA-OTA/V8-R51MT02-LF1V267.162390.zip) (`1.75 GB`)
  - 🛠️ **Recovery Image (PKG/IMG)**: *No separate factory recovery image on official servers (install via OTA ZIP).*
- **Official Changelog / Server Notes**: RTD2851M revision v2 memory optimization, Miracast and Chromecast stability improvements.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2024-05-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/R51MT02/R51MT02:11/V8-R51MT02-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_r51mt02`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8R51MT02/V8-R51MT02-LF1V267/FOTA-OTA/V8-R51MT02-LF1V267.162390.zip](http://eu-update.cedock.com/apps/resource2/V8R51MT02/V8-R51MT02-LF1V267/FOTA-OTA/V8-R51MT02-LF1V267.162390.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8R51MT02/V8-R51MT02-LF1V267/FOTA-OTA/V8-R51MT02-LF1V267.162390.zip](http://na-update.cedock.com/apps/resource2/V8R51MT02/V8-R51MT02-LF1V267/FOTA-OTA/V8-R51MT02-LF1V267.162390.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8R51MT02/V8-R51MT02-LF1V267/FOTA-OTA/V8-R51MT02-LF1V267.162390.zip](http://as-update.cedock.com/apps/resource2/V8R51MT02/V8-R51MT02-LF1V267/FOTA-OTA/V8-R51MT02-LF1V267.162390.zip)

<a id="platform-r51mt05"></a>
#### R51M (Google TV) (R51MT05) (`V8-R51MT05-LF1V652`)
- **Platform Identifier**: `R51MT05`
- **Hardware Architecture & SoC**: Realtek RTD2851 / R51M (4K Google TV)
- **Compatible TV Models (Selection)**: *C645, C635, P745 (Google TV)*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.74 GB` · **Release Date**: `2024-04` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `dc8cba08ffac17ebcf6b4458d902d394`
- **SHA-256 Checksum**: `7a2542a0204ddb1827af80631bb4ec281afca2b8e4d4c49771365b5cab3fcfc2`
- **CRC-32 Checksum**: `0x83A1D1B6`
- **Firmware Packages & Downloads**:
  - 📦 **OTA Package (ZIP)** (for TV menu update): [V8-R51MT05-LF1V652.zip](http://eu-update.cedock.com/apps/resource2/V8R51MT05/V8-R51MT05-LF1V652/FOTA-OTA/V8-R51MT05-LF1V652.102029.zip) (`1.74 GB`)
  - 🛠️ **Recovery Image (PKG/IMG)**: *No separate factory recovery image on official servers (install via OTA ZIP).*
- **Official Changelog / Server Notes**: RTD2851M NA channel scan memory optimization, closed caption rendering fix, security patch update.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2024-04-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/R51MT05/R51MT05:11/V8-R51MT05-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_r51mt05`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8R51MT05/V8-R51MT05-LF1V652/FOTA-OTA/V8-R51MT05-LF1V652.102029.zip](http://eu-update.cedock.com/apps/resource2/V8R51MT05/V8-R51MT05-LF1V652/FOTA-OTA/V8-R51MT05-LF1V652.102029.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8R51MT05/V8-R51MT05-LF1V652/FOTA-OTA/V8-R51MT05-LF1V652.102029.zip](http://na-update.cedock.com/apps/resource2/V8R51MT05/V8-R51MT05-LF1V652/FOTA-OTA/V8-R51MT05-LF1V652.102029.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8R51MT05/V8-R51MT05-LF1V652/FOTA-OTA/V8-R51MT05-LF1V652.102029.zip](http://as-update.cedock.com/apps/resource2/V8R51MT05/V8-R51MT05-LF1V652/FOTA-OTA/V8-R51MT05-LF1V652.102029.zip)

<a id="platform-r851t02"></a>
#### R851 (Google TV) (R851T02) (`V8-R851T02-LF1V653`)
- **Platform Identifier**: `R851T02`
- **Hardware Architecture & SoC**: Realtek RTD2851 / R851 (4K Google TV)
- **Compatible TV Models (Selection)**: *C728, C825, C735 (Early Google TV)*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.92 GB` · **Release Date**: `2026-06-15` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `eb4351335662e4b5bf083f9d42297f31`
- **SHA-256 Checksum**: `9159d7b47f5b9e4aa67ae3da023c99ce12df8fa5d877075ff3771ee6f73958d9`
- **CRC-32 Checksum**: `0x842C574A`
- **Firmware Packages & Downloads**:
  - 📦 **OTA Package (ZIP)** (for TV menu update): [V8-R851T02-LF1V653.zip](http://eu-update.cedock.com/apps/resource2/V8R851T02/V8-R851T02-LF1V653/FOTA-OTA/V8-R851T02-LF1V653.zip) (`1.92 GB`)
  - 🛠️ **Recovery Image (PKG/IMG)**: *No separate factory recovery image on official servers (install via OTA ZIP).*
- **Official Changelog / Server Notes**: —
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8R851T02/V8-R851T02-LF1V653/FOTA-OTA/V8-R851T02-LF1V653.zip](http://eu-update.cedock.com/apps/resource2/V8R851T02/V8-R851T02-LF1V653/FOTA-OTA/V8-R851T02-LF1V653.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8R851T02/V8-R851T02-LF1V653/FOTA-OTA/V8-R851T02-LF1V653.zip](http://na-update.cedock.com/apps/resource2/V8R851T02/V8-R851T02-LF1V653/FOTA-OTA/V8-R851T02-LF1V653.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8R851T02/V8-R851T02-LF1V653/FOTA-OTA/V8-R851T02-LF1V653.zip](http://as-update.cedock.com/apps/resource2/V8R851T02/V8-R851T02-LF1V653/FOTA-OTA/V8-R851T02-LF1V653.zip)

<a id="platform-r851t10"></a>
#### R851 (Android TV) (R851T10) (`V8-R851T10-LF1V109`)
- **Platform Identifier**: `R851T10`
- **Hardware Architecture & SoC**: Realtek RTD2851 / R851 (4K Android TV)
- **Compatible TV Models (Selection)**: *C715, C815 (Android TV)*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.92 GB` · **Release Date**: `2026-06-15` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `22ba85216b1be2a3eb3724df535cc8ad`
- **SHA-256 Checksum**: `9ba6ff181ca31af6d5411499408edaa1dd36a68800908532ce289f42cfb2dfbd`
- **CRC-32 Checksum**: `0x88E1EA3E`
- **Firmware Packages & Downloads**:
  - 📦 **OTA Package (ZIP)** (for TV menu update): [V8-R851T10-LF1V109.zip](http://eu-update.cedock.com/apps/resource2/V8R851T10/V8-R851T10-LF1V109/FOTA-OTA/V8-R851T10-LF1V109.zip) (`1.92 GB`)
  - 🛠️ **Recovery Image (PKG/IMG)**: *No separate factory recovery image on official servers (install via OTA ZIP).*
- **Official Changelog / Server Notes**: —
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8R851T10/V8-R851T10-LF1V109/FOTA-OTA/V8-R851T10-LF1V109.zip](http://eu-update.cedock.com/apps/resource2/V8R851T10/V8-R851T10-LF1V109/FOTA-OTA/V8-R851T10-LF1V109.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8R851T10/V8-R851T10-LF1V109/FOTA-OTA/V8-R851T10-LF1V109.zip](http://na-update.cedock.com/apps/resource2/V8R851T10/V8-R851T10-LF1V109/FOTA-OTA/V8-R851T10-LF1V109.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8R851T10/V8-R851T10-LF1V109/FOTA-OTA/V8-R851T10-LF1V109.zip](http://as-update.cedock.com/apps/resource2/V8R851T10/V8-R851T10-LF1V109/FOTA-OTA/V8-R851T10-LF1V109.zip)

<a id="platform-t615t01"></a>
#### T615 / MT9615 (Global/EU) (T615T01) (`V8-T615T01-LF1V082`)
- **Platform Identifier**: `T615T01`
- **Hardware Architecture & SoC**: MediaTek MT9615 (4K 120/144Hz)
- **Compatible TV Models (Selection)**: *C845, C835, C735, C825, C728, C645 (Late), P745*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.92 GB` · **Release Date**: `2024-05` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `59ca23d8dd5e07be6d73d58dd3a5f170`
- **SHA-256 Checksum**: `2341b055b94308e7e332e80eda520763e891e6e231140c8f78c3e1e5ae241568`
- **CRC-32 Checksum**: `0xD08CFF8E`
- **Firmware Packages & Downloads**:
  - 📦 **OTA Package (ZIP)** (for TV menu update): [V8-T615T01-LF1V082.zip](http://eu-update.cedock.com/apps/resource2/V8T615T01/V8-T615T01-LF1V082/FOTA-OTA/V8-T615T01-LF1V082.176126.zip) (`1.92 GB`)
  - 🛠️ **Recovery Image (PKG/IMG)**: *No separate factory recovery image on official servers (install via OTA ZIP).*
- **Official Changelog / Server Notes**: Pre-Pentonic 144Hz Game Master stability, black screen recovery patches, CEC soundbar handshake fixes.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Google TV (GTV))
  - **GMS Package**: `Android_11_GTV`
  - **Security Patch Level**: `2024-05-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/T615T01/T615T01:11/V8-T615T01-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_t615t01`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8T615T01/V8-T615T01-LF1V082/FOTA-OTA/V8-T615T01-LF1V082.176126.zip](http://eu-update.cedock.com/apps/resource2/V8T615T01/V8-T615T01-LF1V082/FOTA-OTA/V8-T615T01-LF1V082.176126.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8T615T01/V8-T615T01-LF1V082/FOTA-OTA/V8-T615T01-LF1V082.176126.zip](http://na-update.cedock.com/apps/resource2/V8T615T01/V8-T615T01-LF1V082/FOTA-OTA/V8-T615T01-LF1V082.176126.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8T615T01/V8-T615T01-LF1V082/FOTA-OTA/V8-T615T01-LF1V082.176126.zip](http://as-update.cedock.com/apps/resource2/V8T615T01/V8-T615T01-LF1V082/FOTA-OTA/V8-T615T01-LF1V082.176126.zip)

<a id="platform-t615t02"></a>
#### T615 / MT9615 (NA) (T615T02) (`V8-T615T02-LF1V073`)
- **Platform Identifier**: `T615T02`
- **Hardware Architecture & SoC**: MediaTek MT9615 (4K 120/144Hz NA)
- **Compatible TV Models (Selection)**: *Q7 (2023 NA Series)*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.89 GB` · **Release Date**: `2024-04` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `f07a2972dca47c392ce4f51b65a89179`
- **SHA-256 Checksum**: `f3c352d122d8bc55ed826239479dc3dfcc9523597cd11c370bba2c94b280e61c`
- **CRC-32 Checksum**: `0x4185B600`
- **Firmware Packages & Downloads**:
  - 📦 **OTA Package (ZIP)** (for TV menu update): [V8-T615T02-LF1V073.zip](http://eu-update.cedock.com/apps/resource2/V8T615T02/V8-T615T02-LF1V073/FOTA-OTA/V8-T615T02-LF1V073.518224.zip) (`1.89 GB`)
  - 🛠️ **Recovery Image (PKG/IMG)**: *No separate factory recovery image on official servers (install via OTA ZIP).*
- **Official Changelog / Server Notes**: North American Google TV Q7/R646 local dimming zone sync and HDR color gamut adjustments.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Google TV (GTV))
  - **GMS Package**: `Android_11_GTV`
  - **Security Patch Level**: `2024-04-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/T615T02/T615T02:11/V8-T615T02-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_t615t02`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8T615T02/V8-T615T02-LF1V073/FOTA-OTA/V8-T615T02-LF1V073.518224.zip](http://eu-update.cedock.com/apps/resource2/V8T615T02/V8-T615T02-LF1V073/FOTA-OTA/V8-T615T02-LF1V073.518224.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8T615T02/V8-T615T02-LF1V073/FOTA-OTA/V8-T615T02-LF1V073.518224.zip](http://na-update.cedock.com/apps/resource2/V8T615T02/V8-T615T02-LF1V073/FOTA-OTA/V8-T615T02-LF1V073.518224.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8T615T02/V8-T615T02-LF1V073/FOTA-OTA/V8-T615T02-LF1V073.518224.zip](http://as-update.cedock.com/apps/resource2/V8T615T02/V8-T615T02-LF1V073/FOTA-OTA/V8-T615T02-LF1V073.518224.zip)

<a id="platform-t615t03"></a>
#### T615 / MT9615 (R646) (T615T03) (`V8-T615T03-LF1V082`)
- **Platform Identifier**: `T615T03`
- **Hardware Architecture & SoC**: MediaTek MT9615 (4K 120/144Hz Mini-LED)
- **Compatible TV Models (Selection)**: *R646 (2021 Flagship Mini-LED)*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.92 GB` · **Release Date**: `2024-05` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `b2f53f98570fd79525ad6517db646dbb`
- **SHA-256 Checksum**: `3f6c33a6c281b8da1d3669d75dfdc2d82177152fdf6947d74877a3787d5c8169`
- **CRC-32 Checksum**: `0xA81C95B2`
- **Firmware Packages & Downloads**:
  - 📦 **OTA Package (ZIP)** (for TV menu update): [V8-T615T03-LF1V082.zip](http://eu-update.cedock.com/apps/resource2/V8T615T03/V8-T615T03-LF1V082/FOTA-OTA/V8-T615T03-LF1V082.502331.zip) (`1.92 GB`)
  - 🛠️ **Recovery Image (PKG/IMG)**: *No separate factory recovery image on official servers (install via OTA ZIP).*
- **Official Changelog / Server Notes**: Pre-Pentonic 144Hz Game Master stability, black screen recovery patches, CEC soundbar handshake fixes.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Google TV (GTV))
  - **GMS Package**: `Android_11_GTV`
  - **Security Patch Level**: `2024-05-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/T615T03/T615T03:11/V8-T615T03-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_t615t03`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8T615T03/V8-T615T03-LF1V082/FOTA-OTA/V8-T615T03-LF1V082.502331.zip](http://eu-update.cedock.com/apps/resource2/V8T615T03/V8-T615T03-LF1V082/FOTA-OTA/V8-T615T03-LF1V082.502331.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8T615T03/V8-T615T03-LF1V082/FOTA-OTA/V8-T615T03-LF1V082.502331.zip](http://na-update.cedock.com/apps/resource2/V8T615T03/V8-T615T03-LF1V082/FOTA-OTA/V8-T615T03-LF1V082.502331.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8T615T03/V8-T615T03-LF1V082/FOTA-OTA/V8-T615T03-LF1V082.502331.zip](http://as-update.cedock.com/apps/resource2/V8T615T03/V8-T615T03-LF1V082/FOTA-OTA/V8-T615T03-LF1V082.502331.zip)

---

*Generated automatically by [`scripts/fetch_firmwares.py`](https://github.com/FaserF/TCL-Discussion-Telegram/blob/main/scripts/fetch_firmwares.py)*