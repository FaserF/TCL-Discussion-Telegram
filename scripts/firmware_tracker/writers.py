"""
Output file generators for JSON databases (firmwares, beta_test, history, news) and Markdown documentation.
"""

from __future__ import annotations

import json
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from .config import ASSETS_DIR, BETA_TEST_JSON, HISTORY_JSON, JSON_OUT, MD_OUT, NEWS_OUT
from .models import PlatformEntry


def write_json(entries: list[PlatformEntry], generated_at: str) -> None:
    """
    Writes verified firmware records to docs/assets/firmwares.json.
    """
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": generated_at,
        "source": "official TCL Smart TV FOTA API (huan.tv) & CDN (cedock.com)",
        "total_platforms": len(entries),
        "api_fields_documentation": {
            "platform": "Primary hardware platform identifier code (e.g., '0012T01', '0008T01', 'T653T01') matching the TV SoC.",
            "alt_platform_id": "Secondary or legacy alphanumeric platform identifier used interchangeably in OTA requests.",
            "family_name": "Human-readable hardware family and chassis title.",
            "soc_specs": "Technical hardware specifications of the System-on-Chip (SoC) processor and graphics engine.",
            "featured_models": "Known and verified TV model series associated with this platform (selection of examples).",
            "latest_firmware": "Latest verified Production (Stable) firmware release version code (e.g., 'V8-0012T01-LF1V655').",
            "build_number": "Internal 6-digit revision build compilation number (e.g., '003254').",
            "release_type": "Installation package type: 'Full OTA (ZIP)', 'Incremental OTA', or 'IMG / PKG Recovery'.",
            "is_test_release": "Boolean flag indicating if the primary package is a Beta/Test release candidate (R/M build).",
            "release_category": "Classification: 'Production (Stable)', 'Beta / Test Build (RC)', or 'Manufacturing / Test'.",
            "package_size": "Formatted binary package file size in GB/MB.",
            "release_date": "Official publication date or build compilation date (YYYY-MM-DD or YYYY-MM).",
            "md5": "Cryptographic MD5 hash checksum from FOTA server for payload verification.",
            "sha256": "Cryptographic SHA-256 hash checksum for enhanced security and binary verification.",
            "crc32": "IEEE 802.3 32-bit Cyclic Redundancy Check (CRC32) hexadecimal checksum.",
            "changelog": "Official release notes and changelog description extracted from server XML response (<description>/<note>).",
            "extracted_details": {
                "android_version": "Android OS Release version (e.g., '14', '12', '11').",
                "os_flavor": "Operating system experience flavor ('Google TV (GTV)' vs 'Android TV (ATV)').",
                "gms_version": "Google Mobile Services / Experience package designation (e.g., 'Android_14_GTV_U').",
                "security_patch": "Android Security Patch Level date (e.g., '2026-06-05').",
                "build_date_utc": "Unix epoch compilation timestamp of the build (e.g., 1786113311).",
                "build_date_str": "Human-readable compilation date string (e.g., 'Aug 07, 2026').",
                "fingerprint": "Official Android build fingerprint signature.",
                "sdk_level": "Android API SDK level integer (e.g., 34 for Android 14, 31 for Android 12).",
                "incremental_build": "Internal incremental build revision code (e.g., 'AS50', 'AS24', 'AR11').",
                "device_codename": "Hardware device target codename (e.g., 'G10', 'G09', 'BeyondTV4')."
            },
            "stable": "Detailed attributes of the latest verified Production (Stable) firmware release.",
            "beta": "Detailed attributes of the latest active Beta / Release Candidate (RC) firmware release (null if none available).",
            "test": "Detailed attributes of the latest active Manufacturing / Pre-production Test firmware release (null if none available).",
            "region": "Target regional market deployment ('EU', 'NA', 'AS', 'GLOBAL').",
            "download_url": "Direct primary CDN download link for the package.",
            "all_cdn_urls": "Object containing regional CDN mirror URLs mapped by region key ('eu', 'na', 'as').",
            "fota_api_status": "Validation and connection status against the official live TCL FOTA upgrade server.",
            "checked_at": "ISO-8601 UTC timestamp recording when the platform was last queried against the server."
        },
        "firmwares": [asdict(e) for e in entries],
    }
    JSON_OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"[JSON] Written to {JSON_OUT}")


def write_beta_test_json(entries: list[PlatformEntry], generated_at: str) -> None:
    """
    Writes a dedicated catalog of platforms with active Beta or Test builds to docs/assets/firmwares_beta_test.json.
    """
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    beta_test_entries = []
    for e in entries:
        if e.beta or e.test:
            item = {
                "platform": e.platform,
                "alt_platform_id": e.alt_platform_id,
                "family_name": e.family_name,
                "soc_specs": e.soc_specs,
                "featured_models": e.featured_models,
                "region": e.region,
                "fota_api_status": e.fota_api_status,
                "checked_at": e.checked_at,
                "latest_stable_version": e.stable.version if e.stable else e.latest_firmware,
                "beta": asdict(e.beta) if e.beta else None,
                "test": asdict(e.test) if e.test else None,
            }
            beta_test_entries.append(item)

    payload = {
        "generated_at": generated_at,
        "source": "official TCL Smart TV FOTA API (huan.tv) & CDN (cedock.com)",
        "total_platforms_with_pre_releases": len(beta_test_entries),
        "api_fields_documentation": {
            "platform": "Primary hardware platform identifier code.",
            "family_name": "Human-readable hardware family title.",
            "latest_stable_version": "Latest official production stable firmware version for comparison.",
            "beta": "Latest active Beta / Release Candidate (RC) firmware release (null if none).",
            "test": "Latest active Manufacturing / Pre-production Test firmware release (null if none).",
        },
        "pre_releases": beta_test_entries,
    }
    BETA_TEST_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"[Beta/Test JSON] Written to {BETA_TEST_JSON}")


def save_firmware_history(history: dict[str, list[dict[str, Any]]], entries: Optional[list[PlatformEntry]] = None) -> None:
    """
    Saves the aggregated historical database to docs/assets/firmwares_history.json.
    STRICT RULE:
    - Contains all previous/older firmware releases for each platform.
    - Excludes the current active latest Stable release (which lives in firmwares.json).
    - Excludes the current active latest Beta / Test releases (which live in firmwares_beta_test.json).
    - Excludes initial placeholder V001 entries.
    """
    active_versions_by_platform: dict[str, set[str]] = {}
    if entries:
        for e in entries:
            active_set = set()
            if e.latest_firmware:
                active_set.add(e.latest_firmware)
            if e.stable and e.stable.version:
                active_set.add(e.stable.version)
            if e.beta and e.beta.version:
                active_set.add(e.beta.version)
            if e.test and e.test.version:
                active_set.add(e.test.version)
            active_set.add(f"V8-{e.platform}-LF1V001")
            active_versions_by_platform[e.platform] = active_set

    cleaned_history: dict[str, list[dict[str, Any]]] = {}
    for pid, v_list in history.items():
        if pid.startswith("_") or not isinstance(v_list, list):
            continue
        excluded = active_versions_by_platform.get(pid, {f"V8-{pid}-LF1V001"})

        seen_versions = set()
        platform_hist = []
        for item in v_list:
            if not isinstance(item, dict):
                continue
            v_code = item.get("version")
            if not v_code or v_code in excluded or str(v_code).endswith("-LF1V001"):
                continue
            if v_code not in seen_versions:
                seen_versions.add(v_code)
                platform_hist.append(item)

        if platform_hist:
            cleaned_history[pid] = platform_hist

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": "official TCL Smart TV FOTA historical archive (cedock.com / huan.tv)",
        "total_archived_platforms": len(cleaned_history),
        "total_archived_releases": sum(len(v) for v in cleaned_history.values()),
        "api_fields_documentation": {
            "version": "Historical firmware release version identifier.",
            "build_number": "Internal 6-digit revision build compilation number.",
            "release_type": "Package format: 'Full OTA (ZIP)', 'Incremental OTA', or 'IMG / PKG Recovery'.",
            "release_category": "Classification: 'Production (Stable)', 'Beta / Test Build (RC)', or 'Manufacturing / Test'.",
            "is_test_release": "Boolean flag indicating if the package was a Beta/Test release candidate.",
            "package_size": "Formatted binary package file size in GB/MB.",
            "release_date": "Official publication date or build compilation date (YYYY-MM-DD or YYYY-MM).",
            "md5": "Cryptographic MD5 hash checksum.",
            "sha256": "Cryptographic SHA-256 hash checksum for enhanced security and verification.",
            "crc32": "IEEE 802.3 32-bit Cyclic Redundancy Check (CRC32) hexadecimal checksum.",
            "changelog": "Official release notes and changelog description.",
            "download_url": "Direct primary CDN download URL on official TCL CDN.",
            "all_cdn_urls": "Dictionary mapping regional CDN keys to direct mirror download URLs.",
            "extracted_details": "Deep build properties extracted from the package payload.",
        },
        "history": cleaned_history,
    }
    HISTORY_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"[History JSON] Written {payload['total_archived_releases']} historical releases across {payload['total_archived_platforms']} platforms to {HISTORY_JSON}")


def write_markdown(entries: list[PlatformEntry], generated_at: str, history: Optional[dict[str, list[dict[str, Any]]]] = None) -> None:
    """
    Renders docs/firmwares.md overview table, platform cards, and collapsible previous versions archive.
    """
    hist = history or {}
    lines = [
        "---",
        "title: TCL Smart TV Firmware Hub",
        "description: Official, comprehensive firmware tracker and package repository for all global TCL Android TV and Google TV platforms.",
        "---",
        "",
        "# 📡 TCL Smart TV Firmware Hub",
        "",
        "Welcome to the official **TCL Smart TV Firmware Hub**. This catalog tracks, aggregates, and validates official firmware releases across all known TCL hardware platforms globally. Data is synchronized directly with official TCL FOTA upgrade servers (`huan.tv`) and high-speed Content Delivery Networks (`cedock.com`).",
        "",
        "> 💡 **Automated Verification & Integrity Guarantee**  ",
        "> All firmware binaries listed below are verified through server-side MD5 signatures, SHA-256 cryptographic hashes, and IEEE 802.3 32-bit CRC32 checksums. Deep technical build properties are extracted via non-destructive byte-range inspection.",
        "",
        f"*Last database update: `{generated_at}` UTC*",
        "",
        "---",
        "",
        "## 📑 Quick Platform Index",
        "",
        "| Platform ID | Family / Chassis | Latest Firmware | OS Flavor | Release Date | Checksums (MD5 · SHA256 · CRC32) | Direct Download |",
        "|---|---|---|:---:|:---:|---|:---:|",
    ]

    for e in entries:
        fw_code = f"`{e.latest_firmware}`"
        dl_link = f"[:material-download: Download]({e.download_url})" if e.download_url else "—"

        os_tag = "—"
        if e.extracted_details and e.extracted_details.android_version != "—":
            os_tag = f"Android {e.extracted_details.android_version}"
        elif "ATV" in e.family_name:
            os_tag = "Android TV"
        elif "GTV" in e.family_name or "Pentonic" in e.family_name:
            os_tag = "Google TV"

        md5_short = f"`{e.md5[:8]}...`" if e.md5 else "—"
        sha_short = f"`{e.sha256[:8]}...`" if e.sha256 else "—"
        crc_str = f"`0x{e.crc32}`" if e.crc32 else "—"
        chk_summary = f"{md5_short} · {sha_short} · {crc_str}"

        lines.append(
            f"| [`{e.platform}`](#platform-{e.platform.lower()}) | **{e.family_name}** | {fw_code} | `{os_tag}` | `{e.release_date}` | {chk_summary} | {dl_link} |"
        )

    lines += [
        "",
        "---",
        "",
        "## 🛠️ Detailed Platform Specifications & Package Downloads",
        "",
    ]

    for e in entries:
        ext_md_lines = []
        if e.extracted_details:
            d = e.extracted_details
            if d.android_version != "—":
                ext_md_lines.append(f"- **Android OS Version**: `Android {d.android_version}` ({d.os_flavor})")
            if d.gms_version != "—":
                ext_md_lines.append(f"- **GMS Package**: `{d.gms_version}`")
            if d.security_patch != "—":
                ext_md_lines.append(f"- **Security Patch Level**: `{d.security_patch}`")
            if d.build_date_str != "—":
                ext_md_lines.append(f"- **Build Date**: `{d.build_date_str}`")
            if d.fingerprint != "—":
                ext_md_lines.append(f"- **Build Fingerprint**: `{d.fingerprint}`")
            if d.sdk_level:
                ext_md_lines.append(f"- **SDK API Level**: `{d.sdk_level}`")
            if d.incremental_build != "—":
                ext_md_lines.append(f"- **Incremental Revision**: `{d.incremental_build}`")
            if d.device_codename != "—":
                ext_md_lines.append(f"- **Target Device Codename**: `{d.device_codename}`")

        sha_field = f"- **SHA-256 Checksum**: `{e.sha256}`" if e.sha256 else ""
        crc_field = f"- **CRC-32 Checksum**: `0x{e.crc32}`" if e.crc32 else ""

        lines += [
            f'<a id="platform-{e.platform.lower()}"></a>',
            f"#### {e.family_name} (`{e.latest_firmware}`)",
            f"- **Platform Identifier**: `{e.platform}`" + (f" (Alternative ID: `{e.alt_platform_id}`)" if e.alt_platform_id != e.platform else ""),
            f"- **Hardware Architecture & SoC**: {e.soc_specs}",
            f"- **Compatible TV Models (Selection)**: *{e.featured_models}*",
            f"- **Package Type**: `{e.release_type}` · **Size**: `{e.package_size}` · **Release Date**: `{e.release_date}` · **Region**: `{e.region}`",
            f"- **FOTA Verification Status**: `{e.fota_api_status}`",
            f"- **MD5 Checksum**: `{e.md5 or '—'}`",
        ]
        if sha_field:
            lines.append(sha_field)
        if crc_field:
            lines.append(crc_field)

        lines.append(f"- **Official Changelog / Server Notes**: {e.changelog or 'Official production release.'}")

        if e.is_test_release:
            lines += [
                "> ⚠️ **Beta / Test Release Candidate Notice**  ",
                "> *This firmware build is a pre-release / test version (`R`/`M`-series). It may contain experimental features or stability bugs. Flash at your own discretion.*",
            ]

        if ext_md_lines:
            lines += ["- **Extracted Android Build Properties**:", *[f"  {l}" for l in ext_md_lines]]

        if e.beta:
            b_crc_str = f" · **CRC-32**: `0x{e.beta.crc32}`" if e.beta.crc32 else ""
            b_sha_str = f" · **SHA-256**: `{e.beta.sha256}`" if e.beta.sha256 else ""
            lines += [
                f"> 🧪 **Active Beta / Release Candidate (RC)**: `{e.beta.version}`  ",
                f"> **Type & Size**: `{e.beta.release_type}` · `{e.beta.package_size}` · **Release Date**: `{e.beta.release_date}`  ",
                f"> **MD5**: `{e.beta.md5 or '—'}`{b_sha_str}{b_crc_str}  ",
                f"> **Download**: [Direct Beta Download]({e.beta.download_url}) · *{e.beta.changelog or 'Beta testing build'}*",
                "",
            ]

        if e.test:
            t_crc_str = f" · **CRC-32**: `0x{e.test.crc32}`" if e.test.crc32 else ""
            t_sha_str = f" · **SHA-256**: `{e.test.sha256}`" if e.test.sha256 else ""
            lines += [
                f"> 🔬 **Active Manufacturing / Pre-production Test**: `{e.test.version}`  ",
                f"> **Type & Size**: `{e.test.release_type}` · `{e.test.package_size}` · **Release Date**: `{e.test.release_date}`  ",
                f"> **MD5**: `{e.test.md5 or '—'}`{t_sha_str}{t_crc_str}  ",
                f"> **Download**: [Direct Test Download]({e.test.download_url}) · *{e.test.changelog or 'Test build'}*",
                "",
            ]

        lines += [
            f"- **EU / Global CDN**: [{e.all_cdn_urls.get('eu')}]({e.all_cdn_urls.get('eu')})",
            f"- **North America (NA) CDN**: [{e.all_cdn_urls.get('na')}]({e.all_cdn_urls.get('na')})",
            f"- **Asia-Pacific (AS) CDN**: [{e.all_cdn_urls.get('as')}]({e.all_cdn_urls.get('as')})",
            "",
        ]

        p_history = hist.get(e.platform, [])
        active_versions = {e.latest_firmware}
        if e.stable:
            active_versions.add(e.stable.version)
        if e.beta:
            active_versions.add(e.beta.version)
        if e.test:
            active_versions.add(e.test.version)

        prev_versions = [h for h in p_history if h.get("version") not in active_versions]
        if prev_versions:
            lines += [
                f"<details>",
                f"<summary><b>📦 Previous Firmware Versions Archive ({len(prev_versions)} build{'s' if len(prev_versions) > 1 else ''})</b></summary>",
                "",
                "| Version | Release Date | Package Type & Size | Category | Changelog / Notes | Download Link |",
                "|---|:---:|---|:---:|---|:---:|",
            ]
            for pv in prev_versions:
                pv_ver = pv.get("version", "")
                pv_date = pv.get("release_date", "—")
                pv_type = pv.get("release_type", "Full OTA (ZIP)")
                pv_sz = pv.get("package_size", "—")
                pv_type_sz = f"`{pv_type}` · `{pv_sz}`" if pv_sz != "—" else f"`{pv_type}`"
                pv_cat = pv.get("release_category", "Production (Stable)")
                pv_cat_tag = f"⚠️ *{pv_cat}*" if pv.get("is_test_release") else f"**{pv_cat}**"
                pv_cl = pv.get("changelog") or "—"
                pv_dl = pv.get("download_url") or ""
                pv_dl_md = f"[:material-download: Download]({pv_dl})" if pv_dl else "—"
                lines.append(f"| `{pv_ver}` | `{pv_date}` | {pv_type_sz} | {pv_cat_tag} | *{pv_cl}* | {pv_dl_md} |")
            lines += [
                "",
                "</details>",
                "",
            ]

    lines += [
        "---",
        "",
        "*Generated automatically by [`scripts/fetch_firmwares.py`]"
        "(https://github.com/FaserF/TCL-Discussion-Telegram/blob/main/scripts/fetch_firmwares.py)*",
    ]

    MD_OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"[MD]   Written to {MD_OUT}")


def update_news_json(updated_releases: list[PlatformEntry], generated_at: str) -> None:
    """
    Appends newly discovered firmware releases to docs/assets/news.json.
    """
    if not updated_releases:
        return

    items = []
    if NEWS_OUT.exists():
        try:
            old = json.loads(NEWS_OUT.read_text(encoding="utf-8"))
            if isinstance(old, list):
                items = old
            elif isinstance(old, dict) and "news" in old:
                items = old["news"]
        except Exception:
            items = []

    for entry in updated_releases:
        news_item = {
            "id": f"fw-{entry.platform.lower()}-{entry.latest_firmware.lower()}",
            "type": "firmware_update",
            "title": f"New Firmware Released: {entry.family_name} ({entry.latest_firmware})",
            "platform": entry.platform,
            "version": entry.latest_firmware,
            "release_date": entry.release_date,
            "timestamp": generated_at,
            "download_url": entry.download_url,
            "md5": entry.md5,
            "sha256": entry.sha256,
            "crc32": entry.crc32,
            "summary": (
                f"TCL released firmware {entry.latest_firmware} for {entry.family_name} "
                f"({entry.platform}). Package format: {entry.release_type} ({entry.package_size}). "
                f"{entry.changelog or ''}"
            ).strip(),
        }
        if not any(it.get("id") == news_item["id"] for it in items):
            items.insert(0, news_item)

    items = items[:50]
    NEWS_OUT.write_text(json.dumps({"generated_at": generated_at, "news": items}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"[News] Updated {NEWS_OUT} with {len(updated_releases)} new release(s)")
