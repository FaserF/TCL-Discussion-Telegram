"""
Unit tests for CN region firmware tracking, TDP/HUAN protocol signing,
known project lookup, and official firmware URL parsing/validation.
"""

from __future__ import annotations

import io
import json
import sys
import zipfile
from pathlib import Path
from unittest.mock import MagicMock, patch

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from firmware_tracker import (  # noqa: E402
    build_channel_release,
    build_huan_upgrade_xml,
    check_tv_fota,
    compute_huan_sign,
    compute_tcl1_hmac_sha256,
    construct_cdn_url,
    inspect_manual_firmware_url,
    parse_chipsets_markdown,
    parse_firmware_url,
    parse_huan_upgrade_response,
    parse_ota_metadata_text,
    query_leiniao_tdp,
    resolve_cn_target,
    validate_firmware_url,
    write_markdown,
)
from firmware_tracker.models import PlatformEntry  # noqa: E402

SAMPLE_CN_URL = (
    "https://file-fota-tv.api.leiniao.com/2026/10/12/full/ab/d61e1b75fb/"
    "V8-T653T11-LF1V751.zip"
)


def test_resolve_cn_target_known_project() -> None:
    by_platform = resolve_cn_target("T653T11")
    assert by_platform is not None
    assert by_platform["project_id"] == "12061"
    assert by_platform["dev_model"] == "FF-CN-MT9653-R675C"

    by_project = resolve_cn_target("12061")
    assert by_project is not None
    assert by_project["platform"] == "T653T11"

    by_model = resolve_cn_target("ff-cn-mt9653-r675c")
    assert by_model is not None
    assert by_model["device_codename"] == "tcl_mt5879_cn"

    by_short_model = resolve_cn_target("R675C")
    assert by_short_model is not None
    assert by_short_model["platform"] == "T653T11"

    assert resolve_cn_target("nonexistent-model") is None


def test_parse_and_validate_cn_firmware_url() -> None:
    assert validate_firmware_url(SAMPLE_CN_URL) is True
    parsed = parse_firmware_url(SAMPLE_CN_URL)
    assert parsed is not None
    assert parsed["region"] == "CN"
    assert parsed["is_cn"] is True
    assert parsed["platform"] == "T653T11"
    assert parsed["version"] == "V8-T653T11-LF1V751"
    assert parsed["release_date"] == "2026-10-12"
    assert parsed["release_type"] == "Full OTA (ZIP)"
    assert parsed["is_test_release"] is False

    inc_url = (
        "https://file-fota-tv.api.leiniao.com/2026/10/12/inc/ab/d61e1b75fb/"
        "V8-T653T11-LF1V751.zip"
    )
    inc_parsed = parse_firmware_url(inc_url)
    assert inc_parsed is not None
    assert inc_parsed["release_type"] == "Incremental OTA"


def test_parse_and_validate_international_and_invalid_urls() -> None:
    eu_url = (
        "http://eu-update.cedock.com/apps/resource2/V80012T01/"
        "V8-0012T01-LF1V655/FOTA-OTA/V8-0012T01-LF1V655.628400.zip"
    )
    parsed_eu = parse_firmware_url(eu_url)
    assert parsed_eu is not None
    assert parsed_eu["region"] == "EU"
    assert parsed_eu["platform"] == "0012T01"
    assert parsed_eu["build_number"] == "628400"

    assert validate_firmware_url("https://evil.example.com/V8-T653T11-LF1V751.zip") is False
    assert validate_firmware_url("file:///etc/passwd") is False
    assert validate_firmware_url("http://127.0.0.1/V8-T653T11-LF1V751.zip") is False
    assert validate_firmware_url("https://file-fota-tv.api.leiniao.com/readme.txt") is False


def test_huan_cn_xml_signing_and_response_parsing() -> None:
    xml_body = build_huan_upgrade_xml(
        platform_id="T653T11",
        current_ver="V8-T653T11-LF1V489",
        region="CN",
        project_id="12061",
        dev_model="FF-CN-MT9653-R675C",
    )
    assert "<appid>V8T653T11</appid>" in xml_body
    assert "<projectid>12061</projectid>" in xml_body
    assert "<devmodel>FF-CN-MT9653-R675C</devmodel>" in xml_body
    assert "<region>CN</region>" in xml_body

    sig = compute_huan_sign(
        "d49a5258bfcc5f6c3e430f67a0313e90",
        "0123456789abcdef0123456789abcdef",
        "1795562000",
        "POST",
        "/service/upmp/upgradeIncrInterface",
        xml_body,
    )
    assert len(sig) == 32

    no_update_xml = (
        b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        b"<upgradeIncrResponse><state>0000</state><note>\xe6\x88\x90\xe5\x8a\x9f</note></upgradeIncrResponse>"
    )
    assert parse_huan_upgrade_response(no_update_xml, region="cn") is None

    update_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
    <upgradeIncrResponse>
      <state>0000</state>
      <version>V8-T653T11-LF1V751</version>
      <file_url>{SAMPLE_CN_URL}</file_url>
      <file_size>2231822195</file_size>
      <md5>abcdef0123456789abcdef0123456789</md5>
      <release_date>2026-10-12</release_date>
    </upgradeIncrResponse>""".encode()
    parsed = parse_huan_upgrade_response(update_xml, region="cn")
    assert parsed is not None
    assert parsed["version"] == "V8-T653T11-LF1V751"
    assert parsed["file_url"] == SAMPLE_CN_URL
    assert parsed["package_size"] == "2.08 GB"


def test_query_leiniao_tdp_and_tcl1_signing() -> None:
    hdrs, sig = compute_tcl1_hmac_sha256(
        "POST",
        "/tdp-api/api/fms/v2/device/upgrade",
        "",
        {
            "Host": "tdp-o.api.leiniao.com",
            "Content-Type": "application/json; charset=UTF-8",
            "XTCL-App": "com.tcl.versionUpdateApp",
            "XTCL-Timestamp": "1787339989",
            "XTCL-nonce": "09bfb79e140b4fbf9733d7a5880907e2",
        },
        b"{}",
        "test-secret",
        "1787339989",
    )
    assert hdrs == "content-type;host;xtcl-app;xtcl-nonce;xtcl-timestamp"
    assert len(sig) > 10

    mock_resp = MagicMock()
    mock_resp.__enter__.return_value = mock_resp
    mock_resp.read.return_value = json.dumps(
        {
            "error_code": 0,
            "data": {
                "targetVersion": "V8-T653T11-LF1V751",
                "downloadUrl": SAMPLE_CN_URL,
                "fileSize": 2231822195,
                "md5": "0123456789abcdef0123456789abcdef",
            },
        }
    ).encode("utf-8")

    with patch("urllib.request.urlopen", return_value=mock_resp) as mock_open:
        res = query_leiniao_tdp("T653T11", "V8-T653T11-LF1V489")
        assert res is not None
        assert res["version"] == "V8-T653T11-LF1V751"
        assert res["file_url"] == SAMPLE_CN_URL
        assert res["release_date"] == "2026-10-12"
        sent_req = mock_open.call_args[0][0]
        sent_body = json.loads(sent_req.data.decode("utf-8"))
        assert sent_body["project_id"] == "12061"
        assert sent_body["platform"] == "T653T11"

    err_resp = MagicMock()
    err_resp.__enter__.return_value = err_resp
    err_resp.read.return_value = json.dumps(
        {"error_code": 10001, "error_desc": "invalid param"}
    ).encode("utf-8")
    with patch("urllib.request.urlopen", return_value=err_resp):
        assert query_leiniao_tdp("T653T11", "V8-T653T11-LF1V489") is None


def test_check_tv_fota_cn_isolation() -> None:
    called_regions: list[str] = []

    def fake_single(region: str, model_id: str, ver: str, timeout: float = 1.5):
        called_regions.append(region)
        return None

    with (
        patch("firmware_tracker.fota_client.query_huan_cn_fota", return_value=None),
        patch("firmware_tracker.fota_client._single_fota_query", side_effect=fake_single),
        patch("firmware_tracker.fota_client.query_leiniao_tdp", return_value=None),
    ):
        assert check_tv_fota("T653T11", "V8-T653T11-LF1V489", region="cn") is None
        assert called_regions == ["cn"]

    called_regions.clear()
    with patch("firmware_tracker.fota_client._single_fota_query", side_effect=fake_single):
        assert check_tv_fota("0012T01", "V8-0012T01-LF1V001", region="eu") is None
        assert "cn" not in called_regions


def test_cn_metadata_parsing_and_channel_release(tmp_path: Path) -> None:
    meta_text = """
ota-type=BLOCK
post-build=TCL/tcl_mt5879_cn_db/tcl_mt5879_cn:11/RQ3A.210705.001/2026100921:user/release-keys
post-build-incremental=2026100921
post-sdk-level=30
post-security-patch-level=2022-09-05
post-software-version-id=V8-T653T11-LF1V751
post-timestamp=1791550919
pre-device=tcl_mt5879_cn
"""
    details = parse_ota_metadata_text(meta_text)
    assert details.android_version == "11"
    assert details.os_flavor == "Android TV (CN)"
    assert details.device_codename == "tcl_mt5879_cn"
    assert details.sdk_level == 30

    assert construct_cdn_url("cn", "T653T11", "V8-T653T11-LF1V751") == ""
    rel = build_channel_release(
        {"version": "V8-T653T11-LF1V751", "download_url": SAMPLE_CN_URL},
        "T653T11",
        "CN",
    )
    assert rel is not None
    assert rel.all_cdn_urls == {"cn": SAMPLE_CN_URL}

    platforms = parse_chipsets_markdown()
    assert "T653T11" in platforms
    assert platforms["T653T11"]["region"] == "CN"
    assert platforms["T653T11"]["project_id"] == "12061"

    entry = PlatformEntry(
        platform="T653T11",
        alt_platform_id="T653T11",
        family_name="Pentonic 700 (CN) (T653T11)",
        soc_specs="MediaTek MT9653 / MT5879",
        featured_models="R675C, FF-CN-MT9653-R675C",
        latest_firmware="V8-T653T11-LF1V751",
        region="CN",
        download_url=SAMPLE_CN_URL,
        all_cdn_urls={"cn": SAMPLE_CN_URL},
    )
    out_md = tmp_path / "firmwares.md"
    with patch("firmware_tracker.writers.MD_OUT", out_md):
        write_markdown([entry], "2026-11-24T00:00:00+00:00")
    rendered = out_md.read_text(encoding="utf-8")
    assert "[None](None)" not in rendered
    assert "China (CN) CDN (Leiniao)" in rendered
    assert SAMPLE_CN_URL in rendered


def test_inspect_manual_firmware_url() -> None:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        zf.writestr(
            "META-INF/com/android/metadata",
            "post-build=TCL/tcl_mt5879_cn_db/tcl_mt5879_cn:11/RQ3A.210705.001/2026100921:user/release-keys\n"
            "pre-device=tcl_mt5879_cn\n",
        )
    zip_bytes = buf.getvalue()

    head_resp = MagicMock()
    head_resp.__enter__.return_value = head_resp
    head_resp.status = 200
    head_resp.headers = {"Content-Length": "2231822195"}

    range_resp = MagicMock()
    range_resp.__enter__.return_value = range_resp
    range_resp.read.return_value = zip_bytes

    with patch(
        "urllib.request.urlopen", side_effect=[head_resp, range_resp, range_resp]
    ):
        info = inspect_manual_firmware_url(SAMPLE_CN_URL)
        assert info is not None
        assert info["package_size"] == "2.08 GB"
        assert info["extracted_details"] is not None
        assert info["extracted_details"].device_codename == "tcl_mt5879_cn"
