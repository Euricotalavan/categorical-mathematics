# V20 · Unbounded Operators, Semigroups, and Evolution

ReadFlow R1 B-08 edition · Chapters 258–269 · 182 PDF pages · 2026-11-28

- [Reading PDF](V20-B08-ReadFlow-R1.pdf)
- [LaTeX, dependencies, paired PDF, and review records](V20-B08-ReadFlow-R1-Source.zip)
- [SHA-256 checksums](SHA256SUMS)

The 99 numbered sections include 55 worked examples and 82 exercises with
full solutions. The fixed edition passed independent whole-volume
mathematical review and page-by-page layout checks. The source archive
contains 254 literature responsibilities, their disposition and locations,
the remaining source limits, and the audit records. The public source
archive uses the reviewed manuscript and PDF verbatim. Two evidence
records omit working access links.

## Verify and rebuild

Run `sha256sum -c SHA256SUMS` next to the downloads. Extract the source ZIP
into a separate directory. From that directory, on a system with XeLaTeX
and fontconfig, run:

```sh
python3 verify.py
python3 roles/layout_final/build.py --full --front frontmatter.tex --back bibliography.tex --preamble v20-layout-preamble.tex --name rebuild
```

The new PDF is at `roles/layout_final/runs/rebuild/build/entry.pdf`.
