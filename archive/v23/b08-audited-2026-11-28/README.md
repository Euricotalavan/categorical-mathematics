# V23 · Complex Analysis

ReadFlow R1 B-08 edition · Chapters 291–304 · 262 PDF pages · 2026-11-28

- [Reading PDF](V23-B08-ReadFlow-R1.pdf)
- [LaTeX, dependencies, paired PDF, and review records](V23-B08-ReadFlow-R1-Source.zip)
- [SHA-256 checksums](SHA256SUMS)

The volume contains 119 numbered sections, 110 worked examples, and 136 exercises
with full solutions. It develops holomorphic functions and contour integration
through conformal mapping, entire and meromorphic functions, the Nevanlinna first
main theorem, and the Picard theorems. The fixed source and PDF passed independent
whole-volume mathematical review and all-page layout review.

## Verify and rebuild

Run `sha256sum -c SHA256SUMS` next to the downloads. Extract the source ZIP and
run the following commands from the extracted directory with Python 3.10 or
newer, XeLaTeX, and fontconfig installed.

```sh
python3 verify_release.py
python3 verify.py
python3 tools/build.py --full --preamble layout/v23-breaks.tex --name release-rebuild
```

The rebuilt PDF appears at `.build/release-rebuild/build/entry.pdf`. Source
coverage and the final review are recorded in `review/B01/` and `review/B07/`.
