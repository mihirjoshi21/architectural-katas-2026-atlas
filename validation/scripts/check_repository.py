#!/usr/bin/env python3
"""Offline structural checks for this documentation repository, not a Markdown renderer."""
from pathlib import Path
import json,re,struct,sys,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[2]
errors=[];links=0
for p in sorted(R.rglob('*.md')):
 text=p.read_text();fences=re.findall(r'^\s*```',text,re.M)
 if len(fences)%2:errors.append(f'{p.relative_to(R)}: unmatched code fence')
 # Strip fenced examples before checking ordinary inline file/image links.
 prose=re.sub(r'```.*?```','',text,flags=re.S)
 for dest in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',prose):
  dest=dest.split(' "',1)[0].strip('<>')
  if re.match(r'^[a-zA-Z][\w+.-]*:',dest):continue
  if dest.startswith('#'):
   headings=re.findall(r'^#{1,6}\s+(.+)$',prose,re.M)
   slugs={re.sub(r'[^\w\s-]','',h.lower()).replace(' ','-') for h in headings}
   if dest[1:] not in slugs:errors.append(f'{p.relative_to(R)}: missing heading {dest}')
   continue
  target=dest.split('#',1)[0]
  if target and not (p.parent/target).exists():errors.append(f'{p.relative_to(R)}: missing {dest}')
  links+=1
 if re.search(r'\b(?:TODO|TBD|FIXME)\b',prose):errors.append(f'{p.relative_to(R)}: unresolved implementation placeholder')
manifest=json.loads((R/'diagrams/manifest.json').read_text())
ids=[d['id'] for d in manifest]
if len(ids)!=14 or len(set(ids))!=14:errors.append('Expected 14 unique diagrams')
for d in manifest:
 for ext,folder in [('drawio','drawio'),('svg','rendered'),('png','rendered')]+([('mmd','src')] if d['mermaid'] else []):
  path=R/'diagrams'/folder/(d['id']+'.'+ext)
  if not path.exists():errors.append(f'Missing {path.relative_to(R)}');continue
  if ext=='mmd' and not path.read_text().startswith(('flowchart TB','sequenceDiagram','stateDiagram-v2','gantt')):errors.append(str(path)+': unexpected source format')
  if ext in ('svg','drawio'):
   try:ET.parse(path)
   except ET.ParseError as e:errors.append(f'{path}: {e}')
  if ext=='png':
   b=path.read_bytes()
   if b[:8]!=b'\x89PNG\r\n\x1a\n' or struct.unpack('>I',b[16:20])[0]<1600:errors.append(str(path)+': invalid/undersized PNG')
adrs=json.loads((R/'adrs/index.json').read_text())
if {a['id'] for a in adrs}!={f'ADR-{i:03d}' for i in range(1,12)}:errors.append('ADR index does not cover 001–011')
for a in adrs:
 if not (R/'adrs'/a['file']).exists():errors.append('Missing '+a['file'])
trace=(R/'requirements/traceability.md').read_text()
for i in range(1,13):
 if not re.search(r'\| R'+f'{i:02d}'+r' \|',trace):errors.append(f'Missing traceability R{i:02d}')
readme=(R/'README.md').read_text()
for d in manifest:
 if f'(diagrams/rendered/{d["id"]}.svg)' not in readme:errors.append('README missing diagram '+d['id'])
if readme.count('<details>')!=readme.count('</details>'):errors.append('README: unbalanced details sections')
for a in adrs:
 if a.get('status')!='Accepted architecture decision':errors.append('Unexpected decision status: '+a['id'])
if errors:
 print('\n'.join(errors));sys.exit(1)
print(f'PASS: {len(list(R.rglob("*.md")))} Markdown files, {links} local links, 14 diagrams with editable draw.io/SVG/PNG, 11 ADRs, 12 requirement rows.')
print('Limits: remote links, browser rendering, custom diagram semantic equivalence and architectural correctness require review.')
