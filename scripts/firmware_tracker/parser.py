"""
Parsers for chipsets.md documentation and local JSON database loaders.
"""

from __future__ import annotations

import json
import re
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from .config import CHIPSETS_MD, HISTORY_JSON, JSON_OUT
from .models import ExtractedBuildDetails, PlatformEntry


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

                primary_match = re.search(r"\*\*([0-9A-Za-z]+(?:T[0-9]+)?)\*\*", id_raw)
                if not primary_match:
                    continue
                p_id = primary_match.group(1)

                found_ids = re.findall(r"([0-9A-Za-z]+(?:T[0-9]+)?)", id_raw)
                clean_ids = [i for i in found_ids if i not in ("and", "or", "to", "ID", "IDs", "TV", "Menu") and len(i) >= 4]
                alt_id = clean_ids[1] if len(clean_ids) > 1 and clean_ids[1] != p_id else p_id

                reg = "NA" if ("(NA" in fam_raw or "(NA" in id_raw or "NA" in p_id or p_id in ("0012T02", "T653T02", "T615T02")) else "EU"

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
                    "extracted_details": None,
                    "region": reg,
                }

    print(f"[Chipsets Parser] Dynamically loaded {len(platforms)} platform definitions from {CHIPSETS_MD.name}")
    return platforms


def load_existing_platforms() -> dict[str, dict[str, Any]]:
    """
    Loads currently tracked platform states and verified metadata from docs/assets/firmwares.json.
    """
    if not JSON_OUT.exists():
        return {}
    try:
        data = json.loads(JSON_OUT.read_text(encoding="utf-8"))
        res = {}
        for fw in data.get("firmwares", []):
            pid = fw.get("platform")
            if pid:
                res[pid] = {
                    k: fw.get(k)
                    for k in (
                        "latest_firmware", "build_number", "release_type", "package_size",
                        "release_date", "md5", "sha256", "crc32", "changelog",
                        "download_url", "recovery_pkg_url", "recovery_pkg_size",
                        "recovery_pkg_md5", "recovery_pkg_sha256", "extracted_details",
                        "region", "stable", "beta", "test"
                    )
                }
        return res
    except Exception:
        return {}


def load_firmware_history() -> dict[str, list[dict[str, Any]]]:
    """
    Loads the persistent historical database from docs/assets/firmwares_history.json.
    """
    if not HISTORY_JSON.exists():
        return {}
    try:
        data = json.loads(HISTORY_JSON.read_text(encoding="utf-8"))
        if "history" in data and isinstance(data["history"], dict):
            return data["history"]
        return {k: v for k, v in data.items() if isinstance(v, list)}
    except Exception:
        return {}


def record_firmware_history_entry(history: dict[str, list[dict[str, Any]]], entry: PlatformEntry) -> None:
    """
    Records a firmware version snapshot into the working history dictionary.
    """
    pid = entry.platform
    if pid not in history:
        history[pid] = []

    existing_versions = {h.get("version") for h in history[pid] if isinstance(h, dict)}
    if entry.latest_firmware and entry.latest_firmware not in existing_versions and not entry.latest_firmware.endswith("-LF1V001"):
        record = {
            "version": entry.latest_firmware,
            "build_number": entry.build_number,
            "release_type": entry.release_type,
            "is_test_release": entry.is_test_release,
            "release_category": entry.release_category,
            "package_size": entry.package_size,
            "release_date": entry.release_date,
            "md5": entry.md5,
            "sha256": entry.sha256,
            "crc32": entry.crc32,
            "changelog": entry.changelog,
            "download_url": entry.download_url,
            "recovery_pkg_url": entry.recovery_pkg_url,
            "recovery_pkg_size": entry.recovery_pkg_size,
            "recovery_pkg_md5": entry.recovery_pkg_md5,
            "recovery_pkg_sha256": entry.recovery_pkg_sha256,
            "all_cdn_urls": entry.all_cdn_urls,
            "extracted_details": asdict(entry.extracted_details) if entry.extracted_details else None,
            "recorded_at": datetime.now(timezone.utc).isoformat(),
        }
        history[pid].insert(0, record)
