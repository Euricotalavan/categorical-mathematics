from pathlib import Path
import hashlib, json, re
here=Path(__file__).resolve().parent
root=here.parents[2]
manifest=json.loads((here/'MANIFEST.json').read_text())
errors=[]
for r in manifest['files']:
 p=root/r['path']
 if not p.is_file():errors.append('missing '+r['path']);continue
 data=p.read_bytes()
 if len(data)!=r['bytes'] or hashlib.sha256(data).hexdigest()!=r['sha256']:errors.append('identity '+r['path'])
 if re.search(rb'libfile_[A-Za-z0-9_-]{20,}|file_000[0-9a-f]{20,}|/workspace/(?:scratch|projects)/|https://chatgpt\.com/(?:library[?]|c/|share/)|ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}',data):errors.append('private locator '+r['path'])
print(json.dumps({'checked':len(manifest['files']),'errors':errors,'scope':'public artifact identity and private-locator regression; not mathematical or human-reading validation'},ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
