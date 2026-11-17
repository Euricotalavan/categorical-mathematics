# ReadFlow R1 — adopted unified layout template

## Current decision

On 2026-11-17 the owner explicitly confirmed that the **ReadFlow R1 implementation actually used for V0 R1 is formally adopted as the unified layout template for subsequent volumes**. It is no longer an experiment, trial, or candidate template. This record changes template status only; it does not change any mathematical acceptance decision.

## Fixed, recoverable implementation

- Git artifact version: `8b9dc7f3749de81e47de9f525d7c5e0b3f8036c3`.
- Source: `archive/v0/readflow-r1-editorial-2026-11-17/V0-ReadFlow-R1-Source.zip`.
- Size: 7,007,679 bytes.
- SHA256: `5f91243f32d7e76d643575a76488d5b1e26d4909aa3017bd812cb526bf5ed732`.
- ZIP root: `V0-ReadFlow-R1/`.
- The complete implementation, companion files and build configuration are in this source ZIP. Do not substitute a research kit, an S2.1 sample, a prior Study template, or only one isolated style file.

Key implementation files (relative to ZIP root):

| File | SHA256 |
| --- | --- |
| `layout/shared/readflow-base.tex` | `cc9cc678504651f8f1baa196a714a70de1331684589d71b14353c77ec6f6f63b` |
| `layout/shared/style.tex` | `3156948196771ed4d21f9b9b47992053c576105cbce4b57d5d9496ecfd2b1626` |
| `layout/study/config.tex` | `fdccf765bbb70ff9f8b178a81af841d721cb4f962c9d90ddb476d5728e1c0424` |
| `layout/study/readflow-layout.tex` | `b04bf2f5bb7611b8a4899c9a582050681d36d71fba8b0c44a31f8d87d2924f69` |

Use the complete package's `MANIFEST.json`, build instructions, dependency requirements and accompanying QA. Volume-specific content, chapter numbering and metadata are not part of this adoption decision and must follow the authoritative volume handoff.

## Historical statements and unchanged limits

The fixed source ZIP intentionally retains its packaging-time wording, including “isolated whole-volume editorial trial”, “not an adopted common Study template” and “not ... pushed to GitHub”. These describe the earlier state. The template-status wording is superseded by this adoption record; the upload status is superseded by `VERIFICATION.md`. Do not rewrite the fixed ZIP or its hashes merely to update historical prose.

V0 remains a textbook editorial candidate awaiting independent strict mathematical whole-volume final review. Existing OPEN/UNKNOWN, source-literature coverage limitations and mathematical review requirements are unchanged. Adopting a template does not constitute mathematical correctness, full visual acceptance of future volumes, or cross-machine/paper/accessibility certification. No V1/V2 or other volume was revised or reapproved by this record.
