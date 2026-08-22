> **INTERNAL DEVELOPER REFERENCE (Not for public web publication)**
> This reference documents the reverse-engineered FOTA XML protocol, HMAC signing specifications, and CDN infrastructure.

# TCL TV Firmware Update Mechanisms

Technical reference for the TCL Smart TV FOTA (Firmware Over-The-Air) update infrastructure, URL patterns, reverse-engineering findings, and server protocols.

---

## 1. Firmware CDN & Direct Download Patterns

TCL TV firmwares are hosted on AWS S3 / CloudFront infrastructure, routed through regional CDN nodes under the `cedock.com` domain.

### 1.1 OTA ZIP Download URL Pattern

```
http://{region}-update.cedock.com/apps/resource2/{PlatformDir}/{FirmwareName}/FOTA-OTA/{FirmwareName}.{BuildNumber}.zip
```

| Placeholder | Description | Example |
|---|---|---|
| `{region}` | Regional CDN node prefix | `eu`, `na`, `as` |
| `{PlatformDir}` | Platform identifier without dashes, prefixed with `V8` | `V8R851T02`, `V8T653T01`, `V8R51MT05` |
| `{FirmwareName}` | Full firmware release name | `V8-R851T02-LF1V653`, `V8-R51MT05-LF1V652` |
| `{BuildNumber}` | Numeric compilation timestamp suffix | `019203`, `019519`, `008946` |

### 1.2 Known CDN Hosts

| Host | Region |
|---|---|
| `eu-update.cedock.com` | Europe / Global |
| `na-update.cedock.com` | North America / Latin America |
| `as-update.cedock.com` | Asia-Pacific |
| `as.update.cedock.com` | Asia-Pacific (legacy dot-notation) |

### 1.3 Live-Confirmed Examples

```
http://eu-update.cedock.com/apps/resource2/V8R851T02/V8-R851T02-LF1V653/FOTA-OTA/V8-R851T02-LF1V653.019203.zip
http://na-update.cedock.com/apps/resource2/V8R851T02/V8-R851T02-LF1V653/FOTA-OTA/V8-R851T02-LF1V653.019203.zip
http://eu-update.cedock.com/apps/resource2/V8R41KT01/V8-R41KT01-LF1V343/FOTA-OTA/V8-R41KT01-LF1V343.008946.zip
http://eu-update.cedock.com/apps/resource2/V8T615T01/V8-T615T01-LF1V082/FOTA-OTA/V8-T615T01-LF1V082.zip
http://as-update.cedock.com/apps/resource2/V8R51MT02/V8-R51MT02-LF1V238/FOTA-OTA/V8-R51MT02-LF1V238.019519.zip
```

### 1.4 Why Blind URL Construction (Brute-Forcing) Fails

The `{BuildNumber}` (e.g. `019203`) is timestamp/compilation-based and assigned server-side during the release build. A request with a missing or incorrect BuildNumber returns HTTP 403 or 404. Therefore, direct URL construction without querying the FOTA API is not feasible for unannounced releases.

### 1.5 Alternative Repository (`celesw.tcl.com`)

In addition to `cedock.com`, TCL maintains a public file repository for service centers and software packages:

```
http://celesw.tcl.com/CSEU%20TV/Software/
```

This index contains select full firmware packages and recovery images, but is not continuously updated in real-time like the FOTA backend.

---

## 2. Official TV FOTA Update API (`huan.tv`)

TCL Smart TVs communicate with the `huan.tv` backend for software discovery and OTA upgrade queries.

### 2.1 Regional API Hosts & AppKeys

*Source: `ProtocolAddrChanger.java` (lines 39–79) and `ProtocolConstTools.java` (`a/a/c/e/b/a.java`, fields `a`–`t`).*

| Region | API Host | App-ID | AppKey (MD5 hex) |
|---|---|---|---|
| Europe / Africa / Middle East / Global default | `eu-filter-upgrade.huan.tv` | `upmp-eu` | `4b93841c48eb1af1dfbe2c82384136c9` |
| North America / Latin America / Canada | `na-filter-upgrade.huan.tv` | `upmp-na` | `dacf21ce497259eae5f65312da7d868c` |
| Asia-Pacific / Australia / Taiwan / Hong Kong / Japan | `as-filter-upgrade.huan.tv` | `upmp-as` | `35b8fa949e0578f41f6e751991c800aa` |
| China | `filter-upgrade.huan.tv` | `upmp-cn` | `d49a5258bfcc5f6c3e430f67a0313e90` |
| Test / Development | `testfilter-upgrade.huan.tv` | `upmp-test` | `3550bec90eee953f85361ff46d378e4e` |

### 2.2 Available Endpoints

*Source: `ProtocolConstTools.java` (`a/a/c/e/b/a.java`).*

| Endpoint Path | Purpose |
|---|---|
| `/service/upmp/upgradeIncrInterface` | Primary incremental & full OTA update check |
| `/service/platform/getUpgradeByVerID` | Query upgrade details by specific Version ID |
| `/service/getinfo/getUpgradeByDnum/` | Query upgrade info by device serial number (`dnum`) |
| `/service/upmp/operateInterface` | Reporting & status confirmation |

### 2.3 Primary Authentication (`HUAN-Sign`)

All requests to `/service/upmp/upgradeIncrInterface` are authenticated using `HUAN-*` headers:

| Header | Description |
|---|---|
| `HUAN-AppId` | Regional App-ID (e.g. `upmp-eu`) |
| `HUAN-RequestId` | 32-character hexadecimal UUID |
| `HUAN-Timestamp` | Unix timestamp in seconds (`System.currentTimeMillis() / 1000`) |
| `HUAN-Sign` | MD5 hash of: `AppKey + RequestId + Timestamp + Method + Path + XmlBody` |

*Source: `SystemInterceptor.java` (`a/a/c/e/o/u.java`, lines 17–49).*

### 2.4 Request Format (`upgradeIncrRequest`)

*Source: `RequestsXmlUtils.java` (lines 45–93) and `UpdateRequestXml.java`.*

```xml
<?xml version="1.0" encoding="UTF-8"?>
<upgradeIncrRequest>
  <apiversion>1.0</apiversion>
  <upmptype>3</upmptype>
  <app>
    <appid>V8R51MT05</appid>
    <increment>0</increment>
    <ver>V8-R51MT05-LF1V652</ver>
    <verid>0</verid>
  </app>
  <parameter>
    <callid>0</callid>
    <client>
      <devmodel>TCL-EU-RTD51M-S1</devmodel>
      <didtoken>00000000000000000000000000000000</didtoken>
      <dnum>000000000</dnum>
      <projectid>0</projectid>
      <systemver>11</systemver>
    </client>
    <https>true</https>
    <language>en</language>
    <region>EU</region>
    <timezone>Europe/Berlin</timezone>
  </parameter>
</upgradeIncrRequest>
```

### 2.5 Response Structure (`upgradeIncrResponse`)

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<upgradeIncrResponse>
  <servertime>1787340235</servertime>
  <callid>d3be4b98fda6223dfe68d3b056999678</callid>
  <state>0000</state>
  <note>成功</note>
  <language>en</language>
  <apiversion>1.0</apiversion>
</upgradeIncrResponse>
```

**Known State Codes:**

| State Code | Meaning |
|---|---|
| `0000` | Query successful |
| `9014` | XML parsing error or malformed structure |
| `9016` | Parameter validation failure |
| `9018` | Invalid device serial number (`dnum`) |
| `111018` | Request timestamp timeout |

---

## 3. Secondary Authentication & Analytics (`TCL1-HMAC-SHA256`)

In addition to `HUAN-Sign`, `SystemUpdate.apk` implements an AWS Signature V4-style authentication mechanism (`TCL1-HMAC-SHA256`) used for reporting, BI analytics, and auxiliary services (`on-hweudc-o.api.leiniao.com`, `eu-global-auth-tclupdate.cedock.com`).

*Source: `SignInterceptor.java` (`com/tcl/ff/component/core/http/core/interceptors/SignInterceptor.java`).*

### 3.1 Headers Generated

| Header | Example |
|---|---|
| `XTCL-App` | `com.tcl.versionUpdateApp` or `b11d9e6f68864833b0d77b43dfa446de` |
| `XTCL-Timestamp` | `1787339989` |
| `XTCL-nonce` | `09bfb79e140b4fbf9733d7a5880907e2` (UUID without dashes) |
| `XTCL-Authorization` | `TCL1-HMAC-SHA256 Credential={AppId},SignedHeaders={headers},Signature={sig}` |

### 3.2 Canonical Request & Signing Algorithm

1. **Header Sorting**: Sorted case-insensitive map of `xtcl-*`, `host`, and `content-type` headers.
2. **Body Hash**: `Base64(SHA256(BodyBytes))`.
3. **Canonical Request**:
   ```
   {METHOD}\n{PATH}\n{QUERY}\n{SORTED_HEADERS_STRING}\n{BODY_HASH}
   ```
4. **Canonical Request Hash**: `Base64(SHA256(CanonicalRequest))`
5. **String to Sign**:
   ```
   TCL1-HMAC-SHA256\n{TIMESTAMP}\n{CANONICAL_REQUEST_HASH}
   ```
6. **Signature**: `Base64(HMAC-SHA256(AppKey, StringToSign))`

---

## 4. Firmware Structure & APK Extraction

To inspect updater binaries and reverse-engineer API logic, firmware packages must be extracted:

### 4.1 Extraction Workflow

1. **Decompress Payload**: Firmware ZIPs contain sparse Android partition files compressed with Brotli (`.new.dat.br`).
2. **Convert to Raw Images**: Use `brotli -d` followed by `sdat2img.py` to generate raw partition images (`product.img`, `system.img`).
3. **Mount / Extract**: Open `.img` files using `7z` or Linux loop-mounting.

### 4.2 Application Locations

The core updater logic resides on the `product` partition:

| Application | Path in Firmware | Purpose |
|---|---|---|
| `SystemUpdate.apk` | `product/app/SystemUpdate/SystemUpdate.apk` | Main OTA client, UI, and network services |
| `TTVSCore.apk` | `product/app/TTVSCore/` | Core background TV service |
| `TCL_ALL_BI.apk` | `product/app/TCL_ALL_BI/` | Analytics and device metrics reporting |

*APK Architecture: `SystemUpdate.apk` is composed entirely of Dalvik bytecode (`classes.dex`, `classes2.dex`) with no compiled native `.so` libraries.*

---

## 5. Automation Strategy

The project implements automated firmware monitoring via GitHub Actions:

- **Script**: `scripts/fetch_firmwares.py` connects to `huan.tv` using the verified `HUAN-Sign` protocol.
- **Cadence**: Scheduled daily every 24 hours at 06:00 German Time (04:00 UTC) via `.github/workflows/firmware-tracker.yml`.
- **Output**: Generates `docs/firmwares.md` and `docs/assets/firmwares.json` for live status tracking.
