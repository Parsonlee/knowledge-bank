import base64
import json
import tempfile
import unittest
from pathlib import Path

from dailydose_pipeline import (
    article_filename,
    bootstrap_manifest,
    list_starred_messages,
    parse_message,
)


class PipelineTest(unittest.TestCase):
    def test_remote_list_follows_all_pages(self):
        calls = []

        def fake_call(args):
            params = json.loads(args[args.index("--params") + 1])
            calls.append(params)
            if "pageToken" not in params:
                return {"messages": [{"id": "a"}], "nextPageToken": "next"}
            return {"messages": [{"id": "b"}]}

        self.assertEqual([item["id"] for item in list_starred_messages(fake_call)], ["a", "b"])
        self.assertEqual(calls[1]["pageToken"], "next")

    def test_multiple_articles_use_id_only_in_filename(self):
        self.assertEqual(article_filename("2026-08-10", "First article", "abcdef123456"), "2026-08-10_First-article_abcdef.md")
        self.assertNotIn("part", article_filename("2026-08-10", "Second", "abcdef123456"))

    def test_parse_message_splits_h2_articles(self):
        membership = base64.urlsafe_b64encode(b"https://www.dailydoseofds.com/membership").decode().rstrip("=")
        raw = (
            "Subject: Weekly\nFrom: sender@example.com\nDate: Mon, 10 Aug 2026 10:00:00 +0000\n"
            "MIME-Version: 1.0\nContent-Type: text/html; charset=utf-8\n\n"
            "<html><body><h2>First</h2><p>A</p><h2>Second</h2><p>B</p>"
            f'<h2><a href="https://click.kit-mail3.com/x/{membership}">Succeed in AI Engineering roles</a></h2>'
            "<p>Master full-stack AI engineering</p></body></html>"
        ).encode()
        response = {"raw": base64.urlsafe_b64encode(raw).decode().rstrip("=")}
        metadata, articles = parse_message("abcdef123456", response)
        self.assertEqual(metadata["formatted_date"], "2026-08-10")
        self.assertEqual([item["title"] for item in articles], ["First", "Second"])

    def test_bootstrap_reads_ingested_history_idempotently(self):
        with tempfile.TemporaryDirectory() as temporary:
            archive = Path(temporary) / "archive"
            archive.mkdir()
            article = archive / "2026-08-10_Title_abcdef_part2.md"
            article.write_text("# Title\n\n- **ID**: abcdef123456\n", encoding="utf-8")
            manifest = archive / "manifest.json"
            progress = archive / "ingest_progress.json"
            progress.write_text(json.dumps({article.name: True}), encoding="utf-8")
            bootstrap_manifest(archive, manifest, progress, include_legacy=False)
            data = bootstrap_manifest(archive, manifest, progress, include_legacy=False)
            self.assertEqual(len(data["emails"]["abcdef123456"]["articles"]), 1)


if __name__ == "__main__":
    unittest.main()
