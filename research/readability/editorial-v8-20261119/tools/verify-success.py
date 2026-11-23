#!/usr/bin/env python3
"""Verify the published research package, not textbook quality or mathematical correctness."""
from pathlib import Path
import ast
import hashlib
import json
import re
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.duplicate_ids = []
        self.links = []
        self.images = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            if attrs["id"] in self.ids:
                self.duplicate_ids.append(attrs["id"])
            self.ids.add(attrs["id"])
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if tag == "img":
            assert attrs.get("alt"), "Image missing alt text"
            assert attrs.get("src", "").startswith("data:image/png;base64,"), "Image is not self-contained"
            self.images += 1


def check_relative(target, base):
    parsed = urlsplit(target)
    if parsed.scheme or target.startswith("#"):
        return
    assert (base / unquote(parsed.path)).exists(), f"Missing relative target: {target}"


def main():
    manifest = json.loads((ROOT / "SUCCESS-MANIFEST.json").read_text())
    for row in manifest["files"]:
        p = ROOT / row["path"]
        data = p.read_bytes()
        assert len(data) == row["bytes"], row["path"]
        assert hashlib.sha256(data).hexdigest() == row["sha256"], row["path"]
        if p.suffix == ".json":
            json.loads(data)
        if p.suffix == ".py":
            ast.parse(data.decode("utf-8"))
        if p.suffix in {".md", ".json", ".diff"}:
            text = data.decode("utf-8")
            assert not re.search(r"libfile_|file_0000|chatgpt\.com/api/library|/workspace/|/mnt/data/", text), p
        if p.suffix == ".md":
            for target in re.findall(r"\]\(([^)]+)\)", data.decode("utf-8")):
                check_relative(target, p.parent)
    html = Links()
    html.feed((ROOT / "SUCCESS-ANALYSIS.html").read_text())
    assert not html.duplicate_ids, html.duplicate_ids
    for target in html.links:
        if target.startswith("#"):
            assert unquote(target[1:]) in html.ids, target
        else:
            check_relative(target, ROOT)
    assert html.images == 4, html.images
    feedback = json.loads((ROOT / "evidence/success-feedback.json").read_text())
    assert feedback["subjective_page_quality_range"] == [85, 93]
    assert feedback["mean_score"] is None and feedback["per_page_rating_table"] is None
    pdf = json.loads((ROOT / "evidence/success-pdf-counts.json").read_text())
    assert pdf["accepted_page_element_exclusion"]["matches"] == 1663
    print(json.dumps({"files_verified": len(manifest["files"]), "html_images": html.images,
                      "local_links": "PASS", "json_python_syntax": "PASS",
                      "scope": "Published research file integrity only; not textbook mathematical or reading acceptance"}, indent=2))


if __name__ == "__main__":
    main()
