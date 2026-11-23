"""Emit traceable questions, never a readability score or automatic page edits.

Usage: python reading_diagnostics.py INPUT.pdf --map reading-map.json --out issues.json
The map is supplied by a content reviewer. PDF extraction cannot infer mathematical
obligations, exercise/solution roles, or whether a deliberate short page is justified.
"""
import argparse, hashlib, json, re, unicodedata
from pathlib import Path
import fitz

def normal(s):
    s=re.sub(r'-\s*\n\s*','',s)
    return re.sub(r'\W+','',unicodedata.normalize('NFKC',s)).lower()

def inspect(pdf, mapping):
    doc=fitz.open(pdf); sha=hashlib.sha256(Path(pdf).read_bytes()).hexdigest()
    pages=[];issues=[]
    for i,p in enumerate(doc,1):
        clip=fitz.Rect(45,65,p.rect.width-45,p.rect.height-55)
        text=p.get_text(clip=clip)
        pages.append({'page':i,'text':text,'norm':normal(text),'chars':sum(not c.isspace() for c in text)})
    def issue(rule,loc,detail,owner='行文排版',status='CANDIDATE'):
        issues.append({'id':f'D{len(issues)+1:03}','rule':rule,'status':status,'pdf_sha256':sha,'pages':loc,'evidence':detail,'responsible_role':owner,'required_review':'Read the complete mathematical unit and adjacent pages; no automatic edit or pass.'})
    if mapping.get('expected_sha256') and mapping['expected_sha256']!=sha:
        issue('SOURCE_IDENTITY',[],'PDF hash differs from the supplied reading map. Anchors below cannot authorize changes.','來源協調','BLOCKED')
        return {'pdf':str(pdf),'sha256':sha,'issues':issues,'status':'BLOCKED'}
    classes={int(k):v for k,v in mapping.get('page_roles',{}).items()}
    for p in pages:
        role=classes.get(p['page'],'UNKNOWN')
        first=' '.join(p['text'].splitlines()[:3])
        if re.search(r'\b(that index|this same|these maps|the preceding|such an|needs one)\b',first,re.I):
            issue('CONTINUATION_DEPENDENCY',[max(1,p['page']-1),p['page']],{'first_lines':first,'role':role,'question':'Can the referent and current proof goal be recovered without unnecessary search?'})
        if 0<p['chars']<500:
            if role in ['frontmatter','toc_tail','intentional_section_end','exercise_set_end']:
                continue
            issue('SHORT_PAGE_REVIEW',[p['page']],{'characters':p['chars'],'role':role,'question':'Is this a legitimate ending or a detached conclusion?'})
        # The threshold is a historic anomaly flag only, excluded for problem statements.
        if p['chars']>1750 and role!='exercise_statements':
            issue('DENSITY_REVIEW_ONLY',[p['page']],{'characters':p['chars'],'role':role,'question':'Classify prose/formula/diagram/problem regions before any decision. This is not a failure or a cap.'})
    for edge in mapping.get('edges',[]):
        endpoints=[]
        for anchor in [edge['from_anchor'],edge['to_anchor']]:
            ns=normal(anchor)
            hit=[p['page'] for p in pages if ns in p['norm']]
            endpoints.append(hit)
        if any(len(h)!=1 for h in endpoints):
            issue('ANCHOR_UNKNOWN',sorted(set(sum(endpoints,[]))),{'edge_id':edge['id'],'hits':endpoints,'anchors':[edge['from_anchor'],edge['to_anchor']]},'內容定位','UNKNOWN')
        elif endpoints[0][0]!=endpoints[1][0]:
            issue('CRITICAL_EDGE_CROSSES_PAGE',list(range(min(endpoints[0][0],endpoints[1][0]),max(endpoints[0][0],endpoints[1][0])+1)),{'edge_id':edge['id'],'kind':edge['kind'],'from_anchor':edge['from_anchor'],'to_anchor':edge['to_anchor'],'question':edge['review_question']})
    for unit in mapping.get('units',[]):
        hits=[]
        for anchor in [unit['start_anchor'],unit['end_anchor']]:
            hits.append([p['page'] for p in pages if normal(anchor) in p['norm']])
        if all(len(h)==1 for h in hits):
            span=[hits[0][0],hits[1][0]]
            if span[0]!=span[1] and not unit.get('crossing_permitted',True):
                issue('SHORT_UNIT_SPLIT',list(range(span[0],span[1]+1)),{'unit_id':unit['id'],'kind':unit['kind'],'question':'Does the split separate necessary conditions, data, or instructions? Verify actual PDF.'})
        else:issue('ANCHOR_UNKNOWN',sorted(set(sum(hits,[]))),{'unit_id':unit['id'],'hits':hits},'內容定位','UNKNOWN')
    return {'pdf':str(pdf),'sha256':sha,'pages':len(doc),'method':'Unicode-normalized anchor matching and page candidates. No overall score. No automatic repairs. Roles supplied, not inferred.','observed_page_roles':classes,'issues':issues,'human_reading_outcome':'NOT_MEASURED'}

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('pdf');a.add_argument('--map',required=True);a.add_argument('--out',required=True);x=a.parse_args()
    result=inspect(x.pdf,json.loads(Path(x.map).read_text()));Path(x.out).write_text(json.dumps(result,ensure_ascii=False,indent=2))
    print(json.dumps({'pages':result.get('pages'),'questions':len(result['issues']),'score':None}))
