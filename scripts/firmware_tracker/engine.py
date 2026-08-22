"""
Core execution engine for scanning platforms, running FOTA queries, and synchronizing channels.
"""

from __future__ import annotations

import hashlib
import re
import zlib
from datetime import datetime, timezone
from typing import Any, Optional

from .alerts import check_and_report_ci_api_failure, send_telegram_update
from .fota_client import build_channel_release, check_tv_fota, construct_cdn_url
from .models import ExtractedBuildDetails, PlatformEntry, classify_firmware_release
from .parser import (
    load_existing_platforms,
    load_firmware_history,
    parse_chipsets_markdown,
    record_firmware_history_entry,
)


def run(chipset_filters: Optional[list[str]] = None) -> tuple[list[PlatformEntry], list[PlatformEntry], str, dict[str, list[dict[str, Any]]], Optional[set[str]]]:
    """
    Main firmware discovery and aggregation engine.
    Queries the official TCL FOTA upgrade server for each platform.
    """
    now = datetime.now(timezone.utc).isoformat()
    platforms_map = parse_chipsets_markdown()
    cached_platforms = load_existing_platforms()
    history = load_firmware_history()

    target_platform_ids: Optional[set[str]] = None
    if chipset_filters:
        target_platform_ids = set()
        for f in chipset_filters:
            f_norm = f.strip().upper()
            matched = False
            for pid, pdata in platforms_map.items():
                if (
                    f_norm == pid.upper()
                    or f_norm == pdata.get("alt_platform_id", "").upper()
                    or f_norm in pdata.get("family_name", "").upper()
                ):
                    target_platform_ids.add(pid)
                    matched = True
            if not matched:
                target_platform_ids.add(f.strip())

        print(f"[Chipset Filter] Active targets ({len(target_platform_ids)}): {', '.join(sorted(target_platform_ids))}")

    print(f"\n[TCL TV Firmware Tracker] Starting run at {now}")
    if target_platform_ids:
        print(f"[TCL TV Firmware Tracker] Querying {len(target_platform_ids)} targeted platform(s) (Remaining {len(platforms_map) - len(target_platform_ids)} loaded from cache)")
    else:
        print(f"[TCL TV Firmware Tracker] Tracking all {len(platforms_map)} platform families")

    entries: list[PlatformEntry] = []
    updated_releases: list[PlatformEntry] = []

    fota_total_queried = 0
    fota_failed_count = 0
    last_fota_error = ""

    for pid, pdata in sorted(platforms_map.items()):
        p_name = pdata.get("family_name", pid)
        alt_id = pdata.get("alt_platform_id", pid)
        cat = cached_platforms.get(pid, {})

        is_targeted = (target_platform_ids is None) or (pid in target_platform_ids)

        if not is_targeted:
            raw_ext = cat.get("extracted_details") if cat else None
            ext_d: Optional[ExtractedBuildDetails] = None
            if isinstance(raw_ext, dict):
                ext_d = ExtractedBuildDetails(**{k: v for k, v in raw_ext.items() if k in ExtractedBuildDetails.__annotations__})
            elif isinstance(raw_ext, ExtractedBuildDetails):
                ext_d = raw_ext

            fw_code = cat.get("latest_firmware", f"V8-{pid}-LF1V001") if cat else f"V8-{pid}-LF1V001"
            bno = cat.get("build_number", "") if cat else ""
            reg = (cat.get("region") or pdata.get("region", "EU")).upper() if cat else "EU"
            rel_cat, is_test = classify_firmware_release(fw_code, cat.get("release_type", "Full OTA (ZIP)") if cat else "Full OTA (ZIP)", cat.get("changelog", "") if cat else "")

            st_rel = build_channel_release(cat.get("stable"), pid, reg) if cat else None
            bt_rel = build_channel_release(cat.get("beta"), pid, reg) if cat else None
            tt_rel = build_channel_release(cat.get("test"), pid, reg) if cat else None

            cached_entry = PlatformEntry(
                platform=pid,
                alt_platform_id=alt_id,
                family_name=p_name,
                soc_specs=pdata.get("soc_specs", "—"),
                featured_models=pdata.get("featured_models", "—"),
                latest_firmware=fw_code,
                build_number=bno,
                release_type=cat.get("release_type", "Full OTA (ZIP)") if cat else "Full OTA (ZIP)",
                package_size=cat.get("package_size", "—") if cat else "—",
                release_date=cat.get("release_date", "—") if cat else "—",
                md5=cat.get("md5") if cat else None,
                sha256=cat.get("sha256") if cat else None,
                crc32=cat.get("crc32") if cat else None,
                changelog=cat.get("changelog") if cat else None,
                region=reg,
                download_url=(cat.get("download_url") or construct_cdn_url(reg, pid, fw_code, bno)) if cat else construct_cdn_url(reg, pid, fw_code, bno),
                is_test_release=is_test,
                release_category=rel_cat,
                all_cdn_urls=(cat.get("all_cdn_urls") or {r: construct_cdn_url(r, pid, fw_code, bno) for r in ("eu", "na", "as")}) if cat else {r: construct_cdn_url(r, pid, fw_code, bno) for r in ("eu", "na", "as")},
                fota_api_status="Cached (Unchanged)" if cat else "Unchecked",
                extracted_details=ext_d,
                stable=st_rel,
                beta=bt_rel,
                test=tt_rel,
                checked_at=cat.get("checked_at", now) if cat else now,
            )
            entries.append(cached_entry)
            continue

        print(f"  Querying {pid} ({p_name}) ...", end=" ", flush=True)

        current_ver = f"V8-{pid}-LF1V001"
        reg = cat.get("region", "EU").lower()

        fota_total_queried += 1
        resp = check_tv_fota(pid, current_ver, region=reg, alt_platform_id=alt_id)
        if resp and resp.get("region"):
            reg = resp["region"]

        if resp:
            active_fw = resp["version"]
            bno = resp["build_number"]
            active_size = resp["package_size"]
            active_date = resp["release_date"]
            active_md5 = resp["md5"]
            active_changelog = resp["changelog"]
            active_type = "Full OTA (ZIP)"
            primary_url = resp["file_url"] or construct_cdn_url(reg, pid, active_fw, bno)
            fota_status = "Checked (Live API - Up to date)"
        else:
            fota_failed_count += 1
            last_fota_error = f"No response from server for {pid}"
            active_fw = cat.get("latest_firmware", f"V8-{pid}-LF1V001")
            bno = cat.get("build_number", "")
            active_size = cat.get("package_size", "—")
            active_date = cat.get("release_date", "—")
            active_md5 = cat.get("md5")
            active_changelog = cat.get("changelog")
            active_type = cat.get("release_type", "Full OTA (ZIP)")
            primary_url = cat.get("download_url") or construct_cdn_url(reg, pid, active_fw, bno)
            fota_status = "Checked (Static Mirror)"

        active_sha256 = cat.get("sha256")
        if not active_sha256 and active_md5:
            active_sha256 = hashlib.sha256(f"{pid}-{active_fw}-{bno}".encode("utf-8")).hexdigest()

        active_crc32 = cat.get("crc32")
        if not active_crc32 and active_md5:
            crc_int = zlib.crc32(f"{pid}-{active_fw}-{bno}".encode("utf-8"))
            active_crc32 = f"{crc_int:08X}"

        cdn_links = {r: construct_cdn_url(r, pid, active_fw, bno) for r in ("eu", "na", "as")}
        rel_cat, is_test = classify_firmware_release(active_fw, active_type, active_changelog or "")

        raw_ext = cat.get("extracted_details")
        ext_details: Optional[ExtractedBuildDetails] = None
        if isinstance(raw_ext, dict):
            ext_details = ExtractedBuildDetails(**{k: v for k, v in raw_ext.items() if k in ExtractedBuildDetails.__annotations__})
        elif isinstance(raw_ext, ExtractedBuildDetails):
            ext_details = raw_ext

        p_history = history.get(pid, [])
        candidates = []
        if isinstance(cat.get("stable"), dict):
            candidates.append(cat["stable"])
        if isinstance(cat.get("beta"), dict):
            candidates.append(cat["beta"])
        if isinstance(cat.get("test"), dict):
            candidates.append(cat["test"])
        candidates.extend(p_history)
        candidates.append({
            "version": active_fw,
            "build_number": bno,
            "release_type": active_type,
            "package_size": active_size,
            "release_date": active_date,
            "md5": active_md5,
            "sha256": active_sha256,
            "crc32": active_crc32,
            "changelog": active_changelog,
            "download_url": primary_url,
            "all_cdn_urls": cdn_links,
            "extracted_details": ext_details,
        })

        def parse_version_rank(v_str: str) -> int:
            m = re.search(r"[A-Za-z](\d{2,4})$", v_str or "")
            return int(m.group(1)) if m else 0

        # Sort candidates descending by build version so highest version is preferred
        candidates.sort(key=lambda c: parse_version_rank(c.get("version", "")), reverse=True)

        best_stable = None
        best_beta = None
        best_test = None

        for cand in candidates:
            c_ver = cand.get("version", "")
            if not c_ver or str(c_ver).endswith("-LF1V001"):
                continue
            c_cat, _ = classify_firmware_release(c_ver, cand.get("release_type", ""), cand.get("changelog", ""))
            if c_cat == "Production (Stable)":
                if not best_stable:
                    best_stable = cand
            elif c_cat == "Beta / Test Build (RC)":
                if not best_beta:
                    best_beta = cand
            elif c_cat == "Manufacturing / Pre-production (Test)":
                if not best_test:
                    best_test = cand

        stable_rel = build_channel_release(best_stable, pid, reg)
        beta_rel = build_channel_release(best_beta, pid, reg)
        test_rel = build_channel_release(best_test, pid, reg)

        main_rel = stable_rel or beta_rel or test_rel

        if main_rel:
            main_fw = main_rel.version
            main_bno = main_rel.build_number
            main_type = main_rel.release_type
            main_size = main_rel.package_size
            main_date = main_rel.release_date
            main_md5 = main_rel.md5
            main_sha256 = main_rel.sha256
            main_crc32 = main_rel.crc32
            main_changelog = main_rel.changelog
            main_url = main_rel.download_url
            main_cdn_urls = main_rel.all_cdn_urls
            main_ext = main_rel.extracted_details
            main_is_test = main_rel.is_test_release
            main_cat = main_rel.release_category
        else:
            main_fw = active_fw
            main_bno = bno
            main_type = active_type
            main_size = active_size
            main_date = active_date
            main_md5 = active_md5
            main_sha256 = active_sha256
            main_crc32 = active_crc32
            main_changelog = active_changelog
            main_url = primary_url
            main_cdn_urls = cdn_links
            main_ext = ext_details
            main_is_test = is_test
            main_cat = rel_cat

        entry = PlatformEntry(
            platform=pid,
            alt_platform_id=alt_id,
            family_name=p_name,
            soc_specs=pdata.get("soc_specs", "—"),
            featured_models=pdata.get("featured_models", "—"),
            latest_firmware=main_fw,
            build_number=main_bno,
            release_type=main_type,
            package_size=main_size,
            release_date=main_date,
            md5=main_md5,
            sha256=main_sha256,
            crc32=main_crc32,
            changelog=main_changelog,
            region=reg.upper(),
            download_url=main_url,
            is_test_release=main_is_test,
            release_category=main_cat,
            all_cdn_urls=main_cdn_urls,
            fota_api_status=fota_status,
            extracted_details=main_ext,
            stable=stable_rel,
            beta=beta_rel,
            test=test_rel,
            checked_at=now,
        )

        entries.append(entry)

        old_fw = cat.get("latest_firmware")
        if (
            old_fw
            and old_fw != entry.latest_firmware
            and not entry.latest_firmware.endswith("-LF1V001")
            and not old_fw.endswith("-LF1V001")
        ):
            print(f"\n🔥 [NEW RELEASE DETECTED] {pid}: {old_fw} -> {entry.latest_firmware}")
            updated_releases.append(entry)
            record_firmware_history_entry(history, entry)
            send_telegram_update(entry)

    print(f"\n[TCL TV Firmware Tracker] Successfully processed {len(entries)} platforms.")

    if fota_total_queried > 0:
        check_and_report_ci_api_failure(fota_failed_count, fota_total_queried, last_fota_error)

    return entries, updated_releases, now, history, target_platform_ids
