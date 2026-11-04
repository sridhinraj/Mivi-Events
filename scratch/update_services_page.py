with open('services.html', 'r', encoding='utf-8') as f:
    s_html = f.read()

# Target insertion right after </section> of page-hero
target_pos = s_html.find('</section>')
if target_pos != -1:
    shelf_section = """
    <!-- Interactive 3D Tactile Event Shelf (AshenPress Engine) -->
    <section class="section" style="padding-top: 20px; padding-bottom: 20px;">
      <div style="text-align: center; margin-bottom: 30px;">
        <span class="eyebrow" style="color:var(--gold);">3D Interactive Portfolio Shelf</span>
        <h2 style="font-family:var(--aftika); font-size:clamp(28px, 4.5vw, 52px); color:#fff; margin-top:8px;">
          The 3D <em>Event Production Shelf</em>
        </h2>
        <p style="color:rgba(245,243,239,0.76); max-width:720px; margin:12px auto 0; font-size:16px;">
          Ten clothbound volumes capturing our event disciplines. Hover over any volume, click to draw from the shelf, click <strong>Look inside</strong> to flip, and drag to rotate in 3D.
        </p>
      </div>

      <div style="position:relative; width:100%; height:820px; max-height:85vh; border-radius:16px; overflow:hidden; border:1px solid var(--gold-border); box-shadow:0 24px 60px rgba(0,0,0,0.85); background:#0a0104; margin-bottom: 40px;">
        <iframe src="services-shelf.html" title="Mivi Events — What We Do · 3D Event Production Shelf" style="width:100%; height:100%; border:0; display:block;" loading="lazy"></iframe>
      </div>

      <!-- Studio Location Card (Google Maps) -->
      <div style="background:rgba(26,5,14,0.7); border:1px solid var(--gold-border); border-radius:14px; padding: clamp(24px, 3.5vw, 40px); display:grid; grid-template-columns: 1.2fr 1fr; gap: 32px; align-items: center;">
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
            <a href="https://maps.app.goo.gl/Mda7YqqpYMXd67vEA" target="_blank" rel="noopener" class="btn btn-gold" style="display:inline-flex; align-items:center; gap:8px;">
              <svg viewBox="0 0 24 24" style="width:16px;height:16px;fill:currentColor;"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>
              Open in Google Maps &rarr;
            </a>
            <a href="https://wa.me/918877229985" target="_blank" rel="noopener" class="btn btn-outline" style="display:inline-flex; align-items:center; gap:8px;">
              WhatsApp Consultation
            </a>
          </div>
        </div>
        <div style="border-radius:12px; overflow:hidden; border:1px solid rgba(212,175,55,0.3); box-shadow:0 12px 30px rgba(0,0,0,0.6);">
          <img src="lookbook/spread-00.jpg" alt="Mivi Event Planners Studio Production" style="width:100%; height:auto; display:block;">
        </div>
      </div>
    </section>
"""
    first_close = target_pos + len('</section>')
    s_html = s_html[:first_close] + shelf_section + s_html[first_close:]
    with open('services.html', 'w', encoding='utf-8') as out:
        out.write(s_html)
    print("services.html updated with 3D shelf and maps card!")
