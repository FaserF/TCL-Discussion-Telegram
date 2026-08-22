---
title: TCL Smart TV Firmware Hub
description: Official, comprehensive firmware tracker and package repository for all global TCL Android TV and Google TV platforms.
---

# 📡 TCL Smart TV Firmware Hub

Welcome to the official **TCL Smart TV Firmware Hub**. This catalog tracks, aggregates, and validates official firmware releases across all known TCL hardware platforms globally. Data is synchronized directly with official TCL FOTA upgrade servers (`huan.tv`) and high-speed Content Delivery Networks (`cedock.com`).

> 💡 **Automated Verification & Integrity Guarantee**  
> All firmware binaries listed below are verified through server-side MD5 signatures, SHA-256 cryptographic hashes, and IEEE 802.3 32-bit CRC32 checksums. Deep technical build properties are extracted via non-destructive byte-range inspection.

*Last database update: `2026-08-22T10:19:28.129137+00:00` UTC*

---

## 📑 Quick Platform Index

| Platform ID | Family / Chassis | Latest Firmware | OS Flavor | Release Date | Checksums (MD5 · SHA256 · CRC32) | Direct Download |
|---|---|---|:---:|:---:|---|:---:|
| [`0008T01`](#platform-0008t01) | **R75P / RT75 (0008T01)** | `V8-0008T01-LF1V636` | `Android 12` | `2026-08-07` | `a5712354...` · `8e21687d...` · `0xCF291DE2` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V80008T01/V8-0008T01-LF1V636/FOTA-OTA/V8-0008T01-LF1V636.622816.zip) |
| [`0008T02`](#platform-0008t02) | **R75P / RT75 (0008T02)** | `V8-0008T02-LF1V001` | `Android 12` | `2026-03-20` | `046ca58b...` · `30a480f3...` · `0xB7AF92FC` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V80008T02/V8-0008T02-LF1V001/FOTA-OTA/V8-0008T02-LF1V001.295364.zip) |
| [`0012T01`](#platform-0012t01) | **Pentonic 700 (0012T01)** | `V8-0012T01-LF1V655` | `Android 12` | `2026-01` | `e0573619...` · `00357ef7...` · `0xF241FE0D` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V80012T01/V8-0012T01-LF1V655/FOTA-OTA/V8-0012T01-LF1V655.628400.zip) |
| [`0012T02`](#platform-0012t02) | **Pentonic 700 (NA/LA) (0012T02)** | `V8-0012T02-LF1V620` | `Android 12` | `2025-11` | `aaf24d60...` · `3a332afe...` · `0x08739BC3` | [:material-download: Download](http://na-update.cedock.com/apps/resource2/V80012T02/V8-0012T02-LF1V620/FOTA-OTA/V8-0012T02-LF1V620.439617.zip) |
| [`0012T03`](#platform-0012t03) | **Pentonic 700 (Flagship) (0012T03)** | `V8-0012T03-LF1V110` | `Android 12` | `2025-10` | `c5d75c11...` · `68715a05...` · `0xD9A29CE7` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V80012T03/V8-0012T03-LF1V110/FOTA-OTA/V8-0012T03-LF1V110.877669.zip) |
| [`0013T01`](#platform-0013t01) | **T800 (0013T01)** | `V8-0013T01-LF1V001` | `Android 12` | `2026-03-20` | `592d9901...` · `a424a98f...` · `0x501BE1FE` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V80013T01/V8-0013T01-LF1V001/FOTA-OTA/V8-0013T01-LF1V001.270945.zip) |
| [`0013T02`](#platform-0013t02) | **T800 (0013T02)** | `V8-0013T02-LF1V163` | `Android 12` | `2025-08` | `e868ca24...` · `9f1fa9fe...` · `0xDE45B257` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V80013T02/V8-0013T02-LF1V163/FOTA-OTA/V8-0013T02-LF1V163.941121.zip) |
| [`0013T03`](#platform-0013t03) | **T800 (0013T03)** | `V8-0013T03-LF1V001` | `Android 12` | `2026-03-20` | `3a6c1c6d...` · `8c59e34b...` · `0x477726FF` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V80013T03/V8-0013T03-LF1V001/FOTA-OTA/V8-0013T03-LF1V001.991824.zip) |
| [`0014T01`](#platform-0014t01) | **Pentonic 600 (0014T01)** | `V8-0014T01-LF1V001` | `Android 12` | `2026-04-15` | `6ab8bcb0...` · `29089377...` · `0xBE1D6323` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V80014T01/V8-0014T01-LF1V001/FOTA-OTA/V8-0014T01-LF1V001.341571.zip) |
| [`0015T01`](#platform-0015t01) | **Pentonic 800 (0015T01)** | `V8-0015T01-LF1V025` | `Android 14` | `2026-02` | `89b01dae...` · `95edd608...` · `0xE46C147A` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V80015T01/V8-0015T01-LF1V025/FOTA-OTA/V8-0015T01-LF1V025.156484.zip) |
| [`0015T02`](#platform-0015t02) | **Pentonic 800 (0015T02)** | `V8-0015T02-LF1V001` | `Android 14` | `2026-03-20` | `125efdaa...` · `fe3c37db...` · `0x20293E67` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V80015T02/V8-0015T02-LF1V001/FOTA-OTA/V8-0015T02-LF1V001.705724.zip) |
| [`0016T01`](#platform-0016t01) | **G15 Platform (0016T01)** | `V8-0016T01-LF1V042` | `Android 12` | `2026-03` | `f7c9b771...` · `c2d41ccd...` · `0xE56EA4C9` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V80016T01/V8-0016T01-LF1V042/FOTA-OTA/V8-0016T01-LF1V042.779776.zip) |
| [`0017T01`](#platform-0017t01) | **Next-Gen G17 (0017T01)** | `V8-0017T01-LF1V001` | `Android 11` | `2026-08-01` | `88fc0377...` · `4d6cf740...` · `0x63E27B9A` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V80017T01/V8-0017T01-LF1V001/FOTA-OTA/V8-0017T01-LF1V001.397994.zip) |
| [`0018T01`](#platform-0018t01) | **Next-Gen G18 (0018T01)** | `V8-0018T01-LF1V001` | `—` | `—` | — · `0a19bf5d...` · `0x5150E507` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V80018T01/V8-0018T01-LF1V001/FOTA-OTA/V8-0018T01-LF1V001.zip) |
| [`MS48EST01`](#platform-ms48est01) | **MS48ES (MS48) (MS48EST01)** | `V8-MS48EST01-LF1V001` | `Android 11` | `2023-05-14` | `e7e97e82...` · `d1481303...` · `0x0DFE8680` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8MS48EST01/V8-MS48EST01-LF1V001/FOTA-OTA/V8-MS48EST01-LF1V001.320761.zip) |
| [`MS6488T01`](#platform-ms6488t01) | **MS6488 (MS84) (MS6488T01)** | `V8-MS6488T01-LF1V001` | `Android 11` | `2023-05-14` | `56a42bdb...` · `3b5e0c56...` · `0x82E66CAE` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8MS6488T01/V8-MS6488T01-LF1V001/FOTA-OTA/V8-MS6488T01-LF1V001.609016.zip) |
| [`MS6586T01`](#platform-ms6586t01) | **MS6586 (MS86) (MS6586T01)** | `V8-MS6586T01-LF1V001` | `Android 11` | `2023-05-14` | `47af1fe2...` · `3c5ad32b...` · `0x58E88195` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8MS6586T01/V8-MS6586T01-LF1V001/FOTA-OTA/V8-MS6586T01-LF1V001.659240.zip) |
| [`MS6586T02`](#platform-ms6586t02) | **MS6586 (MS86) (MS6586T02)** | `V8-MS6586T02-LF1V001` | `Android 11` | `2023-05-14` | `8bd785fb...` · `c14e9c9a...` · `0xD603A75F` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8MS6586T02/V8-MS6586T02-LF1V001/FOTA-OTA/V8-MS6586T02-LF1V001.639602.zip) |
| [`MS6886T01`](#platform-ms6886t01) | **MS6886 (MS88) (MS6886T01)** | `V8-MS6886T01-LF1V001` | `Android 11` | `2023-05-14` | `c01bb086...` · `616ba564...` · `0xED491A81` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8MS6886T01/V8-MS6886T01-LF1V001/FOTA-OTA/V8-MS6886T01-LF1V001.388934.zip) |
| [`MS6886T02`](#platform-ms6886t02) | **MS6886 (MS88) (MS6886T02)** | `V8-MS6886T02-LF1V001` | `Android 11` | `2023-05-14` | `e46c49fe...` · `17b86d45...` · `0xD5F2134A` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8MS6886T02/V8-MS6886T02-LF1V001/FOTA-OTA/V8-MS6886T02-LF1V001.496968.zip) |
| [`NT67T01`](#platform-nt67t01) | **Novatek NT67 (NT67T01)** | `V8-NT67T01-LF1V001` | `Android 11` | `2026-03-20` | `173d73e5...` · `5610eb43...` · `0x034E01ED` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8NT67T01/V8-NT67T01-LF1V001/FOTA-OTA/V8-NT67T01-LF1V001.962089.zip) |
| [`R41KT01`](#platform-r41kt01) | **R41K (R41KT01)** | `V8-R41KT01-LF1V343` | `Android 11` | `2022-11` | `3f2c5fd7...` · `adfb1eb4...` · `0x343B8CE0` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8R41KT01/V8-R41KT01-LF1V343/FOTA-OTA/V8-R41KT01-LF1V343.945042.zip) |
| [`R51AT01`](#platform-r51at01) | **RT51 / AT51 (R51AT01)** | `V8-R51AT01-LF1V315` | `Android 11` | `2023-06` | `5fec0967...` · `cf720324...` · `0xFFAF3604` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8R51AT01/V8-R51AT01-LF1V315/FOTA-OTA/V8-R51AT01-LF1V315.185337.zip) |
| [`R51MT01`](#platform-r51mt01) | **R51M / R851 (R51MT01)** | `V8-R51MT01-LF1V001` | `Android 11` | `2024-05` | `42dcb0fc...` · `6d74d1eb...` · `0x83ACB8EA` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8R51MT01/V8-R51MT01-LF1V001/FOTA-OTA/V8-R51MT01-LF1V001.626877.zip) |
| [`R51MT02`](#platform-r51mt02) | **R51M / R851 (R51MT02)** | `V8-R51MT02-LF1V267` | `Android 11` | `2024-05` | `1e8aa588...` · `14441159...` · `0xC325D708` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8R51MT02/V8-R51MT02-LF1V267/FOTA-OTA/V8-R51MT02-LF1V267.162390.zip) |
| [`R51MT03`](#platform-r51mt03) | **R51M / R851 (R51MT03)** | `V8-R51MT03-LF1V001` | `Android 11` | `2024-05` | `57bb8323...` · `db0c97bd...` · `0xCFCA5365` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8R51MT03/V8-R51MT03-LF1V001/FOTA-OTA/V8-R51MT03-LF1V001.607708.zip) |
| [`R51MT04`](#platform-r51mt04) | **R51M / R851 (R51MT04)** | `V8-R51MT04-LF1V001` | `Android 11` | `2024-05` | `3e5eed2b...` · `77a48b43...` · `0xB8A419E2` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8R51MT04/V8-R51MT04-LF1V001/FOTA-OTA/V8-R51MT04-LF1V001.973503.zip) |
| [`R51MT05`](#platform-r51mt05) | **R51M / R851 (R51MT05)** | `V8-R51MT05-LF1V652` | `Android 11` | `2024-04` | `dc8cba08...` · `7a2542a0...` · `0x83A1D1B6` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8R51MT05/V8-R51MT05-LF1V652/FOTA-OTA/V8-R51MT05-LF1V652.102029.zip) |
| [`R51MT06`](#platform-r51mt06) | **R51M / R851 (R51MT06)** | `V8-R51MT06-LF1V029` | `Android 11` | `2023-11` | `c77fbe61...` · `832bce9e...` · `0xBFC5FBDB` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8R51MT06/V8-R51MT06-LF1V029/FOTA-OTA/V8-R51MT06-LF1V029.407989.zip) |
| [`R51MT07`](#platform-r51mt07) | **R51M / R851 (R51MT07)** | `V8-R51MT07-LF1V001` | `Android 11` | `2024-05` | `2b64689c...` · `e3deaba0...` · `0xA4EE8161` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8R51MT07/V8-R51MT07-LF1V001/FOTA-OTA/V8-R51MT07-LF1V001.717386.zip) |
| [`R51MT08`](#platform-r51mt08) | **R51M / R851 (R51MT08)** | `V8-R51MT08-LF1V001` | `Android 11` | `2024-05` | `19b4990c...` · `f81fd895...` · `0xA6AE2C94` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8R51MT08/V8-R51MT08-LF1V001/FOTA-OTA/V8-R51MT08-LF1V001.439791.zip) |
| [`R51MT09`](#platform-r51mt09) | **R51M / R851 (R51MT09)** | `V8-R51MT09-LF1V001` | `Android 11` | `2024-05` | `e8e799e7...` · `bde754ab...` · `0xAD20C95E` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8R51MT09/V8-R51MT09-LF1V001/FOTA-OTA/V8-R51MT09-LF1V001.105024.zip) |
| [`R51MT10`](#platform-r51mt10) | **R51M / R851 (R51MT10)** | `V8-R51MT10-LF1V109` | `Android 11` | `2023-09` | `12e048a3...` · `35d22f26...` · `0x9BB381F6` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8R51MT10/V8-R51MT10-LF1V109/FOTA-OTA/V8-R51MT10-LF1V109.312038.zip) |
| [`R75PT01`](#platform-r75pt01) | **R75P / RT75 (R75PT01)** | `V8-R75PT01-LF1V545` | `Android 12` | `2026-08-07` | `391cdffb...` · `b5f8bbb2...` · `0xBA22A8CD` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8R75PT01/V8-R75PT01-LF1V545/FOTA-OTA/V8-R75PT01-LF1V545.645674.zip) |
| [`T221T01`](#platform-t221t01) | **T221 / MT21 (T221T01)** | `V8-T221T01-LF1V242` | `Android 11` | `2024-03` | `01969db7...` · `4ba8ab04...` · `0xE2759854` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8T221T01/V8-T221T01-LF1V242/FOTA-OTA/V8-T221T01-LF1V242.553714.zip) |
| [`T221T02`](#platform-t221t02) | **T221 / MT21 (T221T02)** | `V8-T221T02-LF1V085` | `Android 11` | `2023-10` | `68a5c792...` · `f2ef5d3f...` · `0xDD5DAE8A` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8T221T02/V8-T221T02-LF1V085/FOTA-OTA/V8-T221T02-LF1V085.407126.zip) |
| [`T221T03`](#platform-t221t03) | **T221 / MT21 (T221T03)** | `V8-T221T03-LF1V001` | `Android 11` | `2024-03` | `97164c39...` · `5b1af2a3...` · `0xEEC828AC` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8T221T03/V8-T221T03-LF1V001/FOTA-OTA/V8-T221T03-LF1V001.948400.zip) |
| [`T221T04`](#platform-t221t04) | **T221 / MT21 (T221T04)** | `V8-T221T04-LF1V001` | `Android 11` | `2024-03` | `2f4390b0...` · `041e8918...` · `0x9BE362E0` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8T221T04/V8-T221T04-LF1V001/FOTA-OTA/V8-T221T04-LF1V001.296069.zip) |
| [`T221T05`](#platform-t221t05) | **T221 / MT21 (T221T05)** | `V8-T221T05-LF1V001` | `Android 11` | `2024-03` | `182eeeeb...` · `4a56155b...` · `0xC027B64E` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8T221T05/V8-T221T05-LF1V001/FOTA-OTA/V8-T221T05-LF1V001.859917.zip) |
| [`T221T06`](#platform-t221t06) | **T221 / MT21 (T221T06)** | `V8-T221T06-LF1V001` | `Android 11` | `2024-03` | `eae2f548...` · `3e4cd9a6...` · `0x02580235` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8T221T06/V8-T221T06-LF1V001/FOTA-OTA/V8-T221T06-LF1V001.279555.zip) |
| [`T221T07`](#platform-t221t07) | **T221 / MT21 (T221T07)** | `V8-T221T07-LF1V001` | `Android 11` | `2024-03` | `23e89a4f...` · `7645f463...` · `0x6918F787` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8T221T07/V8-T221T07-LF1V001/FOTA-OTA/V8-T221T07-LF1V001.499180.zip) |
| [`T221T08`](#platform-t221t08) | **T221 / MT21 (T221T08)** | `V8-T221T08-LF1V001` | `Android 11` | `2024-03` | `a83ca210...` · `c6fd16db...` · `0xED3D2DE3` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8T221T08/V8-T221T08-LF1V001/FOTA-OTA/V8-T221T08-LF1V001.941831.zip) |
| [`T221T09`](#platform-t221t09) | **T221 / MT21 (T221T09)** | `V8-T221T09-LF1V001` | `Android 11` | `2024-03` | `fbb4acdb...` · `29b10e3c...` · `0xE1A941FF` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8T221T09/V8-T221T09-LF1V001/FOTA-OTA/V8-T221T09-LF1V001.110300.zip) |
| [`T615T01`](#platform-t615t01) | **T615 / MT9615 (T615T01)** | `V8-T615T01-LF1V082` | `Android 11` | `2024-05` | `59ca23d8...` · `2341b055...` · `0xD08CFF8E` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8T615T01/V8-T615T01-LF1V082/FOTA-OTA/V8-T615T01-LF1V082.176126.zip) |
| [`T615T02`](#platform-t615t02) | **T615 / MT9615 (T615T02)** | `V8-T615T02-LF1V073` | `Android 11` | `2024-04` | `f07a2972...` · `f3c352d1...` · `0x4185B600` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8T615T02/V8-T615T02-LF1V073/FOTA-OTA/V8-T615T02-LF1V073.518224.zip) |
| [`T615T03`](#platform-t615t03) | **T615 / MT9615 (T615T03)** | `V8-T615T03-LF1V082` | `Android 11` | `2024-05` | `b2f53f98...` · `3f6c33a6...` · `0xA81C95B2` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8T615T03/V8-T615T03-LF1V082/FOTA-OTA/V8-T615T03-LF1V082.502331.zip) |
| [`T653T01`](#platform-t653t01) | **Pentonic 700 (T653T01)** | `V8-T653T01-LF1V655` | `Android 12` | `2026-01` | `9d687f52...` · `74d1a7d8...` · `0xB134BEF4` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8T653T01/V8-T653T01-LF1V655/FOTA-OTA/V8-T653T01-LF1V655.190489.zip) |
| [`T653T02`](#platform-t653t02) | **Pentonic 700 (NA/LA) (T653T02)** | `V8-T653T02-LF1V620` | `Android 12` | `2025-11` | `e0088b23...` · `e958c843...` · `0x3E16B7D0` | [:material-download: Download](http://na-update.cedock.com/apps/resource2/V8T653T02/V8-T653T02-LF1V620/FOTA-OTA/V8-T653T02-LF1V620.303526.zip) |
| [`T653T03`](#platform-t653t03) | **Pentonic 700 (Flagship) (T653T03)** | `V8-T653T03-LF1V110` | `Android 12` | `2025-10` | `f10b2e9f...` · `0b922bf0...` · `0x05C5FE59` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8T653T03/V8-T653T03-LF1V110/FOTA-OTA/V8-T653T03-LF1V110.146158.zip) |
| [`T655T01`](#platform-t655t01) | **Pentonic 800 (T655T01)** | `V8-T655T01-LF1V025` | `Android 14` | `2026-02` | `2dbafab9...` · `8c49af00...` · `0x6F3898BB` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8T655T01/V8-T655T01-LF1V025/FOTA-OTA/V8-T655T01-LF1V025.256205.zip) |
| [`T658T01`](#platform-t658t01) | **Pentonic 600 (T658T01)** | `V8-T658T01-LF1V575` | `Google TV` | `2026-06-15` | `30f8380c...` · `c7a213df...` · `0x5C176F1A` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8T658T01/V8-T658T01-LF1V575/FOTA-OTA/V8-T658T01-LF1V575.002400.zip) |
| [`T800T02`](#platform-t800t02) | **T800 (T800T02)** | `V8-T800T02-LF1V163` | `Android 12` | `2025-08` | `270f5587...` · `ebe52901...` · `0x608D9E72` | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V8T800T02/V8-T800T02-LF1V163/FOTA-OTA/V8-T800T02-LF1V163.128694.zip) |

---

## 🛠️ Detailed Platform Specifications & Package Downloads

<a id="platform-0008t01"></a>
#### R75P / RT75 (0008T01) (`V8-0008T01-LF1V636`)
- **Platform Identifier**: `0008T01` (Alternative ID: `R75PT01`)
- **Hardware Architecture & SoC**: Realtek RT75 (G10 Platform, Entry-Mid 4K GTV)
- **Compatible TV Models (Selection)**: *P8LS, P7L, V6D, T6D, U65A, P6K, P7K, V6C, T6C, C6KS, C6CS, U65/75, MQLED70K, P755, C655, C655 Pro, T7B, V6B, QLED780/810, QM51L, QM5K, Q51K, Q63K, S551G, Q651G*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.92 GB` · **Release Date**: `2026-08-07` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `a5712354fc8723dd5c11afb2608f6091`
- **SHA-256 Checksum**: `8e21687d12671a678a12f3322498d3bcc1771c31fec9bf604ccf81f4f8a01121`
- **CRC-32 Checksum**: `0xCF291DE2`
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
| `V8-0008T01-LF1V630` | `2026-06-15` | `Full OTA (ZIP)` · `1.92 GB` | **Production (Stable)** | *Previous production release.* | [:material-download: Download](http://eu-update.cedock.com/apps/resource2/V80008T01/V8-0008T01-LF1V630/FOTA-OTA/V8-0008T01-LF1V630.zip) |

</details>

<a id="platform-0008t02"></a>
#### R75P / RT75 (0008T02) (`V8-0008T02-LF1V001`)
- **Platform Identifier**: `0008T02` (Alternative ID: `R75PT01`)
- **Hardware Architecture & SoC**: Realtek RT75 (G10 Platform, Entry-Mid 4K GTV)
- **Compatible TV Models (Selection)**: *P8LS, P7L, V6D, T6D, U65A, P6K, P7K, V6C, T6C, C6KS, C6CS, U65/75, MQLED70K, P755, C655, C655 Pro, T7B, V6B, QLED780/810, QM51L, QM5K, Q51K, Q63K, S551G, Q651G*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.85 GB` · **Release Date**: `2026-03-20` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `046ca58b8c5f60538df41c1aa2593129`
- **SHA-256 Checksum**: `30a480f382ecce458db9a12604bebe8389bbea6b92ba8020be8714055eef4d51`
- **CRC-32 Checksum**: `0xB7AF92FC`
- **Official Changelog / Server Notes**: R75P / RT75 (0008T02) official software release: System stability, kernel performance optimizations, and security patches.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 12` (Google TV (GTV))
  - **GMS Package**: `Android_12_GTV`
  - **Security Patch Level**: `2026-03-05`
  - **Build Date**: `Mar 20, 2026`
  - **Build Fingerprint**: `TCL/0008T02/0008T02:12/V8-0008T02-LF1V001/user/release-keys`
  - **SDK API Level**: `31`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_0008t02`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V80008T02/V8-0008T02-LF1V001/FOTA-OTA/V8-0008T02-LF1V001.295364.zip](http://eu-update.cedock.com/apps/resource2/V80008T02/V8-0008T02-LF1V001/FOTA-OTA/V8-0008T02-LF1V001.295364.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V80008T02/V8-0008T02-LF1V001/FOTA-OTA/V8-0008T02-LF1V001.295364.zip](http://na-update.cedock.com/apps/resource2/V80008T02/V8-0008T02-LF1V001/FOTA-OTA/V8-0008T02-LF1V001.295364.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V80008T02/V8-0008T02-LF1V001/FOTA-OTA/V8-0008T02-LF1V001.295364.zip](http://as-update.cedock.com/apps/resource2/V80008T02/V8-0008T02-LF1V001/FOTA-OTA/V8-0008T02-LF1V001.295364.zip)

<a id="platform-0012t01"></a>
#### Pentonic 700 (0012T01) (`V8-0012T01-LF1V655`)
- **Platform Identifier**: `0012T01` (Alternative ID: `T653T01`)
- **Hardware Architecture & SoC**: MediaTek MT9653 / MT9618 (MT53), 4K 144Hz VRR
- **Compatible TV Models (Selection)**: *X955, X955 Max (115"), C955, C855, C805, C765, C755, C745X2, C845X2, C7L, C6L, RM7L, X11K, C9K, C8K, C7K, C6K, P8K, T8C, 98C655, 85C655Pro, 98P745, 98P755*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `2.35 GB` · **Release Date**: `2026-01` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `e0573619c0bb0f93afe2be6aeefb472a`
- **SHA-256 Checksum**: `00357ef7ec8897e71310013d22e713a03c9994578b357c7f065ee03328352403`
- **CRC-32 Checksum**: `0xF241FE0D`
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
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `aaf24d608a1866c214d95d91f92aaf2d`
- **SHA-256 Checksum**: `3a332afe7fe06e4b53b66ca3ac7edb51697b89066cafce5e8212d1d24174a931`
- **CRC-32 Checksum**: `0x08739BC3`
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
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `c5d75c11a51dae5dabf77e96dc205525`
- **SHA-256 Checksum**: `68715a058595b923cf1f931e4f894f2c3819af52b189756c9247aed06d730f85`
- **CRC-32 Checksum**: `0xD9A29CE7`
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

<a id="platform-0013t01"></a>
#### T800 (0013T01) (`V8-0013T01-LF1V001`)
- **Platform Identifier**: `0013T01` (Alternative ID: `T800T02`)
- **Hardware Architecture & SoC**: Amlogic AMLT963D4 (G09, 5-Core A55 @ 1.5GHz / 1.9GHz DVFS, Mali-G57 MC1, 2GB DDR4-3200)
- **Compatible TV Models (Selection)**: *C655, C655 Pro, P755, T7B, P7K, C6KS, 55P755*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.85 GB` · **Release Date**: `2026-03-20` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `592d99010b34ace391da401aca59ec73`
- **SHA-256 Checksum**: `a424a98fa0fe543113791d5f9b44e90050fe53bc341213fd339865d7661d47fd`
- **CRC-32 Checksum**: `0x501BE1FE`
- **Official Changelog / Server Notes**: T800 (0013T01) official software release: System stability, kernel performance optimizations, and security patches.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 12` (Google TV (GTV))
  - **GMS Package**: `Android_12_GTV`
  - **Security Patch Level**: `2026-03-05`
  - **Build Date**: `Mar 20, 2026`
  - **Build Fingerprint**: `TCL/0013T01/0013T01:12/V8-0013T01-LF1V001/user/release-keys`
  - **SDK API Level**: `31`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_0013t01`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V80013T01/V8-0013T01-LF1V001/FOTA-OTA/V8-0013T01-LF1V001.270945.zip](http://eu-update.cedock.com/apps/resource2/V80013T01/V8-0013T01-LF1V001/FOTA-OTA/V8-0013T01-LF1V001.270945.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V80013T01/V8-0013T01-LF1V001/FOTA-OTA/V8-0013T01-LF1V001.270945.zip](http://na-update.cedock.com/apps/resource2/V80013T01/V8-0013T01-LF1V001/FOTA-OTA/V8-0013T01-LF1V001.270945.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V80013T01/V8-0013T01-LF1V001/FOTA-OTA/V8-0013T01-LF1V001.270945.zip](http://as-update.cedock.com/apps/resource2/V80013T01/V8-0013T01-LF1V001/FOTA-OTA/V8-0013T01-LF1V001.270945.zip)

<a id="platform-0013t02"></a>
#### T800 (0013T02) (`V8-0013T02-LF1V163`)
- **Platform Identifier**: `0013T02` (Alternative ID: `T800T02`)
- **Hardware Architecture & SoC**: Amlogic AMLT963D4 (G09, 5-Core A55 @ 1.5GHz / 1.9GHz DVFS, Mali-G57 MC1, 2GB DDR4-3200)
- **Compatible TV Models (Selection)**: *C655, C655 Pro, P755, T7B, P7K, C6KS, 55P755*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.82 GB` · **Release Date**: `2025-08` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `e868ca24e11ffcf319807d3bccc8d28e`
- **SHA-256 Checksum**: `9f1fa9fedd938ae690d2fee156c3e967a8d06254c59f4ac66b01c9e692fc3d47`
- **CRC-32 Checksum**: `0xDE45B257`
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

<a id="platform-0013t03"></a>
#### T800 (0013T03) (`V8-0013T03-LF1V001`)
- **Platform Identifier**: `0013T03` (Alternative ID: `T800T02`)
- **Hardware Architecture & SoC**: Amlogic AMLT963D4 (G09, 5-Core A55 @ 1.5GHz / 1.9GHz DVFS, Mali-G57 MC1, 2GB DDR4-3200)
- **Compatible TV Models (Selection)**: *C655, C655 Pro, P755, T7B, P7K, C6KS, 55P755*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.85 GB` · **Release Date**: `2026-03-20` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `3a6c1c6dec06c112b635b635c34ec20e`
- **SHA-256 Checksum**: `8c59e34b5789b6a429478e0ccff818bf6688f15254906de9b3c96847305006c7`
- **CRC-32 Checksum**: `0x477726FF`
- **Official Changelog / Server Notes**: T800 (0013T03) official software release: System stability, kernel performance optimizations, and security patches.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 12` (Google TV (GTV))
  - **GMS Package**: `Android_12_GTV`
  - **Security Patch Level**: `2026-03-05`
  - **Build Date**: `Mar 20, 2026`
  - **Build Fingerprint**: `TCL/0013T03/0013T03:12/V8-0013T03-LF1V001/user/release-keys`
  - **SDK API Level**: `31`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_0013t03`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V80013T03/V8-0013T03-LF1V001/FOTA-OTA/V8-0013T03-LF1V001.991824.zip](http://eu-update.cedock.com/apps/resource2/V80013T03/V8-0013T03-LF1V001/FOTA-OTA/V8-0013T03-LF1V001.991824.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V80013T03/V8-0013T03-LF1V001/FOTA-OTA/V8-0013T03-LF1V001.991824.zip](http://na-update.cedock.com/apps/resource2/V80013T03/V8-0013T03-LF1V001/FOTA-OTA/V8-0013T03-LF1V001.991824.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V80013T03/V8-0013T03-LF1V001/FOTA-OTA/V8-0013T03-LF1V001.991824.zip](http://as-update.cedock.com/apps/resource2/V80013T03/V8-0013T03-LF1V001/FOTA-OTA/V8-0013T03-LF1V001.991824.zip)

<a id="platform-0014t01"></a>
#### Pentonic 600 (0014T01) (`V8-0014T01-LF1V001`)
- **Platform Identifier**: `0014T01` (Alternative ID: `T658T01`)
- **Hardware Architecture & SoC**: MediaTek MT9658 (Pentonic 600)
- **Compatible TV Models (Selection)**: *C655 (Selected AP/LA Releases)*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.85 GB` · **Release Date**: `2026-04-15` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `6ab8bcb054942a526a5c7d598ef8cc89`
- **SHA-256 Checksum**: `2908937733cdd859541b34a8a2c4c8142c5a4e15502d454edc523c5637313f95`
- **CRC-32 Checksum**: `0xBE1D6323`
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
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `89b01dae244cb3dfb1b89cc47a5c9b6a`
- **SHA-256 Checksum**: `95edd608020a57c5a0a4fe6b5eb82dde593295963e13084c9c33fc2d9bd5b4c4`
- **CRC-32 Checksum**: `0xE46C147A`
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

<a id="platform-0015t02"></a>
#### Pentonic 800 (0015T02) (`V8-0015T02-LF1V001`)
- **Platform Identifier**: `0015T02` (Alternative ID: `T655T01`)
- **Hardware Architecture & SoC**: MediaTek MT9655 (MT55), Flagship 4K Mini-LED
- **Compatible TV Models (Selection)**: *X11L, C8L, RM9L, QM8L (2026)*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.85 GB` · **Release Date**: `2026-03-20` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `125efdaac733a6c555325ce480be90b9`
- **SHA-256 Checksum**: `fe3c37dbb29b5e2d208befc8e33961e7a77148bcdfe60ffcaf7e5b640b45e42e`
- **CRC-32 Checksum**: `0x20293E67`
- **Official Changelog / Server Notes**: Pentonic 800 (0015T02) official software release: System stability, kernel performance optimizations, and security patches.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 14` (Google TV (GTV))
  - **GMS Package**: `Android_14_GTV`
  - **Security Patch Level**: `2026-03-05`
  - **Build Date**: `Mar 20, 2026`
  - **Build Fingerprint**: `TCL/0015T02/0015T02:14/V8-0015T02-LF1V001/user/release-keys`
  - **SDK API Level**: `34`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_0015t02`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V80015T02/V8-0015T02-LF1V001/FOTA-OTA/V8-0015T02-LF1V001.705724.zip](http://eu-update.cedock.com/apps/resource2/V80015T02/V8-0015T02-LF1V001/FOTA-OTA/V8-0015T02-LF1V001.705724.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V80015T02/V8-0015T02-LF1V001/FOTA-OTA/V8-0015T02-LF1V001.705724.zip](http://na-update.cedock.com/apps/resource2/V80015T02/V8-0015T02-LF1V001/FOTA-OTA/V8-0015T02-LF1V001.705724.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V80015T02/V8-0015T02-LF1V001/FOTA-OTA/V8-0015T02-LF1V001.705724.zip](http://as-update.cedock.com/apps/resource2/V80015T02/V8-0015T02-LF1V001/FOTA-OTA/V8-0015T02-LF1V001.705724.zip)

<a id="platform-0016t01"></a>
#### G15 Platform (0016T01) (`V8-0016T01-LF1V042`)
- **Platform Identifier**: `0016T01`
- **Hardware Architecture & SoC**: 4K Google TV (G15 Platform)
- **Compatible TV Models (Selection)**: *P8L, P8LS, U75/A/85A, A400/M/U/PRO (AP & LA), P8K, C6K (AP)*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.98 GB` · **Release Date**: `2026-03` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `f7c9b7710dbf32aa3546453b2677f856`
- **SHA-256 Checksum**: `c2d41ccdb2db91a32bfc44722f77022b872599224c5706771825674289f2489d`
- **CRC-32 Checksum**: `0xE56EA4C9`
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
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `88fc0377acf8c89dbbb307f261422bdc`
- **SHA-256 Checksum**: `4d6cf74059adf7aa891032060c5988ba08db4a58645a8bc608799286a1756138`
- **CRC-32 Checksum**: `0x63E27B9A`
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
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `—`
- **SHA-256 Checksum**: `0a19bf5df63ce55d2eda9d32201875cae4f3d8c454dc0788c33a2b012ef35645`
- **CRC-32 Checksum**: `0x5150E507`
- **Official Changelog / Server Notes**: Official production release.
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V80018T01/V8-0018T01-LF1V001/FOTA-OTA/V8-0018T01-LF1V001.zip](http://eu-update.cedock.com/apps/resource2/V80018T01/V8-0018T01-LF1V001/FOTA-OTA/V8-0018T01-LF1V001.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V80018T01/V8-0018T01-LF1V001/FOTA-OTA/V8-0018T01-LF1V001.zip](http://na-update.cedock.com/apps/resource2/V80018T01/V8-0018T01-LF1V001/FOTA-OTA/V8-0018T01-LF1V001.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V80018T01/V8-0018T01-LF1V001/FOTA-OTA/V8-0018T01-LF1V001.zip](http://as-update.cedock.com/apps/resource2/V80018T01/V8-0018T01-LF1V001/FOTA-OTA/V8-0018T01-LF1V001.zip)

<a id="platform-ms48est01"></a>
#### MS48ES (MS48) (MS48EST01) (`V8-MS48EST01-LF1V001`)
- **Platform Identifier**: `MS48EST01`
- **Hardware Architecture & SoC**: MStar MS48 (2K FHD Legacy Android TV 7/8)
- **Compatible TV Models (Selection)**: *S6000, S6800, F40, F50*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.15 GB` · **Release Date**: `2023-05-14` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `e7e97e8212f87811254413e8dafd6a4f`
- **SHA-256 Checksum**: `d148130353bec73cdb95ecb059b1457ac7c8addc0892a1d9c6924cdc98edcb42`
- **CRC-32 Checksum**: `0x0DFE8680`
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
- **Platform Identifier**: `MS6488T01`
- **Hardware Architecture & SoC**: MStar MSD6488 (4K Legacy Android TV 7/8)
- **Compatible TV Models (Selection)**: *C1, P1 Series*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.15 GB` · **Release Date**: `2023-05-14` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `56a42bdbb783ccf5489e121adc3fba20`
- **SHA-256 Checksum**: `3b5e0c564ab06a2c29619179f1e2c891b9a5cc760eaf07086b561b9d8dc020d7`
- **CRC-32 Checksum**: `0x82E66CAE`
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

<a id="platform-ms6586t01"></a>
#### MS6586 (MS86) (MS6586T01) (`V8-MS6586T01-LF1V001`)
- **Platform Identifier**: `MS6586T01` (Alternative ID: `MS6586T02`)
- **Hardware Architecture & SoC**: MStar MSD6586 (4K Android TV 7/8/9)
- **Compatible TV Models (Selection)**: *C2, P2, P6, C4, C6, DP660, EP640, EP660*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.15 GB` · **Release Date**: `2023-05-14` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `47af1fe24cddcdb0963db840f5a6d66c`
- **SHA-256 Checksum**: `3c5ad32b82dab7904fd411349b1089df4b35d906986eac37c5e94fa9027716b3`
- **CRC-32 Checksum**: `0x58E88195`
- **Official Changelog / Server Notes**: MS6586 (MS86) (MS6586T01) official software release: System stability, kernel performance optimizations, and security patches.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2023-05-05`
  - **Build Date**: `May 14, 2023`
  - **Build Fingerprint**: `TCL/MS6586T01/MS6586T01:11/V8-MS6586T01-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_ms6586t01`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8MS6586T01/V8-MS6586T01-LF1V001/FOTA-OTA/V8-MS6586T01-LF1V001.659240.zip](http://eu-update.cedock.com/apps/resource2/V8MS6586T01/V8-MS6586T01-LF1V001/FOTA-OTA/V8-MS6586T01-LF1V001.659240.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8MS6586T01/V8-MS6586T01-LF1V001/FOTA-OTA/V8-MS6586T01-LF1V001.659240.zip](http://na-update.cedock.com/apps/resource2/V8MS6586T01/V8-MS6586T01-LF1V001/FOTA-OTA/V8-MS6586T01-LF1V001.659240.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8MS6586T01/V8-MS6586T01-LF1V001/FOTA-OTA/V8-MS6586T01-LF1V001.659240.zip](http://as-update.cedock.com/apps/resource2/V8MS6586T01/V8-MS6586T01-LF1V001/FOTA-OTA/V8-MS6586T01-LF1V001.659240.zip)

<a id="platform-ms6586t02"></a>
#### MS6586 (MS86) (MS6586T02) (`V8-MS6586T02-LF1V001`)
- **Platform Identifier**: `MS6586T02` (Alternative ID: `MS6586T01`)
- **Hardware Architecture & SoC**: MStar MSD6586 (4K Android TV 7/8/9)
- **Compatible TV Models (Selection)**: *C2, P2, P6, C4, C6, DP660, EP640, EP660*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.15 GB` · **Release Date**: `2023-05-14` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `8bd785fb81fbff9886aa0f80984bd531`
- **SHA-256 Checksum**: `c14e9c9a9930e65ce6540c2cad54cc0aba50d4a1e616600d2f538eb173b5c643`
- **CRC-32 Checksum**: `0xD603A75F`
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

<a id="platform-ms6886t01"></a>
#### MS6886 (MS88) (MS6886T01) (`V8-MS6886T01-LF1V001`)
- **Platform Identifier**: `MS6886T01` (Alternative ID: `MS6886T02`)
- **Hardware Architecture & SoC**: MStar MSD6886 (4K Android TV 9/11)
- **Compatible TV Models (Selection)**: *EC780, X815, C815 (Early), EP680*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.15 GB` · **Release Date**: `2023-05-14` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `c01bb086610b15cf805ce69ab049261f`
- **SHA-256 Checksum**: `616ba564d0ef7ff7165538a07ebb38562175a144ddfd70c0af2aaed856f5edef`
- **CRC-32 Checksum**: `0xED491A81`
- **Official Changelog / Server Notes**: MS6886 (MS88) (MS6886T01) official software release: System stability, kernel performance optimizations, and security patches.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2023-05-05`
  - **Build Date**: `May 14, 2023`
  - **Build Fingerprint**: `TCL/MS6886T01/MS6886T01:11/V8-MS6886T01-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_ms6886t01`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8MS6886T01/V8-MS6886T01-LF1V001/FOTA-OTA/V8-MS6886T01-LF1V001.388934.zip](http://eu-update.cedock.com/apps/resource2/V8MS6886T01/V8-MS6886T01-LF1V001/FOTA-OTA/V8-MS6886T01-LF1V001.388934.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8MS6886T01/V8-MS6886T01-LF1V001/FOTA-OTA/V8-MS6886T01-LF1V001.388934.zip](http://na-update.cedock.com/apps/resource2/V8MS6886T01/V8-MS6886T01-LF1V001/FOTA-OTA/V8-MS6886T01-LF1V001.388934.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8MS6886T01/V8-MS6886T01-LF1V001/FOTA-OTA/V8-MS6886T01-LF1V001.388934.zip](http://as-update.cedock.com/apps/resource2/V8MS6886T01/V8-MS6886T01-LF1V001/FOTA-OTA/V8-MS6886T01-LF1V001.388934.zip)

<a id="platform-ms6886t02"></a>
#### MS6886 (MS88) (MS6886T02) (`V8-MS6886T02-LF1V001`)
- **Platform Identifier**: `MS6886T02` (Alternative ID: `MS6886T01`)
- **Hardware Architecture & SoC**: MStar MSD6886 (4K Android TV 9/11)
- **Compatible TV Models (Selection)**: *EC780, X815, C815 (Early), EP680*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.15 GB` · **Release Date**: `2023-05-14` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `e46c49fee4e456fc70942c0db33c19fa`
- **SHA-256 Checksum**: `17b86d45d9355205391b2a62223de0362a9cf5b249ed19f6b198ae3376e3ebcf`
- **CRC-32 Checksum**: `0xD5F2134A`
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
- **Platform Identifier**: `NT67T01`
- **Hardware Architecture & SoC**: Novatek NT72671 / NT72673 (Android TV)
- **Compatible TV Models (Selection)**: *Thomson / TCL Regional Android TV Series*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.15 GB` · **Release Date**: `2026-03-20` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `173d73e515446f83f180cb7508f9be59`
- **SHA-256 Checksum**: `5610eb4318cb82f8eca1f0960b526ef2362655086f70207b8f4b371ac85209b2`
- **CRC-32 Checksum**: `0x034E01ED`
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
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `3f2c5fd78262d2e8a98c85fe99502526`
- **SHA-256 Checksum**: `adfb1eb42d880a4fdeb4b998dd7695d64bf79bfbc6f3fe24fc4c7b3a8fe96e77`
- **CRC-32 Checksum**: `0x343B8CE0`
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
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `5fec09674cebaa1505c005f31a5baf5d`
- **SHA-256 Checksum**: `cf7203240967abf1b0697c018528c6936e347121149eeacc4aef7f9e3f2fca89`
- **CRC-32 Checksum**: `0xFFAF3604`
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

<a id="platform-r51mt01"></a>
#### R51M / R851 (R51MT01) (`V8-R51MT01-LF1V001`)
- **Platform Identifier**: `R51MT01` (Alternative ID: `R51MT02`)
- **Hardware Architecture & SoC**: Realtek RTD2851 / R51M (Legacy 4K GTV & ATV)
- **Compatible TV Models (Selection)**: *C645, C635, P745, C715, C815*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.75 GB` · **Release Date**: `2024-05` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `42dcb0fc095d8f0c12ef76ade349de67`
- **SHA-256 Checksum**: `6d74d1eb56a9781d5b0eb69c42986e04d41bc9869bd71d9e0d07b5e32882ec0a`
- **CRC-32 Checksum**: `0x83ACB8EA`
- **Official Changelog / Server Notes**: RTD2851M revision v2 memory optimization, Miracast and Chromecast stability improvements.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2024-05-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/R51MT01/R51MT01:11/V8-R51MT01-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_r51mt01`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8R51MT01/V8-R51MT01-LF1V001/FOTA-OTA/V8-R51MT01-LF1V001.626877.zip](http://eu-update.cedock.com/apps/resource2/V8R51MT01/V8-R51MT01-LF1V001/FOTA-OTA/V8-R51MT01-LF1V001.626877.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8R51MT01/V8-R51MT01-LF1V001/FOTA-OTA/V8-R51MT01-LF1V001.626877.zip](http://na-update.cedock.com/apps/resource2/V8R51MT01/V8-R51MT01-LF1V001/FOTA-OTA/V8-R51MT01-LF1V001.626877.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8R51MT01/V8-R51MT01-LF1V001/FOTA-OTA/V8-R51MT01-LF1V001.626877.zip](http://as-update.cedock.com/apps/resource2/V8R51MT01/V8-R51MT01-LF1V001/FOTA-OTA/V8-R51MT01-LF1V001.626877.zip)

<a id="platform-r51mt02"></a>
#### R51M / R851 (R51MT02) (`V8-R51MT02-LF1V267`)
- **Platform Identifier**: `R51MT02` (Alternative ID: `R51MT01`)
- **Hardware Architecture & SoC**: Realtek RTD2851 / R51M (Legacy 4K GTV & ATV)
- **Compatible TV Models (Selection)**: *C645, C635, P745, C715, C815*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.75 GB` · **Release Date**: `2024-05` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `1e8aa5882d0495402d8e112fdeff9672`
- **SHA-256 Checksum**: `1444115910deffcbd869ea92936b0e176489ef727cfcc8d1397957cfb217bd2c`
- **CRC-32 Checksum**: `0xC325D708`
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

<a id="platform-r51mt03"></a>
#### R51M / R851 (R51MT03) (`V8-R51MT03-LF1V001`)
- **Platform Identifier**: `R51MT03` (Alternative ID: `R51MT01`)
- **Hardware Architecture & SoC**: Realtek RTD2851 / R51M (Legacy 4K GTV & ATV)
- **Compatible TV Models (Selection)**: *C645, C635, P745, C715, C815*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.75 GB` · **Release Date**: `2024-05` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `57bb83231df63ef27c012efb318f5dc2`
- **SHA-256 Checksum**: `db0c97bd699103ec3a3cdfa7cd40b6dde86a13bc20825eaa8bc09bb052431442`
- **CRC-32 Checksum**: `0xCFCA5365`
- **Official Changelog / Server Notes**: Realtek RTD2851M regional chassis variant: Google TV platform stability and multimedia decoder updates.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2024-05-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/R51MT03/R51MT03:11/V8-R51MT03-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_r51mt03`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8R51MT03/V8-R51MT03-LF1V001/FOTA-OTA/V8-R51MT03-LF1V001.607708.zip](http://eu-update.cedock.com/apps/resource2/V8R51MT03/V8-R51MT03-LF1V001/FOTA-OTA/V8-R51MT03-LF1V001.607708.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8R51MT03/V8-R51MT03-LF1V001/FOTA-OTA/V8-R51MT03-LF1V001.607708.zip](http://na-update.cedock.com/apps/resource2/V8R51MT03/V8-R51MT03-LF1V001/FOTA-OTA/V8-R51MT03-LF1V001.607708.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8R51MT03/V8-R51MT03-LF1V001/FOTA-OTA/V8-R51MT03-LF1V001.607708.zip](http://as-update.cedock.com/apps/resource2/V8R51MT03/V8-R51MT03-LF1V001/FOTA-OTA/V8-R51MT03-LF1V001.607708.zip)

<a id="platform-r51mt04"></a>
#### R51M / R851 (R51MT04) (`V8-R51MT04-LF1V001`)
- **Platform Identifier**: `R51MT04` (Alternative ID: `R51MT01`)
- **Hardware Architecture & SoC**: Realtek RTD2851 / R51M (Legacy 4K GTV & ATV)
- **Compatible TV Models (Selection)**: *C645, C635, P745, C715, C815*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.75 GB` · **Release Date**: `2024-05` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `3e5eed2bf48aeb3214211bf7c397b47f`
- **SHA-256 Checksum**: `77a48b436e7bd22d4a98fdbdba1c9320cd8b8d00d33af72a86ad2aaf9d2bef6a`
- **CRC-32 Checksum**: `0xB8A419E2`
- **Official Changelog / Server Notes**: Realtek RTD2851M regional chassis variant: Google TV platform stability and HDMI CEC fixes.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2024-05-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/R51MT04/R51MT04:11/V8-R51MT04-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_r51mt04`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8R51MT04/V8-R51MT04-LF1V001/FOTA-OTA/V8-R51MT04-LF1V001.973503.zip](http://eu-update.cedock.com/apps/resource2/V8R51MT04/V8-R51MT04-LF1V001/FOTA-OTA/V8-R51MT04-LF1V001.973503.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8R51MT04/V8-R51MT04-LF1V001/FOTA-OTA/V8-R51MT04-LF1V001.973503.zip](http://na-update.cedock.com/apps/resource2/V8R51MT04/V8-R51MT04-LF1V001/FOTA-OTA/V8-R51MT04-LF1V001.973503.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8R51MT04/V8-R51MT04-LF1V001/FOTA-OTA/V8-R51MT04-LF1V001.973503.zip](http://as-update.cedock.com/apps/resource2/V8R51MT04/V8-R51MT04-LF1V001/FOTA-OTA/V8-R51MT04-LF1V001.973503.zip)

<a id="platform-r51mt05"></a>
#### R51M / R851 (R51MT05) (`V8-R51MT05-LF1V652`)
- **Platform Identifier**: `R51MT05` (Alternative ID: `R51MT01`)
- **Hardware Architecture & SoC**: Realtek RTD2851 / R51M (Legacy 4K GTV & ATV)
- **Compatible TV Models (Selection)**: *C645, C635, P745, C715, C815*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.74 GB` · **Release Date**: `2024-04` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `dc8cba08ffac17ebcf6b4458d902d394`
- **SHA-256 Checksum**: `7a2542a0204ddb1827af80631bb4ec281afca2b8e4d4c49771365b5cab3fcfc2`
- **CRC-32 Checksum**: `0x83A1D1B6`
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

<a id="platform-r51mt06"></a>
#### R51M / R851 (R51MT06) (`V8-R51MT06-LF1V029`)
- **Platform Identifier**: `R51MT06` (Alternative ID: `R51MT01`)
- **Hardware Architecture & SoC**: Realtek RTD2851 / R51M (Legacy 4K GTV & ATV)
- **Compatible TV Models (Selection)**: *C645, C635, P745, C715, C815*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.71 GB` · **Release Date**: `2023-11` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `c77fbe610cd7f0ba8aefefb023e641be`
- **SHA-256 Checksum**: `832bce9eb5ecd1873eae58ec2a9d8ef66a7d22e1f084775de2ed747ea19659fe`
- **CRC-32 Checksum**: `0xBFC5FBDB`
- **Official Changelog / Server Notes**: Series 5/6 NA Google TV interface performance tweaks, optical audio latency reduction.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2023-11-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/R51MT06/R51MT06:11/V8-R51MT06-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_r51mt06`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8R51MT06/V8-R51MT06-LF1V029/FOTA-OTA/V8-R51MT06-LF1V029.407989.zip](http://eu-update.cedock.com/apps/resource2/V8R51MT06/V8-R51MT06-LF1V029/FOTA-OTA/V8-R51MT06-LF1V029.407989.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8R51MT06/V8-R51MT06-LF1V029/FOTA-OTA/V8-R51MT06-LF1V029.407989.zip](http://na-update.cedock.com/apps/resource2/V8R51MT06/V8-R51MT06-LF1V029/FOTA-OTA/V8-R51MT06-LF1V029.407989.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8R51MT06/V8-R51MT06-LF1V029/FOTA-OTA/V8-R51MT06-LF1V029.407989.zip](http://as-update.cedock.com/apps/resource2/V8R51MT06/V8-R51MT06-LF1V029/FOTA-OTA/V8-R51MT06-LF1V029.407989.zip)

<a id="platform-r51mt07"></a>
#### R51M / R851 (R51MT07) (`V8-R51MT07-LF1V001`)
- **Platform Identifier**: `R51MT07` (Alternative ID: `R51MT01`)
- **Hardware Architecture & SoC**: Realtek RTD2851 / R51M (Legacy 4K GTV & ATV)
- **Compatible TV Models (Selection)**: *C645, C635, P745, C715, C815*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.75 GB` · **Release Date**: `2024-05` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `2b64689c27f51939ef35aea0cef1db7c`
- **SHA-256 Checksum**: `e3deaba04a144b0eb2003601985d98b943beeb1c0659598fbe8ac2288ac24a98`
- **CRC-32 Checksum**: `0xA4EE8161`
- **Official Changelog / Server Notes**: Realtek RTD2851M regional variant build: picture profile presets and audio delay calibration.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2024-05-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/R51MT07/R51MT07:11/V8-R51MT07-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_r51mt07`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8R51MT07/V8-R51MT07-LF1V001/FOTA-OTA/V8-R51MT07-LF1V001.717386.zip](http://eu-update.cedock.com/apps/resource2/V8R51MT07/V8-R51MT07-LF1V001/FOTA-OTA/V8-R51MT07-LF1V001.717386.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8R51MT07/V8-R51MT07-LF1V001/FOTA-OTA/V8-R51MT07-LF1V001.717386.zip](http://na-update.cedock.com/apps/resource2/V8R51MT07/V8-R51MT07-LF1V001/FOTA-OTA/V8-R51MT07-LF1V001.717386.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8R51MT07/V8-R51MT07-LF1V001/FOTA-OTA/V8-R51MT07-LF1V001.717386.zip](http://as-update.cedock.com/apps/resource2/V8R51MT07/V8-R51MT07-LF1V001/FOTA-OTA/V8-R51MT07-LF1V001.717386.zip)

<a id="platform-r51mt08"></a>
#### R51M / R851 (R51MT08) (`V8-R51MT08-LF1V001`)
- **Platform Identifier**: `R51MT08` (Alternative ID: `R51MT01`)
- **Hardware Architecture & SoC**: Realtek RTD2851 / R51M (Legacy 4K GTV & ATV)
- **Compatible TV Models (Selection)**: *C645, C635, P745, C715, C815*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.75 GB` · **Release Date**: `2024-05` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `19b4990c0db71617e35766c8a0270580`
- **SHA-256 Checksum**: `f81fd8956f086624523d3045137a8b4744d00bb2bd23e86d093deab0d4cb3c3c`
- **CRC-32 Checksum**: `0xA6AE2C94`
- **Official Changelog / Server Notes**: Realtek RTD2851M regional variant build: Wi-Fi driver robustness and system stability.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2024-05-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/R51MT08/R51MT08:11/V8-R51MT08-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_r51mt08`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8R51MT08/V8-R51MT08-LF1V001/FOTA-OTA/V8-R51MT08-LF1V001.439791.zip](http://eu-update.cedock.com/apps/resource2/V8R51MT08/V8-R51MT08-LF1V001/FOTA-OTA/V8-R51MT08-LF1V001.439791.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8R51MT08/V8-R51MT08-LF1V001/FOTA-OTA/V8-R51MT08-LF1V001.439791.zip](http://na-update.cedock.com/apps/resource2/V8R51MT08/V8-R51MT08-LF1V001/FOTA-OTA/V8-R51MT08-LF1V001.439791.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8R51MT08/V8-R51MT08-LF1V001/FOTA-OTA/V8-R51MT08-LF1V001.439791.zip](http://as-update.cedock.com/apps/resource2/V8R51MT08/V8-R51MT08-LF1V001/FOTA-OTA/V8-R51MT08-LF1V001.439791.zip)

<a id="platform-r51mt09"></a>
#### R51M / R851 (R51MT09) (`V8-R51MT09-LF1V001`)
- **Platform Identifier**: `R51MT09` (Alternative ID: `R51MT01`)
- **Hardware Architecture & SoC**: Realtek RTD2851 / R51M (Legacy 4K GTV & ATV)
- **Compatible TV Models (Selection)**: *C645, C635, P745, C715, C815*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.75 GB` · **Release Date**: `2024-05` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `e8e799e7aa6962f008a83dc20f9d9909`
- **SHA-256 Checksum**: `bde754ab07fce8972c9fa1f6b555c8b679340033fb360c071e536fdfb575b343`
- **CRC-32 Checksum**: `0xAD20C95E`
- **Official Changelog / Server Notes**: Realtek RTD2851M regional variant build: TV tuner reception and channel scan optimizations.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2024-05-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/R51MT09/R51MT09:11/V8-R51MT09-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_r51mt09`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8R51MT09/V8-R51MT09-LF1V001/FOTA-OTA/V8-R51MT09-LF1V001.105024.zip](http://eu-update.cedock.com/apps/resource2/V8R51MT09/V8-R51MT09-LF1V001/FOTA-OTA/V8-R51MT09-LF1V001.105024.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8R51MT09/V8-R51MT09-LF1V001/FOTA-OTA/V8-R51MT09-LF1V001.105024.zip](http://na-update.cedock.com/apps/resource2/V8R51MT09/V8-R51MT09-LF1V001/FOTA-OTA/V8-R51MT09-LF1V001.105024.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8R51MT09/V8-R51MT09-LF1V001/FOTA-OTA/V8-R51MT09-LF1V001.105024.zip](http://as-update.cedock.com/apps/resource2/V8R51MT09/V8-R51MT09-LF1V001/FOTA-OTA/V8-R51MT09-LF1V001.105024.zip)

<a id="platform-r51mt10"></a>
#### R51M / R851 (R51MT10) (`V8-R51MT10-LF1V109`)
- **Platform Identifier**: `R51MT10` (Alternative ID: `R51MT01`)
- **Hardware Architecture & SoC**: Realtek RTD2851 / R51M (Legacy 4K GTV & ATV)
- **Compatible TV Models (Selection)**: *C645, C635, P745, C715, C815*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.73 GB` · **Release Date**: `2023-09` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `12e048a36c2c42d5ef03d6b9c13cfc26`
- **SHA-256 Checksum**: `35d22f268eb206b4105c14a96b42c186229ec04be2f9fe367edc6fc4c5faa6ca`
- **CRC-32 Checksum**: `0x9BB381F6`
- **Official Changelog / Server Notes**: Series 4/5 entry 4K stability build, USB multimedia playback codec updates.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2023-09-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/R51MT10/R51MT10:11/V8-R51MT10-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_r51mt10`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8R51MT10/V8-R51MT10-LF1V109/FOTA-OTA/V8-R51MT10-LF1V109.312038.zip](http://eu-update.cedock.com/apps/resource2/V8R51MT10/V8-R51MT10-LF1V109/FOTA-OTA/V8-R51MT10-LF1V109.312038.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8R51MT10/V8-R51MT10-LF1V109/FOTA-OTA/V8-R51MT10-LF1V109.312038.zip](http://na-update.cedock.com/apps/resource2/V8R51MT10/V8-R51MT10-LF1V109/FOTA-OTA/V8-R51MT10-LF1V109.312038.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8R51MT10/V8-R51MT10-LF1V109/FOTA-OTA/V8-R51MT10-LF1V109.312038.zip](http://as-update.cedock.com/apps/resource2/V8R51MT10/V8-R51MT10-LF1V109/FOTA-OTA/V8-R51MT10-LF1V109.312038.zip)

<a id="platform-r75pt01"></a>
#### R75P / RT75 (R75PT01) (`V8-R75PT01-LF1V545`)
- **Platform Identifier**: `R75PT01` (Alternative ID: `0008T01`)
- **Hardware Architecture & SoC**: Realtek RT75 (G10 Platform, Entry-Mid 4K GTV)
- **Compatible TV Models (Selection)**: *P8LS, P7L, V6D, T6D, U65A, P6K, P7K, V6C, T6C, C6KS, C6CS, U65/75, MQLED70K, P755, C655, C655 Pro, T7B, V6B, QLED780/810, QM51L, QM5K, Q51K, Q63K, S551G, Q651G*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.92 GB` · **Release Date**: `2026-08-07` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `391cdffb44411798ca5a12a431d245ec`
- **SHA-256 Checksum**: `b5f8bbb203043f3b3e5d566cc9f526827cc086ea311ce31ee30d9e8f50a4806d`
- **CRC-32 Checksum**: `0xBA22A8CD`
- **Official Changelog / Server Notes**: Android 14 Google TV (GTV U) release: Security patch 2026-06-05, G10_4K_US_NF AS50 release.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 12` (Google TV (GTV))
  - **GMS Package**: `Android_12_GTV`
  - **Security Patch Level**: `2026-08-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/R75PT01/R75PT01:12/V8-R75PT01-LF1V001/user/release-keys`
  - **SDK API Level**: `31`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_r75pt01`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8R75PT01/V8-R75PT01-LF1V545/FOTA-OTA/V8-R75PT01-LF1V545.645674.zip](http://eu-update.cedock.com/apps/resource2/V8R75PT01/V8-R75PT01-LF1V545/FOTA-OTA/V8-R75PT01-LF1V545.645674.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8R75PT01/V8-R75PT01-LF1V545/FOTA-OTA/V8-R75PT01-LF1V545.645674.zip](http://na-update.cedock.com/apps/resource2/V8R75PT01/V8-R75PT01-LF1V545/FOTA-OTA/V8-R75PT01-LF1V545.645674.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8R75PT01/V8-R75PT01-LF1V545/FOTA-OTA/V8-R75PT01-LF1V545.645674.zip](http://as-update.cedock.com/apps/resource2/V8R75PT01/V8-R75PT01-LF1V545/FOTA-OTA/V8-R75PT01-LF1V545.645674.zip)

<a id="platform-t221t01"></a>
#### T221 / MT21 (T221T01) (`V8-T221T01-LF1V242`)
- **Platform Identifier**: `T221T01` (Alternative ID: `T221T02`)
- **Hardware Architecture & SoC**: MediaTek MT21 (2K / FHD Google TV & Android TV)
- **Compatible TV Models (Selection)**: *S350G, S55H, S5200 (Late), 32S5400, S5400A*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.38 GB` · **Release Date**: `2024-03` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `01969db7ee5a4e9ed5baecba1b8ea497`
- **SHA-256 Checksum**: `4ba8ab041d7dcd6635300023e1b428ca69c9ac84586ea1c529eca1319fa9d021`
- **CRC-32 Checksum**: `0xE2759854`
- **Official Changelog / Server Notes**: MediaTek MT21 global FHD release: Android TV 11 stability build and tuner optimization.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2024-03-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/T221T01/T221T01:11/V8-T221T01-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_t221t01`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8T221T01/V8-T221T01-LF1V242/FOTA-OTA/V8-T221T01-LF1V242.553714.zip](http://eu-update.cedock.com/apps/resource2/V8T221T01/V8-T221T01-LF1V242/FOTA-OTA/V8-T221T01-LF1V242.553714.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8T221T01/V8-T221T01-LF1V242/FOTA-OTA/V8-T221T01-LF1V242.553714.zip](http://na-update.cedock.com/apps/resource2/V8T221T01/V8-T221T01-LF1V242/FOTA-OTA/V8-T221T01-LF1V242.553714.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8T221T01/V8-T221T01-LF1V242/FOTA-OTA/V8-T221T01-LF1V242.553714.zip](http://as-update.cedock.com/apps/resource2/V8T221T01/V8-T221T01-LF1V242/FOTA-OTA/V8-T221T01-LF1V242.553714.zip)

<a id="platform-t221t02"></a>
#### T221 / MT21 (T221T02) (`V8-T221T02-LF1V085`)
- **Platform Identifier**: `T221T02` (Alternative ID: `T221T01`)
- **Hardware Architecture & SoC**: MediaTek MT21 (2K / FHD Google TV & Android TV)
- **Compatible TV Models (Selection)**: *S350G, S55H, S5200 (Late), 32S5400, S5400A*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.34 GB` · **Release Date**: `2023-10` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `68a5c7925e8b72a66daede8b64d220e5`
- **SHA-256 Checksum**: `f2ef5d3ff9432f92e169bdebd383abf3bd76fabd8a46bedab3884ac426570e73`
- **CRC-32 Checksum**: `0xDD5DAE8A`
- **Official Changelog / Server Notes**: MediaTek MT21 NA market release: ATSC channel scan fix and HDMI ARC latency improvements.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2023-10-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/T221T02/T221T02:11/V8-T221T02-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_t221t02`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8T221T02/V8-T221T02-LF1V085/FOTA-OTA/V8-T221T02-LF1V085.407126.zip](http://eu-update.cedock.com/apps/resource2/V8T221T02/V8-T221T02-LF1V085/FOTA-OTA/V8-T221T02-LF1V085.407126.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8T221T02/V8-T221T02-LF1V085/FOTA-OTA/V8-T221T02-LF1V085.407126.zip](http://na-update.cedock.com/apps/resource2/V8T221T02/V8-T221T02-LF1V085/FOTA-OTA/V8-T221T02-LF1V085.407126.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8T221T02/V8-T221T02-LF1V085/FOTA-OTA/V8-T221T02-LF1V085.407126.zip](http://as-update.cedock.com/apps/resource2/V8T221T02/V8-T221T02-LF1V085/FOTA-OTA/V8-T221T02-LF1V085.407126.zip)

<a id="platform-t221t03"></a>
#### T221 / MT21 (T221T03) (`V8-T221T03-LF1V001`)
- **Platform Identifier**: `T221T03` (Alternative ID: `T221T01`)
- **Hardware Architecture & SoC**: MediaTek MT21 (2K / FHD Google TV & Android TV)
- **Compatible TV Models (Selection)**: *S350G, S55H, S5200 (Late), 32S5400, S5400A*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.38 GB` · **Release Date**: `2024-03` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `97164c39541f33efde286c81e4ea1b50`
- **SHA-256 Checksum**: `5b1af2a3147006c1d2ad9534c143fc6770f24b9ec6987e4128c5c4ca7cb1e33c`
- **CRC-32 Checksum**: `0xEEC828AC`
- **Official Changelog / Server Notes**: MediaTek MT21 2K/FHD regional variant release: Android TV 11 stability build and tuner optimization.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2024-03-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/T221T03/T221T03:11/V8-T221T03-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_t221t03`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8T221T03/V8-T221T03-LF1V001/FOTA-OTA/V8-T221T03-LF1V001.948400.zip](http://eu-update.cedock.com/apps/resource2/V8T221T03/V8-T221T03-LF1V001/FOTA-OTA/V8-T221T03-LF1V001.948400.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8T221T03/V8-T221T03-LF1V001/FOTA-OTA/V8-T221T03-LF1V001.948400.zip](http://na-update.cedock.com/apps/resource2/V8T221T03/V8-T221T03-LF1V001/FOTA-OTA/V8-T221T03-LF1V001.948400.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8T221T03/V8-T221T03-LF1V001/FOTA-OTA/V8-T221T03-LF1V001.948400.zip](http://as-update.cedock.com/apps/resource2/V8T221T03/V8-T221T03-LF1V001/FOTA-OTA/V8-T221T03-LF1V001.948400.zip)

<a id="platform-t221t04"></a>
#### T221 / MT21 (T221T04) (`V8-T221T04-LF1V001`)
- **Platform Identifier**: `T221T04` (Alternative ID: `T221T01`)
- **Hardware Architecture & SoC**: MediaTek MT21 (2K / FHD Google TV & Android TV)
- **Compatible TV Models (Selection)**: *S350G, S55H, S5200 (Late), 32S5400, S5400A*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.38 GB` · **Release Date**: `2024-03` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `2f4390b02b56e2b205babbe265be2596`
- **SHA-256 Checksum**: `041e8918fa013147208797775927744450c2059ce85c4ad403df87f3dbda9a14`
- **CRC-32 Checksum**: `0x9BE362E0`
- **Official Changelog / Server Notes**: MediaTek MT21 2K/FHD regional variant release: Android TV 11 stability build and tuner optimization.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2024-03-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/T221T04/T221T04:11/V8-T221T04-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_t221t04`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8T221T04/V8-T221T04-LF1V001/FOTA-OTA/V8-T221T04-LF1V001.296069.zip](http://eu-update.cedock.com/apps/resource2/V8T221T04/V8-T221T04-LF1V001/FOTA-OTA/V8-T221T04-LF1V001.296069.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8T221T04/V8-T221T04-LF1V001/FOTA-OTA/V8-T221T04-LF1V001.296069.zip](http://na-update.cedock.com/apps/resource2/V8T221T04/V8-T221T04-LF1V001/FOTA-OTA/V8-T221T04-LF1V001.296069.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8T221T04/V8-T221T04-LF1V001/FOTA-OTA/V8-T221T04-LF1V001.296069.zip](http://as-update.cedock.com/apps/resource2/V8T221T04/V8-T221T04-LF1V001/FOTA-OTA/V8-T221T04-LF1V001.296069.zip)

<a id="platform-t221t05"></a>
#### T221 / MT21 (T221T05) (`V8-T221T05-LF1V001`)
- **Platform Identifier**: `T221T05` (Alternative ID: `T221T01`)
- **Hardware Architecture & SoC**: MediaTek MT21 (2K / FHD Google TV & Android TV)
- **Compatible TV Models (Selection)**: *S350G, S55H, S5200 (Late), 32S5400, S5400A*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.38 GB` · **Release Date**: `2024-03` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `182eeeebcf4f43cb85556e6fa5020482`
- **SHA-256 Checksum**: `4a56155b8224381f5af60a8952e8f5b656ae18b92b71c21e23ad15c8c5c0f275`
- **CRC-32 Checksum**: `0xC027B64E`
- **Official Changelog / Server Notes**: MediaTek MT21 2K/FHD regional variant release: Android TV 11 stability build and tuner optimization.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2024-03-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/T221T05/T221T05:11/V8-T221T05-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_t221t05`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8T221T05/V8-T221T05-LF1V001/FOTA-OTA/V8-T221T05-LF1V001.859917.zip](http://eu-update.cedock.com/apps/resource2/V8T221T05/V8-T221T05-LF1V001/FOTA-OTA/V8-T221T05-LF1V001.859917.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8T221T05/V8-T221T05-LF1V001/FOTA-OTA/V8-T221T05-LF1V001.859917.zip](http://na-update.cedock.com/apps/resource2/V8T221T05/V8-T221T05-LF1V001/FOTA-OTA/V8-T221T05-LF1V001.859917.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8T221T05/V8-T221T05-LF1V001/FOTA-OTA/V8-T221T05-LF1V001.859917.zip](http://as-update.cedock.com/apps/resource2/V8T221T05/V8-T221T05-LF1V001/FOTA-OTA/V8-T221T05-LF1V001.859917.zip)

<a id="platform-t221t06"></a>
#### T221 / MT21 (T221T06) (`V8-T221T06-LF1V001`)
- **Platform Identifier**: `T221T06` (Alternative ID: `T221T01`)
- **Hardware Architecture & SoC**: MediaTek MT21 (2K / FHD Google TV & Android TV)
- **Compatible TV Models (Selection)**: *S350G, S55H, S5200 (Late), 32S5400, S5400A*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.38 GB` · **Release Date**: `2024-03` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `eae2f54861f68bc897bd0b69d539bd64`
- **SHA-256 Checksum**: `3e4cd9a630266af15bc8b8c3851b94cdcc738402969bebe07105adfbe150c68f`
- **CRC-32 Checksum**: `0x02580235`
- **Official Changelog / Server Notes**: MediaTek MT21 2K/FHD regional variant release: Android TV 11 stability build and tuner optimization.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2024-03-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/T221T06/T221T06:11/V8-T221T06-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_t221t06`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8T221T06/V8-T221T06-LF1V001/FOTA-OTA/V8-T221T06-LF1V001.279555.zip](http://eu-update.cedock.com/apps/resource2/V8T221T06/V8-T221T06-LF1V001/FOTA-OTA/V8-T221T06-LF1V001.279555.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8T221T06/V8-T221T06-LF1V001/FOTA-OTA/V8-T221T06-LF1V001.279555.zip](http://na-update.cedock.com/apps/resource2/V8T221T06/V8-T221T06-LF1V001/FOTA-OTA/V8-T221T06-LF1V001.279555.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8T221T06/V8-T221T06-LF1V001/FOTA-OTA/V8-T221T06-LF1V001.279555.zip](http://as-update.cedock.com/apps/resource2/V8T221T06/V8-T221T06-LF1V001/FOTA-OTA/V8-T221T06-LF1V001.279555.zip)

<a id="platform-t221t07"></a>
#### T221 / MT21 (T221T07) (`V8-T221T07-LF1V001`)
- **Platform Identifier**: `T221T07` (Alternative ID: `T221T01`)
- **Hardware Architecture & SoC**: MediaTek MT21 (2K / FHD Google TV & Android TV)
- **Compatible TV Models (Selection)**: *S350G, S55H, S5200 (Late), 32S5400, S5400A*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.38 GB` · **Release Date**: `2024-03` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `23e89a4f83eb7803aa554b30163b4d48`
- **SHA-256 Checksum**: `7645f46384c1cc0ccdd031da8fcb415de4fe1d359a6db460eeb571838ea8d2ff`
- **CRC-32 Checksum**: `0x6918F787`
- **Official Changelog / Server Notes**: MediaTek MT21 2K/FHD regional variant release: Android TV 11 stability build and tuner optimization.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2024-03-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/T221T07/T221T07:11/V8-T221T07-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_t221t07`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8T221T07/V8-T221T07-LF1V001/FOTA-OTA/V8-T221T07-LF1V001.499180.zip](http://eu-update.cedock.com/apps/resource2/V8T221T07/V8-T221T07-LF1V001/FOTA-OTA/V8-T221T07-LF1V001.499180.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8T221T07/V8-T221T07-LF1V001/FOTA-OTA/V8-T221T07-LF1V001.499180.zip](http://na-update.cedock.com/apps/resource2/V8T221T07/V8-T221T07-LF1V001/FOTA-OTA/V8-T221T07-LF1V001.499180.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8T221T07/V8-T221T07-LF1V001/FOTA-OTA/V8-T221T07-LF1V001.499180.zip](http://as-update.cedock.com/apps/resource2/V8T221T07/V8-T221T07-LF1V001/FOTA-OTA/V8-T221T07-LF1V001.499180.zip)

<a id="platform-t221t08"></a>
#### T221 / MT21 (T221T08) (`V8-T221T08-LF1V001`)
- **Platform Identifier**: `T221T08` (Alternative ID: `T221T01`)
- **Hardware Architecture & SoC**: MediaTek MT21 (2K / FHD Google TV & Android TV)
- **Compatible TV Models (Selection)**: *S350G, S55H, S5200 (Late), 32S5400, S5400A*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.38 GB` · **Release Date**: `2024-03` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `a83ca210bd7afa6d3fced6a3f2be0f16`
- **SHA-256 Checksum**: `c6fd16db3b8a9d3d858335720c8c19f9d85413ac42991e459976ed0b1b80d8bb`
- **CRC-32 Checksum**: `0xED3D2DE3`
- **Official Changelog / Server Notes**: MediaTek MT21 2K/FHD regional variant release: Android TV 11 stability build and tuner optimization.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2024-03-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/T221T08/T221T08:11/V8-T221T08-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_t221t08`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8T221T08/V8-T221T08-LF1V001/FOTA-OTA/V8-T221T08-LF1V001.941831.zip](http://eu-update.cedock.com/apps/resource2/V8T221T08/V8-T221T08-LF1V001/FOTA-OTA/V8-T221T08-LF1V001.941831.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8T221T08/V8-T221T08-LF1V001/FOTA-OTA/V8-T221T08-LF1V001.941831.zip](http://na-update.cedock.com/apps/resource2/V8T221T08/V8-T221T08-LF1V001/FOTA-OTA/V8-T221T08-LF1V001.941831.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8T221T08/V8-T221T08-LF1V001/FOTA-OTA/V8-T221T08-LF1V001.941831.zip](http://as-update.cedock.com/apps/resource2/V8T221T08/V8-T221T08-LF1V001/FOTA-OTA/V8-T221T08-LF1V001.941831.zip)

<a id="platform-t221t09"></a>
#### T221 / MT21 (T221T09) (`V8-T221T09-LF1V001`)
- **Platform Identifier**: `T221T09` (Alternative ID: `T221T01`)
- **Hardware Architecture & SoC**: MediaTek MT21 (2K / FHD Google TV & Android TV)
- **Compatible TV Models (Selection)**: *S350G, S55H, S5200 (Late), 32S5400, S5400A*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.38 GB` · **Release Date**: `2024-03` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `fbb4acdbca8424adf78abefb20cf80ba`
- **SHA-256 Checksum**: `29b10e3c747283e7aadedfd7cf8fe685a50d7f930e5bf4eec91e41d47b0c7d7a`
- **CRC-32 Checksum**: `0xE1A941FF`
- **Official Changelog / Server Notes**: MediaTek MT21 2K/FHD regional variant release: Android TV 11 stability build and tuner optimization.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 11` (Android TV (ATV))
  - **GMS Package**: `Android_11_ATV`
  - **Security Patch Level**: `2024-03-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/T221T09/T221T09:11/V8-T221T09-LF1V001/user/release-keys`
  - **SDK API Level**: `30`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_t221t09`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8T221T09/V8-T221T09-LF1V001/FOTA-OTA/V8-T221T09-LF1V001.110300.zip](http://eu-update.cedock.com/apps/resource2/V8T221T09/V8-T221T09-LF1V001/FOTA-OTA/V8-T221T09-LF1V001.110300.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8T221T09/V8-T221T09-LF1V001/FOTA-OTA/V8-T221T09-LF1V001.110300.zip](http://na-update.cedock.com/apps/resource2/V8T221T09/V8-T221T09-LF1V001/FOTA-OTA/V8-T221T09-LF1V001.110300.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8T221T09/V8-T221T09-LF1V001/FOTA-OTA/V8-T221T09-LF1V001.110300.zip](http://as-update.cedock.com/apps/resource2/V8T221T09/V8-T221T09-LF1V001/FOTA-OTA/V8-T221T09-LF1V001.110300.zip)

<a id="platform-t615t01"></a>
#### T615 / MT9615 (T615T01) (`V8-T615T01-LF1V082`)
- **Platform Identifier**: `T615T01` (Alternative ID: `T615T02`)
- **Hardware Architecture & SoC**: MediaTek MT9615 (4K 120/144Hz)
- **Compatible TV Models (Selection)**: *C845, C835, C735, C825, C728, C645 (Late), P745, Q7 (2023), R646 (2021)*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.92 GB` · **Release Date**: `2024-05` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `59ca23d8dd5e07be6d73d58dd3a5f170`
- **SHA-256 Checksum**: `2341b055b94308e7e332e80eda520763e891e6e231140c8f78c3e1e5ae241568`
- **CRC-32 Checksum**: `0xD08CFF8E`
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
#### T615 / MT9615 (T615T02) (`V8-T615T02-LF1V073`)
- **Platform Identifier**: `T615T02` (Alternative ID: `T615T01`)
- **Hardware Architecture & SoC**: MediaTek MT9615 (4K 120/144Hz)
- **Compatible TV Models (Selection)**: *C845, C835, C735, C825, C728, C645 (Late), P745, Q7 (2023), R646 (2021)*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.89 GB` · **Release Date**: `2024-04` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `f07a2972dca47c392ce4f51b65a89179`
- **SHA-256 Checksum**: `f3c352d122d8bc55ed826239479dc3dfcc9523597cd11c370bba2c94b280e61c`
- **CRC-32 Checksum**: `0x4185B600`
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
#### T615 / MT9615 (T615T03) (`V8-T615T03-LF1V082`)
- **Platform Identifier**: `T615T03` (Alternative ID: `T615T01`)
- **Hardware Architecture & SoC**: MediaTek MT9615 (4K 120/144Hz)
- **Compatible TV Models (Selection)**: *C845, C835, C735, C825, C728, C645 (Late), P745, Q7 (2023), R646 (2021)*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.92 GB` · **Release Date**: `2024-05` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `b2f53f98570fd79525ad6517db646dbb`
- **SHA-256 Checksum**: `3f6c33a6c281b8da1d3669d75dfdc2d82177152fdf6947d74877a3787d5c8169`
- **CRC-32 Checksum**: `0xA81C95B2`
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

<a id="platform-t653t01"></a>
#### Pentonic 700 (T653T01) (`V8-T653T01-LF1V655`)
- **Platform Identifier**: `T653T01` (Alternative ID: `0012T01`)
- **Hardware Architecture & SoC**: MediaTek MT9653 / MT9618 (MT53), 4K 144Hz VRR
- **Compatible TV Models (Selection)**: *X955, X955 Max (115"), C955, C855, C805, C765, C755, C745X2, C845X2, C7L, C6L, RM7L, X11K, C9K, C8K, C7K, C6K, P8K, T8C, 98C655, 85C655Pro, 98P745, 98P755*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `2.35 GB` · **Release Date**: `2026-01` · **Region**: `EU`
- **FOTA Verification Status**: `Checked (Static Mirror)`
- **MD5 Checksum**: `9d687f52557a5a18b1649ffb0fa58fc4`
- **SHA-256 Checksum**: `74d1a7d82f256fea9372d4b4f8be0119727dd1418a96fbdd839dc30e92894d78`
- **CRC-32 Checksum**: `0xB134BEF4`
- **Official Changelog / Server Notes**: Android 12/14 Google TV: Dolby Vision IQ enhancements, Game Master 2.0 stability, 144Hz VRR optimizations.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 12` (Google TV (GTV))
  - **GMS Package**: `Android_12_GTV`
  - **Security Patch Level**: `2026-01-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/T653T01/T653T01:12/V8-T653T01-LF1V001/user/release-keys`
  - **SDK API Level**: `31`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_t653t01`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8T653T01/V8-T653T01-LF1V655/FOTA-OTA/V8-T653T01-LF1V655.190489.zip](http://eu-update.cedock.com/apps/resource2/V8T653T01/V8-T653T01-LF1V655/FOTA-OTA/V8-T653T01-LF1V655.190489.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8T653T01/V8-T653T01-LF1V655/FOTA-OTA/V8-T653T01-LF1V655.190489.zip](http://na-update.cedock.com/apps/resource2/V8T653T01/V8-T653T01-LF1V655/FOTA-OTA/V8-T653T01-LF1V655.190489.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8T653T01/V8-T653T01-LF1V655/FOTA-OTA/V8-T653T01-LF1V655.190489.zip](http://as-update.cedock.com/apps/resource2/V8T653T01/V8-T653T01-LF1V655/FOTA-OTA/V8-T653T01-LF1V655.190489.zip)

<a id="platform-t653t02"></a>
#### Pentonic 700 (NA/LA) (T653T02) (`V8-T653T02-LF1V620`)
- **Platform Identifier**: `T653T02` (Alternative ID: `0012T02`)
- **Hardware Architecture & SoC**: MediaTek Pentonic 700 (G08 / N. America & LATAM)
- **Compatible TV Models (Selection)**: *QM891G, QM851G, QM751G, Q651G, Q750G, S551G, RM7L, QM7L, Q77L, X11K, QM8K, QM7K, Q77K, QM6K, QM67K*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `2.28 GB` · **Release Date**: `2025-11` · **Region**: `NA`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `e0088b23848c42387dc960abed08f18e`
- **SHA-256 Checksum**: `e958c84356ebd594b126b5908d34842ebde12895cc28b234ed944300347cabeb`
- **CRC-32 Checksum**: `0x3E16B7D0`
- **Official Changelog / Server Notes**: North American Google TV: QM851G/QM751G local dimming timing adjustments, ATSC 3.0 tuner stability.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 12` (Google TV (GTV))
  - **GMS Package**: `Android_12_GTV`
  - **Security Patch Level**: `2025-11-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/T653T02/T653T02:12/V8-T653T02-LF1V001/user/release-keys`
  - **SDK API Level**: `31`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_t653t02`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8T653T02/V8-T653T02-LF1V620/FOTA-OTA/V8-T653T02-LF1V620.303526.zip](http://eu-update.cedock.com/apps/resource2/V8T653T02/V8-T653T02-LF1V620/FOTA-OTA/V8-T653T02-LF1V620.303526.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8T653T02/V8-T653T02-LF1V620/FOTA-OTA/V8-T653T02-LF1V620.303526.zip](http://na-update.cedock.com/apps/resource2/V8T653T02/V8-T653T02-LF1V620/FOTA-OTA/V8-T653T02-LF1V620.303526.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8T653T02/V8-T653T02-LF1V620/FOTA-OTA/V8-T653T02-LF1V620.303526.zip](http://as-update.cedock.com/apps/resource2/V8T653T02/V8-T653T02-LF1V620/FOTA-OTA/V8-T653T02-LF1V620.303526.zip)

<a id="platform-t653t03"></a>
#### Pentonic 700 (Flagship) (T653T03) (`V8-T653T03-LF1V110`)
- **Platform Identifier**: `T653T03` (Alternative ID: `0012T03`)
- **Hardware Architecture & SoC**: MediaTek Pentonic 700 (G16)
- **Compatible TV Models (Selection)**: *QM9K Series*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `2.41 GB` · **Release Date**: `2025-10` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `f10b2e9f3a23f36b74b96d837a45a326`
- **SHA-256 Checksum**: `0b922bf0abd31f9f886c0658f51a0dcbe2a88eb51a034567738180f7b4d96f5a`
- **CRC-32 Checksum**: `0x05C5FE59`
- **Official Changelog / Server Notes**: G16 flagship chassis DSP audio processor updates and high-zone Mini-LED panel drive optimizations.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 12` (Google TV (GTV))
  - **GMS Package**: `Android_12_GTV`
  - **Security Patch Level**: `2025-10-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/T653T03/T653T03:12/V8-T653T03-LF1V001/user/release-keys`
  - **SDK API Level**: `31`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_t653t03`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8T653T03/V8-T653T03-LF1V110/FOTA-OTA/V8-T653T03-LF1V110.146158.zip](http://eu-update.cedock.com/apps/resource2/V8T653T03/V8-T653T03-LF1V110/FOTA-OTA/V8-T653T03-LF1V110.146158.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8T653T03/V8-T653T03-LF1V110/FOTA-OTA/V8-T653T03-LF1V110.146158.zip](http://na-update.cedock.com/apps/resource2/V8T653T03/V8-T653T03-LF1V110/FOTA-OTA/V8-T653T03-LF1V110.146158.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8T653T03/V8-T653T03-LF1V110/FOTA-OTA/V8-T653T03-LF1V110.146158.zip](http://as-update.cedock.com/apps/resource2/V8T653T03/V8-T653T03-LF1V110/FOTA-OTA/V8-T653T03-LF1V110.146158.zip)

<a id="platform-t655t01"></a>
#### Pentonic 800 (T655T01) (`V8-T655T01-LF1V025`)
- **Platform Identifier**: `T655T01` (Alternative ID: `0015T01`)
- **Hardware Architecture & SoC**: MediaTek MT9655 (MT55), Flagship 4K Mini-LED
- **Compatible TV Models (Selection)**: *X11L, C8L, RM9L, QM8L (2026)*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `~2.1 GB` · **Release Date**: `2026-02` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `2dbafab978b799be10b47723a1f83814`
- **SHA-256 Checksum**: `8c49af00a0f3b1dacb0af68669bfa19dd2d631c544d8ab8f986d132f19825f30`
- **CRC-32 Checksum**: `0x6F3898BB`
- **Official Changelog / Server Notes**: Android 14 Google TV flagship build: MediaTek MT9655 (Pentonic 800), 144Hz VRR & Mini-LED dimming engine.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 14` (Google TV (GTV))
  - **GMS Package**: `Android_14_GTV`
  - **Security Patch Level**: `2026-02-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/T655T01/T655T01:14/V8-T655T01-LF1V001/user/release-keys`
  - **SDK API Level**: `34`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_t655t01`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8T655T01/V8-T655T01-LF1V025/FOTA-OTA/V8-T655T01-LF1V025.256205.zip](http://eu-update.cedock.com/apps/resource2/V8T655T01/V8-T655T01-LF1V025/FOTA-OTA/V8-T655T01-LF1V025.256205.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8T655T01/V8-T655T01-LF1V025/FOTA-OTA/V8-T655T01-LF1V025.256205.zip](http://na-update.cedock.com/apps/resource2/V8T655T01/V8-T655T01-LF1V025/FOTA-OTA/V8-T655T01-LF1V025.256205.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8T655T01/V8-T655T01-LF1V025/FOTA-OTA/V8-T655T01-LF1V025.256205.zip](http://as-update.cedock.com/apps/resource2/V8T655T01/V8-T655T01-LF1V025/FOTA-OTA/V8-T655T01-LF1V025.256205.zip)

<a id="platform-t658t01"></a>
#### Pentonic 600 (T658T01) (`V8-T658T01-LF1V575`)
- **Platform Identifier**: `T658T01` (Alternative ID: `0014T01`)
- **Hardware Architecture & SoC**: MediaTek MT9658 (Pentonic 600)
- **Compatible TV Models (Selection)**: *C655 (Selected AP/LA Releases)*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.92 GB` · **Release Date**: `2026-06-15` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `30f8380c248ecbad00468e6065603f3b`
- **SHA-256 Checksum**: `c7a213df69b1a47015657193046f10386fe18f9af71dc1ee9c16543e81cd5b0e`
- **CRC-32 Checksum**: `0x5C176F1A`
- **Official Changelog / Server Notes**: Previous production release.
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8T658T01/V8-T658T01-LF1V575/FOTA-OTA/V8-T658T01-LF1V575.002400.zip](http://eu-update.cedock.com/apps/resource2/V8T658T01/V8-T658T01-LF1V575/FOTA-OTA/V8-T658T01-LF1V575.002400.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8T658T01/V8-T658T01-LF1V575/FOTA-OTA/V8-T658T01-LF1V575.002400.zip](http://na-update.cedock.com/apps/resource2/V8T658T01/V8-T658T01-LF1V575/FOTA-OTA/V8-T658T01-LF1V575.002400.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8T658T01/V8-T658T01-LF1V575/FOTA-OTA/V8-T658T01-LF1V575.002400.zip](http://as-update.cedock.com/apps/resource2/V8T658T01/V8-T658T01-LF1V575/FOTA-OTA/V8-T658T01-LF1V575.002400.zip)

<a id="platform-t800t02"></a>
#### T800 (T800T02) (`V8-T800T02-LF1V163`)
- **Platform Identifier**: `T800T02` (Alternative ID: `0013T02`)
- **Hardware Architecture & SoC**: Amlogic AMLT963D4 (G09, 5-Core A55 @ 1.5GHz / 1.9GHz DVFS, Mali-G57 MC1, 2GB DDR4-3200)
- **Compatible TV Models (Selection)**: *C655, C655 Pro, P755, T7B, P7K, C6KS, 55P755*
- **Package Type**: `Full OTA (ZIP)` · **Size**: `1.82 GB` · **Release Date**: `2025-08` · **Region**: `EU`
- **FOTA Verification Status**: `Cached (Unchanged)`
- **MD5 Checksum**: `270f558789d902fe7ffbdc7f9357931e`
- **SHA-256 Checksum**: `ebe52901c55e4211acb4a6c01bed21d6d3ad93180bd08c3875e7929f936a1bc4`
- **CRC-32 Checksum**: `0x608D9E72`
- **Official Changelog / Server Notes**: Amlogic G09 Google TV system optimization: DVFS CPU scaling, memory management improvements.
- **Extracted Android Build Properties**:
  - **Android OS Version**: `Android 12` (Google TV (GTV))
  - **GMS Package**: `Android_12_GTV`
  - **Security Patch Level**: `2025-08-05`
  - **Build Date**: `Aug 07, 2026`
  - **Build Fingerprint**: `TCL/T800T02/T800T02:12/V8-T800T02-LF1V001/user/release-keys`
  - **SDK API Level**: `31`
  - **Incremental Revision**: `LF1V001`
  - **Target Device Codename**: `tcl_t800t02`
- **EU / Global CDN**: [http://eu-update.cedock.com/apps/resource2/V8T800T02/V8-T800T02-LF1V163/FOTA-OTA/V8-T800T02-LF1V163.128694.zip](http://eu-update.cedock.com/apps/resource2/V8T800T02/V8-T800T02-LF1V163/FOTA-OTA/V8-T800T02-LF1V163.128694.zip)
- **North America (NA) CDN**: [http://na-update.cedock.com/apps/resource2/V8T800T02/V8-T800T02-LF1V163/FOTA-OTA/V8-T800T02-LF1V163.128694.zip](http://na-update.cedock.com/apps/resource2/V8T800T02/V8-T800T02-LF1V163/FOTA-OTA/V8-T800T02-LF1V163.128694.zip)
- **Asia-Pacific (AS) CDN**: [http://as-update.cedock.com/apps/resource2/V8T800T02/V8-T800T02-LF1V163/FOTA-OTA/V8-T800T02-LF1V163.128694.zip](http://as-update.cedock.com/apps/resource2/V8T800T02/V8-T800T02-LF1V163/FOTA-OTA/V8-T800T02-LF1V163.128694.zip)

---

*Generated automatically by [`scripts/fetch_firmwares.py`](https://github.com/FaserF/TCL-Discussion-Telegram/blob/main/scripts/fetch_firmwares.py)*