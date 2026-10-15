from pathlib import Path
from decimal import Decimal
import csv,json,hashlib,re

root=Path(__file__).resolve().parents[1]
def rows(name):
    with (root/'data'/name).open(encoding='utf-8-sig',newline='') as f:
        return list(csv.DictReader(f))
scale=rows('scale_effects_49_contrasts.csv')
assert len(scale)==49
assert sum(x['main_table']=='True' for x in scale)==16
for x in scale:
    assert Decimal(x['result'])-Decimal(x['baseline'])==Decimal(x['gain_pp']),x
    assert 0<=Decimal(x['baseline'])<=100 and 0<=Decimal(x['result'])<=100
compact=rows('compact_configurations_24.csv')
assert len(compact)==24 and len({x['system_generator'] for x in compact})==24
for x in compact:
    sizes=re.findall(r'(\d+(?:\.\d+)?)B',x['system_generator'])
    assert sizes and all(Decimal(n)<4 for n in sizes),x['system_generator']
    for key in ['BIRD_dev_EX','Spider_dev_EX']:
        if x[key]!='NR':
            for n in x[key].split('/'):
                assert 0<=Decimal(n.strip())<=100,(key,n)
source=json.loads((root/'metadata/source_manifest.json').read_text(encoding='utf-8'))
assert len(source)==33 and len({x['file'] for x in source})==33
for x in source:
    assert x['url'].startswith('https://') and re.fullmatch('[0-9a-f]{64}',x['sha256'])
refs=json.loads((root/'metadata/reference_renumbering.json').read_text(encoding='utf-8'))
assert len(refs['current_references'])==58
assert sorted(map(int,refs['old_to_new'].values()))==list(range(1,59))
manifest=json.loads((root/'manifest.json').read_text(encoding='utf-8'))
for x in manifest:
    f=root/x['path']
    assert f.is_file() and hashlib.sha256(f.read_bytes()).hexdigest()==x['sha256'],x['path']
print(json.dumps({'scale_contrasts':49,'main_table4_contrasts':16,'table9_configurations':24,'source_pdf_records':33,'references':58,'hashes_verified':len(manifest),'independent_model_replication':False},indent=2))
