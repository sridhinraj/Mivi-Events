with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS for stage-container and scrolltrack so the old hero is removed from view and lookbook is the Hero
old_stage_css = """    /* Scrolltrack for 3D Hero stage */
    #scrolltrack {
      height: 120vh;
      pointer-events: none;
    }

    /* 3D Stage Section */
    #stage-container {
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 10;
      display: grid;
      place-items: center;
      transition: opacity .8s ease, transform .8s ease;
    }
    #stage-container.scrolled-out {
      opacity: 0;
      pointer-events: none;
      transform: translateY(-40px);
    }"""

new_stage_css = """    /* Scrolltrack for 3D Hero stage - deactivated so Lookbook is Hero */
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

if old_stage_css in html:
    html = html.replace(old_stage_css, new_stage_css)
    print("Replaced stage-container CSS successfully!")
else:
    print("Warning: old_stage_css not matched exactly, checking alternate...")
    # Let's search for #stage-container
    idx = html.find("#stage-container {")
    print("Index of #stage-container:", idx)

# 2. Update lookbook-section CSS to be the grand Hero Section
old_lookbook_css = """    #lookbook-section {
      position: relative;
      z-index: 25;
      padding: clamp(60px, 8vh, 100px) 0 clamp(40px, 6vh, 80px);
      background: radial-gradient(circle at 50% 20%, #1f040e 0%, #0d0105 60%, #000000 100%);
      border-top: 1px solid var(--gold-border);
      box-shadow: 0 -24px 60px rgba(0,0,0,0.85);
    }"""

new_lookbook_css = """    #lookbook-section {
      position: relative;
      z-index: 25;
      min-height: 100vh;
      min-height: 100dvh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: calc(var(--safe-top) + 84px) 0 clamp(40px, 5vh, 60px);
      background: radial-gradient(circle at 50% 30%, #22040f 0%, #0d0105 55%, #000000 100%);
      box-shadow: 0 24px 60px rgba(0,0,0,0.85);
    }"""

if old_lookbook_css in html:
    html = html.replace(old_lookbook_css, new_lookbook_css)
    print("Updated lookbook-section CSS to Hero layout!")
else:
    print("Warning: old_lookbook_css not matched exactly")

# 3. Adjust cue, bio, and colophon so they don't cover the Lookbook Hero
old_bio_css = """.bio {
      position: fixed;
      bottom: calc(var(--pad) + var(--safe-bottom));
      left: calc(var(--pad) + var(--safe-left));
      max-width: clamp(280px, 28vw, 380px);
      z-index: 30;
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      background: rgba(16, 3, 8, .65);
      border: 1px solid var(--gold-border);
      border-radius: 14px;
      padding: 18px 20px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      box-shadow: 0 16px 40px rgba(0,0,0,.6);
      transition: opacity .4s ease, transform .4s ease;
    }"""

new_bio_css = """.bio {
      position: fixed;
      bottom: calc(var(--pad) + var(--safe-bottom));
      left: calc(var(--pad) + var(--safe-left));
      max-width: clamp(280px, 28vw, 360px);
      z-index: 30;
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      background: rgba(16, 3, 8, .85);
      border: 1px solid var(--gold-border);
      border-radius: 14px;
      padding: 16px 18px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      box-shadow: 0 16px 40px rgba(0,0,0,.7);
      opacity: 0;
      pointer-events: none;
      transform: translateY(20px);
      transition: opacity .4s ease, transform .4s ease;
    }
    body.show-bio .bio {
      opacity: 1;
      pointer-events: auto;
      transform: none;
    }"""

if old_bio_css in html:
    html = html.replace(old_bio_css, new_bio_css)
    print("Adjusted bio CSS successfully!")

# Ensure cue is hidden from hero
html = html.replace(".cue {\n      position: fixed;\n      bottom: calc(var(--pad) + var(--safe-bottom));\n      left: 50%;", ".cue {\n      display: none !important;\n      position: fixed;\n      bottom: calc(var(--pad) + var(--safe-bottom));\n      left: 50%;")

# Write out updated index.html
with open('index.html', 'w', encoding='utf-8') as out:
    out.write(html)

print("Updated index.html written!")
