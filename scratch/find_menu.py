with open('index.html', encoding='utf-8', errors='ignore') as f:
    for idx, line in enumerate(f):
        if 'id="menu"' in line or 'menu-btn' in line or 'gridbtn' in line:
            print(idx + 1, line.strip()[:80])
