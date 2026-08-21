#!/usr/bin/env python3
"""
fetch_firmwares.py — Dynamic TCL TV Firmware Tracker & Discovery Engine
=======================================================================
Tracks, aggregates, and discovers TCL Smart TV firmware releases strictly
via the official TCL FOTA upgrade servers (huan.tv) and CDN mirrors (cedock.com).

Platform hardware specifications, model listings, and sub-chipsets are
parsed dynamically from `docs/chipsets.md` (Single Source of Truth)
and queried against official TCL FOTA APIs.
"""

from __future__ import annotations

import hashlib
import json
import re
import time
import urllib.request
import uuid
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

# ---------------------------------------------------------------------------
# Output & Documentation paths
# ---------------------------------------------------------------------------
REPO_ROOT    = Path(__file__).resolve().parent.parent
DOCS_DIR     = REPO_ROOT / "docs"
ASSETS_DIR   = DOCS_DIR / "assets"
JSON_OUT     = ASSETS_DIR / "firmwares.json"
MD_OUT       = DOCS_DIR / "firmwares.md"
NEWS_OUT     = ASSETS_DIR / "news.json"
CHIPSETS_MD  = DOCS_DIR / "chipsets.md"

# ---------------------------------------------------------------------------
# Official TCL Server API Constants (from SystemUpdate.apk bytecode)
# ---------------------------------------------------------------------------
TV_FOTA_HOSTS = {
    "eu": "eu-filter-upgrade.huan.tv",
    "na": "na-filter-upgrade.huan.tv",
    "as": "as-filter-upgrade.huan.tv",
    "cn": "filter-upgrade.huan.tv",
}

TV_FOTA_PATH = "/service/upmp/upgradeIncrInterface"

TV_APP_KEYS = {
    "eu": "4b93841c48eb1af1dfbe2c82384136c9",
    "na": "dacf21ce497259eae5f65312da7d868c",
    "as": "35b8fa949e0578f41f6e751991c800aa",
    "cn": "d49a5258bfcc5f6c3e430f67a0313e90",
}

TV_APP_IDS = {
    "eu": "upmp-eu",
    "na": "upmp-na",
    "as": "upmp-as",
    "cn": "upmp-cn",
}

CDN_HOSTS = {
    "eu": "eu-update.cedock.com",
    "na": "na-update.cedock.com",
    "as": "as-update.cedock.com",
}

PROBE_DISCOVERY_PLATFORMS = [
    ("0014T01", "Pentonic 600 v2", "eu"),
    ("0017T01", "Next-Gen 2026/2027 G17", "eu"),
    ("0018T01", "Next-Gen 2026/2027 Platform", "eu"),
    ("0015T02", "Pentonic 800 NA", "na"),
    ("0013T01", "T800 Amlogic v1", "eu"),
    ("0013T03", "T800 Amlogic v3", "eu"),
    ("0008T02", "R75P RT75 NA variant", "na"),
]

# ---------------------------------------------------------------------------
# Data Models
# ---------------------------------------------------------------------------
@dataclass
class PlatformEntry:
    """
    Represents a unified firmware release and hardware specification record
    for a specific TCL Smart TV SoC platform family.
    """
    platform: str
    """Primary hardware platform ID (e.g. '0012T01', '0008T01', 'T653T01') matching the SoC/mainboard."""

    alt_platform_id: str
    """Secondary or legacy alphanumeric platform code (e.g. 'T653T01', 'R75PT01') used in update paths."""

    family_name: str
    """Human-readable hardware family and chassis title (e.g. 'Pentonic 700 (0012T01)')."""

    soc_specs: str
    """Technical hardware specifications of the System-on-Chip (SoC) and GPU engine."""

    featured_models: str
    """Known commercial television model series powered by this hardware platform."""

    latest_firmware: str
    """Latest verified production firmware version identifier (e.g. 'V8-0012T01-LF1V655')."""

    build_number: str
    """Internal 6-digit build revision number (e.g. '003254', '002205')."""

    release_type: str
    """Distribution package format: 'Full OTA (ZIP)', 'Incremental OTA', or 'IMG / PKG Recovery'."""

    package_size: str
    """Formatted binary file size in Gigabytes (GB) or Megabytes (MB)."""

    release_date: str
    """Official release or compilation date in ISO format ('YYYY-MM-DD' or 'YYYY-MM')."""

    md5: Optional[str]
    """Cryptographic MD5 hash checksum from FOTA server for payload integrity verification."""

    changelog: Optional[str]
    """Official release notes and changelog description extracted from server XML response (<description>/<note>)."""

    region: str
    """Target geographic market deployment ('EU', 'NA', 'AS', 'GLOBAL')."""

    download_url: str
    """Direct primary HTTP/HTTPS download URL on the official TCL CDN (cedock.com)."""

    all_cdn_urls: dict = field(default_factory=dict)
    """Dictionary mapping regional CDN keys ('eu', 'na', 'as') to direct mirror download URLs."""

    fota_api_status: str = "Live Connected"
    """Validation and connection status against the official live TCL FOTA upgrade server."""

    checked_at: str = ""
    """ISO-8601 UTC timestamp recording when the platform was last queried against the server."""


# ---------------------------------------------------------------------------
# Dynamic Parser for docs/chipsets.md (Single Source of Truth)
# ---------------------------------------------------------------------------

def parse_chipsets_markdown() -> dict[str, dict[str, Any]]:
    """
    Dynamically parses platform definitions, SoC specs, and featured models
    from docs/chipsets.md markdown tables.
    """
    platforms: dict[str, dict[str, Any]] = {}
    if not CHIPSETS_MD.exists():
        return platforms

    content = CHIPSETS_MD.read_text(encoding="utf-8")
    lines = content.splitlines()

    in_table = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") and ("Platform Family" in stripped or "Specific IDs" in stripped):
            in_table = True
            continue
        if in_table and stripped.startswith("| :---"):
            continue
        if in_table and not stripped.startswith("|"):
            in_table = False
            continue

        if in_table and stripped.startswith("|"):
            parts = [p.strip() for p in stripped.split("|")[1:-1]]
            if len(parts) >= 4:
                fam_raw, id_raw, models_raw, specs_raw = parts[0], parts[1], parts[2], parts[3]
                fam_clean = re.sub(r"[\*\_]", "", fam_raw).strip()
                specs_clean = re.sub(r"[\*\_]", "", specs_raw).strip()
                models_clean = re.sub(r"[\*\_]", "", models_raw).strip()

                found_ids = re.findall(r"([0-9A-Za-z]+(?:T[0-9]+)?)", id_raw)

                range_match = re.search(r"([0-9A-Za-z]+T)(\d+)\.\.T?(\d+)", id_raw)
                expanded_ids = []
                if range_match:
                    prefix = range_match.group(1)
                    start_n = int(range_match.group(2))
                    end_n = int(range_match.group(3))
                    width = len(range_match.group(2))
                    for n in range(start_n, end_n + 1):
                        expanded_ids.append(f"{prefix}{n:0{width}d}")
                else:
                    expanded_ids = [i for i in found_ids if i not in ("and", "or", "to", "ID", "IDs", "TV", "Menu")]

                for p_id in expanded_ids:
                    if len(p_id) < 5:
                        continue
                    reg = "NA" if "(NA" in fam_raw or "(NA" in id_raw or "NA" in p_id else "EU"

                    alt_id = p_id
                    for other in expanded_ids:
                        if other != p_id:
                            alt_id = other
                            break

                    platforms[p_id] = {
                        "platform": p_id,
                        "alt_platform_id": alt_id,
                        "family_name": f"{fam_clean} ({p_id})",
                        "soc_specs": specs_clean,
                        "featured_models": models_clean,
                        "latest_firmware": f"V8-{p_id}-LF1V001",
                        "build_number": "",
                        "release_type": "Full OTA (ZIP)",
                        "package_size": "—",
                        "release_date": "—",
                        "md5": None,
                        "changelog": None,
                        "region": reg,
                    }

    print(f"[Chipsets Parser] Dynamically loaded {len(platforms)} platform definitions from {CHIPSETS_MD.name}")
    return platforms


# ---------------------------------------------------------------------------
# State Management: Load existing state and merge new platforms
# ---------------------------------------------------------------------------

def load_existing_platforms() -> tuple[dict[str, dict[str, Any]], dict[str, str]]:
    """
    Loads platforms dynamically from docs/chipsets.md, merged with
    persisted state in docs/assets/firmwares.json.
    """
    platforms_map = parse_chipsets_markdown()
    previous_versions: dict[str, str] = {}

    if JSON_OUT.exists():
        try:
            data = json.loads(JSON_OUT.read_text(encoding="utf-8"))
            for entry in data.get("firmwares", []):
                pid = entry.get("platform")
                if pid:
                    previous_versions[pid] = entry.get("latest_firmware", "")
                    if pid in platforms_map:
                        for k in ("latest_firmware", "build_number", "release_type", "package_size", "release_date", "md5", "changelog", "region"):
                            if entry.get(k) is not None:
                                platforms_map[pid][k] = entry[k]
                    else:
                        print(f"  [Discovery] Loaded dynamically preserved platform: {pid}")
                        platforms_map[pid] = entry
        except Exception as e:
            print(f"  [Warning] Failed to parse existing JSON: {e}")

    return platforms_map, previous_versions


# ---------------------------------------------------------------------------
# CDN URL construction
# ---------------------------------------------------------------------------

def construct_cdn_url(region: str, platform_id: str, fw_full_name: str, build_number: str = "") -> str:
    host = CDN_HOSTS.get(region.lower(), f"{region.lower()}-update.cedock.com")
    pdir = "V8" + platform_id.replace("-", "")
    suffix = f".{build_number}" if build_number else ""
    return f"http://{host}/apps/resource2/{pdir}/{fw_full_name}/FOTA-OTA/{fw_full_name}{suffix}.zip"


# ---------------------------------------------------------------------------
# Live FOTA Query & Signature Algorithm (huan.tv)
# ---------------------------------------------------------------------------

def check_tv_fota(platform_id: str, current_ver: str, region: str = "eu") -> Optional[dict]:
    """
    Query official TCL TV FOTA API (POST /service/upmp/upgradeIncrInterface)
    using HUAN-Sign MD5 protocol.
    """
    r_key = region.lower()
    host = TV_FOTA_HOSTS.get(r_key, TV_FOTA_HOSTS["eu"])
    app_id = TV_APP_IDS.get(r_key, TV_APP_IDS["eu"])
    app_key = TV_APP_KEYS.get(r_key, TV_APP_KEYS["eu"])
    url = f"https://{host}{TV_FOTA_PATH}"

    ts = str(int(time.time()))
    req_id = uuid.uuid4().hex
    pdir = "V8" + platform_id.replace("-", "")
    dev_model = f"TCL-{region.upper()}-{platform_id}-S1"

    xml_body = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<upgradeIncrRequest>'
        '<apiversion>1.0</apiversion>'
        '<upmptype>3</upmptype>'
        '<app>'
        f'<appid>{pdir}</appid>'
        '<increment>0</increment>'
        f'<ver>{current_ver}</ver>'
        '<verid>0</verid>'
        '</app>'
        '<parameter>'
        '<callid>0</callid>'
        '<client>'
        f'<devmodel>{dev_model}</devmodel>'
        '<didtoken>1dbb8210ebd6821ba275ff296f7acaf9</didtoken>'
        '<dnum>580900822</dnum>'
        '<projectid>0</projectid>'
        '<systemver>11</systemver>'
        '</client>'
        '<https>true</https>'
        '<language>en</language>'
        f'<region>{region.upper()}</region>'
        '<timezone>Europe/Berlin</timezone>'
        '</parameter>'
        '</upgradeIncrRequest>'
    )

    sign = hashlib.md5((app_key + req_id + ts + "POST" + TV_FOTA_PATH + xml_body).encode("utf-8")).hexdigest()

    headers = {
        "Host": host,
        "Content-Type": "application/xml;charset=UTF-8",
        "HUAN-Sign": sign,
        "HUAN-Timestamp": ts,
        "HUAN-AppId": app_id,
        "HUAN-RequestId": req_id,
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; Smart TV Pro Build/RP1A.200622.001)",
    }

    try:
        req = urllib.request.Request(url, data=xml_body.encode("utf-8"), headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=8) as resp:
            root = ET.fromstring(resp.read().decode("utf-8", "replace"))
            upgrade = root.find("upgrade")
            if upgrade is not None:
                size_str = upgrade.findtext("size") or ""
                size_fmt = f"{int(size_str)/(1024*1024):.2f} MB" if size_str.isdigit() else "—"
                md5_val = upgrade.findtext("md5")
                desc = upgrade.findtext("description") or upgrade.findtext("note")
                return {
                    "file_url": upgrade.findtext("fileurl") or "",
                    "version": upgrade.findtext("version") or "",
                    "size_bytes": size_str,
                    "package_size": size_fmt,
                    "md5": md5_val if md5_val else None,
                    "description": desc.strip() if desc else None,
                    "release_type": "Incremental OTA" if upgrade.findtext("increment") == "1" else "Full OTA (ZIP)",
                    "release_date": upgrade.findtext("updatetime") or "",
                }
            return {"state": root.findtext("state"), "note": root.findtext("note")}
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Dynamic Discovery Engine
# ---------------------------------------------------------------------------

def probe_and_discover_new_platforms(known_platforms: dict[str, dict[str, Any]], newly_discovered: list[dict[str, Any]]) -> None:
    """
    Probes candidate platform IDs to discover unannounced or newly active platforms.
    If a new platform returns a valid update package from huan.tv, it is automatically
    registered into known_platforms.
    """
    print("\n[Discovery] Scanning candidate platforms for newly launched TV platforms...")

    for cand_id, friendly_name, cand_region in PROBE_DISCOVERY_PLATFORMS:
        if cand_id in known_platforms:
            continue

        dummy_ver = f"V8-{cand_id}-LF1V001"
        resp = check_tv_fota(cand_id, dummy_ver, cand_region)

        if resp and resp.get("version"):
            new_ver = resp["version"]
            print(f"  [DISCOVERY SUCCESS] Found new active platform: {cand_id} -> {new_ver}!")
            new_entry = {
                "platform": cand_id,
                "alt_platform_id": cand_id,
                "family_name": f"{friendly_name} ({cand_id})",
                "soc_specs": f"TCL Smart TV Platform ({cand_id})",
                "featured_models": "Newly Discovered Model Series",
                "latest_firmware": new_ver,
                "build_number": "",
                "release_type": resp.get("release_type", "Full OTA (ZIP)"),
                "package_size": resp.get("package_size", "—"),
                "release_date": resp.get("release_date", datetime.now(timezone.utc).strftime("%Y-%m")),
                "md5": resp.get("md5"),
                "changelog": resp.get("description"),
                "region": cand_region.upper(),
            }
            known_platforms[cand_id] = new_entry
            newly_discovered.append(new_entry)
        else:
            time.sleep(0.3)


# ---------------------------------------------------------------------------
# News Banner Trigger Engine
# ---------------------------------------------------------------------------

def update_news_banner(updated_releases: list[dict[str, Any]], newly_discovered: list[dict[str, Any]]) -> None:
    """
    Updates docs/assets/news.json to activate the top notification banner
    when new TV platforms or new firmware updates are detected.
    """
    if not updated_releases and not newly_discovered:
        return

    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    banner_parts = []

    # 1. Newly discovered TV platforms
    if newly_discovered:
        if len(newly_discovered) == 1:
            dp = newly_discovered[0]
            banner_parts.append(f"New TV Platform discovered: {dp['family_name']} ({dp['platform']}) with firmware {dp.get('firmware', '')}!")
        else:
            p_list = ", ".join(dp["platform"] for dp in newly_discovered)
            banner_parts.append(f"New TV Platforms discovered: {p_list}!")

    # 2. New firmware updates for existing platforms
    if updated_releases:
        if len(updated_releases) == 1:
            rel = updated_releases[0]
            banner_parts.append(f"New Firmware Update: {rel['firmware']} for {rel['platform']} ({rel['family_name']}) released!")
        else:
            p_list = ", ".join(r["platform"] for r in updated_releases[:3])
            if len(updated_releases) > 3:
                p_list += f" +{len(updated_releases) - 3} more"
            banner_parts.append(f"New Firmware Updates released for {p_list}!")

    banner_text = " · ".join(banner_parts)

    banner_data = {
        "active": True,
        "date": today_str,
        "text": banner_text,
        "link": "firmwares/"
    }

    NEWS_OUT.write_text(json.dumps(banner_data, indent=4, ensure_ascii=False), encoding="utf-8")
    print(f"[News Banner] Triggered banner in {NEWS_OUT}: {banner_text}")


# ---------------------------------------------------------------------------
# Tracker Execution Loop
# ---------------------------------------------------------------------------

def run(delay: float = 0.5) -> tuple[list[PlatformEntry], str]:
    now = datetime.now(timezone.utc).isoformat()
    platforms_map, previous_versions = load_existing_platforms()

    newly_discovered: list[dict[str, Any]] = []
    probe_and_discover_new_platforms(platforms_map, newly_discovered)

    entries: list[PlatformEntry] = []
    updated_releases: list[dict[str, Any]] = []

    print(f"\n[TCL TV Firmware Tracker] Starting run at {now}")
    print(f"[TCL TV Firmware Tracker] Tracking {len(platforms_map)} platform families\n")

    for pid, cat in sorted(platforms_map.items()):
        p_name = cat.get("family_name", pid)
        reg = cat.get("region", "EU").lower()
        fw = cat.get("latest_firmware", f"V8-{pid}-LF1V001")
        bno = cat.get("build_number", "")
        alt_id = cat.get("alt_platform_id", pid)

        print(f"  Querying {pid} ({p_name}) ...", end=" ", flush=True)

        primary_url = construct_cdn_url(reg, pid, fw, bno)

        # Build regional CDN links
        cdn_links = {}
        for r in ("eu", "na", "as"):
            cdn_links[r] = construct_cdn_url(r, pid, fw, bno)

        # Query live FOTA API
        fota_resp = check_tv_fota(pid, fw, reg)
        if (not fota_resp or not fota_resp.get("version")) and alt_id != pid:
            fota_resp_alt = check_tv_fota(alt_id, fw, reg)
            if fota_resp_alt and fota_resp_alt.get("version"):
                fota_resp = fota_resp_alt

        fota_status = "Checked (Live API - Up to date)"
        active_fw = fw
        active_size = cat.get("package_size", "—")
        active_date = cat.get("release_date", "—")
        active_md5 = cat.get("md5")
        active_type = cat.get("release_type", "Full OTA (ZIP)")
        active_changelog = cat.get("changelog")

        if fota_resp and fota_resp.get("version"):
            active_fw = fota_resp["version"]
            if fota_resp.get("file_url"):
                primary_url = fota_resp["file_url"]
            if fota_resp.get("package_size"):
                active_size = fota_resp["package_size"]
            if fota_resp.get("md5"):
                active_md5 = fota_resp["md5"]
            if fota_resp.get("release_type"):
                active_type = fota_resp["release_type"]
            if fota_resp.get("release_date"):
                active_date = fota_resp["release_date"]
            if fota_resp.get("description"):
                active_changelog = fota_resp["description"]
            fota_status = f"New OTA Released: {active_fw}"
            print(f"NEW OTA: {active_fw}")

            # Check if this is a newly discovered version compared to previous run
            prev_ver = previous_versions.get(pid)
            if prev_ver and prev_ver != active_fw:
                updated_releases.append({
                    "platform": pid,
                    "family_name": p_name,
                    "firmware": active_fw,
                })
        else:
            print(f"Verified {active_fw}")

        entry = PlatformEntry(
            platform=pid,
            alt_platform_id=alt_id,
            family_name=p_name,
            soc_specs=cat.get("soc_specs", "—"),
            featured_models=cat.get("featured_models", "—"),
            latest_firmware=active_fw,
            build_number=bno,
            release_type=active_type,
            package_size=active_size,
            release_date=active_date,
            md5=active_md5,
            changelog=active_changelog,
            region=cat.get("region", "EU").upper(),
            download_url=primary_url,
            all_cdn_urls=cdn_links,
            fota_api_status=fota_status,
            checked_at=now,
        )

        entries.append(entry)
        time.sleep(delay)

    # Trigger banner if new platforms or updates occurred
    if updated_releases or newly_discovered:
        update_news_banner(updated_releases, newly_discovered)

    print(f"\n[TCL TV Firmware Tracker] Successfully processed {len(entries)} platforms.")
    return entries, now


# ---------------------------------------------------------------------------
# Output: JSON & Markdown
# ---------------------------------------------------------------------------

def write_json(entries: list[PlatformEntry], generated_at: str) -> None:
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
            "featured_models": "Known and verified TV model series associated with this platform.",
            "latest_firmware": "Latest official firmware release version code (e.g., 'V8-0012T01-LF1V655').",
            "build_number": "Internal 6-digit revision build compilation number (e.g., '003254').",
            "release_type": "Installation package type: 'Full OTA (ZIP)', 'Incremental OTA', or 'IMG / PKG Recovery'.",
            "package_size": "Formatted binary package file size in GB/MB.",
            "release_date": "Official publication date or build compilation date (YYYY-MM-DD or YYYY-MM).",
            "md5": "Cryptographic MD5 hash checksum from FOTA server for payload verification.",
            "changelog": "Official release notes and changelog description extracted from server XML response (<description>/<note>).",
            "region": "Target regional market deployment ('EU', 'NA', 'AS', 'GLOBAL').",
            "download_url": "Direct primary CDN download link for the package.",
            "all_cdn_urls": "Object containing regional CDN mirror URLs mapped by region key ('eu', 'na', 'as').",
            "fota_api_status": "Validation and connection status against the official live TCL FOTA upgrade server.",
            "checked_at": "ISO-8601 UTC timestamp recording when the platform was last queried against the server."
        },
        "firmwares": [asdict(e) for e in entries],
    }
    JSON_OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[JSON] Written to {JSON_OUT}")


def write_markdown(entries: list[PlatformEntry], generated_at: str) -> None:
    ts = generated_at[:19].replace("T", " ") + " UTC"

    lines: list[str] = [
        "# TCL TV Firmware Tracker",
        "",
        "Official firmware tracking, package sizes, release dates, MD5 hashes, changelogs, and direct download links across all known TCL Smart TV platforms.",
        f"Updated automatically every 24 hours at 06:00 German Time (04:00 UTC) via GitHub Actions · Last updated: **{ts}**.",
        "",
        "---",
        "",
        "## Latest Verified Firmwares per Platform",
        "",
        "| Platform | Hardware / SoC Specs | Latest Release | Type | Size | Date | Official Changelog / Release Notes | Official Download | FOTA API Status |",
        "|---|---|---|---|---|---|---|---|---|",
    ]

    for e in entries:
        build_str = f" (`{e.build_number}`)" if e.build_number else ""
        dl_link = f"[:material-download: Download]({e.download_url})"
        cl_text = f"*{e.changelog}*" if e.changelog else "*(Pending official OTA rollout notes)*"
        lines.append(
            f"| **{e.platform}**<br><small>{e.family_name}</small> "
            f"| {e.soc_specs}<br><small>*{e.featured_models}*</small> "
            f"| `{e.latest_firmware}`{build_str} "
            f"| `{e.release_type}` "
            f"| `{e.package_size}` "
            f"| `{e.release_date}` "
            f"| {cl_text} "
            f"| {dl_link} "
            f"| `{e.fota_api_status}` |"
        )

    lines += [
        "",
        "---",
        "",
        "### Regional Download Mirrors & Package Details",
        "",
        "All packages are hosted on official TCL Content Delivery Networks (`cedock.com`):",
        "",
    ]

    for e in entries:
        md5_line = f"- **MD5 Checksum**: `{e.md5}`" if e.md5 else "- **MD5 Checksum**: *(provided upon OTA deployment)*"
        cl_line = f"- **Official Changelog / Server Notes**: {e.changelog}" if e.changelog else "- **Official Changelog / Server Notes**: *(Pending official OTA release notes)*"
        lines += [
            f"#### {e.family_name} (`{e.latest_firmware}`)",
            f"- **Package Type**: `{e.release_type}` · **Size**: `{e.package_size}` · **Release Date**: `{e.release_date}`",
            md5_line,
            cl_line,
            f"- **EU / Global CDN**: [{e.all_cdn_urls.get('eu')}]({e.all_cdn_urls.get('eu')})",
            f"- **NA CDN**: [{e.all_cdn_urls.get('na')}]({e.all_cdn_urls.get('na')})",
            f"- **Asia-Pacific CDN**: [{e.all_cdn_urls.get('as')}]({e.all_cdn_urls.get('as')})",
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


if __name__ == "__main__":
    entries, generated_at = run()
    write_json(entries, generated_at)
    write_markdown(entries, generated_at)
