"""Daily Dose of DS 邮件解析器。"""

from __future__ import annotations

import base64
import copy
import email
import re
import urllib.parse
from email import policy
from email.utils import parsedate_to_datetime
from typing import Any

import html2text
from bs4 import BeautifulSoup


IGNORED_HEADINGS = [
    r"In today's newsletter", r"Together with", r"TODAY's Daily dose", r"ADVERTISE TO",
    r"SPONSOR US", r"THAT'S A WRAP", r"Today’s email was brought to you", r"Looking for more",
    r"In case you missed it", r"Update your profile", r"Unsubscribe",
]


def decode_tracking_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    host = parsed.netloc.casefold()
    if "convertkit" not in host and "kit-mail" not in host:
        return url
    encoded = parsed.path.strip("/").split("/")[-1]
    if len(encoded) <= 20:
        return url
    try:
        encoded += "=" * (-len(encoded) % 4)
        decoded = base64.urlsafe_b64decode(encoded).decode("utf-8", errors="ignore")
        return decoded if decoded.startswith("http") else url
    except (ValueError, UnicodeDecodeError):
        return url


def extract_html(raw_message: str) -> tuple[email.message.EmailMessage, BeautifulSoup]:
    padded = raw_message + "=" * (-len(raw_message) % 4)
    message = email.message_from_bytes(base64.urlsafe_b64decode(padded), policy=policy.default)
    html_body = ""
    plain_body = ""
    for part in message.walk() if message.is_multipart() else [message]:
        if "attachment" in str(part.get("Content-Disposition", "")):
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


def ignored_heading(heading: Any) -> bool:
    text = heading.get_text(" ", strip=True)
    if any(re.search(pattern, text, re.IGNORECASE) for pattern in IGNORED_HEADINGS):
        return True
    return any(
        urllib.parse.urlparse(anchor["href"]).path.rstrip("/").casefold() == "/membership"
        for anchor in heading.find_all("a", href=True)
    )


def parse(message_id: str, response: dict[str, Any]) -> tuple[dict[str, str], list[dict[str, str]]]:
    if "raw" not in response:
        raise ValueError("邮件响应缺少 raw 字段")
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
        if "open.convertkit-mail" in image["src"] or "pixel" in image["src"]:
            image.decompose()

    converter = html2text.HTML2Text()
    converter.body_width = 0
    converter.ignore_links = False
    converter.ignore_images = False
    converter.protect_links = True
    converter.unicode_snob = True

    headings = soup.find_all("h2")
    valid_headings = [heading for heading in headings if not ignored_heading(heading)]
    articles: list[dict[str, str]] = []
    if valid_headings:
        for position, heading in enumerate(valid_headings, 1):
            article_soup = BeautifulSoup("", "html.parser")
            article_soup.append(copy.copy(heading))
            node = heading.next_sibling
            while node and getattr(node, "name", None) != "h2":
                article_soup.append(copy.copy(node))
                node = node.next_sibling
            articles.append({
                "title": heading.get_text(" ", strip=True).replace("\u200b", ""),
                "body": re.sub(r"\n{3,}", "\n\n", converter.handle(str(article_soup))).replace("\u200b", ""),
                "part": str(position),
            })
    elif not headings:
        articles.append({
            "title": subject.replace("\u200b", ""),
            "body": re.sub(r"\n{3,}", "\n\n", converter.handle(str(soup))).replace("\u200b", ""),
            "part": "1",
        })
    return {"subject": subject, "sender": sender, "date": date, "formatted_date": formatted_date}, articles
