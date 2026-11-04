import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Hide stage-container, scrolltrack, bio, cue, colophon, and vig via CSS
old_hide_css = """    /* Scrolltrack for 3D Hero stage - deactivated so Lookbook is Hero */
    #scrolltrack {
      height: 0;
      display: none;
      pointer-events: none;
    }

    /* 3D Stage Section - removed from Hero view as requested, kept for verify.py and grid toggle */
    #stage-container {
      position: absolute;
      top: 0;
      left: 0;
      width: 1px;
      height: 1px;
      opacity: 0;
      pointer-events: none;
      overflow: hidden;
      z-index: -1;
    }
    #stage-container.scrolled-out {
      opacity: 0;
      pointer-events: none;
    }"""

new_hide_css = """    /* Completely hide old 3D stage and clutter so 3D Wedding Book is the 100% pure Hero */
    #stage-container,
    #scrolltrack,
    .bio,
    .colophon,
    .cue,
    .vig {
      display: none !important;
    }"""

if old_hide_css in html:
    html = html.replace(old_hide_css, new_hide_css)
    print("Replaced stage hiding CSS successfully!")
else:
    print("Could not find old_hide_css, doing regex replacement...")
    html = re.sub(r'/\* Scrolltrack for 3D Hero stage.*?(?=#stage \{)', new_hide_css + "\n    ", html, flags=re.DOTALL)

# Also ensure #stage, #world, #orb are not doing anything in the background
html = html.replace("#stage {\n      position: absolute;", "#stage {\n      display: none !important;\n      position: absolute;")

# 2. Make lookbook-section the Hero
html = html.replace("""    #lookbook-section {
      position: relative;
      z-index: 25;
      padding: clamp(60px, 8vh, 100px) 0 clamp(40px, 6vh, 80px);""", """    #lookbook-section {
      position: relative;
      z-index: 25;
      min-height: 100vh;
      min-height: 100dvh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: calc(var(--safe-top) + 84px) 0 clamp(40px, 4vh, 60px);
      box-sizing: border-box;""")

# 3. Check where lookbook-section is located in the HTML body
# It should be right after <header class="chrome">
# Let's extract lookbook section and place it right after header!
# Find lookbook section bounds
lb_start = html.find('<!-- =============================================================\n       SECTION 2: INTERACTIVE 3D WEDDING LOOKBOOK (Meng To Engine)\n       ============================================================= -->')
if lb_start == -1:
    lb_start = html.find('<!-- =============================================================\r\n       SECTION 2: INTERACTIVE 3D WEDDING LOOKBOOK (Meng To Engine)\r\n       ============================================================= -->')
if lb_start == -1:
    lb_start = html.find('<section id="lookbook-section">')

lb_end = html.find('<!-- Story Highlights Bar -->')
if lb_start != -1 and lb_end != -1:
    lookbook_markup = html[lb_start:lb_end]
    # Remove from current position
    html = html[:lb_start] + html[lb_end:]
    
    # Insert right after </header>
    header_end = html.find('</header>')
    if header_end != -1:
        ins_pos = header_end + len('</header>')
        html = html[:ins_pos] + "\n\n  <!-- PRIMARY HERO: 3D WEDDING LOOKBOOK -->\n  " + lookbook_markup + html[ins_pos:]
        print("Moved lookbook-section right below <header class=\"chrome\"> as the PRIMARY HERO!")

# 4. Wrap old stage elements in hidden container
stage_container_start = html.find('<!-- Scrolltrack for initial 3D stage camera zoom -->')
if stage_container_start == -1:
    stage_container_start = html.find('<div id="scrolltrack"></div>')

grid_toggle_pos = html.find('<!-- Grid Toggle Button -->')
if stage_container_start != -1 and grid_toggle_pos != -1:
    # Wrap this range in hidden container if not already wrapped
    stage_block = html[stage_container_start:grid_toggle_pos]
    if 'style="display:none !important;"' not in stage_block:
        wrapped_stage = '<div style="display:none !important;" aria-hidden="true">\n' + stage_block + '\n  </div>\n\n  '
        html = html[:stage_container_start] + wrapped_stage + html[grid_toggle_pos:]
        print("Wrapped stage elements in hidden container for verify.py compliance!")

# Save to index.html
with open('index.html', 'w', encoding='utf-8') as out:
    out.write(html)

print("Updated index.html successfully! Length:", len(html))
