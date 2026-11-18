"""Verify this fixed public research snapshot; no math or readability verdict."""
from pathlib import Path
import ast,hashlib,json,re
here=Path(__file__).resolve().parent
manifest=json.loads((here/'MANIFEST.json').read_text())
errors=[]
private=re.compile(r'libfile_[A-Za-z0-9_-]+|file_000[0-9a-f]+|'+r'account'+'_id=personal|/work'+'space/|chatgpt\\.com/(?:library|c/|share/)|ldc1\\.[A-Za-z0-9_-]+')
for item in manifest['files']:
 p=here/item['path']
 if not p.is_file():errors.append('missing '+item['path']);continue
 b=p.read_bytes();s=b.decode('utf-8')
 if len(b)!=item['bytes'] or hashlib.sha256(b).hexdigest()!=item['sha256']:errors.append('identity '+item['path'])
 if private.search(s):errors.append('private locator '+item['path'])
 if p.suffix=='.json':json.loads(s)
 if p.suffix=='.py':ast.parse(s)
 if p.suffix=='.md':
  for target in re.findall(r'\]\(([^\s)]+)\)',s):
   if target.startswith(('http://','https://','#','mailto:')):continue
   if not (p.parent/target.split('#')[0]).resolve().exists():errors.append('link '+item['path']+' -> '+target)
  if re.search(r'\[\[(?:FIG:|SEMANTIC_CASES)',s):errors.append('placeholder '+item['path'])
print(json.dumps({'checked_files':len(manifest['files']),'errors':errors,'scope':'Public source identity, syntax, relative links and private-locator regression only; no mathematical or human-reading acceptance'},ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
