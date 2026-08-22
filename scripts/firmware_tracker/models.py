"""
Data models and dataclasses for TCL Smart TV platforms and firmware releases.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Optional


def classify_firmware_release(version_str: str, raw_release_type: str = "Full OTA (ZIP)", description: str = "") -> tuple[str, bool]:
    """
    Classifies a firmware release into:
    - release_category: 'Production (Stable)', 'Beta / Test Build (RC)', or 'Manufacturing / Test'
    - is_test_release: True for Beta / Test builds, False for Production releases.
    """
    v_upper = (version_str or "").upper()
    desc_upper = (description or "").upper()

    if re.search(r"[-_]LF\d*R\d+$|[-_]R\d{3,}$|[-_]RC\d*", v_upper) or "LF1R" in v_upper:
        return "Beta / Test Build (RC)", True
    if re.search(r"[-_]LF\d*M\d+$|[-_]M\d{3,}$|[-_]TEST", v_upper) or "LF1M" in v_upper:
        return "Manufacturing / Pre-production (Test)", True
    if "[TEST]" in desc_upper or "[BETA]" in desc_upper or "TEST BUILD" in desc_upper or "RELEASE CANDIDATE" in desc_upper:
        return "Beta / Test Build (RC)", True

    return "Production (Stable)", False


@dataclass
class ExtractedBuildDetails:
    """
    Detailed build parameters extracted from remote ZIP archives via HTTP Range headers.
    """
    android_version: str = "—"
    os_flavor: str = "—"
    gms_version: str = "—"
    security_patch: str = "—"
    build_date_utc: Optional[int] = None
    build_date_str: str = "—"
    fingerprint: str = "—"
    sdk_level: Optional[int] = None
    incremental_build: str = "—"
    device_codename: str = "—"


@dataclass
class ChannelRelease:
    """
    Firmware release attributes for a specific release channel (Stable, Beta, or Test).
    """
    version: str
    build_number: str = ""
    release_type: str = "Full OTA (ZIP)"
    release_category: str = "Production (Stable)"
    is_test_release: bool = False
    package_size: str = "—"
    release_date: str = "—"
    md5: Optional[str] = None
    sha256: Optional[str] = None
    crc32: Optional[str] = None
    changelog: Optional[str] = None
    download_url: str = ""
    all_cdn_urls: dict = field(default_factory=dict)
    extracted_details: Optional[ExtractedBuildDetails] = None


@dataclass
class PlatformEntry:
    """
    Represents a TCL hardware platform family and its firmware tracking state.
    """
    platform: str
    alt_platform_id: str
    family_name: str
    soc_specs: str
    featured_models: str
    latest_firmware: str
    build_number: str = ""
    release_type: str = "Full OTA (ZIP)"
    package_size: str = "—"
    release_date: str = "—"
    md5: Optional[str] = None
    sha256: Optional[str] = None
    crc32: Optional[str] = None
    changelog: Optional[str] = None
    region: str = "EU"
    download_url: str = ""
    is_test_release: bool = False
    release_category: str = "Production (Stable)"
    all_cdn_urls: dict = field(default_factory=dict)
    fota_api_status: str = "Unchecked"
    extracted_details: Optional[ExtractedBuildDetails] = None
    stable: Optional[ChannelRelease] = None
    beta: Optional[ChannelRelease] = None
    test: Optional[ChannelRelease] = None
    checked_at: str = ""
