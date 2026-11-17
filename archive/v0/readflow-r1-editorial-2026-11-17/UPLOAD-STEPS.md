# Completion steps — upload the missing binary assets

This file documents the single remaining Git transfer dependency. It is **not** a receipt of completed upload.

1. Obtain the three delivered, fixed **V0 ReadFlow R1** artifacts from the originating ChatGPT conversation (2026-11-17): `V0-ReadFlow-R1-Source.zip`, `V0-ReadFlow-R1.pdf`, `V0-ReadFlow-R1-Print.pdf`. Do not substitute the raw PDF copies inside the source ZIP; they have different hashes.
2. Check out this branch and put the three exact files beside this README:

```sh
git clone https://github.com/Euricotalavan/categorical-mathematics.git
cd categorical-mathematics
git fetch origin v0-readflow-r1-upload-20261117
git switch --track origin/v0-readflow-r1-upload-20261117
# Copy your 3 fixed artifacts to archive/v0/readflow-r1-editorial-2026-11-17/
python3 archive/v0/readflow-r1-editorial-2026-11-17/verify_release.py archive/v0/readflow-r1-editorial-2026-11-17
```

3. If and only if the script prints PASS (with PyMuPDF also available for PDF page/TOC checks), commit the exact files:

```sh
git add archive/v0/readflow-r1-editorial-2026-11-17/V0-ReadFlow-R1-Source.zip \
        archive/v0/readflow-r1-editorial-2026-11-17/V0-ReadFlow-R1.pdf \
        archive/v0/readflow-r1-editorial-2026-11-17/V0-ReadFlow-R1-Print.pdf
git commit -m "Publish V0 ReadFlow R1 editorial candidate (source and paired PDFs)"
git push origin v0-readflow-r1-upload-20261117
```

4. Re-fetch the remote branch; verify all three files exist remotely, compare byte SHA-256, and confirm repo still public. Only then fast-forward main (if main has moved, inspect and merge without force-push, preserving all existing history). The branch already prepares the root README pointer:

```sh
git switch main
git pull --ff-only origin main
git merge --ff-only v0-readflow-r1-upload-20261117
git push origin main
```

If the fast-forward fails, **stop** and reconcile the changed main instead of force pushing or rewriting historical archives.

5. Record the final main commit SHA. **Git current V0 editorial candidate** does not mean final mathematical publication; it still awaits the dedicated thickening final reviewer. Keep the 2026-11-13 V0 archive unchanged and all OPEN/UNKNOWN items visible.

Repository visibility: PUBLIC on 2026-11-17. The source package was checked to have no standalone font files, no other PDF textbook attachments and no obvious credential-pattern matches. Do not upload additional licensed source books or secrets.
