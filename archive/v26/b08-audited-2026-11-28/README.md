# V26 · Harmonic Functions and Classical Potential Theory

ReadFlow R1 B-08 edition · Chapters 325–332 · 196 PDF pages · 2026-11-28

- [Reading PDF](V26-B08-ReadFlow-R1.pdf)
- [LaTeX source, dependencies, paired PDF, and review records](V26-B08-ReadFlow-R1-Source.zip)
- [SHA-256 checksums](SHA256SUMS)

The volume contains 55 worked examples and 104 exercises with complete
solutions. It develops mean-value properties, subharmonic comparison,
Green functions, Perron's method, capacity, and boundary behavior, then
relates explicit potential methods to weak formulations of the Dirichlet
problem. This edition passed independent whole-volume mathematical review
and all-page layout review.

## Verify and rebuild

Run `sha256sum -c SHA256SUMS` next to both downloads. Extract the source ZIP
and run the following commands with Python 3.10 or later, XeLaTeX, TeX Live,
and fontconfig.

```sh
python3 verify.py
python3 tools/build.py --full --name release-rebuild
```

The rebuilt PDF is `.build/release-rebuild/volume26.pdf`. The exact reviewed
PDF is under `paired/`. The independent review is in
`evidence/B07/B07-Final-Audit.md`, and `evidence/B08/` contains the rebuild
verification. The source-coverage records state the scope of the proofs and
identify the original books whose full text could not be checked.
