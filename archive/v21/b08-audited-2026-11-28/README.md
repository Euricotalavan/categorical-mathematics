# V21 · Fourier Analysis and Integral Transforms

ReadFlow R1 B-08 edition · Chapters 270–281 · 301 PDF pages · 2026-11-28

- [Reading PDF](V21-B08-ReadFlow-R1.pdf)
- [LaTeX, dependencies, paired PDF, and review records](V21-B08-ReadFlow-R1-Source.zip)
- [SHA-256 checksums](SHA256SUMS)

The 90 numbered sections include 101 worked examples and 119 exercises with
full solutions. The fixed source and PDF passed independent whole-volume
mathematical review and layout checks. The source archive includes the
179-entry literature responsibility table and records the remaining
limits of original-source verification.

## Verify and rebuild

Run `sha256sum -c SHA256SUMS` next to the downloads. Extract the source ZIP.
From its `V21-ReadFlow-R1` directory, on a system with XeLaTeX and fontconfig, run

```sh
python3 verify.py
python3 tools/build.py --full --preamble notation.tex --front frontmatter.tex --back bibliography.tex --name rebuild
```

The rebuilt PDF is at `tools/runs/rebuild/build/entry.pdf`.
