from pathlib import Path
from decimal import Decimal
import csv,json,hashlib,re
root=Path(__file__).resolve().parents[1]
def rows(name):
    with (root/'data'/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
scale=rows('scale_effects.csv');compact=rows('compact_configurations.csv')
assert len(scale)==85 and sum(x['main_table']=='True' for x in scale)==22
for x in scale:
    assert Decimal(x['result'])-Decimal(x['baseline'])==Decimal(x['gain_pp']),x
    assert 0<=Decimal(x['baseline'])<=100 and 0<=Decimal(x['result'])<=100
    assert 1<=int(x['source_reference'])<=61 and x['source_location']
assert len(compact)==37 and len({x['system_generator'] for x in compact})==37
for x in compact:
    sizes=re.findall(r'(\d+(?:\.\d+)?)B',x['system_generator'])
    assert sizes and all(Decimal(n)<4 for n in sizes),x
    for key in ['BIRD_dev_EX','Spider_dev_EX']:
        if x[key]!='NR':
            for n in x[key].split('/'):assert 0<=Decimal(n.strip())<=100
    assert all(1<=int(n)<=61 for n in re.findall(r'\[(\d+)\]',x['numerical_source_venue']))
byname={x['system_generator']:x for x in compact}
assert 'DB content' in byname['T5-3B + PICARD']['inference_search_auxiliaries']
assert byname['Graphix-T5-3B']['Spider_dev_EX']=='78.20'
assert byname['RASAT-3B + PICARD']['Spider_dev_EX']=='80.50'
assert byname['Llama-3.2-1B-Instruct (untuned, SC)']['Spider_dev_EX']=='30.79'
assert byname['Qwen2.5-Coder-1.5B instruct (single-shot)']['BIRD_dev_EX']=='14.71'
source=json.loads((root/'metadata/source_manifest.json').read_text(encoding='utf-8'))
assert len(source)==37 and len({x['file'] for x in source})==37
for x in source:assert x['url'].startswith('https://') and re.fullmatch('[0-9a-f]{64}',x['sha256'])
refs=json.loads((root/'metadata/reference_renumbering.json').read_text(encoding='utf-8'))
assert sorted(map(int,refs['current_references']))==list(range(1,62))
assert set(refs['old_to_new'].values())<=set(range(1,62)) and len(refs['retired_references'])==1
extra=json.loads((root/'metadata/additional_evidence.json').read_text(encoding='utf-8'))
assert extra['RASAT']['SParC']['dev_PICARD_QEM_IEM_QEX_IEX']==[67.7,49.1,73.3,54]
assert extra['data_amount_and_cost']['OmniSQL']['derived_student_GPU_hours']==[8*24*d for d in [6,12,20]]
assert extra['data_amount_and_cost']['OmniSQL']['synthesis_GPU_hours'] is None
manifest=json.loads((root/'manifest.json').read_text(encoding='utf-8'))
allowed={x['path'] for x in manifest}|{'manifest.json'}
actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and '.git' not in p.relative_to(root).parts}
assert actual==allowed and len(actual)==11,actual
for x in manifest:
    f=root/x['path'];assert len(f.read_bytes())==x['bytes'] and hashlib.sha256(f.read_bytes()).hexdigest()==x['sha256'],x['path']
    assert not re.search(r'(?<![A-Za-z0-9_])[A-Za-z]:[\\/]|gh[pousr]_[A-Za-z0-9]{20,}',f.read_text(encoding='utf-8-sig')),x['path']
print(json.dumps({'scale_contrasts':85,'main_table4_contrasts':22,'table9_configurations':37,'source_pdf_records':37,'references':61,'manifest_hashes_verified':len(manifest),'independent_model_replication':False},indent=2))
