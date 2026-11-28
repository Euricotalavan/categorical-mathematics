# V25 · Several Complex Variables

ReadFlow R1 B-08 edition · Chapters 313–324 · 212 PDF pages · 2026-11-28

- [Reading PDF](V25-B08-ReadFlow-R1.pdf)
- [LaTeX source, dependencies, paired PDF, and review records](V25-B08-ReadFlow-R1-Source.zip)
- [SHA-256 checksums](SHA256SUMS)

This volume contains 92 worked examples and 131 exercises with complete solutions.
It develops Hartogs extension, integral formulas, pseudoconvexity, and a weighted
solution of the d-bar equation. It uses these tools to prove approximation and
the sufficient direction of the Levi problem, then treats Bergman kernels,
Weierstrass preparation, and local examples of analytic sets and spaces.
The fixed edition passed independent whole-volume mathematical review and
all-page layout review.

## Verify and rebuild

Run `sha256sum -c SHA256SUMS` next to both downloads. Extract the source ZIP and
run these commands from the extracted directory with Python 3.10 or later,
XeLaTeX, TeX Live, and fontconfig.

```sh
python3 verify.py
python3 tools/build.py --full --name release-rebuild
```

The rebuilt PDF is `.build/release-rebuild/volume25.pdf`. The exact reviewed PDF
is under `paired/`. See `evidence/B07/B07-Final-Audit.md` for the terminal review
and `evidence/B08/` for the archive record and rebuild comparison. The public
source bundle keeps the approved bibliography. Its preflight notes were edited
for publication.
