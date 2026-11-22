"""
TCL Smart TV Firmware Tracker Package.
"""

from .alerts import check_and_report_ci_api_failure, send_telegram_update
from .config import (
    ASSETS_DIR,
    BETA_TEST_JSON,
    CDN_HOSTS,
    CHIPSETS_MD,
    DOCS_BASE_URL,
    DOCS_DIR,
    HISTORY_JSON,
    JSON_OUT,
    MD_OUT,
    NEWS_OUT,
    REPO_ROOT,
    TV_APP_IDS,
    TV_APP_KEYS,
    TV_FOTA_HOSTS,
    TV_FOTA_PATH,
)
from .engine import run
from .extractor import (
    extract_metadata_from_zip_bytes,
    fetch_remote_zip_metadata_range,
    get_all_candidate_mirrors,
    parse_ota_metadata_text,
    parse_zip_central_directory,
    process_firmware_extractions_sequentially,
)
from .fota_client import (
    build_channel_release,
    check_tv_fota,
    construct_cdn_url,
    tv_fota_sign,
)
from .models import (
    ChannelRelease,
    ExtractedBuildDetails,
    PlatformEntry,
    classify_firmware_release,
)
from .parser import (
    load_existing_platforms,
    load_firmware_history,
    parse_chipsets_markdown,
    record_firmware_history_entry,
)
from .writers import (
    save_firmware_history,
    update_news_json,
    write_beta_test_json,
    write_json,
    write_markdown,
)

__all__ = [
    "ChannelRelease",
    "ExtractedBuildDetails",
    "PlatformEntry",
    "build_channel_release",
    "check_and_report_ci_api_failure",
    "check_tv_fota",
    "classify_firmware_release",
    "construct_cdn_url",
    "extract_metadata_from_zip_bytes",
    "fetch_remote_zip_metadata_range",
    "get_all_candidate_mirrors",
    "load_existing_platforms",
    "load_firmware_history",
    "parse_chipsets_markdown",
    "parse_ota_metadata_text",
    "parse_zip_central_directory",
    "process_firmware_extractions_sequentially",
    "record_firmware_history_entry",
    "run",
    "save_firmware_history",
    "send_telegram_update",
    "tv_fota_sign",
    "update_news_json",
    "write_beta_test_json",
    "write_json",
    "write_markdown",
]
