# V22 · Approximation, Sampling, and Reconstruction

ReadFlow R1 B-08 edition · Chapters 282–290 · 201 PDF pages · 2026-11-28

- [Reading PDF](V22-B08-ReadFlow-R1.pdf)
- [LaTeX, dependencies, paired PDF, and review records](V22-B08-ReadFlow-R1-Source.zip)
- [SHA-256 checksums](SHA256SUMS)

The volume contains 67 numbered sections, 70 worked examples, and 87 exercises
with full solutions. It moves from polynomial, rational, and spline approximation
through best-error spaces to sampling, reconstruction, and numerical stability.
The fixed source and PDF passed independent whole-volume mathematical review and
layout checks.

## Verify and rebuild

Run `sha256sum -c SHA256SUMS` next to the downloads. Extract the source ZIP,
then run these commands from the extracted directory with Python 3.10 or newer,
XeLaTeX, and fontconfig installed.

```sh
python3 verify.py
python3 layout-prep/tools/build.py --full \
  --front "$(pwd)/frontmatter.tex" \
  --back "$(pwd)/bibliography.tex" \
  --name rebuild
```

Build output is under `layout-prep/tools/runs/rebuild/`. Source locations and
reference versions are recorded under `review/B01/`.
