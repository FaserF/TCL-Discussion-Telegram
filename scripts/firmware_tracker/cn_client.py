"""
China (CN) region FOTA/TDP protocol helpers and official firmware URL parser/validator.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import re
import urllib.request
import uuid
import xml.etree.ElementTree as ET
from datetime import UTC, datetime
from typing import Any
from urllib.parse import urlparse

from .config import (
    CN_KNOWN_PROJECTS,
    CN_TDP_ENDPOINT,
    OFFICIAL_CDN_DOMAIN_SUFFIXES,
    OFFICIAL_CDN_EXACT_HOSTS,
    TV_APP_IDS,
    TV_APP_KEYS,
    TV_FOTA_HOSTS,
    TV_FOTA_PATH,
)
from .models import classify_firmware_release

_LEINIAO_PATH_RE = re.compile(
    r"^/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/"
    r"(?P<kind>full|inc|incr|diff|ota|pkg|img)/"
    r"[0-9a-fA-F]+/[0-9a-fA-F]+/"
    r"(?P<filename>V8-[A-Z0-9]+-[A-Z0-9]+(?:\.\d+)?\.(?:zip|pkg|img|bin))$",
    re.IGNORECASE,
)
_FW_FILENAME_RE = re.compile(
    r"^(?P<version>V8-(?P<platform>[A-Z0-9]+)-[A-Z0-9]+)"
    r"(?:\.(?P<build_number>\d{4,8}))?"
    r"(?:_(?P<pkg_tag>PKG|IMG))?"
    r"\.(?P<ext>zip|pkg|img|bin)$",
    re.IGNORECASE,
)


def is_cn_platform(platform_id: str, region: str = "") -> bool:
    """Returns True if the platform or region corresponds to China (CN)."""
    if region and region.strip().upper() == "CN":
        return True
    return platform_id.strip().upper() in CN_KNOWN_PROJECTS


def resolve_cn_target(query: str) -> dict[str, str] | None:
    """
    Resolves a platform ID, Project ID, TV model string, or device codename
    to a known CN hardware profile in CN_KNOWN_PROJECTS.
    """
    q = (query or "").strip().lower()
    if not q:
        return None
    for profile in CN_KNOWN_PROJECTS.values():
        searchable = [
            profile.get("platform", ""),
            profile.get("app_id", ""),
            profile.get("dev_model", ""),
            profile.get("device_codename", ""),
            profile.get("project_id", ""),
        ]
        if any(q == val.lower() for val in searchable if val):
            return dict(profile)
        models_str = profile.get("models", "").lower()
        if q in [m.strip() for m in models_str.split(",") if m.strip()]:
            return dict(profile)
        if len(q) >= 4 and (
            q in profile.get("dev_model", "").lower()
            or q in profile.get("device_codename", "").lower()
            or q in models_str
        ):
            return dict(profile)
    return None


def compute_huan_sign(
    app_key: str,
    request_id: str,
    timestamp: str,
    method: str,
    path: str,
    xml_body: str,
) -> str:
    """Computes the HUAN-Sign MD5 digest documented for huan.tv upgrade endpoints."""
    raw = f"{app_key}{request_id}{timestamp}{method.upper()}{path}{xml_body}"
    return hashlib.md5(raw.encode("utf-8")).hexdigest()


def build_huan_upgrade_xml(
    platform_id: str,
    current_ver: str,
    region: str = "CN",
    project_id: str = "0",
    dev_model: str = "",
    language: str = "zh",
    timezone: str = "Asia/Shanghai",
) -> str:
    """Builds the <upgradeIncrRequest> XML body for huan.tv FOTA endpoints."""
    pid_clean = platform_id.strip().upper()
    app_id = pid_clean if pid_clean.startswith("V8") else f"V8{pid_clean.replace('-', '')}"
    model_val = dev_model or f"TCL-{region.upper()}-{pid_clean}"
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        "<upgradeIncrRequest>\n"
        "  <apiversion>1.0</apiversion>\n"
        "  <upmptype>3</upmptype>\n"
        "  <app>\n"
        f"    <appid>{app_id}</appid>\n"
        "    <increment>0</increment>\n"
        f"    <ver>{current_ver}</ver>\n"
        "    <verid>0</verid>\n"
        "  </app>\n"
        "  <parameter>\n"
        "    <callid>0</callid>\n"
        "    <client>\n"
        f"      <devmodel>{model_val}</devmodel>\n"
        "      <didtoken>00000000000000000000000000000000</didtoken>\n"
        "      <dnum>000000000</dnum>\n"
        f"      <projectid>{project_id or '0'}</projectid>\n"
        "      <systemver>11</systemver>\n"
        "    </client>\n"
        "    <https>true</https>\n"
        f"    <language>{language}</language>\n"
        f"    <region>{region.upper()}</region>\n"
        f"    <timezone>{timezone}</timezone>\n"
        "  </parameter>\n"
        "</upgradeIncrRequest>"
    )


def _format_size_str(raw_size: str | int | None) -> str:
    if raw_size is None:
        return "—"
    txt = str(raw_size).strip()
    if not txt:
        return "—"
    if txt.isdigit():
        sz_bytes = int(txt)
        if sz_bytes > 1024 * 1024 * 1024:
            return f"{sz_bytes / (1024**3):.2f} GB"
        return f"{sz_bytes / (1024**2):.1f} MB"
    return txt


def parse_huan_upgrade_response(
    xml_bytes: bytes, region: str = "cn"
) -> dict[str, Any] | None:
    """Parses both <upgradeIncrResponse> and legacy <response> XML payloads."""
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError:
        return None

    state = (
        root.findtext(".//state")
        or root.findtext(".//errorcode")
        or root.findtext(".//status")
        or "0"
    ).strip()
    if state not in ("0000", "0", "200", "SUCCESS", ""):
        return None

    version = (
        root.findtext(".//version")
        or root.findtext(".//target_version")
        or root.findtext(".//newversion")
        or root.findtext(".//ver")
    )
    if not version or version.strip().endswith("-LF1V001"):
        return None

    file_url = (
        root.findtext(".//file_url")
        or root.findtext(".//fileurl")
        or root.findtext(".//url")
        or ""
    ).strip()
    if not file_url and not root.findtext(".//version") and not root.findtext(".//target_version"):
        return None

    package_size = _format_size_str(
        root.findtext(".//file_size")
        or root.findtext(".//filesize")
        or root.findtext(".//size")
    )
    md5_val = (
        root.findtext(".//md5")
        or root.findtext(".//file_md5")
        or root.findtext(".//filemd5")
        or None
    )
    rel_date = (
        root.findtext(".//release_date")
        or root.findtext(".//releasedate")
        or root.findtext(".//date")
        or "—"
    ).strip()
    changelog = (
        root.findtext(".//description")
        or root.findtext(".//changelog")
        or root.findtext(".//note")
        or None
    )
    if changelog and changelog.strip() in ("成功", "success", "ok"):
        changelog = None

    build_num = (root.findtext(".//build_number") or "").strip()
    if not build_num and file_url:
        m_bno = re.search(r"\.(\d{6})\.zip", file_url)
        if m_bno:
            build_num = m_bno.group(1)

    return {
        "version": version.strip(),
        "file_url": file_url or None,
        "package_size": package_size,
        "release_date": rel_date,
        "md5": md5_val.strip() if md5_val else None,
        "changelog": changelog.strip() if changelog else None,
        "build_number": build_num,
        "region": region.lower(),
    }


def query_huan_cn_fota(
    platform_id: str,
    current_ver: str,
    project_id: str = "",
    dev_model: str = "",
    timeout: float = 2.5,
) -> dict[str, Any] | None:
    """Queries filter-upgrade.huan.tv (upmp-cn) using HUAN-* signed upgradeIncrRequest."""
    profile = CN_KNOWN_PROJECTS.get(platform_id.upper(), {})
    eff_proj = project_id or profile.get("project_id", "0")
    eff_model = dev_model or profile.get("dev_model", "")
    lang = profile.get("language", "zh")
    tz = profile.get("timezone", "Asia/Shanghai")

    xml_body = build_huan_upgrade_xml(
        platform_id=platform_id,
        current_ver=current_ver,
        region="CN",
        project_id=eff_proj,
        dev_model=eff_model,
        language=lang,
        timezone=tz,
    )
    req_id = uuid.uuid4().hex
    ts = str(int(datetime.now(UTC).timestamp()))
    app_id = TV_APP_IDS["cn"]
    app_key = TV_APP_KEYS["cn"]
    sign = compute_huan_sign(app_key, req_id, ts, "POST", TV_FOTA_PATH, xml_body)

    url = f"http://{TV_FOTA_HOSTS['cn']}{TV_FOTA_PATH}"
    headers = {
        "Content-Type": "application/xml; charset=UTF-8",
        "User-Agent": "TCL-SystemUpdate/1.0",
        "Accept": "application/xml, text/xml, */*",
        "Connection": "close",
        "HUAN-AppId": app_id,
        "HUAN-RequestId": req_id,
        "HUAN-Timestamp": ts,
        "HUAN-Sign": sign,
    }
    req = urllib.request.Request(
        url, data=xml_body.encode("utf-8"), headers=headers, method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return parse_huan_upgrade_response(resp.read(), region="cn")
    except Exception:
        return None


def compute_tcl1_hmac_sha256(
    method: str,
    path: str,
    query: str,
    headers: dict[str, str],
    body_bytes: bytes,
    app_key: str,
    timestamp: str,
) -> tuple[str, str]:
    """
    Computes (signed_headers, signature) for TCL1-HMAC-SHA256 authentication
    used by Leiniao TDP/BI APIs as documented in PROTOCOL_REFERENCE.md.
    """
    relevant = {
        k.lower(): v.strip()
        for k, v in headers.items()
        if k.lower().startswith("xtcl-") or k.lower() in ("host", "content-type")
    }
    sorted_keys = sorted(relevant.keys())
    signed_headers = ";".join(sorted_keys)
    headers_str = "\n".join(f"{k}:{relevant[k]}" for k in sorted_keys)
    body_hash = base64.b64encode(hashlib.sha256(body_bytes).digest()).decode("ascii")
    canonical = f"{method.upper()}\n{path}\n{query}\n{headers_str}\n{body_hash}"
    canonical_hash = base64.b64encode(
        hashlib.sha256(canonical.encode("utf-8")).digest()
    ).decode("ascii")
    string_to_sign = f"TCL1-HMAC-SHA256\n{timestamp}\n{canonical_hash}"
    sig = base64.b64encode(
        hmac.new(
            app_key.encode("utf-8"), string_to_sign.encode("utf-8"), hashlib.sha256
        ).digest()
    ).decode("ascii")
    return signed_headers, sig


def query_leiniao_tdp(
    platform_id: str,
    current_ver: str,
    project_id: str = "",
    dev_model: str = "",
    device_codename: str = "",
    dnum: str = "000000000",
    timeout: float = 3.0,
    xtcl_app: str = "",
    xtcl_key: str = "",
) -> dict[str, Any] | None:
    """
    Queries the CN Leiniao TDP v2 device upgrade endpoint:
    https://tdp-o.api.leiniao.com/tdp-api/api/fms/v2/device/upgrade
    """
    profile = CN_KNOWN_PROJECTS.get(platform_id.upper(), {})
    eff_proj = project_id or profile.get("project_id", "0")
    eff_model = dev_model or profile.get("dev_model", "")
    eff_codename = device_codename or profile.get("device_codename", "")

    payload = {
        "project_id": eff_proj,
        "platform": platform_id,
        "model": eff_model or platform_id,
        "device": eff_codename or eff_model or platform_id,
        "version": current_ver,
        "dnum": dnum,
    }
    body_bytes = json.dumps(payload, separators=(",", ":")).encode("utf-8")
    parsed_ep = urlparse(CN_TDP_ENDPOINT)
    headers: dict[str, str] = {
        "Content-Type": "application/json; charset=UTF-8",
        "Host": parsed_ep.netloc,
        "User-Agent": "TCL-SystemUpdate/1.0",
        "Connection": "close",
    }

    app_val = xtcl_app or os.environ.get("TCL_XTCL_APP", "")
    key_val = xtcl_key or os.environ.get("TCL_XTCL_KEY", "")
    if app_val and key_val:
        ts = str(int(datetime.now(UTC).timestamp()))
        nonce = uuid.uuid4().hex
        headers["XTCL-App"] = app_val
        headers["XTCL-Timestamp"] = ts
        headers["XTCL-nonce"] = nonce
        signed_hdrs, sig = compute_tcl1_hmac_sha256(
            "POST", parsed_ep.path, "", headers, body_bytes, key_val, ts
        )
        headers["XTCL-Authorization"] = (
            f"TCL1-HMAC-SHA256 Credential={app_val},SignedHeaders={signed_hdrs},Signature={sig}"
        )

    req = urllib.request.Request(
        CN_TDP_ENDPOINT, data=body_bytes, headers=headers, method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = json.loads(resp.read().decode("utf-8"))
    except Exception:
        return None

    if not isinstance(raw, dict):
        return None
    err_code = raw.get("error_code", raw.get("code", 0))
    if err_code not in (0, "0", 200, "200", None):
        return None

    data = raw.get("data") if isinstance(raw.get("data"), dict) else raw
    ver = (
        data.get("version")
        or data.get("targetVersion")
        or data.get("target_version")
        or data.get("fwVersion")
    )
    file_url = (
        data.get("file_url")
        or data.get("url")
        or data.get("downloadUrl")
        or data.get("download_url")
    )
    if not ver and isinstance(file_url, str):
        parsed_u = parse_firmware_url(file_url)
        if parsed_u:
            ver = parsed_u["version"]
    if not ver or str(ver).strip().endswith("-LF1V001"):
        return None

    pkg_type = "Full OTA (ZIP)"
    if isinstance(file_url, str) and (
        "/inc/" in file_url or "/incr/" in file_url or "/diff/" in file_url
    ):
        pkg_type = "Incremental OTA"

    parsed_url_info = (
        parse_firmware_url(file_url) if isinstance(file_url, str) else None
    )
    return {
        "version": str(ver).strip(),
        "file_url": str(file_url).strip() if file_url else None,
        "package_size": _format_size_str(
            data.get("file_size") or data.get("fileSize") or data.get("size")
        ),
        "release_date": str(
            data.get("release_date")
            or data.get("releaseDate")
            or (parsed_url_info["release_date"] if parsed_url_info else "—")
        ).strip(),
        "md5": (data.get("md5") or data.get("fileMd5") or None),
        "changelog": data.get("description") or data.get("changelog") or None,
        "build_number": (
            parsed_url_info["build_number"] if parsed_url_info else ""
        ),
        "release_type": pkg_type,
        "region": "cn",
    }


def _is_official_cdn_host(host: str) -> bool:
    host_l = (host or "").strip().lower().split(":")[0]
    if not host_l:
        return False
    if host_l in OFFICIAL_CDN_EXACT_HOSTS:
        return True
    return any(host_l.endswith(sfx) for sfx in OFFICIAL_CDN_DOMAIN_SUFFIXES)


def validate_firmware_url(url: str) -> bool:
    """
    Validates that a manually entered firmware URL uses http/https, points to an
    official TCL / Leiniao / Cedock CDN domain, and ends with a firmware package.
    """
    return parse_firmware_url(url) is not None


def parse_firmware_url(url: str) -> dict[str, Any] | None:
    """
    Parses and validates an official TCL firmware download URL (CN Leiniao FOTA,
    Global Cedock CDN, or celesw.tcl.com service archive).
    """
    raw = (url or "").strip()
    if not raw:
        return None
    parsed = urlparse(raw)
    if parsed.scheme not in ("http", "https") or not _is_official_cdn_host(
        parsed.netloc
    ):
        return None

    host = parsed.netloc.lower()
    path = parsed.path or ""
    filename = path.rsplit("/", 1)[-1]
    fw_match = _FW_FILENAME_RE.match(filename)
    if not fw_match:
        return None

    version = fw_match.group("version").upper()
    platform = fw_match.group("platform").upper()
    build_number = fw_match.group("build_number") or ""
    pkg_tag = (fw_match.group("pkg_tag") or "").upper()
    ext = fw_match.group("ext").lower()

    region = "EU"
    release_date = "—"
    release_type = "Full OTA (ZIP)"
    if ext in ("pkg", "img", "bin") or pkg_tag in ("PKG", "IMG") or "/FOTA-IMG/" in path:
        release_type = "IMG / PKG Recovery"

    if host.endswith(".api.leiniao.com"):
        region = "CN"
        m_cn = _LEINIAO_PATH_RE.match(path)
        if m_cn:
            release_date = f"{m_cn.group('year')}-{m_cn.group('month')}-{m_cn.group('day')}"
            kind = m_cn.group("kind").lower()
            if kind in ("inc", "incr", "diff"):
                release_type = "Incremental OTA"
            elif kind in ("pkg", "img"):
                release_type = "IMG / PKG Recovery"
    elif host.startswith("na-") or host.startswith("na."):
        region = "NA"
    elif host.startswith("as-") or host.startswith("as."):
        region = "AS"

    rel_cat, is_test = classify_firmware_release(version, release_type, "")
    return {
        "url": raw,
        "host": host,
        "region": region,
        "is_cn": region == "CN",
        "platform": platform,
        "version": version,
        "build_number": build_number,
        "filename": filename,
        "release_date": release_date,
        "release_type": release_type,
        "release_category": rel_cat,
        "is_test_release": is_test,
    }


def inspect_manual_firmware_url(
    url: str, timeout: float = 3.0
) -> dict[str, Any] | None:
    """
    Validates a manually supplied firmware URL, probes HTTP HEAD for size/date,
    and inspects ZIP metadata via HTTP Range requests when applicable.
    """
    from .extractor import fetch_remote_zip_metadata_range

    parsed = parse_firmware_url(url)
    if not parsed:
        return None

    result = dict(parsed)
    result["package_size"] = "—"
    result["extracted_details"] = None

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "*/*",
        "Connection": "close",
    }
    try:
        req = urllib.request.Request(parsed["url"], headers=headers, method="HEAD")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            if resp.status in (200, 206):
                cl = resp.headers.get("Content-Length")
                if cl and cl.isdigit():
                    result["package_size"] = _format_size_str(int(cl))
                lm = resp.headers.get("Last-Modified")
                if lm and result["release_date"] == "—":
                    result["release_date"] = lm
    except Exception:
        pass

    if parsed["filename"].lower().endswith(".zip"):
        ext = fetch_remote_zip_metadata_range(parsed["url"], timeout=timeout)
        if ext is not None:
            result["extracted_details"] = ext

    return result
