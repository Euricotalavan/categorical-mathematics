#!/usr/bin/env python3
"""Validate the exact V0 ReadFlow R1 release assets before a Git promotion.

Checks three delivered binary byte-identities, ZIP CRC, the absence of bundled
standalone font files, and basic PDF navigation/page counts if PyMuPDF is
available. This does NOT mathematically review the book.
"""
import hashlib
import pathlib
import sys
import zipfile

FILES = {
    "V0-ReadFlow-R1-Source.zip": ("5f91243f32d7e76d643575a76488d5b1e26d4909aa3017bd812cb526bf5ed732", 7007679),
    "V0-ReadFlow-R1.pdf": ("b3a3b02c92ad060476aadfffa88b18a079a8e7ffc667334f645878aae06b7edb", 2424427),
    "V0-ReadFlow-R1-Print.pdf": ("71fffbbfcfa12c63c981ffefcf8a26365c2e14aed11d28a0c77b202b7298115e", 2316055),
}

def main(folder):
    root = pathlib.Path(folder)
    failed = False
    for name, (expected_hash, expected_bytes) in FILES.items():
        path = root / name
        if not path.is_file():
            print(f"MISSING: {name}")
            failed = True
            continue
        data = path.read_bytes()
        actual_hash = hashlib.sha256(data).hexdigest()
        if actual_hash != expected_hash or len(data) != expected_bytes:
            print(f"MISMATCH: {name}, bytes={len(data)}, SHA256={actual_hash}")
            failed = True
        else:
            print(f"OK hash: {name}")
    zip_path = root / "V0-ReadFlow-R1-Source.zip"
    if zip_path.is_file():
        try:
            with zipfile.ZipFile(zip_path) as archive:
                names = archive.namelist()
                bad = archive.testzip()
                font_files = [n for n in names if n.lower().endswith((".otf", ".ttf", ".woff", ".woff2"))]
                if bad or font_files or len(names) != 914:
                    print(f"BAD ZIP: first_crc_bad={bad}; font_files={font_files}; members={len(names)}")
                    failed = True
                else:
                    print("OK ZIP: 914 members, CRC pass, no standalone font files")
        except Exception as exc:
            print(f"BAD ZIP: {exc}")
            failed = True
    try:
        import fitz
    except ImportError:
        print("PDF document checks skipped (install PyMuPDF to enable)")
    else:
        for name in ("V0-ReadFlow-R1.pdf", "V0-ReadFlow-R1-Print.pdf"):
            path = root / name
            if path.is_file():
                with fitz.open(path) as doc:
                    if len(doc) != 464 or len(doc.get_toc()) != 291:
                        print(f"BAD PDF: {name}, pages={len(doc)}, toc={len(doc.get_toc())}")
                        failed = True
                    else:
                        print(f"OK PDF: {name}, 464 pages, 291 TOC entries")
    print("PASS — release byte identities and basic structure" if not failed else "FAIL — DO NOT PROMOTE")
    return int(failed)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
