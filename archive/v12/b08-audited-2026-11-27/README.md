# V12 — Dependent Type Theory and Formalized Mathematics

ReadFlow R1 audited edition · Chapters 154–166 · 71 PDF pages · 2026-11-27

- [Reading PDF](V12-B08-ReadFlow-R1.pdf)
- [LaTeX, Lean, PDF, and build instructions](V12-B08-ReadFlow-R1.zip)
- [SHA-256 checksums](SHA256SUMS)

The public bundle preserves the audited LaTeX, formal Lean files, and paired PDF. It includes the 67-entry coverage map, verification programs, and an isolated diagnostic experiment.

## Rebuild

From the extracted bundle, run `python verify_sources.py` to verify the chapter and coverage locations. Use Lean 4.33.0 at commit `d8b18978322de05a8f3dba51ef03cf5461676c17` to run `python verify_lean.py` and `python checks/run_cross_check.py . <lean executable>`.

Take the fonts listed in `FONTS.sha256` from the [fixed ReadFlow R1 source package](https://github.com/Euricotalavan/categorical-mathematics/blob/8b9dc7f3749de81e47de9f525d7c5e0b3f8036c3/archive/v0/readflow-r1-editorial-2026-11-17/V0-ReadFlow-R1-Source.zip) and place them in `source/fonts/`. With XeLaTeX and the template packages available, run `python build_pdf.py` from the bundle directory. For a clean extraction, retain the auxiliary files and run one extra XeLaTeX pass on `V12-B07.tex` from `source/layout/study/` to stabilize the PDF page labels. Use the PDF created by that third pass.

The public source verifier pins the extracted public responsibility table. The edition's original chapter files, the Lean sources including §159.3, and the audited PDF retain their archived byte contents.
