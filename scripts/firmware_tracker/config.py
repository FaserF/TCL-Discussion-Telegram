"""
Configuration, filesystem paths, and server endpoints for the TCL Firmware Tracker.
"""

from __future__ import annotations

import os
from pathlib import Path

# ---------------------------------------------------------------------------
# Output & Documentation paths
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DOCS_DIR = REPO_ROOT / "docs"
ASSETS_DIR = DOCS_DIR / "assets"
JSON_OUT = ASSETS_DIR / "firmwares.json"
BETA_TEST_JSON = ASSETS_DIR / "firmwares_beta_test.json"
HISTORY_JSON = ASSETS_DIR / "firmwares_history.json"
MD_OUT = DOCS_DIR / "firmwares.md"
NEWS_OUT = ASSETS_DIR / "news.json"
CHIPSETS_MD = DOCS_DIR / "chipsets.md"

DOCS_BASE_URL = "https://faserf.github.io/TCL-Discussion-Telegram/firmwares/"

# ---------------------------------------------------------------------------
# Official TCL Server API Constants (from SystemUpdate.apk bytecode)
# ---------------------------------------------------------------------------
TV_FOTA_HOSTS = {
    "eu": "eu-filter-upgrade.huan.tv",
    "na": "na-filter-upgrade.huan.tv",
    "as": "as-filter-upgrade.huan.tv",
    "cn": "filter-upgrade.huan.tv",
    "test": "testfilter-upgrade.huan.tv",
}

TV_FOTA_PATH = "/service/upmp/upgradeIncrInterface"

TV_APP_KEYS = {
    "eu": "4b93841c48eb1af1dfbe2c82384136c9",
    "na": "dacf21ce497259eae5f65312da7d868c",
    "as": "35b8fa949e0578f41f6e751991c800aa",
    "cn": "d49a5258bfcc5f6c3e430f67a0313e90",
    "test": "3550bec90eee953f85361ff46d378e4e",
}

TV_APP_IDS = {
    "eu": "upmp-eu",
    "na": "upmp-na",
    "as": "upmp-as",
    "cn": "upmp-cn",
    "test": "upmp-test",
}

CDN_HOSTS = {
    "eu": "eu-update.cedock.com",
    "na": "na-update.cedock.com",
    "as": "as-update.cedock.com",
}
