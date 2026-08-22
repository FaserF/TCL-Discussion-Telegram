"""
Telegram broadcast alerts and GitHub Actions CI issue reporter.
"""

from __future__ import annotations

import html
import json
import os
import urllib.request

from .config import DOCS_BASE_URL
from .models import PlatformEntry


def format_size(size_str: str) -> str:
    """Formats file size for alert messages."""
    return size_str if size_str and size_str != "—" else "N/A"


def format_telegram_message(entry: PlatformEntry) -> str:
    """
    Builds the formatted HTML notification payload for community Telegram channels.
    """
    safe_family = html.escape(entry.family_name)
    safe_fw = html.escape(entry.latest_firmware)
    safe_platform = html.escape(entry.platform)
    safe_models = html.escape(entry.featured_models)
    safe_changelog = html.escape(entry.changelog) if entry.changelog else ""
    safe_type = html.escape(entry.release_type)
    safe_size = format_size(entry.package_size)
    safe_date = html.escape(entry.release_date)

    if entry.is_test_release:
        tag_badge = "🧪 <b>TEST / BETA BUILD (RC)</b> ⚠️"
        warning_banner = (
            "⚠️ <b>Caution:</b> <i>This is a Pre-Release / Test build. Experimental features may contain bugs.</i>\n\n"
        )
    else:
        tag_badge = "🚀 <b>NEW OFFICIAL FIRMWARE RELEASE</b>"
        warning_banner = ""

    checksum_lines = ""
    if entry.md5:
        checksum_lines += f"🔑 <b>MD5:</b> <code>{html.escape(entry.md5)}</code>\n"
    if entry.sha256:
        checksum_lines += f"🔒 <b>SHA-256:</b> <code>{html.escape(entry.sha256)}</code>\n"
    if entry.crc32:
        checksum_lines += f"🛡️ <b>CRC-32:</b> <code>0x{html.escape(entry.crc32)}</code>\n"

    ext_lines = ""
    if entry.extracted_details:
        d = entry.extracted_details
        ext_lines = (
            f"📱 <b>OS Version:</b> Android {html.escape(d.android_version)} ({html.escape(d.os_flavor)})\n"
            f"🛡️ <b>Security Patch:</b> <code>{html.escape(d.security_patch)}</code>\n"
            f"📅 <b>Build Date:</b> {html.escape(d.build_date_str)}\n"
        )

    msg = (
        f"{tag_badge}\n\n"
        f"{warning_banner}"
        f"📺 <b>Platform:</b> <code>{safe_platform}</code> ({safe_family})\n"
        f"📦 <b>Firmware Version:</b> <code>{safe_fw}</code>\n"
        f"📋 <b>Package Type:</b> {safe_type}\n"
        f"💾 <b>Size:</b> {safe_size}\n"
        f"🗓️ <b>Release Date:</b> {safe_date}\n"
        f"{checksum_lines}"
        f"{ext_lines}"
        f"🎯 <b>Known Compatible Models:</b> <i>{safe_models}</i>\n\n"
        f"📝 <b>Official Notes:</b>\n<i>{safe_changelog}</i>\n\n"
        f"⬇️ <b>Official Downloads:</b>\n"
        f"• <a href=\"{entry.all_cdn_urls.get('eu', entry.download_url)}\">🇪🇺 EU / Global CDN Mirror</a>\n"
        f"• <a href=\"{entry.all_cdn_urls.get('na', entry.download_url)}\">🇺🇸 North America CDN Mirror</a>\n"
        f"• <a href=\"{entry.all_cdn_urls.get('as', entry.download_url)}\">🌏 Asia-Pacific CDN Mirror</a>\n\n"
        f"📖 <a href=\"{DOCS_BASE_URL}#platform-{safe_platform.lower()}\">View full platform specifications on documentation</a>\n"
        f"💬 <b>Discussion & Community:</b> @tclupdates"
    )
    return msg


def send_telegram_update(entry: PlatformEntry) -> bool:
    """
    Broadcasts a new release announcement to Telegram.
    """
    bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not bot_token or not chat_id:
        return False

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": format_telegram_message(entry),
        "parse_mode": "HTML",
        "disable_web_page_preview": True,
    }

    try:
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status == 200
    except Exception as e:
        print(f"[Telegram Alert] Error broadcasting update for {entry.platform}: {e}")
        return False


def check_and_report_ci_api_failure(failed_count: int, total_count: int, last_error_msg: str) -> None:
    """
    When running in GitHub Actions CI, detects if the FOTA upgrade API is failing
    (e.g., due to rotated HMAC keys, blocked endpoints, or auth changes).
    Creates an issue automatically if one is not already open (anti-spam).
    """
    if os.environ.get("GITHUB_ACTIONS") != "true":
        return

    if total_count == 0 or failed_count < (total_count // 2):
        return

    repo = os.environ.get("GITHUB_REPOSITORY")
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not repo or not token:
        print("[CI Alert] GITHUB_REPOSITORY or GITHUB_TOKEN not available. Skipping issue creation.")
        return

    issue_title = "[FOTA API Alert] TCL Upgrade API Authentication Failure (Secret / HMAC Key Rotation Required)"
    issues_url = f"https://api.github.com/repos/{repo}/issues?state=open"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "TCL-Firmware-Tracker-CI",
    }

    try:
        req = urllib.request.Request(issues_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            existing_issues = json.loads(resp.read().decode("utf-8"))
            for issue in existing_issues:
                if issue.get("title") == issue_title:
                    print("[CI Alert] Open alert issue already exists. Skipping duplicate issue creation.")
                    return

        issue_body = (
            f"### ⚠️ TCL FOTA Upgrade API Outage / Key Rotation Detected\n\n"
            f"The automatic firmware tracking engine detected that **{failed_count}/{total_count}** queries "
            f"failed during the latest scheduled run in GitHub Actions.\n\n"
            f"**Details:**\n"
            f"- **Error Output:** `{last_error_msg}`\n"
            f"- **Possible Causes:** The official TCL FOTA upgrade server (`huan.tv`) may have rotated its HMAC signing key, "
            f"updated its API path, or blocked incoming requests.\n\n"
            f"Please inspect SystemUpdate.apk bytecode or network traces to update `TV_APP_KEYS` if needed.\n\n"
            f"*This alert was automatically generated by `scripts/fetch_firmwares.py`.*"
        )

        create_url = f"https://api.github.com/repos/{repo}/issues"
        create_payload = {
            "title": issue_title,
            "body": issue_body,
            "labels": ["bug", "api-alert", "automated"],
        }
        req_post = urllib.request.Request(
            create_url,
            data=json.dumps(create_payload).encode("utf-8"),
            headers=headers,
            method="POST",
        )
        with urllib.request.urlopen(req_post, timeout=10) as resp:
            if resp.status in (200, 201):
                print(f"[CI Alert] Successfully created GitHub issue: '{issue_title}'")
    except Exception as e:
        print(f"[CI Alert] Failed to query or create GitHub issue: {e}")
