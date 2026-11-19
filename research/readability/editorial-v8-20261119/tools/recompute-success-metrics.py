#!/usr/bin/env python3
"""Recompute descriptive v8 statistics from the fixed public CSV evidence.

This checks the published tables, not the underlying PDF extraction. It is not a
readability score, a mathematical audit, or a causal estimate of reader benefit.
"""
from __future__ import annotations

import csv
import argparse
import hashlib
import io
import json
import math
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPOSITORY = "Euricotalavan/categorical-mathematics"
RESEARCH_COMMIT = "287d217676ab8119a29bdd83367c33545e5dff3d"
BOOK_COMMIT = "60fe8d1910c06c309958edb9efcd20d63cbb08ac"
BASE = f"https://raw.githubusercontent.com/{REPOSITORY}/{RESEARCH_COMMIT}/research/readability/editorial-v8-20261119"
NAMES = ["README.md", "page-density.csv", "chapter-density.csv", "input-pdfs.json"]
EXPECTED_SHA256 = {
    "README.md": "83d6c1dbcbb3022299e94f8489813203ebba438d9243b3ee19fb15588582f30f",
    "page-density.csv": "2ccd592adad95a8104cea3100bb9b4769c1de427d5fabdf57f4f44deecb1a40d",
    "chapter-density.csv": "83feb1e994dd57737444892fdb85d03c99dddb24f857a4124784a111316a851b",
    "input-pdfs.json": "3c58bcfd118f38c91d2fca64cd77f34ae3b20bedb7f3b977549ab92c54d73315",
}


def quantile_linear(values, probability):
    values = sorted(values)
    index = (len(values) - 1) * probability
    lo, hi = math.floor(index), math.ceil(index)
    return values[lo] + (values[hi] - values[lo]) * (index - lo)


def stats(rows):
    chars = [r["chars"] for r in rows]
    return {
        "body_pages": len(rows),
        "chars": sum(chars),
        "chars_per_page": sum(chars) / len(rows),
        "p90_linear": quantile_linear(chars, .9),
        "strictly_over_1750": sum(c > 1750 for c in chars),
        "strictly_over_p2_p90_1841_2": sum(c > 1841.2 for c in chars),
        "max_chars": max(chars),
        "min_chars": min(chars),
        "text_letters_font_estimate": sum(r["text_letters"] for r in rows),
        "math_chars_font_estimate": sum(r["math_chars"] for r in rows),
    }


def pct(before, after):
    return 100 * (after / before - 1)


def main():
    global ROOT
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True, help="Isolated output directory; do not overwrite published evidence")
    args = parser.parse_args()
    ROOT = args.output_dir.resolve()
    ROOT.mkdir(parents=True, exist_ok=True)
    published = Path(__file__).resolve().parents[1] / "evidence"
    if ROOT == published.resolve():
        raise SystemExit("Use a separate scratch output directory, not the published evidence directory")
    sources = []
    strings = {}
    input_dir = ROOT / "inputs"
    input_dir.mkdir(exist_ok=True)
    for name in NAMES:
        path = input_dir / name
        if not path.exists():
            with urllib.request.urlopen(f"{BASE}/{name}", timeout=40) as response:
                path.write_bytes(response.read())
        data = path.read_bytes()
        actual_sha = hashlib.sha256(data).hexdigest()
        assert actual_sha == EXPECTED_SHA256[name], (name, actual_sha)
        strings[name] = data.decode("utf-8")
        sources.append({
            "path": f"research/readability/editorial-v8-20261119/{name}",
            "commit": RESEARCH_COMMIT,
            "url": f"https://github.com/{REPOSITORY}/blob/{RESEARCH_COMMIT}/research/readability/editorial-v8-20261119/{name}",
            "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
            "git_blob_sha1": hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest(),
        })
    rows = list(csv.DictReader(io.StringIO(strings["page-density.csv"])))
    for r in rows:
        for key in ("chapter", "pdf_page", "printed_page", "chapter_page", "chars", "text_letters", "math_chars"):
            r[key] = int(r[key])
        assert r["last_in_chapter"] in ("True", "False")
        r["last_in_chapter"] = r["last_in_chapter"] == "True"
    assert len({(r["version"], r["volume"], r["pdf_page"]) for r in rows}) == len(rows)
    by_version = {v: [r for r in rows if r["version"] == v] for v in ("P2", "v8")}
    totals = {v: stats(rr) for v, rr in by_version.items()}
    volumes = {volume: {v: stats([r for r in rr if r["volume"] == volume])
                       for v, rr in by_version.items()} for volume in ("V0", "V1", "V2")}
    nonfinal = {v: stats([r for r in rr if not r["last_in_chapter"]])
                for v, rr in by_version.items()}
    chapters = []
    chapter_input = list(csv.DictReader(io.StringIO(strings["chapter-density.csv"])))
    for old in chapter_input:
        ch = int(old["chapter"])
        volume = "V0" if ch <= 9 else "V1" if ch <= 28 else "V2"
        p = [r for r in by_version["P2"] if r["chapter"] == ch]
        n = [r for r in by_version["v8"] if r["chapter"] == ch]
        for rr, prefix in ((p, "p2"), (n, "v8")):
            assert len({r["volume"] for r in rr}) == 1
            assert [r["pdf_page"] for r in rr] == list(range(int(old[f"{prefix}_pdf_first"]), int(old[f"{prefix}_pdf_last"]) + 1))
            assert sum(r["last_in_chapter"] for r in rr) == 1 and rr[-1]["last_in_chapter"]
            assert [r["chapter_page"] for r in rr] == list(range(1, len(rr) + 1))
            s = stats(rr)
            assert s["chars"] == int(old[f"{prefix}_chars"])
            assert abs(s["chars_per_page"] - float(old[f"{prefix}_chars_per_page"])) < 1e-6
        ps, ns = stats(p), stats(n)
        delta = pct(ps["chars_per_page"], ns["chars_per_page"])
        char_delta = pct(ps["chars"], ns["chars"])
        assert abs(delta - float(old["mean_delta_pct"])) < 1e-6
        assert abs(char_delta - float(old["total_delta_pct"])) < 1e-6
        chapters.append({"chapter": ch, "volume": volume, "title": old["title"],
                         "P2": ps, "v8": ns, "density_delta_pct": delta,
                         "chars_delta_pct": char_delta, "same_page_count": len(p) == len(n)})
    assert [c["chapter"] for c in chapters] == list(range(52))
    input_pdfs = json.loads(strings["input-pdfs.json"])
    for version, rr in by_version.items():
        for vol in volumes:
            entries = [r for r in rr if r["volume"] == vol]
            recorded = input_pdfs[f"{version}_{vol}"]
            assert min(r["pdf_page"] for r in entries) == recorded["chapter_first"]
            assert max(r["pdf_page"] for r in entries) == recorded["chapter_end"]
            assert len(entries) == recorded["chapter_end"] - recorded["chapter_first"] + 1
    p, n = totals["P2"], totals["v8"]
    original_mean = p["chars_per_page"]
    text_first_mean = n["chars"] / p["body_pages"]
    pages_first_mean = p["chars"] / n["body_pages"]
    total_delta = pct(original_mean, n["chars_per_page"])
    result = {
        "status": "independent CSV recomputation; not PDF re-extraction, reader test, or mathematical acceptance",
        "research_commit": RESEARCH_COMMIT, "book_commit": BOOK_COMMIT,
        "sources": sources, "page_rows": len(rows), "chapter_rows": len(chapters),
        "totals": totals, "volumes": volumes, "excluding_each_chapter_last_page": nonfinal,
        "changes": {
            "density_delta_pct": total_delta, "chars_delta_pct": pct(p["chars"], n["chars"]),
            "body_pages_delta_pct": pct(p["body_pages"], n["body_pages"]),
            "p90_delta_pct": pct(p["p90_linear"], n["p90_linear"]),
            "nonfinal_density_delta_pct": pct(nonfinal["P2"]["chars_per_page"], nonfinal["v8"]["chars_per_page"]),
            "text_letters_delta_pct": pct(p["text_letters_font_estimate"], n["text_letters_font_estimate"]),
            "math_chars_delta_pct": pct(p["math_chars_font_estimate"], n["math_chars_font_estimate"]),
        },
        "density_arithmetic_decomposition": {
            "warning": "Order-dependent arithmetic decomposition of characters/pages, not causal effects on subjective reading.",
            "text_first": {
                "text_contribution_percentage_points": 100 * (text_first_mean - original_mean) / original_mean,
                "pages_contribution_percentage_points": 100 * (n["chars_per_page"] - text_first_mean) / original_mean,
            },
            "pages_first": {
                "pages_contribution_percentage_points": 100 * (pages_first_mean - original_mean) / original_mean,
                "text_contribution_percentage_points": 100 * (n["chars_per_page"] - pages_first_mean) / original_mean,
            },
        },
        "chapter_counts": {
            "density_decreased": sum(c["density_delta_pct"] < 0 for c in chapters),
            "density_increased": sum(c["density_delta_pct"] > 0 for c in chapters),
            "chars_decreased": sum(c["chars_delta_pct"] < 0 for c in chapters),
            "chars_increased": sum(c["chars_delta_pct"] > 0 for c in chapters),
            "same_page_count": sum(c["same_page_count"] for c in chapters),
        },
        "same_page_count_chapters": [c["chapter"] for c in chapters if c["same_page_count"]],
        "density_increased_chapters": [c["chapter"] for c in chapters if c["density_delta_pct"] > 0],
        "chapters": chapters,
        "scope_limits": [
            "Body pages contain narrative, formulas, exercises and solutions; no page-type labels are provided.",
            "P2 body-only >1750 count is 152/809; earlier all-PDF count 164/841 has a different denominator.",
            "The user's 85–93 range has no supplied page-by-page scores, mean, sample size or measured comprehension/retention.",
            "P2 is a comparison edition, not the documented direct parent of v8 edits; editing continued from editorial v4.",
            "PDF inputs' SHA256 values are read from the fixed manifest; this script does not download or hash those PDFs.",
            "The source CSV's font labels estimate character composition; they do not certify mathematical completeness.",
        ],
    }
    (ROOT / "metrics.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("page_rows", "chapter_rows", "totals", "changes", "chapter_counts", "same_page_count_chapters", "density_increased_chapters", "density_arithmetic_decomposition")}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
