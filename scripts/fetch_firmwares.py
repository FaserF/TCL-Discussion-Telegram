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
import json
import sys
from dataclasses import asdict
from pathlib import Path

# Ensure scripts directory is in sys.path
SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from firmware_tracker import (  # noqa: E402
    inspect_manual_firmware_url,
    process_firmware_extractions_sequentially,
    resolve_cn_target,
    run,
    save_firmware_history,
    update_news_json,
    write_beta_test_json,
    write_json,
    write_markdown,
    writers,
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="TCL Smart TV Firmware Tracker & Discovery Engine"
    )
    parser.add_argument(
        "-c",
        "--chipset",
        "--platform",
        nargs="*",
        default=None,
        help="One or more chipset/platform IDs or names to filter (e.g. --chipset 0008T01 or -c T653T11). Defaults to 'all'.",
    )
    parser.add_argument(
        "-r",
        "--region",
        default=None,
        help="Filter tracked platforms by market region (e.g. EU, NA, AS, CN).",
    )
    parser.add_argument(
        "-m",
        "--model",
        default="",
        help="TV model or device string to resolve/override (e.g. FF-CN-MT9653-R675C, R675C, tcl_mt5879_cn).",
    )
    parser.add_argument(
        "--project-id",
        default="",
        help="Hardware Project ID override for FOTA/TDP queries (e.g. 12061).",
    )
    parser.add_argument(
        "--manual-url",
        default="",
        help="Validate, parse, and inspect a manually provided official TCL/Leiniao/Cedock firmware URL.",
    )
    parser.add_argument(
        "-f",
        "--force-extract",
        action="store_true",
        help="Force re-extraction of metadata via Range requests even if cached details exist.",
    )
    args = parser.parse_args()

    if args.manual_url:
        info = inspect_manual_firmware_url(args.manual_url)
        if not info:
            print(
                f"[Error] Invalid or untrusted firmware URL: {args.manual_url}",
                file=sys.stderr,
            )
            sys.exit(1)
        if info.get("extracted_details") is not None:
            info["extracted_details"] = asdict(info["extracted_details"])
        print(json.dumps(info, indent=2, ensure_ascii=False))
        return

    chipsets_list: list[str] | None = None
    if args.chipset:
        chipsets_list = []
        for item in args.chipset:
            for piece in item.replace(",", " ").split():
                piece = piece.strip()
                if piece and piece.lower() != "all":
                    chipsets_list.append(piece)
        if not chipsets_list:
            chipsets_list = None

    if not chipsets_list and (args.model or args.project_id):
        resolved = resolve_cn_target(args.model or args.project_id)
        if resolved:
            chipsets_list = [resolved["platform"]]

    entries, updated_releases, generated_at, history, target_pids = run(
        chipset_filters=chipsets_list,
        region_filter=args.region,
        project_id_override=args.project_id,
        model_override=args.model,
    )
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
