import urllib.request, re

url = 'https://www.google.com/maps/place/Mivi+Event+Planners/@10.5700364,76.0547946,17z/data=!4m6!3m5!1s0x3ba793966433f23f:0x5bc3b4f50fa944b8!8m2!3d10.5700364!4d76.0547946!16s%2Fg%2F11nt_cntjx'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode('utf-8', errors='ignore')
        title = re.findall(r'<title>(.*?)</title>', content)
        print('Title:', title)
        photos = re.findall(r'https://lh5\.googleusercontent\.com/p/[a-zA-Z0-9_-]+', content)
        print('Photos count:', len(photos))
        for p in list(set(photos))[:10]:
            print('Photo:', p)
        matches = re.findall(r'Mivi Event Planners[^\"]{0,200}', content)
        for m in matches[:5]:
            print('Mention:', m)
        # Search for address, phone
        addrs = re.findall(r'Pavaratty[^\"]{0,100}', content)
        for a in set(addrs)[:3]:
            print('Addr:', a)
except Exception as e:
    print('Error:', e)
