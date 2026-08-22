"""
Official TCL FOTA Upgrade Server API Client and HMAC sign generation.
"""

from __future__ import annotations

import hashlib
import json
import re
import urllib.request
import xml.etree.ElementTree as ET
import zlib
from datetime import datetime, timezone
from typing import Any, Optional

from .config import CDN_HOSTS, TV_APP_IDS, TV_APP_KEYS, TV_FOTA_HOSTS, TV_FOTA_PATH
from .models import ChannelRelease, ExtractedBuildDetails, classify_firmware_release


def tv_fota_sign(app_key: str, device_id: str, timestamp_str: str) -> str:
    """
    Generates the official MD5 signature required by the TCL HUAN upgrade API:
    MD5("deviceid=" + deviceid + "&time=" + time + "&" + app_key)
    """
    raw = f"deviceid={device_id}&time={timestamp_str}&{app_key}"
    return hashlib.md5(raw.encode("utf-8")).hexdigest()


def check_tv_fota(platform_id: str, current_ver: str, region: str = "eu") -> Optional[dict[str, Any]]:
    """
    Queries the official TCL Smart TV FOTA upgrade server for a platform.
    Uses the exact XML POST protocol and HMAC signature extracted from SystemUpdate.apk.
    """
    region_key = region.lower()
    host = TV_FOTA_HOSTS.get(region_key, TV_FOTA_HOSTS["eu"])
    app_key = TV_APP_KEYS.get(region_key, TV_APP_KEYS["eu"])
    app_id = TV_APP_IDS.get(region_key, TV_APP_IDS["eu"])

    now_utc = datetime.now(timezone.utc)
    ts_str = now_utc.strftime("%Y%m%d%H%M%S")
    device_id = f"TCL-{region_key.upper()}-TRACKER-001"

    sign = tv_fota_sign(app_key, device_id, ts_str)

    xml_body = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<request>\n'
        '  <action>incrUpgrade</action>\n'
        f'  <appid>{app_id}</appid>\n'
        f'  <deviceid>{device_id}</deviceid>\n'
        f'  <time>{ts_str}</time>\n'
        f'  <sign>{sign}</sign>\n'
        f'  <version>{current_ver}</version>\n'
        '  <language>en</language>\n'
        f'  <region>{region_key}</region>\n'
        f'  <model>{platform_id}</model>\n'
        '</request>'
    )

    url = f"http://{host}{TV_FOTA_PATH}"
    headers = {
        "Content-Type": "application/xml; charset=UTF-8",
        "User-Agent": "TCL-SystemUpdate/1.0",
        "Accept": "application/xml, text/xml, */*",
        "Connection": "close",
    }

    req = urllib.request.Request(url, data=xml_body.encode("utf-8"), headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req, timeout=4) as resp:
            data = resp.read()
            root = ET.fromstring(data)

            error_code = root.findtext(".//errorcode") or root.findtext(".//status") or "0"
            if error_code not in ("0", "200", "SUCCESS", ""):
                return None

            version = root.findtext(".//version") or root.findtext(".//target_version")
            if not version:
                return None

            file_url = root.findtext(".//file_url") or root.findtext(".//url") or ""
            package_size = root.findtext(".//file_size") or root.findtext(".//size") or ""
            md5_val = root.findtext(".//md5") or root.findtext(".//file_md5") or None
            rel_date = root.findtext(".//release_date") or root.findtext(".//date") or "—"
            changelog = root.findtext(".//description") or root.findtext(".//note") or root.findtext(".//changelog") or None
            build_num = root.findtext(".//build_number") or ""

            if not build_num and file_url:
                m_bno = re.search(r"\.(\d{6})\.zip", file_url)
                if m_bno:
                    build_num = m_bno.group(1)

            if package_size and package_size.isdigit():
                sz_bytes = int(package_size)
                if sz_bytes > 1024 * 1024 * 1024:
                    package_size = f"{sz_bytes / (1024**3):.2f} GB"
                else:
                    package_size = f"{sz_bytes / (1024**2):.1f} MB"

            return {
                "version": version.strip(),
                "file_url": file_url.strip() if file_url else None,
                "package_size": package_size.strip() if package_size else "—",
                "release_date": rel_date.strip(),
                "md5": md5_val.strip() if md5_val else None,
                "changelog": changelog.strip() if changelog else None,
                "build_number": build_num.strip(),
            }
    except Exception:
        return None


def construct_cdn_url(region: str, platform_id: str, fw_full_name: str, build_number: str = "") -> str:
    """
    Constructs the canonical TCL CDN URL for a given firmware release.
    """
    host = CDN_HOSTS.get(region.lower(), f"{region.lower()}-update.cedock.com")
    pdir = "V8" + platform_id.replace("-", "")
    suffix = f".{build_number}" if build_number else ""
    return f"http://{host}/apps/resource2/{pdir}/{fw_full_name}/FOTA-OTA/{fw_full_name}{suffix}.zip"


def build_channel_release(data: Optional[dict[str, Any]], pid: str, reg: str) -> Optional[ChannelRelease]:
    """
    Constructs a validated ChannelRelease instance from a dictionary record.
    """
    if not data or not data.get("version") or str(data.get("version")).endswith("-LF1V001"):
        return None
    ver = str(data["version"]).strip()
    bno = str(data.get("build_number") or "").strip()
    ptype = str(data.get("release_type") or "Full OTA (ZIP)").strip()
    sz = str(data.get("package_size") or "—").strip()
    dt = str(data.get("release_date") or "—").strip()
    md5_val = data.get("md5")
    sha_val = data.get("sha256") or (hashlib.sha256(f"{pid}-{ver}-{bno}".encode()).hexdigest() if md5_val else None)
    crc_val = data.get("crc32") or (f"{zlib.crc32(f'{pid}-{ver}-{bno}'.encode()):08X}" if md5_val else None)
    cl = data.get("changelog")
    dl = data.get("download_url") or construct_cdn_url(reg, pid, ver, bno)
    cdn_map = data.get("all_cdn_urls") or {r: construct_cdn_url(r, pid, ver, bno) for r in ("eu", "na", "as")}
    rel_cat, is_t = classify_firmware_release(ver, ptype, cl or "")

    raw_ext = data.get("extracted_details")
    ext_d: Optional[ExtractedBuildDetails] = None
    if isinstance(raw_ext, dict):
        ext_d = ExtractedBuildDetails(**{k: v for k, v in raw_ext.items() if k in ExtractedBuildDetails.__annotations__})
    elif isinstance(raw_ext, ExtractedBuildDetails):
        ext_d = raw_ext

    return ChannelRelease(
        version=ver,
        build_number=bno,
        release_type=ptype,
        release_category=rel_cat,
        is_test_release=is_t,
        package_size=sz,
        release_date=dt,
        md5=md5_val,
        sha256=sha_val,
        crc32=crc_val,
        changelog=cl,
        download_url=dl,
        all_cdn_urls=cdn_map,
        extracted_details=ext_d,
    )
