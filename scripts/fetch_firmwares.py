#!/usr/bin/env python3
"""
fetch_firmwares.py — Dynamic TCL TV Firmware Tracker & Discovery Engine
=======================================================================
Tracks, aggregates, and discovers TCL Smart TV firmware releases strictly
via the official TCL FOTA upgrade servers (huan.tv) and CDN mirrors (cedock.com).

This module serves as the primary CLI entrypoint, delegating modular tasks
to the `firmware_tracker` package.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Optional

# Ensure scripts directory is in sys.path
SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import firmware_tracker.writers as writers
from firmware_tracker import (
    ChannelRelease,
    ExtractedBuildDetails,
    PlatformEntry,
    build_channel_release,
    check_and_report_ci_api_failure,
    check_tv_fota,
    classify_firmware_release,
    construct_cdn_url,
    extract_metadata_from_zip_bytes,
    fetch_remote_zip_metadata_range,
    get_all_candidate_mirrors,
    load_existing_platforms,
    load_firmware_history,
    parse_chipsets_markdown,
    parse_ota_metadata_text,
    parse_zip_central_directory,
    process_firmware_extractions_sequentially,
    record_firmware_history_entry,
    run,
    save_firmware_history,
    send_telegram_update,
    tv_fota_sign,
    update_news_json,
    write_beta_test_json,
    write_json,
    write_markdown,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="TCL Smart TV Firmware Tracker & Discovery Engine")
    parser.add_argument(
        "-c", "--chipset", "--platform",
        nargs="*",
        default=None,
        help="One or more chipset/platform IDs or names to filter (e.g. --chipset 0008T01 or -c 0008T01 0012T01). Defaults to 'all'."
    )
    parser.add_argument(
        "-f", "--force-extract",
        action="store_true",
        help="Force re-extraction of metadata via Range requests even if cached details exist."
    )
    args = parser.parse_args()

    chipsets_list: Optional[list[str]] = None
    if args.chipset:
        chipsets_list = []
        for item in args.chipset:
            for piece in item.replace(",", " ").split():
                piece = piece.strip()
                if piece and piece.lower() != "all":
                    chipsets_list.append(piece)
        if not chipsets_list:
            chipsets_list = None

    entries, updated_releases, generated_at, history, target_pids = run(chipset_filters=chipsets_list)
    write_json(entries, generated_at)
    write_beta_test_json(entries, generated_at)
    save_firmware_history(history, entries)
    write_markdown(entries, generated_at, history)
    update_news_json(updated_releases, generated_at)

    process_firmware_extractions_sequentially(
        entries,
        updated_releases,
        generated_at,
        history,
        target_pids=target_pids,
        force_extract=args.force_extract,
        writers_module=writers,
    )


if __name__ == "__main__":
    main()
