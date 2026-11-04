import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the Navigation Links bar to include Lookbook, What We Do, 3D Shelf, Studio Map, and Stage
old_nav = """    <div class="nav-links-bar">
      <a href="#stage-container">Stage</a>
      <a href="#lookbook-section">Lookbook</a>
      <a href="#highlights">Highlights</a>
      <a href="#about">About</a>
      <a href="#services">Services</a>
      <a href="#plates">Plates</a>
      <a href="#contact">Contact</a>
    </div>"""

new_nav = """    <div class="nav-links-bar">
      <a href="#lookbook-section">3D Lookbook</a>
      <a href="#what-we-do">What We Do (3D Shelf)</a>
      <a href="#services">Services</a>
      <a href="#stage-container">3D Stage</a>
      <a href="#maps-studio">Studio Location</a>
      <a href="#contact">Book</a>
    </div>"""

if old_nav in html:
    html = html.replace(old_nav, new_nav)
    print("Updated nav-links-bar successfully!")

# 2. Update mobile menu nav
old_menu_nav = """    <nav>
      <a href="#stage-container">3D Stage View</a>
      <a href="#lookbook-section">Wedding Lookbook</a>
      <a href="#highlights">Story Highlights</a>
      <a href="#about">About Mivi Events</a>
      <a href="#services">Curated Services</a>
      <a href="#plates">Lookbook Plates</a>
      <a href="#contact">Book Consultation</a>
      <a href="https://www.instagram.com/mivi_events/" target="_blank" rel="noopener" style="color:var(--gold);">Instagram @mivi_events</a>
    </nav>"""

new_menu_nav = """    <nav>
      <a href="#lookbook-section">3D Wedding Lookbook</a>
      <a href="#what-we-do">What We Do (3D Shelf)</a>
      <a href="#services">Curated Services</a>
      <a href="#stage-container">3D Stage View</a>
      <a href="#maps-studio">Studio & Google Maps</a>
      <a href="#contact">Book Consultation</a>
      <a href="https://maps.app.goo.gl/Mda7YqqpYMXd67vEA" target="_blank" rel="noopener" style="color:var(--gold-light);">📍 Google Maps Directions</a>
      <a href="https://www.instagram.com/mivi_events/" target="_blank" rel="noopener" style="color:var(--gold);">Instagram @mivi_events</a>
    </nav>"""

if old_menu_nav in html:
    html = html.replace(old_menu_nav, new_menu_nav)
    print("Updated mobile menu nav successfully!")

# 3. Add What We Do 3D Shelf and Google Maps studio section above Services Grid
target_services_marker = """    <!-- Services Grid -->
    <div id="services" class="services-grid">"""

what_we_do_block = """    <!-- WHAT WE DO: Interactive 3D Tactile Event Shelf (AshenPress Engine) -->
    <section id="what-we-do" class="what-we-do-shelf-section" style="margin-top: 60px; padding-top: 40px; border-top: 1px solid var(--gold-border);">
      <div class="section-kicker">Curated Volumes &bull; What We Do</div>
      <h2 class="lookbook-title" style="margin-bottom: 14px;">The 3D <em>Event Production Shelf</em></h2>
      <p style="text-align:center; max-width:760px; margin:0 auto 32px; color:rgba(244,242,239,0.72); font-size:15.5px; line-height:1.65;">
        Explore our ten signature event craft disciplines bound in cloth & gold foil. Hover to inspect, select to draw from the shelf, click <strong>Look inside</strong> to flip and reveal real wedding plates on the back cover, and drag to rotate in 3D.
      </p>
      
      <!-- ThreeUI AshenPress Shader Frame -->
      <div class="shader-frame" style="position:relative; width:100%; height:820px; max-height:85vh; border-radius:16px; overflow:hidden; border:1px solid rgba(212,175,55,0.35); box-shadow:0 24px 60px rgba(0,0,0,0.85); background:#0a0104; margin-bottom: 40px;">
        <iframe src="services-shelf.html" title="Mivi Events — What We Do · The 3D Event Production Shelf" style="width:100%; height:100%; border:0; display:block;" loading="lazy"></iframe>
      </div>

      <!-- Google Maps Studio & Verified Services Card -->
      <div id="maps-studio" class="google-maps-card" style="background:rgba(26,5,14,0.7); border:1px solid var(--gold-border); border-radius:14px; padding: clamp(24px, 3.5vw, 40px); display:grid; grid-template-columns: 1.2fr 1fr; gap: 32px; align-items: center; margin-bottom: 60px;">
        <div>
          <div style="display:inline-flex; align-items:center; gap:8px; background:rgba(212,175,55,0.15); border:1px solid rgba(212,175,55,0.35); padding:6px 14px; border-radius:999px; font-size:12px; color:var(--gold-light); font-weight:600; margin-bottom:14px;">
            <span>★ 5.0 Google Business Rating</span>
            <span>&bull;</span>
            <span>Pavaratty, Thrissur</span>
          </div>
          <h3 style="font-family:var(--aftika); font-size:clamp(22px, 3vw, 34px); color:#fff; margin-bottom:12px; font-weight:700;">
            Visit Our Creative Studio in <em>Pavaratty</em>
          </h3>
          <p style="color:rgba(244,242,239,0.78); font-size:15px; line-height:1.6; margin-bottom:20px;">
            Experience our physical portfolio, custom floral swatches, fabrics, and 3D stage maquettes in person. Located in 3Star Nagar, Pavaratty, Thrissur.
          </p>
          <div style="display:flex; flex-direction:column; gap:10px; font-size:14px; margin-bottom:24px;">
            <div style="display:flex; align-items:center; gap:10px;">
              <span style="color:var(--gold);">📍</span>
              <span>1st Floor, Ezra Building, 3Star Nagar, Pavaratty, Thrissur, Kerala — 680507</span>
            </div>
            <div style="display:flex; align-items:center; gap:10px;">
              <span style="color:var(--gold);">📞</span>
              <span>Studio Direct: <a href="tel:+918877229985" style="color:var(--gold); font-weight:600;">+91 88772 29985</a></span>
            </div>
            <div style="display:flex; align-items:center; gap:10px;">
              <span style="color:var(--gold);">📸</span>
              <span>Instagram: <a href="https://www.instagram.com/mivi_events/" target="_blank" rel="noopener" style="color:var(--gold); font-weight:600;">@mivi_events</a></span>
            </div>
          </div>
          <div style="display:flex; flex-wrap:wrap; gap:14px;">
            <a href="https://maps.app.goo.gl/Mda7YqqpYMXd67vEA" target="_blank" rel="noopener" class="btn-gold" style="display:inline-flex; align-items:center; gap:8px;">
              <svg viewBox="0 0 24 24" style="width:16px;height:16px;fill:currentColor;"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
              Open in Google Maps &rarr;
            </a>
            <a href="https://wa.me/918877229985" target="_blank" rel="noopener" style="display:inline-flex; align-items:center; gap:8px; padding:12px 22px; border-radius:999px; border:1px solid rgba(212,175,55,0.4); color:var(--gold-light); font-weight:600; text-decoration:none;">
              WhatsApp Consultation
            </a>
          </div>
        </div>
        <div style="border-radius:12px; overflow:hidden; border:1px solid rgba(212,175,55,0.3); box-shadow:0 12px 30px rgba(0,0,0,0.6);">
          <img src="lookbook/spread-00.jpg" alt="Mivi Event Planners Studio Production" style="width:100%; height:auto; display:block;">
        </div>
      </div>
    </section>

    <!-- Services Grid -->
    <div id="services" class="services-grid">"""

if target_services_marker in html:
    html = html.replace(target_services_marker, what_we_do_block)
    print("Added What We Do 3D shelf section and Google Maps card successfully!")

# 4. Update verified phone numbers
html = html.replace("+91 98460 00000", "+91 88772 29985")
html = html.replace("wa.me/919846000000", "wa.me/918877229985")

# 5. Write updated index.html
with open('index.html', 'w', encoding='utf-8') as out:
    out.write(html)

print("index.html updated successfully! Length:", len(html))
