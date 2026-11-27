# V17 · Series, Improper Integrals, and Topics in Real Analysis

ReadFlow R1 B-08 edition · Chapters 224–231 · 92 PDF pages · 2026-11-27

- [Reading PDF](V17-B08-ReadFlow-R1.pdf)
- [LaTeX, dependencies, paired PDF, and review records](V17-B08-ReadFlow-R1-Source.zip)
- [SHA-256 checksums](SHA256SUMS)

The volume passed independent whole-volume mathematical review. Its 37 sections
contain 24 exercises with full solutions. On recheck, the auditor verified the
repaired complex unit-disk arguments in Chapters 225–226 and the finite-sum
definition for several improper endpoints in Chapter 228.

The ZIP contains the auditor's verdict, the current literature coverage table,
the layout checks, and the open source and scope limitations. The published
bundle omits links to private checkpoints and retains the approved manuscript,
dependencies, and paired PDF.

## Rebuild

Extract the ZIP and run the following commands from the extracted directory.
The build uses XeLaTeX and the bundled fonts. The package README lists the
required tools.

```sh
python3 verify.py
python3 book/build-v17.py --book-root book --output-dir rebuilt --source-date-epoch 1795737600
```
