import json, os, hashlib

with open('ashen-press.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data.get('files', []):
    rel_path = item['path']
    code = item['code']
    os.makedirs(os.path.dirname(rel_path), exist_ok=True)
    with open(rel_path, 'w', encoding='utf-8') as out:
        out.write(code)
    calculated_sha = hashlib.sha256(code.encode('utf-8')).hexdigest()
    print('Wrote:', rel_path)
    print('Expected SHA:', item['sha256'])
    print('Actual SHA:  ', calculated_sha)
    assert calculated_sha == item['sha256'], f'SHA mismatch for {rel_path}'

print('All 3 registered files successfully written and verified with exact SHA!')
