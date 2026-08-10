# /// script
# requires-python = ">=3.12"
# dependencies = ["beautifulsoup4>=4.12", "html2text>=2024.2.26"]
# ///

"""Daily Dose of DS Gmail 星标邮件同步到 Knowledge Bank 的 Pipeline。"""

from __future__ import annotations

import argparse
import base64
import copy
import email
import json
import re
import subprocess
import sys
import time
import urllib.parse
from collections import Counter
from datetime import datetime, timezone
from email import policy
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any, Callable

import html2text
from bs4 import BeautifulSoup


SCHEMA_VERSION = 1
ROOT = Path(__file__).resolve().parents[1]
ARCHIVE_DIR = ROOT / "raw" / "articles"
STAGING_DIR = ROOT / "Clippings" / "DailyDoseOfDS"
PIPELINE_DIR = STAGING_DIR / ".pipeline"
MANIFEST_PATH = PIPELINE_DIR / "manifest.json"
STATUS_PATH = PIPELINE_DIR / "SYNC_STATUS.md"
INDEX_PATH = PIPELINE_DIR / "ARCHIVE_INDEX.md"
INGEST_PROGRESS_PATH = STAGING_DIR / "ingest_progress.json"

# 旧增量脚本曾把这些 ID 当作“已处理”。迁移时保留这项事实，避免被重新下载。
LEGACY_PROCESSED_IDS = {
    "194be07e12ab82bc", "194cd43e281f59cc", "1955d7c8c16ec8c4", "19664020d007efe2",
    "196ac3a283f20357", "1971dcca96aa74c3", "197658945bda228b", "197b30868d3ba958",
    "197c270c599ab371", "197c7ace7fc9ab0e", "198434ae8570344d", "198e2e9234d8b09f",
    "198fc6ca70584770", "1995434d669b06de", "199df440e83cc2f8", "199f91f3eaa6509e",
    "19a1775d61893cb3", "19a274be34a3e99c", "19a79cbb943dd0f0", "19aa2d674dcfaef6",
    "19acc373a89bc8c4", "19ae0c67c504face", "19b5c7637722a2ba", "19b6bfe2074ca987",
    "19b71b8454693ea2", "19b7766d2c7e9ffc", "19c2a80854fc31f8", "19cba7e7c4fb570a",
    "19ce93b00b8a14f0", "19d11dddb3bc89bd", "19d1c347f366b9ac", "19d21bb1fc294cac",
    "19d2bbc9492d99c6", "19d64a1fd91e185f", "19d838888f466ecf", "19d8df42bfdf06fb",
    "19dbca56ab454b95", "19de58fc0d126e4b", "19deeeb458239986", "19dfa25648e2f2cb",
    "19e60c170373504b", "19e84f32570b4582", "19ea91777352c092", "19ec7f0bdd27389b",
    "19edcc2a8ec8a790", "19ef7234678feae5", "19f00c2716d4e27d", "19f29f70428b228f",
    "19f3d7ecdb9a83ee", "19f6174c7b5adc67", "19f6784a03ed6e1e", "19f6ca0f2c928ca3",
    "19f721c214ca5038", "19f86be0631f8e2c", "19f962933027e3e6", "19fa5754b2a0ee28",
    "19faa9c1ec5cf9ba", "19fb9f018f6c5eda",
}

# 旧拆分器曾把这段邮件 footer 广告误判成文章。保留拒绝记录以防再次入库。
KNOWN_REJECTED_ARTICLES = {
    "2026-08-01_Succeed-in-AI-Engineering-roles_19fbed_part5.md": {
        "message_id": "19fbed5d2cd155dd",
        "title": "Succeed in AI Engineering roles",
        "reason": "footer_ad_parse_bug",
    }
}

IGNORED_HEADINGS = [
    r"In today's newsletter", r"Together with", r"TODAY's Daily dose", r"ADVERTISE TO",
    r"SPONSOR US", r"THAT'S A WRAP", r"Today’s email was brought to you", r"Looking for more",
    r"In case you missed it", r"Update your profile", r"Unsubscribe",
]


class PipelineError(RuntimeError):
    pass


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def empty_manifest() -> dict[str, Any]:
    return {"schema_version": SCHEMA_VERSION, "updated_at": now_iso(), "last_discovery_at": None, "emails": {}}


def load_manifest(path: Path = MANIFEST_PATH) -> dict[str, Any]:
    if not path.exists():
        return empty_manifest()
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != SCHEMA_VERSION or not isinstance(data.get("emails"), dict):
        raise PipelineError(f"不支持的 manifest 格式: {path}")
    return data


def save_manifest(data: dict[str, Any], path: Path = MANIFEST_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data["updated_at"] = now_iso()
    temporary = path.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temporary.replace(path)


def metadata_from_markdown(path: Path) -> dict[str, str]:
    head = path.read_text(encoding="utf-8")[:12000]

    def match(pattern: str) -> str:
        found = re.search(pattern, head, re.MULTILINE)
        return found.group(1).strip() if found else ""

    return {
        "title": match(r"^#\s+(.+)$") or path.stem,
        "subject": match(r"^-\s+\*\*原邮件主题\*\*:\s*(.+)$"),
        "sender": match(r"^-\s+\*\*发送人\*\*:\s*(.+)$"),
        "date": match(r"^-\s+\*\*(?:日期|原始日期)\*\*:\s*(.+)$"),
        "message_id": match(r"^-\s+\*\*ID\*\*:\s*([a-fA-F0-9]+)\s*$"),
    }


def new_email_record(message_id: str, lifecycle: str = "discovered") -> dict[str, Any]:
    return {
        "id": message_id,
        "lifecycle": lifecycle,
        "remote_starred": None,
        "first_seen_at": None,
        "last_seen_at": None,
        "subject": "",
        "sender": "",
        "date": "",
        "attempts": 0,
        "last_error": None,
        "reason": None,
        "articles": [],
    }


def bootstrap_manifest(
    archive_dir: Path = ARCHIVE_DIR,
    manifest_path: Path = MANIFEST_PATH,
    progress_path: Path = INGEST_PROGRESS_PATH,
    include_legacy: bool = True,
) -> dict[str, Any]:
    data = load_manifest(manifest_path)
    emails = data["emails"]
    archive_dir.mkdir(parents=True, exist_ok=True)

    if not progress_path.exists():
        raise PipelineError(f"缺少 Ingest 进度文件: {progress_path}")
    progress = json.loads(progress_path.read_text(encoding="utf-8"))
    archived_by_casefold = {path.name.casefold(): path for path in archive_dir.glob("*.md")}
    article_paths = []
    for filename, ingested in progress.items():
        if not ingested:
            continue
        path = archive_dir / filename
        if not path.exists():
            path = archived_by_casefold.get(filename.casefold(), path)
        if not path.exists():
            print(f"警告：Ingest 已完成但 raw 文件不存在: {filename}", file=sys.stderr)
            continue
        article_paths.append(path)
    physical_files = {path.name for path in article_paths}
    for record in emails.values():
        for article in record.get("articles", []):
            if article.get("status") == "ingested" and article.get("file") not in physical_files:
                article["status"] = "rejected"
                article["reason"] = "missing_from_archive"
        if record.get("lifecycle") == "ingested" and not any(
            article.get("status") == "ingested" for article in record.get("articles", [])
        ):
            record["lifecycle"] = "ignored"
            record["reason"] = "all_ingested_articles_missing"

    for path in article_paths:
        meta = metadata_from_markdown(path)
        message_id = meta["message_id"]
        if not message_id:
            print(f"警告：跳过缺少 ID 元数据的文章 {path.name}", file=sys.stderr)
            continue
        record = emails.setdefault(message_id, new_email_record(message_id, "ingested"))
        record.update({key: meta[key] for key in ("subject", "sender", "date") if meta[key]})
        article_id = f"{message_id}:{path.name}"
        article = next((item for item in record["articles"] if item.get("file") == path.name), None)
        values = {"title": meta["title"], "file": path.name, "status": "ingested", "reason": None}
        if article:
            article.update(values)
        else:
            values["id"] = article_id
            record["articles"].append(values)
        record["lifecycle"] = "ingested"

    if include_legacy:
        for message_id in sorted(LEGACY_PROCESSED_IDS):
            if message_id not in emails:
                record = new_email_record(message_id, "ignored")
                record["reason"] = "legacy_filtered_or_deleted"
                emails[message_id] = record

        for filename, rejected in KNOWN_REJECTED_ARTICLES.items():
            message_id = rejected["message_id"]
            record = emails.setdefault(message_id, new_email_record(message_id, "ignored"))
            article_id = f"{message_id}:{filename}"
            article = next((item for item in record["articles"] if item["id"] == article_id), None)
            values = {
                "id": article_id,
                "title": rejected["title"],
                "file": None,
                "status": "rejected",
                "reason": rejected["reason"],
            }
            if article:
                article.update(values)
            else:
                record["articles"].append(values)

    save_manifest(data, manifest_path)
    return data


def run_gws(args: list[str], retries: int = 3) -> dict[str, Any]:
    command = ["gws", *args]
    last_error = ""
    for attempt in range(retries):
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            output = result.stdout.strip()
            starts = [position for position in (output.find("{"), output.find("[")) if position >= 0]
            if starts:
                try:
                    return json.loads(output[min(starts):])
                except json.JSONDecodeError as exc:
                    last_error = f"JSON 解析失败: {exc}"
            else:
                last_error = "命令未返回 JSON"
        else:
            last_error = result.stderr.strip() or result.stdout.strip()
        if attempt + 1 < retries:
            time.sleep(1.5 * (attempt + 1))
    raise PipelineError(f"gws 调用失败: {last_error}")


def list_starred_messages(call: Callable[[list[str]], dict[str, Any]] = run_gws) -> list[dict[str, str]]:
    messages: list[dict[str, str]] = []
    page_token: str | None = None
    while True:
        params: dict[str, Any] = {"userId": "me", "q": "is:starred", "maxResults": 500}
        if page_token:
            params["pageToken"] = page_token
        response = call(["gmail", "users", "messages", "list", "--params", json.dumps(params), "--format", "json"])
        messages.extend(response.get("messages", []))
        page_token = response.get("nextPageToken")
        if not page_token:
            return messages


def discover(data: dict[str, Any], call: Callable[[list[str]], dict[str, Any]] = run_gws) -> tuple[int, int]:
    remote = list_starred_messages(call)
    timestamp = now_iso()
    remote_ids = {item["id"] for item in remote}
    new_count = 0
    for message_id in remote_ids:
        if message_id not in data["emails"]:
            data["emails"][message_id] = new_email_record(message_id)
            data["emails"][message_id]["first_seen_at"] = timestamp
            new_count += 1
        record = data["emails"][message_id]
        record["remote_starred"] = True
        record["last_seen_at"] = timestamp
    for message_id, record in data["emails"].items():
        if message_id not in remote_ids:
            record["remote_starred"] = False
    data["last_discovery_at"] = timestamp
    return len(remote_ids), new_count


def decode_tracking_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    tracking_host = parsed.netloc.casefold()
    if "convertkit" not in tracking_host and "kit-mail" not in tracking_host:
        return url
    parts = parsed.path.strip("/").split("/")
    encoded = parts[-1] if parts else ""
    if len(encoded) <= 20:
        return url
    try:
        encoded += "=" * (-len(encoded) % 4)
        decoded = base64.urlsafe_b64decode(encoded).decode("utf-8", errors="ignore")
        return decoded if decoded.startswith("http") else url
    except (ValueError, UnicodeDecodeError):
        return url


def clean_filename(title: str) -> str:
    title = re.sub(r'[\\/*?:"<>|]', "", title).strip()
    return re.sub(r"\s+", "-", title) or "untitled"


def article_filename(formatted_date: str, title: str, message_id: str) -> str:
    """文件名只使用 Gmail ID，不混用 part 序号。"""
    return f"{formatted_date}_{clean_filename(title)}_{message_id[:6]}.md"


def ignored_heading(heading: Any) -> bool:
    text = heading.get_text(" ", strip=True)
    if any(re.search(pattern, text, re.IGNORECASE) for pattern in IGNORED_HEADINGS):
        return True
    for anchor in heading.find_all("a", href=True):
        path = urllib.parse.urlparse(anchor["href"]).path.rstrip("/").casefold()
        if path == "/membership":
            return True
    return False


def extract_html(raw_message: str) -> tuple[email.message.EmailMessage, BeautifulSoup]:
    padded = raw_message + "=" * (-len(raw_message) % 4)
    message = email.message_from_bytes(base64.urlsafe_b64decode(padded), policy=policy.default)
    html_body = ""
    parts = message.walk() if message.is_multipart() else [message]
    plain_body = ""
    for part in parts:
        disposition = str(part.get("Content-Disposition", ""))
        if "attachment" in disposition:
            continue
        payload = part.get_payload(decode=True) or b""
        charset = part.get_content_charset() or "utf-8"
        if part.get_content_type() == "text/html" and not html_body:
            html_body = payload.decode(charset, errors="ignore")
        elif part.get_content_type() == "text/plain" and not plain_body:
            plain_body = payload.decode(charset, errors="ignore")
    if not html_body:
        html_body = f"<pre>{plain_body}</pre>" if plain_body else "<p>无可用邮件内容</p>"
    return message, BeautifulSoup(html_body, "html.parser")


def parse_message(message_id: str, response: dict[str, Any]) -> tuple[dict[str, str], list[dict[str, str]]]:
    if "raw" not in response:
        raise PipelineError("邮件响应缺少 raw 字段")
    message, soup = extract_html(response["raw"])
    subject = str(message.get("Subject", f"untitled_{message_id}"))
    sender = str(message.get("From", "未知发送者"))
    date = str(message.get("Date", ""))
    formatted_date = "0000-00-00"
    if date:
        try:
            formatted_date = parsedate_to_datetime(date).strftime("%Y-%m-%d")
        except (TypeError, ValueError, OverflowError):
            pass

    for anchor in soup.find_all("a", href=True):
        anchor["href"] = decode_tracking_url(anchor["href"])
    for image in soup.find_all("img", src=True):
        source = image["src"]
        if "open.convertkit-mail" in source or "pixel" in source:
            image.decompose()

    converter = html2text.HTML2Text()
    converter.body_width = 0
    converter.ignore_links = False
    converter.ignore_images = False
    converter.protect_links = True
    converter.unicode_snob = True

    all_h2 = soup.find_all("h2")
    valid_h2 = [heading for heading in all_h2 if not ignored_heading(heading)]
    articles: list[dict[str, str]] = []
    if valid_h2:
        for position, heading in enumerate(valid_h2, 1):
            title = heading.get_text(" ", strip=True).replace("\u200b", "")
            article_soup = BeautifulSoup("", "html.parser")
            article_soup.append(copy.copy(heading))
            node = heading.next_sibling
            while node and getattr(node, "name", None) != "h2":
                article_soup.append(copy.copy(node))
                node = node.next_sibling
            body = converter.handle(str(article_soup)).replace("\u200b", "")
            articles.append({"title": title, "body": re.sub(r"\n{3,}", "\n\n", body), "part": str(position)})
    elif not all_h2:
        body = converter.handle(str(soup)).replace("\u200b", "")
        articles.append({"title": subject.replace("\u200b", ""), "body": re.sub(r"\n{3,}", "\n\n", body), "part": "1"})
    metadata = {"subject": subject, "sender": sender, "date": date, "formatted_date": formatted_date}
    return metadata, articles


def normalized_title(title: str) -> str:
    return re.sub(r"\s+", " ", title.replace("\u200b", "")).strip().casefold()


def existing_titles(data: dict[str, Any]) -> set[str]:
    return {
        normalized_title(article["title"])
        for record in data["emails"].values()
        for article in record.get("articles", [])
        if article.get("status") in {"ingested", "review"}
    }


def fetch_pending(data: dict[str, Any], call: Callable[[list[str]], dict[str, Any]] = run_gws) -> tuple[int, int]:
    STAGING_DIR.mkdir(parents=True, exist_ok=True)
    titles = existing_titles(data)
    processed = article_count = 0
    candidates = [record for record in data["emails"].values() if record["lifecycle"] in {"discovered", "failed"} and record.get("remote_starred") is not False]
    for record in sorted(candidates, key=lambda item: item["id"]):
        message_id = record["id"]
        record["attempts"] += 1
        try:
            params = json.dumps({"userId": "me", "id": message_id, "format": "raw"})
            response = call(["gmail", "users", "messages", "get", "--params", params, "--format", "json"])
            metadata, articles = parse_message(message_id, response)
            record.update(metadata)
            record["articles"] = []
            for index, article in enumerate(articles, 1):
                title = article["title"]
                article_id = f"{message_id}:{index}"
                if normalized_title(title) in titles:
                    record["articles"].append({"id": article_id, "title": title, "file": None, "status": "rejected", "reason": "duplicate_title"})
                    continue
                filename = article_filename(metadata["formatted_date"], title, message_id)
                output_path = STAGING_DIR / filename
                if output_path.exists():
                    raise PipelineError(f"同一邮件内出现规范化后的同名文章: {filename}")
                header = (
                    f"# {title}\n\n- **原邮件主题**: {metadata['subject']}\n- **发送人**: {metadata['sender']}\n"
                    f"- **日期**: {metadata['date']}\n- **ID**: {message_id}\n\n---\n\n"
                )
                output_path.write_text(header + article["body"], encoding="utf-8")
                record["articles"].append({"id": article_id, "title": title, "file": filename, "status": "review", "reason": None})
                titles.add(normalized_title(title))
                article_count += 1
            record["lifecycle"] = "review" if any(item["status"] == "review" for item in record["articles"]) else "ignored"
            record["reason"] = None if record["lifecycle"] == "review" else "all_articles_rejected"
            record["last_error"] = None
            processed += 1
        except Exception as exc:  # 单封失败不应阻断整批同步
            record["lifecycle"] = "failed"
            record["last_error"] = str(exc)
        save_manifest(data)
    return processed, article_count


def reconcile_ingested(data: dict[str, Any]) -> int:
    """只对账，不绕过 Knowledge Bank 的 Ingest SOP 移动物理文件。"""
    progress = json.loads(INGEST_PROGRESS_PATH.read_text(encoding="utf-8"))
    completed = {filename.casefold() for filename, done in progress.items() if done}
    reconciled = 0
    for record in data["emails"].values():
        for article in record.get("articles", []):
            filename = article.get("file")
            if article.get("status") != "review" or not filename:
                continue
            if filename.casefold() in completed and (ARCHIVE_DIR / filename).exists():
                article["status"] = "ingested"
                article["reason"] = None
                reconciled += 1
        if any(item.get("status") == "ingested" for item in record.get("articles", [])):
            record["lifecycle"] = "ingested"
    return reconciled


def reject_article(data: dict[str, Any], article_id: str, reason: str) -> None:
    for record in data["emails"].values():
        for article in record.get("articles", []):
            if article["id"] != article_id:
                continue
            if article["status"] != "review":
                raise PipelineError(f"文章不是待审状态: {article_id}")
            path = STAGING_DIR / article["file"]
            if path.exists():
                path.unlink()
            article["status"] = "rejected"
            article["reason"] = reason
            if not any(item["status"] == "review" for item in record["articles"]):
                record["lifecycle"] = "ingested" if any(item["status"] == "ingested" for item in record["articles"]) else "ignored"
            return
    raise PipelineError(f"未找到文章: {article_id}")


def ingested_articles(data: dict[str, Any]) -> list[dict[str, str]]:
    result = []
    for record in data["emails"].values():
        for article in record.get("articles", []):
            if article.get("status") == "ingested" and article.get("file") and (ARCHIVE_DIR / article["file"]).exists():
                result.append({"title": article["title"], "file": article["file"], "sender": record.get("sender", ""), "date": record.get("date", "")})
    return sorted(result, key=lambda item: item["file"], reverse=True)


def rebuild_index(data: dict[str, Any]) -> None:
    articles = ingested_articles(data)
    lines = [
        "# 星标技术文章索引\n\n",
        f"已进入 `raw/articles` 的 Daily Dose of DS 文章共 **{len(articles)}** 篇。同步明细见 [SYNC_STATUS.md](./SYNC_STATUS.md)。\n\n",
        "| 序号 | 文章标题 | 发送人 | 日期 | 链接 |\n",
        "| --- | --- | --- | --- | --- |\n",
    ]
    for index, article in enumerate(articles, 1):
        title = article["title"].replace("|", "\\|")
        sender = article["sender"].replace("|", "\\|")
        date = article["date"].replace("|", "\\|")
        lines.append(f"| {index} | {title} | {sender} | {date} | [查看文章](../../../raw/articles/{article['file']}) |\n")
    INDEX_PATH.write_text("".join(lines), encoding="utf-8")


def rebuild_status(data: dict[str, Any]) -> None:
    records = list(data["emails"].values())
    lifecycle_counts = Counter(record["lifecycle"] for record in records)
    remote_counts = Counter("starred" if record.get("remote_starred") is True else "unstarred" if record.get("remote_starred") is False else "unknown" for record in records)
    article_counts = Counter(article["status"] for record in records for article in record.get("articles", []))
    lines = [
        "# Gmail 星标邮件同步状态\n\n",
        f"> 此文件由 Pipeline 生成，请勿手工编辑。机器可读账本为 [`manifest.json`](./manifest.json)。更新时间：`{data['updated_at']}`。\n\n",
        "## 汇总\n\n",
        "| 维度 | 状态 | 数量 |\n| --- | --- | ---: |\n",
    ]
    for key in ("discovered", "failed", "review", "ingested", "ignored"):
        lines.append(f"| 邮件 | {key} | {lifecycle_counts[key]} |\n")
    for key in ("starred", "unstarred", "unknown"):
        lines.append(f"| 远程星标 | {key} | {remote_counts[key]} |\n")
    for key in ("review", "ingested", "rejected"):
        lines.append(f"| 文章 | {key} | {article_counts[key]} |\n")
    lines.extend(["\n## 待处理邮件\n\n", "| Gmail ID | 状态 | 主题 | 错误/原因 |\n| --- | --- | --- | --- |\n"])
    pending = [record for record in records if record["lifecycle"] in {"discovered", "failed", "review"}]
    if pending:
        for record in sorted(pending, key=lambda item: item["id"]):
            detail = record.get("last_error") or record.get("reason") or ""
            lines.append(f"| `{record['id']}` | {record['lifecycle']} | {record.get('subject', '').replace('|', '\\|')} | {detail.replace('|', '\\|')} |\n")
    else:
        lines.append("| - | - | 当前没有待处理邮件 | - |\n")
    lines.extend(["\n## 待审文章\n\n", "| 文章 ID | Gmail ID | 标题 | 文件 |\n| --- | --- | --- | --- |\n"])
    review_articles = [
        (record, article)
        for record in records
        for article in record.get("articles", [])
        if article.get("status") == "review"
    ]
    if review_articles:
        for record, article in review_articles:
            title = article["title"].replace("|", "\\|")
            lines.append(
                f"| `{article['id']}` | `{record['id']}` | {title} | "
                f"[`{article['file']}`](../{article['file']}) |\n"
            )
    else:
        lines.append("| - | - | 当前没有待审文章 | - |\n")
    lines.extend(["\n## 已拒绝文章\n\n", "| Gmail ID | 标题 | 原因 |\n| --- | --- | --- |\n"])
    rejected_articles = [
        (record, article)
        for record in records
        for article in record.get("articles", [])
        if article.get("status") == "rejected"
    ]
    if rejected_articles:
        for record, article in rejected_articles:
            title = article["title"].replace("|", "\\|")
            lines.append(f"| `{record['id']}` | {title} | `{article.get('reason') or 'unspecified'}` |\n")
    else:
        lines.append("| - | 当前没有已拒绝文章 | - |\n")
    lines.extend(["\n## 远程差异\n\n", "| Gmail ID | 本地状态 | 远程状态 |\n| --- | --- | --- |\n"])
    differences = [record for record in records if record.get("remote_starred") is False or record.get("remote_starred") is None]
    for record in sorted(differences, key=lambda item: item["id"]):
        remote_state = "未星标" if record.get("remote_starred") is False else "尚未核对"
        lines.append(f"| `{record['id']}` | {record['lifecycle']} | {remote_state} |\n")
    if not differences:
        lines.append("| - | - | 本地账本与最近一次远程清单一致 |\n")
    STATUS_PATH.write_text("".join(lines), encoding="utf-8")


def refresh_outputs(data: dict[str, Any]) -> None:
    save_manifest(data)
    rebuild_index(data)
    rebuild_status(data)


def print_summary(data: dict[str, Any]) -> None:
    lifecycle = Counter(record["lifecycle"] for record in data["emails"].values())
    articles = Counter(article["status"] for record in data["emails"].values() for article in record.get("articles", []))
    print(f"邮件总数: {len(data['emails'])}")
    print("邮件状态: " + ", ".join(f"{key}={lifecycle[key]}" for key in ("discovered", "failed", "review", "ingested", "ignored")))
    print("文章状态: " + ", ".join(f"{key}={articles[key]}" for key in ("review", "ingested", "rejected")))
    print(f"最近远程核对: {data.get('last_discovery_at') or '从未'}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Gmail 星标邮件文章同步与追踪 Pipeline")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("bootstrap", help="从现有文章和旧 ID 初始化/修复 manifest")
    subparsers.add_parser("discover", help="分页拉取远程星标清单并登记差异")
    subparsers.add_parser("fetch", help="下载并拆分 discovered/failed 邮件到待审目录")
    subparsers.add_parser("reconcile", help="Ingest 完成后，按 raw/articles 和 ingest_progress.json 对账")
    subparsers.add_parser("status", help="显示本地同步状态并刷新状态文档")
    subparsers.add_parser("index", help="按 manifest 和物理文件重建索引")
    reject = subparsers.add_parser("reject", help="明确拒绝一篇待审文章")
    reject.add_argument("article_id")
    reject.add_argument("--reason", default="manual_reject")
    subparsers.add_parser("run", help="先对账，再依次 discover、fetch，不绕过 Ingest SOP")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "bootstrap":
            data = bootstrap_manifest()
        else:
            data = load_manifest()
            if not MANIFEST_PATH.exists():
                raise PipelineError("尚未初始化，请先运行 `uv run starred-emails bootstrap`")

        if args.command == "discover":
            total, added = discover(data)
            print(f"远程星标邮件 {total} 封，新登记 {added} 封。")
        elif args.command == "fetch":
            processed, articles = fetch_pending(data)
            print(f"处理邮件 {processed} 封，生成待审文章 {articles} 篇。")
        elif args.command == "reconcile":
            reconciled = reconcile_ingested(data)
            print(f"对账完成，新确认已 Ingest 文章 {reconciled} 篇。")
        elif args.command == "reject":
            reject_article(data, args.article_id, args.reason)
            print(f"已拒绝 {args.article_id}。")
        elif args.command == "run":
            reconciled = reconcile_ingested(data)
            total, added = discover(data)
            processed, articles = fetch_pending(data)
            print(f"已对账 {reconciled} 篇；远程 {total} 封；新登记 {added} 封；处理 {processed} 封；待 Ingest {articles} 篇。")

        refresh_outputs(data)
        print_summary(data)
        return 0
    except (PipelineError, OSError, json.JSONDecodeError) as exc:
        print(f"错误: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
