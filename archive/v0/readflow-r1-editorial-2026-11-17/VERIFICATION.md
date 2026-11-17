# V0 ReadFlow R1 Git transfer verification

Date: 2026-11-17 UTC.

Artifact commit: `48df0b80b9b6dde4f2213ee8c275c1e7f9c00cd7`.
Previous staging head: `810ccbdded2e814fb43c938273ae60e9a88e5f13`.
Unchanged old main/baseline: `2fd60dfecd1eb970e6b62a6fbea66e3bb05fa7ae`.

The three artifacts were retrieved from their Library delivery identities,
matched against SHA256SUMS.expected, uploaded without byte changes, and then
retrieved again through a fresh Git clone of the remote upload branch.
The fresh clone passed verify_release.py with PyMuPDF available:

- Source ZIP: 7,007,679 bytes, expected SHA256 matched; 914 members, CRC pass.
- Reading PDF: 2,424,427 bytes, expected SHA256 matched; 464 pages, 291 TOC entries.
- Print PDF: 2,316,055 bytes, expected SHA256 matched; 464 pages, 291 TOC entries.
- All 913 listed source package manifest entries matched their individual hashes.
- All 668 frozen mathematical body/diagram assets matched their fixed hashes and the original source ZIP in the old Git archive (ZIP SHA256 `0a0d81675a5c494c14480136321fe53bb9a74e985c7b6b19f9cbd84c25680dfe`).
- ZIP inventory contains only the two generated book PDFs, no standalone font files or other textbook PDF attachments. Basic credential-pattern screening found no matches; this is not an exhaustive security audit.
- Repository visibility was verified PUBLIC. No unrelated Library files were uploaded.

The ZIP contains original compiler PDFs whose hashes differ from the delivered
PDFs due to documented host-side repackaging. Those original identities are
preserved; no file was silently substituted.

Promotion changes only the current V0 editorial-candidate pointer. The old
2026-11-13 V0 archive and all V1/V2 archives are retained unchanged. Chapter 0–9,
existing mathematical content, OPEN/UNKNOWN, and pending independent strict
mathematical whole-volume review are not changed or cleared.

This verifies artifact transfer, integrity and basic PDF structure. It does NOT
claim a fresh TeX build, full visual inspection, mathematical final acceptance,
source-literature completeness, or successful reader-learning evaluation.
