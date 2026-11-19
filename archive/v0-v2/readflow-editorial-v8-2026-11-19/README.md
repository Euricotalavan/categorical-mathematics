# V0–V2 · ReadFlow editorial candidate v8

2026-11-19. This is the three-volume edition after chapter-by-chapter editorial revision, using the adopted ReadFlow R1 template at 10.4 pt type and 16 pt baseline spacing. The volumes retain continuous Chapters 0–51. Independent mathematical final review and inherited open items are pending.

| Volume | Chapters | Pages | Reading PDF | Print PDF |
| --- | ---: | ---: | --- | --- |
| V0 · Language and given constructions | 0–9 | 481 | [Download](reading/volume-0.pdf) | [Download](print/volume-0.pdf) |
| V1 · Conditional categorical foundations | 10–28 | 174 | [Download](reading/volume-1.pdf) | [Download](print/volume-1.pdf) |
| V2 · Arithmetic and number systems | 29–51 | 231 | [Download](reading/volume-2.pdf) | [Download](print/volume-2.pdf) |

Download the three files for a given edition into the same folder and keep their original filenames. Volume 1 links to Volume 0, and Volume 2 links to Volume 1. The three reading PDFs are also included in the [buildable source ZIP](V0-V2-ReadFlow-Editorial-v8-Source.zip).

The public source ZIP preserves the delivered LaTeX sources, build scripts, and reading PDFs byte-for-byte. Its README and manifest describe the public package, which contains the files needed to build and read the books. See [file manifest](MANIFEST.json) and [SHA-256 checksums](SHA256SUMS) for the source ZIP and all six PDFs. The earlier archives remain available under [V0](../../v0/), [V1](../../v1/), and [V2](../../v2/).

To rebuild, extract the ZIP. Install Python 3, XeLaTeX, the ReadFlow R1 TeX dependencies, and the fonts named in the ZIP's README. From the extracted directory, run:

```sh
python verify.py
python build-edition.py --entry volume
python build-edition.py --entry print
```

The build processes V0, V1, and V2 in order and refreshes the cross-volume reference indexes. It saves each linked set in `rebuilt-reading/` or `rebuilt-print/`.

The editorial work includes reuse of established notation and universal properties, line breaks that expose the structure of formulas, and local repairs to awkward proof and exercise continuations. The inherited mathematical prerequisites and literature coverage questions remain open. V2 also has its Stage 6 refinement pending. See the [editorial retrospective and P2 comparison](https://github.com/Euricotalavan/categorical-mathematics/blob/research/readability-methodology-20261117/research/readability/editorial-v8-20261119/README.md).
