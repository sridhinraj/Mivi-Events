import re, json

with open('src/shaders/ashen-press/sources/ashen-press.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# Replace title
shelf_html = orig.replace("<title>Ashen Press — The Art Book Shelf</title>", "<title>Mivi Events — What We Do · The 3D Event Production Shelf</title>")

# Add Gilroy & Aftika fonts in head
font_links = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
<link href="https://fonts.cdnfonts.com/css/aftika" rel="stylesheet">
<link href="https://fonts.cdnfonts.com/css/gilroy-bold" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@qpokychuk/gilroy@1.0.2/index.min.css">"""

shelf_html = re.sub(r'<link rel="preconnect" href="https://fonts.googleapis.com">.*?display=swap" rel="stylesheet">', font_links, shelf_html, flags=re.DOTALL)

# Update CSS variables and fonts to luxury gold/burgundy and Gilroy/Aftika
old_css_root = """:root{
    --bg:#c6ae8e;
    --ink:#241a12;
    --ink-soft:rgba(36,26,18,.6);
    --ease:cubic-bezier(.22,1,.36,1);
  }"""

new_css_root = """:root{
    --bg:#120308;
    --ink:#f5eee1;
    --ink-soft:rgba(245,238,225,.7);
    --gold:#d4af37;
    --gold-light:#f7ecb5;
    --gold-gradient:linear-gradient(135deg, #f7ecb5 0%, #d4af37 50%, #997510 100%);
    --ease:cubic-bezier(.22,1,.36,1);
    --font-serif:"Aftika", "Playfair Display", Georgia, serif;
    --font-sans:"Gilroy", "Gilroy-Medium", Inter, sans-serif;
  }"""

shelf_html = shelf_html.replace(old_css_root, new_css_root)

# Replace fonts in CSS
shelf_html = shelf_html.replace('font-family:Inter,-apple-system,"Helvetica Neue",Helvetica,Arial,sans-serif;', 'font-family:var(--font-sans);')
shelf_html = shelf_html.replace('font-family:"EB Garamond",Georgia,serif;', 'font-family:var(--font-serif);')
shelf_html = shelf_html.replace('background:var(--bg);color:var(--ink);', 'background:#0a0104;color:var(--ink);')

# Update Header & Branding
old_header = """<header>
  <div class="brand">
    <span class="mark rise" data-d="0"><svg viewBox="0 0 24 24"><path d="M12 2c1.6 4.1 5.2 5.7 5.2 10a5.2 5.2 0 0 1-10.4 0C6.8 7.7 10.4 6.1 12 2z"/><path d="M6 20h12v1.6H6z"/></svg></span>
    <span class="brandname rise" data-d="70">Ashen Press</span>
  </div>
  <div class="right">
    <a class="pill rise" data-d="285" href="#" onclick="return false">Join the press</a>
  </div>
</header>"""

new_header = """<header>
  <div class="brand">
    <span class="mark rise" data-d="0" style="background:var(--gold-gradient);color:#120308;">
      <svg viewBox="0 0 24 24" style="fill:#120308;width:16px;height:16px;"><path d="M12 2L15 9H22L16.5 13.5L18.5 20.5L12 16L5.5 20.5L7.5 13.5L2 9H9L12 2Z"/></svg>
    </span>
    <span class="brandname rise" data-d="70" style="font-family:var(--font-serif);font-weight:700;letter-spacing:.08em;">Mivi <em style="font-style:normal;color:var(--gold);">Events</em></span>
  </div>
  <div class="right" style="display:flex;align-items:center;gap:10px;">
    <a class="pill rise" data-d="200" href="https://maps.app.goo.gl/Mda7YqqpYMXd67vEA" target="_blank" rel="noopener" style="background:rgba(212,175,55,.18);border:1px solid rgba(212,175,55,.4);color:var(--gold-light);">📍 Google Maps · Pavaratty</a>
    <a class="pill rise" data-d="285" href="https://wa.me/918877229985" target="_blank" rel="noopener" style="background:var(--gold-gradient);color:#0a0104;font-weight:600;">Plan Your Event</a>
  </div>
</header>"""

shelf_html = shelf_html.replace(old_header, new_header)

# Update detail acts button style
old_detail_acts = """  <div class="acts">
    <button id="detail-look">Look inside</button>
    <button id="detail-close">Close</button>
  </div>"""

new_detail_acts = """  <div class="acts" style="display:flex;flex-wrap:wrap;gap:10px;">
    <button id="detail-look">Look inside</button>
    <a id="detail-map" href="https://maps.app.goo.gl/Mda7YqqpYMXd67vEA" target="_blank" rel="noopener" style="padding:15px 22px;border-radius:999px;background:var(--gold-gradient);color:#090104;font:600 14px/1 var(--font-sans);text-decoration:none;display:inline-flex;align-items:center;box-shadow:0 8px 24px rgba(212,175,55,.3);">Visit Studio &bull; Google Maps</a>
    <button id="detail-close">Close</button>
  </div>"""

shelf_html = shelf_html.replace(old_detail_acts, new_detail_acts)

# Update STUDIO constant
shelf_html = shelf_html.replace("const STUDIO = 'FromSoftware';", "const STUDIO = 'Mivi Events';")

# Update BOOKS constant to the 10 Mivi Event services
old_books_code = """const BOOKS = [
  { id:'nightreign', title:'Nightreign', t1:'ELDEN RING', t2:'NIGHTREIGN',
    sub:'FIELD NOTES FROM LIMVELD', year:'2025', vol:'I', shelf:0, slot:0,
    spine:'#2f4a6b', cloth:'#12161d', edge:'#e4dcc6',
    blurb:'Three nights, one shrinking ring. Expedition plates, nightlord studies and the sky that closes in.' },
  { id:'erdtree', title:'Shadow of the Erdtree', t1:'SHADOW OF THE', t2:'ERDTREE',
    sub:'THE ART OF THE REALM OF SHADOW', year:'2024', vol:'II', shelf:0, slot:1,
    spine:'#7a6a2e', cloth:'#171510', edge:'#e9dfc4',
    blurb:'A land held under a second tree. Shadow-keep architecture, the finger ruins, and the long gold dark.' },
  { id:'ac6', title:'Armored Core VI', t1:'ARMORED CORE VI', t2:'FIRES OF RUBICON',
    sub:'MECHANICAL DESIGN WORKS', year:'2023', vol:'III', shelf:0, slot:2,
    spine:'#b4531f', cloth:'#171310', edge:'#eae3d2',
    blurb:'Frames, boosters and cannon mounts, drawn as engineering. Every part in the assembly, plated and numbered.' },
  { id:'elden-ring', title:'Elden Ring', t1:'ELDEN RING', t2:'',
    sub:'THE ART OF THE LANDS BETWEEN', year:'2022', vol:'IV', shelf:0, slot:3,
    spine:'#c39a3f', cloth:'#15120e', edge:'#e8dfc8',
    blurb:'Six hundred plates from the Lands Between. Erdtree studies, armour sheets, and the bestiary in full.' },
  { id:'sekiro', title:'Sekiro', t1:'SEKIRO', t2:'',
    sub:'SHADOWS DIE TWICE · OFFICIAL ARTWORKS', year:'2019', vol:'V', shelf:0, slot:4,
    spine:'#a8291f', cloth:'#141312', edge:'#e9e1cd',
    blurb:'The Sengoku sketchbook: prosthetic schematics, temple interiors, and every boss in ink.' },

  { id:'ds3', title:'Dark Souls III', t1:'DARK SOULS III', t2:'',
    sub:'DESIGN WORKS', year:'2016', vol:'VI', shelf:1, slot:0,
    spine:'#6a5a4a', cloth:'#161513', edge:'#e2d8c0',
    blurb:'The last of the fires. Lothric in graphite and ash, and the long walk down to the kiln.' },
  { id:'bloodborne', title:'Bloodborne', t1:'BLOODBORNE', t2:'',
    sub:'OFFICIAL ARTWORKS', year:'2015', vol:'VII', shelf:1, slot:1,
    spine:'#7d1a1c', cloth:'#0f0c0d', edge:'#e4d9c4',
    blurb:'Yharnam by lamplight — trick weapons, church attire, and everything that woke up in the night.' },
  { id:'ds2', title:'Dark Souls II', t1:'DARK SOULS II', t2:'',
    sub:'DESIGN WORKS', year:'2014', vol:'VIII', shelf:1, slot:2,
    spine:'#4f5f5a', cloth:'#121614', edge:'#ddd8c6',
    blurb:'Drangleic, drawn cold. Causeways, cliff gates, and a grey sky that never quite breaks.' },
  { id:'dark-souls', title:'Dark Souls', t1:'DARK SOULS', t2:'',
    sub:'DESIGN WORKS', year:'2011', vol:'IX', shelf:1, slot:3,
    spine:'#8a7a5e', cloth:'#1a1815', edge:'#ded3ba',
    blurb:'The first of the ash books. Lordran in graphite, and the bonfire that started all of this.' },
  { id:'demons-souls', title:"Demon's Souls", t1:"DEMON'S SOULS", t2:'',
    sub:'DESIGN WORKS', year:'2009', vol:'X', shelf:1, slot:4,
    spine:'#41586c', cloth:'#101418', edge:'#dcdcd4',
    blurb:'Boletaria in fog. The Nexus archways, the archstones, and a colour palette of two greys.' },
];"""

new_books_code = """const BOOKS = [
  { id:'mandap', title:'Grand Wedding Mandaps', t1:'GRAND WEDDING', t2:'MANDAPS',
    sub:'SACRED NILAVILAKKU & ROYAL FLORAL CANOPIES', year:'2026', vol:'I', shelf:0, slot:0,
    spine:'#871a2a', cloth:'#18050c', edge:'#faeec7',
    blurb:'Bespoke royal Indian & traditional Kerala mandap architecture, hand-carved floral pavilions, golden traditional lamps, and ceremonial sanctums in Thrissur.' },
  { id:'destination', title:'Destination Weddings', t1:'DESTINATION', t2:'WEDDINGS',
    sub:'PALACE, COASTAL BEACH & HERITAGE SANCTUARIES', year:'2026', vol:'II', shelf:0, slot:1,
    spine:'#9a7522', cloth:'#191409', edge:'#f6ebb4',
    blurb:'Turnkey luxury destination weddings across Kerala backwaters, beachside coastal starlight pavilions, and royal heritage estates with end-to-end management.' },
  { id:'stage-lighting', title:'Stage & Lighting Architecture', t1:'STAGE & LIGHTING', t2:'ARCHITECTURE',
    sub:'THEATRICAL SCENIC & KINETIC AMBIENCE', year:'2025', vol:'III', shelf:0, slot:2,
    spine:'#1f3e5a', cloth:'#0d151e', edge:'#dce5ea',
    blurb:'Custom 3D stage installations, computed chiaroscuro lighting, intelligent moving beams, LED wall scenography, and immersive acoustic visual engineering.' },
  { id:'bridal-couture', title:'Bridal & Groom Styling', t1:'BRIDAL & GROOM', t2:'COUTURE',
    sub:'HEIRLOOM SILK & REGAL ENTRY CHOREOGRAPHY', year:'2025', vol:'IV', shelf:0, slot:3,
    spine:'#9c1c30', cloth:'#1c050b', edge:'#f4dec4',
    blurb:'The Crimson Veil couture, gold-woven Kasavu silk styling, royal regalia consulting, and personalized couple entry processions orchestrated to perfection.' },
  { id:'mangalyam', title:'Sacred Mangalyam', t1:'SACRED', t2:'MANGALYAM',
    sub:'AUTHENTIC KERALA RITUALS & TEMPLE BLESSINGS', year:'2025', vol:'V', shelf:0, slot:4,
    spine:'#b8860b', cloth:'#1c1404', edge:'#fcf3cf',
    blurb:'Traditional Kerala rituals, sacred Mangalyam thread ceremonies, Nadaswaram ensembles, and Vedic floral blessings curated with sacred authenticity.' },

  { id:'reception-galas', title:'Reception Galas & Soirées', t1:'RECEPTION GALAS', t2:'& SOIRÉES',
    sub:'MIDNIGHT BALLROOMS & STARLIGHT GALAS', year:'2024', vol:'VI', shelf:1, slot:0,
    spine:'#4a152e', cloth:'#14040c', edge:'#ebd3df',
    blurb:'Grand ballroom celebrations, crystal chandelier stages, velvet lounge seating, live concert acoustics, and gourmet after-parties crafted for eternity.' },
  { id:'floral-artistry', title:'Floral Installations', t1:'FLORAL ARTISTRY', t2:'& INSTALLATIONS',
    sub:'SCULPTURAL BOTANICALS & EXOTIC BLOOMS', year:'2024', vol:'VII', shelf:1, slot:1,
    spine:'#2d5334', cloth:'#0a170d', edge:'#ddedd6',
    blurb:'Cascading Dutch roses, fragrant jasmine ceilings, royal marigold archways, and sustainable botanical sculptural backdrops designed for high elegance.' },
  { id:'royal-entry', title:'Royal Entry & Pyrotechnics', t1:'ROYAL ENTRY', t2:'& PYROTECHNICS',
    sub:'THEATRICAL ENTRIES, COLD SPARKS & SFX', year:'2024', vol:'VIII', shelf:1, slot:2,
    spine:'#8a401b', cloth:'#170c06', edge:'#f0d9c4',
    blurb:'Grand caparisoned elephant processions, synchronized cold-fire fireworks, low-lying fog clouds, and regal musical entrances leaving guests in awe.' },
  { id:'cinematic-films', title:'Cinematic Media & Films', t1:'CINEMATIC MEDIA', t2:'& WEDDING FILMS',
    sub:'DAVINCI MASTER COLOR & STORYTELLING', year:'2024', vol:'IX', shelf:1, slot:3,
    spine:'#2b2342', cloth:'#0f0c18', edge:'#ddd5eb',
    blurb:'Theatrical 4K wedding documentaries, aerial drone cinematography, DaVinci ACES color grading, and editorial memory albums by Mivi Media.' },
  { id:'hospitality-catering', title:'Hospitality & Banquets', t1:'HOSPITALITY', t2:'& ROYAL BANQUETS',
    sub:'BESPOKE MULTI-CUISINE & CONCIERGE', year:'2023', vol:'X', shelf:1, slot:4,
    spine:'#65421f', cloth:'#170e06', edge:'#ebdccb',
    blurb:'Traditional 30-dish royal Kerala Sadhya feasts, international culinary stations, VIP guest logistics, and personalized concierge care in Pavaratty.' },
];"""

shelf_html = shelf_html.replace(old_books_code, new_books_code)

# Replace the giant MARK_SRC and PLATE_SRC definition while keeping `const PLATE = {};` and `function loadPlates(){ ... }`
new_plate_src_setup = """const PLATE_SRC = {
  'mandap': 'lookbook/spread-03.jpg',
  'destination': 'lookbook/spread-06.jpg',
  'stage-lighting': 'lookbook/spread-00.jpg',
  'bridal-couture': 'lookbook/spread-01.jpg',
  'mangalyam': 'lookbook/spread-04.jpg',
  'reception-galas': 'lookbook/spread-07.jpg',
  'floral-artistry': 'lookbook/spread-02.jpg',
  'royal-entry': 'lookbook/spread-05.jpg',
  'cinematic-films': 'IMAGES/instagram_photo_1792216845.jpg',
  'hospitality-catering': 'IMAGES/instagram_photo_1792216856.jpg'
};
const MARK_SRC = {
  'mandap': 'logo.png',
  'destination': 'logo.png',
  'stage-lighting': 'logo.png',
  'bridal-couture': 'logo.png',
  'mangalyam': 'logo.png',
  'reception-galas': 'logo.png',
  'floral-artistry': 'logo.png',
  'royal-entry': 'logo.png',
  'cinematic-films': 'logo.png',
  'hospitality-catering': 'logo.png'
};
const PLATE = {};
function loadPlates(){
  return Promise.all(BOOKS.map(b=>new Promise(res=>{
    const src=PLATE_SRC[b.id];
    if(!src) return res();
    const im=new Image();
    im.crossOrigin='anonymous';
    im.onload=()=>{ PLATE[b.id]=im; res(); };
    im.onerror=()=>{ res(); };
    im.src=src;
  })));
}
"""

p1 = shelf_html.find("/* The plates are generated artwork")
p2 = shelf_html.find("const FOIL = '#efe4cc';")

if p1 != -1 and p2 != -1:
    shelf_html = shelf_html[:p1] + new_plate_src_setup + "\n" + shelf_html[p2:]
    print("Replaced base64 plates block accurately, preserving loadPlates and paintCover!")
else:
    print("Error finding p1 or p2", p1, p2)

# Update foil stamp text from ASHEN PRESS to MIVI EVENTS
shelf_html = shelf_html.replace("tracked(g,'ASHEN PRESS',W*.215,H*.845,W*.022*.30,'left');", "tracked(g,'MIVI EVENTS',W*.215,H*.845,W*.022*.30,'left');")
shelf_html = shelf_html.replace("tracked(g,'ASHEN PRESS',W*.5,H*.920,W*.0215*.34,'center');", "tracked(g,'MIVI EVENTS',W*.5,H*.920,W*.0215*.34,'center');")
shelf_html = shelf_html.replace("g.fillText('AP',W*.52,H*.955);", "g.fillText('ME',W*.52,H*.955);")
shelf_html = shelf_html.replace("g.fillText('AP',0,W*.002);", "g.fillText('ME',0,W*.002);")
shelf_html = shelf_html.replace("g.fillText('Volume '+b.vol+' of the Worlds series',W*.215,H*.875);", "g.fillText('Volume '+b.vol+' · Mivi Event Planners',W*.215,H*.875);")

# Update font family in paintCover and artBack
shelf_html = shelf_html.replace("const fam='\"EB Garamond\",Georgia,serif';", "const fam='\"Aftika\",\"Playfair Display\",Georgia,serif';")
shelf_html = shelf_html.replace("const SERIF = '\"EB Garamond\",Didot,\"Bodoni 72\",Georgia,\"Times New Roman\",serif';", "const SERIF = '\"Aftika\",\"Playfair Display\",Georgia,serif';")
shelf_html = shelf_html.replace("const SANS  = 'Inter,-apple-system,\"Helvetica Neue\",Helvetica,Arial,sans-serif';", "const SANS  = '\"Gilroy\",\"Gilroy-Medium\",Inter,sans-serif';")

with open('services-shelf.html', 'w', encoding='utf-8') as out:
    out.write(shelf_html)

print("Updated services-shelf.html! Size:", len(shelf_html))
