# V18 · Functional Analysis and Bounded Operators

ReadFlow R1 B-08 edition · Chapters 232–245 · 258 PDF pages · 2026-11-27

- [Reading PDF](V18-B08-ReadFlow-R1.pdf)
- [LaTeX, dependencies, paired PDF, and review records](V18-B08-ReadFlow-R1-Source.zip)
- [SHA-256 checksums](SHA256SUMS)

The fixed volume passed independent whole-volume mathematical review. Its 110
sections contain 62 exercises with full solutions. The source archive includes
the final review, rebuild instructions, and 323 source-to-text locations.
Uninspected passages of the reference books are recorded as SOURCE-UNKNOWN.

## Rebuild

Extract the ZIP and run the following from the extracted directory.
The package includes the fonts. See `book/REBUILD.md` for XeLaTeX and platform
requirements.

```sh
python3 verify.py
cd book
python3 build.py --entry v18 --clean
```
