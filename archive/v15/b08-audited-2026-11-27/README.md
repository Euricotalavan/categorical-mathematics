# V15 — Multivariable Analysis

ReadFlow R1 audited edition · Chapters 195–207 · 65 sections · 209 PDF pages · 2026-11-27

- [Reading PDF](V15-B08-ReadFlow-R1.pdf)
- [LaTeX source, dependencies, PDF, and audit](V15-B08-ReadFlow-R1-Source.zip)
- [SHA-256 checksums](SHA256SUMS)

The volume develops multivariable differentiation, Riemann integration and change of variables, and Stokes’ theorem for manifolds with corners. It closes with the inverse and implicit function theorems in Banach spaces.

The independent B-07 review passed the revised source and this exact PDF after verifying all ten corrections. The source package contains the review and the locations of 529 core literature items. Five supporting items remain OPEN and 31 source entries remain UNKNOWN, including Shifrin’s full text.

## Rebuild

From the extracted bundle, run `python3 book/verify.py`. In `book/`, run `python3 build.py --entry volume --clean` with XeLaTeX. The bundle’s README gives the additional flag for an unindexed TeX Live installation and records the independent rebuild comparison.
