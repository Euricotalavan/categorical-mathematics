# V19 · Locally Convex Spaces, Distributions, and Integral Equations

ReadFlow R1 B-08 edition · Chapters 246–257 · 280 PDF pages · 2026-11-28

- [Reading PDF](V19-B08-ReadFlow-R1.pdf)
- [LaTeX, dependencies, paired PDF, and review records](V19-B08-ReadFlow-R1-Source.zip)
- [SHA-256 checksums](SHA256SUMS)

The 122 numbered sections include 74 exercises with full solutions. The
fixed edition passed independent whole-volume mathematical review and
page-by-page layout checks. The source archive records 453 literature
responsibilities, their locations and scope, and unresolved source details.

## Verify and rebuild

Check the downloads with `sha256sum -c SHA256SUMS`. Extract the source ZIP
into a separate directory. The archive contains its own README,
`verify_archive.py`, and the required fonts. Run the following from that
extracted directory with XeLaTeX installed.

```sh
python3 book/verify.py
python3 assemble_coverage.py
python3 book/build.py --entry v19 --clean
```
