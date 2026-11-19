#!/usr/bin/env python3
"""Recheck fixed P2/v8 PDF identities and the 1,663 published body-page counts.

Requires PyMuPDF. Supply local directories each containing volume-0.pdf,
volume-1.pdf and volume-2.pdf. Does not download private historical files, edit
any PDF, run LaTeX or determine mathematical/reading acceptance.
"""
from pathlib import Path
import argparse
import csv
import hashlib
import json
import fitz

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--p2-dir", type=Path, required=True)
    parser.add_argument("--v8-dir", type=Path, required=True)
    args = parser.parse_args()
    identities = json.loads((ROOT / "input-pdfs.json").read_text())
    rows = list(csv.DictReader((ROOT / "page-density.csv").open()))
    docs = {}
    try:
        for version, directory in (("P2", args.p2_dir), ("v8", args.v8_dir)):
            for v in range(3):
                path = directory / f"volume-{v}.pdf"
                data = path.read_bytes()
                record = identities[f"{version}_V{v}"]
                assert hashlib.sha256(data).hexdigest() == record["sha256"], path
                doc = fitz.open(stream=data, filetype="pdf")
                assert len(doc) == record["all_pages"], path
                docs[(version, f"V{v}")] = doc
        mismatches = []
        for row in rows:
            p = docs[(row["version"], row["volume"] )][int(row["pdf_page"]) - 1]
            body = []
            for block in p.get_text("dict")["blocks"]:
                for line in block.get("lines", []):
                    text = "".join(span["text"] for span in line["spans"])
                    x0, y0, _, _ = line["bbox"]
                    if y0 < 55:
                        continue
                    if y0 > 690 and (" / ReadFlow " in text or
                                     (text.strip() == row["printed_page"] and x0 > 400)):
                        continue
                    body.append(text)
            count = sum(not c.isspace() for c in "".join(body))
            if count != int(row["chars"]):
                mismatches.append({"version": row["version"], "volume": row["volume"],
                                   "pdf_page": row["pdf_page"], "actual": count,
                                   "recorded": int(row["chars"])})
        print(json.dumps({"pymupdf": fitz.VersionBind, "pdf_identities": len(docs),
                          "body_pages": len(rows), "matches": len(rows) - len(mismatches),
                          "mismatches": mismatches,
                          "scope": "Character counts only; footer overlap can still exist"}, indent=2))
        if mismatches:
            raise SystemExit(1)
    finally:
        for doc in docs.values():
            doc.close()


if __name__ == "__main__":
    main()
