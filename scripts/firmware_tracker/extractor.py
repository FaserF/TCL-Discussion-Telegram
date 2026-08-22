"""
HTTP Range-based ZIP Central Directory Inspector and OTA metadata extractor.
"""

from __future__ import annotations

import io
import struct
import urllib.request
import zipfile
import zlib
from datetime import datetime, timezone
from typing import Any, Optional

from .models import ExtractedBuildDetails, PlatformEntry
from .parser import record_firmware_history_entry


def parse_ota_metadata_text(raw_text: str) -> ExtractedBuildDetails:
    """
    Parses Android OTA metadata property key-value pairs (from META-INF/com/android/metadata).
    """
    props: dict[str, str] = {}
    for line in raw_text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            k, v = line.split("=", 1)
            props[k.strip()] = v.strip()

    fingerprint = (
        props.get("post-build")
        or props.get("ro.build.fingerprint")
        or props.get("ro.bootimage.build.fingerprint")
        or "—"
    )

    android_ver = "—"
    if fingerprint != "—" and "/" in fingerprint and ":" in fingerprint:
        try:
            slash_idx = fingerprint.find("/")
            colon_idx = fingerprint.find(":", slash_idx)
            if colon_idx != -1:
                sub = fingerprint[colon_idx + 1 :]
                next_slash = sub.find("/")
                if next_slash != -1:
                    candidate = sub[:next_slash].strip()
                    if candidate.isdigit() or (len(candidate) <= 3 and candidate[0].isdigit()):
                        android_ver = candidate
        except Exception:
            pass

    if android_ver == "—":
        for k in ("ro.build.version.release", "ro.product.build.version.release", "android_version"):
            if k in props and props[k]:
                android_ver = props[k]
                break

    os_flavor = "Google TV (GTV)"
    gms = "Android_12_GTV"
    if android_ver != "—":
        if android_ver == "14":
            gms = "Android_14_GTV_U"
            os_flavor = "Google TV (GTV - Android 14 U)"
        elif android_ver == "12":
            gms = "Android_12_GTV"
            os_flavor = "Google TV (GTV)"
        elif android_ver == "11":
            gms = "Android_11_ATV"
            os_flavor = "Android TV (ATV)"
        elif android_ver == "9":
            gms = "Android_9_ATV"
            os_flavor = "Android TV (ATV - Pie)"

    sec_patch = (
        props.get("post-security-patch-level")
        or props.get("ro.build.version.security_patch")
        or "—"
    )

    ts_val: Optional[int] = None
    ts_formatted = "—"
    raw_ts = (
        props.get("post-timestamp")
        or props.get("ro.build.date.utc")
        or props.get("timestamp")
    )
    if raw_ts and raw_ts.isdigit():
        try:
            ts_val = int(raw_ts)
            dt = datetime.fromtimestamp(ts_val, tz=timezone.utc)
            ts_formatted = dt.strftime("%b %d, %Y")
            if sec_patch == "—":
                sec_patch = dt.strftime("%Y-%m-05")
        except Exception:
            pass

    sdk_val: Optional[int] = None
    raw_sdk = (
        props.get("post-sdk-level")
        or props.get("ro.build.version.sdk")
    )
    if raw_sdk and raw_sdk.isdigit():
        sdk_val = int(raw_sdk)
    elif android_ver == "14":
        sdk_val = 34
    elif android_ver == "12":
        sdk_val = 31
    elif android_ver == "11":
        sdk_val = 30
    elif android_ver == "9":
        sdk_val = 28

    incr = props.get("post-build-incremental") or props.get("ro.build.version.incremental") or "—"
    dev = props.get("device") or props.get("ro.product.device") or "—"

    return ExtractedBuildDetails(
        android_version=android_ver,
        os_flavor=os_flavor,
        gms_version=gms,
        security_patch=sec_patch,
        build_date_utc=ts_val,
        build_date_str=ts_formatted,
        fingerprint=fingerprint,
        sdk_level=sdk_val,
        incremental_build=incr,
        device_codename=dev,
    )


def parse_zip_central_directory(tail_bytes: bytes) -> dict[str, tuple[int, int, int]]:
    """
    Parses ZIP Central Directory from tail bytes to locate file headers and byte offsets.
    """
    eocd_sig = b"PK"
    pos = tail_bytes.rfind(eocd_sig)
    if pos == -1:
        return {}

    cd_sig = b"PK"
    files: dict[str, tuple[int, int, int]] = {}
    idx = 0
    while True:
        cd_entry = tail_bytes.find(cd_sig, idx, pos)
        if cd_entry == -1:
            break

        method = struct.unpack("<H", tail_bytes[cd_entry + 10 : cd_entry + 12])[0]
        c_size, u_size = struct.unpack("<II", tail_bytes[cd_entry + 20 : cd_entry + 28])
        fn_len, extra_len, comm_len = struct.unpack("<HHH", tail_bytes[cd_entry + 28 : cd_entry + 34])
        offset = struct.unpack("<I", tail_bytes[cd_entry + 42 : cd_entry + 46])[0]

        fname = tail_bytes[cd_entry + 46 : cd_entry + 46 + fn_len].decode("utf-8", errors="ignore")
        files[fname] = (method, c_size, u_size, offset)
        idx = cd_entry + 46 + fn_len + extra_len + comm_len

    return files


def extract_metadata_from_zip_bytes(zip_bytes: bytes) -> Optional[ExtractedBuildDetails]:
    """
    Inspects in-memory zip bytes for META-INF/com/android/metadata.
    """
    try:
        with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
            for item in zf.namelist():
                if item.endswith("META-INF/com/android/metadata") or item.endswith("metadata"):
                    with zf.open(item) as f:
                        txt = f.read().decode("utf-8", errors="ignore")
                        return parse_ota_metadata_text(txt)
    except Exception:
        pass
    return None


def fetch_remote_zip_metadata_range(url: str, timeout: int = 2) -> Optional[ExtractedBuildDetails]:
    """
    Downloads ONLY the ZIP Central Directory and metadata file using HTTP Range headers (~64KB to 1MB total)
    instead of transferring the full 2 GB archive.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)",
        "Accept": "*/*",
        "Connection": "close",
    }

    # 1. Fetch the last 1MB of the ZIP to inspect the Central Directory
    req_tail = urllib.request.Request(url, headers={**headers, "Range": "bytes=-1048576"})
    tail_data: Optional[bytes] = None
    try:
        with urllib.request.urlopen(req_tail, timeout=timeout) as resp:
            tail_data = resp.read()
    except Exception:
        pass

    if not tail_data:
        try:
            req_head = urllib.request.Request(url, headers={**headers, "Range": "bytes=0-1048576"})
            with urllib.request.urlopen(req_head, timeout=timeout) as resp:
                head_data = resp.read()
                return extract_metadata_from_zip_bytes(head_data)
        except Exception:
            return None

    files = parse_zip_central_directory(tail_data)
    target_name = None
    for fn in files:
        if fn.endswith("META-INF/com/android/metadata") or fn.endswith("metadata") or fn.endswith("build.prop"):
            target_name = fn
            break

    if not target_name:
        return extract_metadata_from_zip_bytes(tail_data)

    method, c_size, u_size, offset = files[target_name]

    req_range = urllib.request.Request(url, headers={**headers, "Range": f"bytes={offset}-{offset + c_size + 256}"})
    try:
        with urllib.request.urlopen(req_range, timeout=timeout) as resp:
            raw_chunk = resp.read()
            if len(raw_chunk) >= 30 and raw_chunk[:4] == b"\x50\x4b\x03\x04":
                loc_fn_len, loc_extra_len = struct.unpack("<HH", raw_chunk[26:30])
                payload_start = 30 + loc_fn_len + loc_extra_len
                comp_data = raw_chunk[payload_start : payload_start + c_size]

                if method == 8:
                    decomp_txt = zlib.decompress(comp_data, -zlib.MAX_WBITS).decode("utf-8", errors="ignore")
                else:
                    decomp_txt = comp_data.decode("utf-8", errors="ignore")

                return parse_ota_metadata_text(decomp_txt)
    except Exception:
        pass

    return None


def get_all_candidate_mirrors(platform: str, fw_name: str, build_number: str, default_url: str) -> list[str]:
    """
    Generates all regional CDN mirror endpoints and alternate paths for a given firmware release.
    """
    pdir = "V8" + platform.replace("-", "")
    bno_suffix = f".{build_number}" if build_number else ""

    mirrors = [
        default_url,
        f"http://eu-update.cedock.com/apps/resource2/{pdir}/{fw_name}/FOTA-OTA/{fw_name}{bno_suffix}.zip",
        f"http://na-update.cedock.com/apps/resource2/{pdir}/{fw_name}/FOTA-OTA/{fw_name}{bno_suffix}.zip",
        f"http://as-update.cedock.com/apps/resource2/{pdir}/{fw_name}/FOTA-OTA/{fw_name}{bno_suffix}.zip",
        f"http://as.update.cedock.com/apps/resource2/{pdir}/{fw_name}/FOTA-OTA/{fw_name}{bno_suffix}.zip",
        f"http://update.cedock.com/apps/resource2/{pdir}/{fw_name}/FOTA-OTA/{fw_name}{bno_suffix}.zip",
        f"http://celesw.tcl.com/CSEU%20TV/Software/{fw_name}.zip",
    ]
    seen = set()
    return [m for m in mirrors if m and not (m in seen or seen.add(m))]


def process_firmware_extractions_sequentially(
    entries: list[PlatformEntry],
    updated_releases: list[PlatformEntry],
    generated_at: str,
    history: dict[str, list[dict[str, Any]]],
    max_missing_per_run: int = 10,
    target_pids: Optional[set[str]] = None,
    force_extract: bool = False,
    writers_module: Optional[Any] = None,
) -> None:
    """
    Sequentially processes firmware packages to extract deep build properties using HTTP Range requests.
    STRICT RULE:
    - ONLY queries when a platform received a new firmware release OR when metadata is missing (null)
      or explicitly forced via CLI.
    - Uses HTTP Range requests to inspect only the ZIP Central Directory in milliseconds without full download.
    - NEVER re-downloads platforms that already have verified extracted_details unless force_extract is set.
    - Incrementally updates firmwares.json, firmwares_history.json, and docs/firmwares.md.
    """
    updated_platform_ids = {u.platform for u in updated_releases}

    if target_pids:
        if force_extract:
            pending_entries = [e for e in entries if e.platform in target_pids]
        else:
            pending_entries = [e for e in entries if e.platform in target_pids and (e.extracted_details is None or e.platform in updated_platform_ids)]
    else:
        new_update_entries = [e for e in entries if e.platform in updated_platform_ids]
        missing_entries = [e for e in entries if (e.extracted_details is None or force_extract) and e.platform not in updated_platform_ids]
        pending_entries = new_update_entries + missing_entries[:max_missing_per_run]

    if not pending_entries:
        print("[Firmware Extraction] All targeted releases have verified metadata. Skipping range checks.")
        return

    print(f"\n[Firmware Extraction] Processing {len(pending_entries)} platform(s) for metadata extraction...")

    updated_any = False
    for idx, e in enumerate(pending_entries):
        if e.platform in updated_platform_ids or force_extract:
            e.extracted_details = None

        print(f"  [{idx+1}/{len(pending_entries)}] Checking firmware metadata for {e.platform} ({e.latest_firmware}) via Range requests...", end=" ", flush=True)

        extracted: Optional[ExtractedBuildDetails] = None

        candidate_mirrors = get_all_candidate_mirrors(e.platform, e.latest_firmware, e.build_number, e.download_url)
        for mirror_url in candidate_mirrors:
            extracted = fetch_remote_zip_metadata_range(mirror_url, timeout=3)
            if extracted:
                print(f"Extracted via Range ({mirror_url[:40]}...): Android {extracted.android_version} ({extracted.os_flavor})")
                break

        if not extracted:
            print("CDN Range check skipped (remote mirrors unreachable or 404).")
            continue

        if extracted:
            e.extracted_details = extracted
            updated_any = True
            record_firmware_history_entry(history, e)
            if writers_module:
                writers_module.write_json(entries, generated_at)
                writers_module.write_beta_test_json(entries, generated_at)
                writers_module.save_firmware_history(history, entries)
                writers_module.write_markdown(entries, generated_at, history)

    if not updated_any:
        print("[Firmware Extraction] Completed (metadata up to date).")
