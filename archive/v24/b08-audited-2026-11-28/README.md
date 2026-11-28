# V24 · Riemann Surfaces

ReadFlow R1 B-08 edition · Chapters 305–312 · 154 PDF pages · 2026-11-28

- [Reading PDF](V24-B08-ReadFlow-R1.pdf)
- [LaTeX source, dependencies, paired PDF, and review records](V24-B08-ReadFlow-R1-Source.zip)
- [SHA-256 checksums](SHA256SUMS)

The volume gives 66 worked examples and 108 exercises with complete solutions.
It starts with complex atlases and holomorphic maps, develops coverings and
analytic continuation, and proves Riemann–Roch through the Dolbeault operator.
The final chapter applies the theorem to principal parts, projective embeddings,
and compact curves. The eight chapters and their paired PDF passed independent
whole-volume mathematical review and all-page layout review.

## Verify and rebuild

Run `sha256sum -c SHA256SUMS` next to the downloads. Extract the source ZIP.
With Python 3.10 or later, XeLaTeX, the TeX Live dependencies, and fontconfig,
run the following commands from the extracted directory.

```sh
python3 verify_release.py
python3 verify.py
python3 tools/build.py --full --name release-rebuild
```

The rebuilt PDF appears at `.build/release-rebuild/build/entry.pdf`.
The source archive includes the exact reviewed PDF under `paired/`.
The manifest describes the public archive. Historical review records refer
to original evidence versions by checksum.
