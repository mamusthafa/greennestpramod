#!/usr/bin/env python3
"""
generate_all.py
Generates all remaining pages for Green Nest Avocado/Coffee Nursery website:
- about.html
- plants.html
- avocado-plants.html
- coffee-plants.html
- pepper-plants.html
- areca-plants.html
- silver-oak-plants.html
- cardamom-plants.html
- rambutan-plants.html
- litchi-plants.html
- other-plants.html
- wholesale-plants.html
- commercial-plantation.html
- bulk-plant-delivery.html
- gallery.html
- faq.html
- contact.html
- sitemap.xml
- robots.txt
"""

import os
from build_pages import render_page

def whatsapp_calc_box(plant_name="Avocado Plants", default_qty="200"):
    return f"""
<div class="whatsapp-enquiry-box">
  <h4>
    <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
    Instant WhatsApp Price Quote
  </h4>
  <p>Fill in your requirements below to instantly generate a customized WhatsApp enquiry message to our nursery team:</p>
  <form class="whatsapp-form">
    <div class="enquiry-form-grid">
      <div class="form-group">
        <label>Your Name</label>
        <input type="text" name="name" class="form-control" placeholder="Grower Name" required>
      </div>
      <div class="form-group">
        <label>Contact Phone</label>
        <input type="tel" name="phone" class="form-control" placeholder="+91 Mobile Number">
      </div>
      <div class="form-group">
        <label>Plant Type</label>
        <input type="text" name="plant" class="form-control" value="{plant_name}" readonly>
      </div>
      <div class="form-group">
        <label>Estimated Quantity</label>
        <input type="text" name="quantity" class="form-control" value="{default_qty}" placeholder="e.g. 100, 500, 1000 saplings">
      </div>
      <div class="form-group">
        <label>Farm / Plantation Location</label>
        <input type="text" name="location" class="form-control" placeholder="District / State (e.g. Mysuru / Hassan / Wayanad)">
      </div>
      <div class="form-group">
        <label>Delivery Destination</label>
        <input type="text" name="delivery" class="form-control" placeholder="Nursery Pickup or Delivery Address">
      </div>
      <div class="form-group full">
        <label>Additional Notes / Questions</label>
        <textarea name="message" class="form-control" rows="2" placeholder="e.g. Inquiring about planting season, spacing recommendation or batch maturity"></textarea>
      </div>
    </div>
    <button type="submit" class="btn btn-whatsapp btn-block">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
      Send WhatsApp Enquiry for Wholesale Price
    </button>
  </form>
</div>
"""

def cta_banner_html(plant_name="Plants"):
    return f"""
<section class="section" style="padding-top: 1rem;">
  <div class="container">
    <div class="cta-banner">
      <h2>Need {plant_name} in Bulk?</h2>
      <p>Tell us your required plant variety, approximate quantity and delivery location. Our nursery team will confirm current availability and provide the wholesale quotation.</p>
      <div class="cta-banner-actions">
        <a href="https://wa.me/919480162989?text=Hello%20Green%20Nest%20Nursery,%20I%20am%20enquiring%20about%20bulk%20{plant_name.replace(' ', '%20')}." target="_blank" rel="noopener" class="btn btn-whatsapp btn-lg">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
          WhatsApp for Wholesale Price
        </a>
        <a href="tel:+919480162989" class="btn btn-outline-white btn-lg">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          Call +91 94801 62989
        </a>
      </div>
    </div>
  </div>
</section>
"""

# =============================================================
# 2. about.html
# =============================================================
about_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="badge-tag accent">Established in Kodagu</div>
    <h1>About Green Nest Avocado/Coffee Nursery</h1>
    <p>Wholesale plant nursery at 7th Hosakote near Kushalnagar, Kodagu, supplying healthy plantation crops and fruit plants across India.</p>
    <div class="breadcrumbs">
      <a href="index.html">Home</a> &gt; <span>About Us</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="spotlight-grid" style="margin-bottom: 4rem;">
      <div class="spotlight-content" style="padding-left: 0;">
        <div class="badge-tag">Nursery Background</div>
        <h2>Rooted in the Heart of Kodagu's Plantation Country</h2>
        <p>Green Nest Avocado/Coffee Nursery is a wholesale plant nursery located at <strong>7th Hosakote near Kushalnagar in Kodagu, Karnataka</strong>.</p>
        <p>We supply avocado, coffee, pepper, areca, silver oak, cardamom, rambutan, litchi and other plantation and fruit plants for farmers, estates, orchards and commercial agricultural projects.</p>
        <p>Our focus is on providing healthy nursery plants, dependable plant availability and convenient bulk supply for growers. Customers can contact us for individual requirements as well as commercial quantities. Bulk plant delivery can also be coordinated across India depending on plant type, quantity, season and destination.</p>
        
        <div style="margin-top: 1.5rem;">
          <a href="contact.html" class="btn btn-primary">Visit Our Nursery &rarr;</a>
        </div>
      </div>
      <div class="spotlight-image">
        <img src="images/787f90a4-7dff-4259-88f1-f6aef6c01ebb.JPG" alt="Green Nest Nursery team inspecting avocado graft" style="border-radius: var(--radius-md);" loading="lazy">
      </div>
    </div>

    <div class="reasons-grid">
      <div class="reason-card">
        <div class="reason-icon">🌱</div>
        <div class="reason-content">
          <h4>Propagation Excellence</h4>
          <p>Carefully selected scions and rootstocks, precision cleft grafting for avocado, and properly hardened nursery stock.</p>
        </div>
      </div>
      <div class="reason-card">
        <div class="reason-icon">🌦️</div>
        <div class="reason-content">
          <h4>Highland Climate Acclimatization</h4>
          <p>Raised in Kodagu's climate, ensuring plants develop sturdy root masses that readily adapt to field planting.</p>
        </div>
      </div>
      <div class="reason-card">
        <div class="reason-icon">🚜</div>
        <div class="reason-content">
          <h4>Estate-Scale Capacity</h4>
          <p>We manage thousands of plants across polyhouses and shaded tunnels to fulfill bulk estate planting schedules.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section-bg">
  <div class="container">
    <div class="section-head">
      <div class="badge-tag">Nursery Operations</div>
      <h2>Inside Our Nursery Facility</h2>
      <p>Look at our nursery shade houses, hardening bays and plant preparation process in Kushalnagar.</p>
    </div>

    <div class="gallery-grid">
      <div class="gallery-item">
        <img src="images/3574ceeb-1850-46fc-8e78-3bb287b365b3.JPG" alt="Nursery avocado beds" loading="lazy">
      </div>
      <div class="gallery-item">
        <img src="images/d68cd26a-d13e-4aed-be7e-04cb50cd66a0.JPG" alt="Cardamom shade house" loading="lazy">
      </div>
      <div class="gallery-item">
        <img src="images/232ed53c-1fa7-45c0-874e-dc74da5d7133.JPG" alt="Coffee seedlings in polybags" loading="lazy">
      </div>
    </div>
  </div>
</section>

{cta_banner_html('Plantation Plants')}
"""

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(render_page(
        title="About Green Nest Nursery | Wholesale Plant Nursery Kodagu",
        description="Green Nest Avocado/Coffee Nursery at 7th Hosakote near Kushalnagar in Kodagu, Karnataka supplies avocado, coffee, pepper, areca and fruit plants in bulk across India.",
        canonical_url="about.html",
        body_content=about_body,
        active_page="about.html"
    ))

# =============================================================
# 3. plants.html (All Plants Catalogue with Filters)
# =============================================================
plants_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="badge-tag accent">Catalogue & Stock</div>
    <h1>Plants Available at Green Nest Nursery</h1>
    <p>Browse healthy, nursery-grown plantation, fruit, spice, and shade tree plants cultivated in Kodagu for commercial growers and estates.</p>
    <div class="breadcrumbs">
      <a href="index.html">Home</a> &gt; <span>Our Plants</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <!-- Category Filter Bar -->
    <div class="filter-nav">
      <button class="filter-btn active" data-filter="all">All Plants</button>
      <button class="filter-btn" data-filter="avocado">Avocado</button>
      <button class="filter-btn" data-filter="coffee">Coffee</button>
      <button class="filter-btn" data-filter="plantation">Plantation Crops</button>
      <button class="filter-btn" data-filter="spices">Spices</button>
      <button class="filter-btn" data-filter="fruits">Fruit Plants</button>
      <button class="filter-btn" data-filter="trees">Trees</button>
    </div>

    <div class="plants-grid">
      <!-- Avocado -->
      <article class="plant-card" data-category="avocado fruits">
        <div class="plant-card-media">
          <span class="plant-tag">Flagship</span>
          <img src="images/cdce181f-6789-47a1-abcc-268d1e585baa.JPG" alt="Avocado plants" loading="lazy">
        </div>
        <div class="plant-card-body">
          <h3 class="plant-card-title">Avocado Plants</h3>
          <p class="plant-card-desc">Premium grafted avocado plants for commercial orchards and estates. Mexican Hass, Ettinger, Pinkerton, Pollock, Supreme Arka, Lamb Hass, Supreme Ravi varieties available.</p>
          <div class="plant-card-actions">
            <a href="avocado-plants.html" class="btn btn-outline btn-sm">View Details &rarr;</a>
            <a href="https://wa.me/919480162989?text=Hello%20Green%20Nest%20Nursery,%20I%20am%20interested%20in%20Avocado%20Plants." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
          </div>
        </div>
      </article>

      <!-- Coffee -->
      <article class="plant-card" data-category="coffee plantation">
        <div class="plant-card-media">
          <span class="plant-tag">Plantation</span>
          <img src="images/232ed53c-1fa7-45c0-874e-dc74da5d7133.JPG" alt="Coffee seedlings" loading="lazy">
        </div>
        <div class="plant-card-body">
          <h3 class="plant-card-title">Coffee Plants</h3>
          <p class="plant-card-desc">Healthy Arabica & Robusta coffee seedlings in polybags for new estates, infilling and replacement planting across South India.</p>
          <div class="plant-card-actions">
            <a href="coffee-plants.html" class="btn btn-outline btn-sm">View Details &rarr;</a>
            <a href="https://wa.me/919480162989?text=Hello%20Green%20Nest%20Nursery,%20I%20am%20interested%20in%20Coffee%20Plants." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
          </div>
        </div>
      </article>

      <!-- Pepper -->
      <article class="plant-card" data-category="spices plantation">
        <div class="plant-card-media">
          <span class="plant-tag">Spices</span>
          <img src="images/1d717b2f-c302-47d6-bc9c-3a795a16784f.JPG" alt="Pepper plants" loading="lazy">
        </div>
        <div class="plant-card-body">
          <h3 class="plant-card-title">Pepper Plants</h3>
          <p class="plant-card-desc">Black pepper rooted cuttings cultivated in polyhouse tunnels. High vigor for trailing on shade and support trees.</p>
          <div class="plant-card-actions">
            <a href="pepper-plants.html" class="btn btn-outline btn-sm">View Details &rarr;</a>
            <a href="https://wa.me/919480162989?text=Hello%20Green%20Nest%20Nursery,%20I%20am%20interested%20in%20Pepper%20Plants." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
          </div>
        </div>
      </article>

      <!-- Areca -->
      <article class="plant-card" data-category="plantation">
        <div class="plant-card-media">
          <span class="plant-tag">Commercial</span>
          <img src="images/2e8e9210-865b-4e33-b0ee-1f1a9c6ebfcd.JPG" alt="Areca plants" loading="lazy">
        </div>
        <div class="plant-card-body">
          <h3 class="plant-card-title">Areca Plants</h3>
          <p class="plant-card-desc">Nursery-grown arecanut saplings for commercial plantations. Deep root systems and uniform growth batches.</p>
          <div class="plant-card-actions">
            <a href="areca-plants.html" class="btn btn-outline btn-sm">View Details &rarr;</a>
            <a href="https://wa.me/919480162989?text=Hello%20Green%20Nest%20Nursery,%20I%20am%20interested%20in%20Areca%20Plants." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
          </div>
        </div>
      </article>

      <!-- Silver Oak -->
      <article class="plant-card" data-category="trees plantation">
        <div class="plant-card-media">
          <span class="plant-tag">Shade Tree</span>
          <img src="images/5a4bd5b2-bece-40cd-8943-75354d8b3944.JPG" alt="Silver oak saplings" loading="lazy">
        </div>
        <div class="plant-card-body">
          <h3 class="plant-card-title">Silver Oak Plants</h3>
          <p class="plant-card-desc">Essential shade and support trees for coffee estates and pepper vines. Fast growing with upright timber structure.</p>
          <div class="plant-card-actions">
            <a href="silver-oak-plants.html" class="btn btn-outline btn-sm">View Details &rarr;</a>
            <a href="https://wa.me/919480162989?text=Hello%20Green%20Nest%20Nursery,%20I%20am%20interested%20in%20Silver%20Oak%20Plants." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
          </div>
        </div>
      </article>

      <!-- Cardamom -->
      <article class="plant-card" data-category="spices plantation">
        <div class="plant-card-media">
          <span class="plant-tag">Spices</span>
          <img src="images/83eec2b4-71c0-4bd3-bd58-5ec64bdb338f.JPG" alt="Cardamom plants" loading="lazy">
        </div>
        <div class="plant-card-body">
          <h3 class="plant-card-title">Cardamom Plants</h3>
          <p class="plant-card-desc">Healthy cardamom planting material nurtured in polybags under controlled shade nets for plantation cultivation.</p>
          <div class="plant-card-actions">
            <a href="cardamom-plants.html" class="btn btn-outline btn-sm">View Details &rarr;</a>
            <a href="https://wa.me/919480162989?text=Hello%20Green%20Nest%20Nursery,%20I%20am%20interested%20in%20Cardamom%20Plants." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
          </div>
        </div>
      </article>

      <!-- Rambutan -->
      <article class="plant-card" data-category="fruits">
        <div class="plant-card-media">
          <span class="plant-tag">Fruit Crop</span>
          <img src="images/rambutan-plant.jpg" alt="Rambutan fruit plants" loading="lazy">
        </div>
        <div class="plant-card-body">
          <h3 class="plant-card-title">Rambutan Plants</h3>
          <p class="plant-card-desc">Grafted rambutan plants suitable for humid tropical regions, farm orchards, and intercropping with irrigation.</p>
          <div class="plant-card-actions">
            <a href="rambutan-plants.html" class="btn btn-outline btn-sm">View Details &rarr;</a>
            <a href="https://wa.me/919480162989?text=Hello%20Green%20Nest%20Nursery,%20I%20am%20interested%20in%20Rambutan%20Plants." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
          </div>
        </div>
      </article>

      <!-- Litchi -->
      <article class="plant-card" data-category="fruits">
        <div class="plant-card-media">
          <span class="plant-tag">Fruit Crop</span>
          <img src="images/litchi-plant.jpg" alt="Litchi fruit plants" loading="lazy">
        </div>
        <div class="plant-card-body">
          <h3 class="plant-card-title">Litchi Plants</h3>
          <p class="plant-card-desc">Commercial litchi layered fruit plants suitable for diversified agricultural land and orchard farming.</p>
          <div class="plant-card-actions">
            <a href="litchi-plants.html" class="btn btn-outline btn-sm">View Details &rarr;</a>
            <a href="https://wa.me/919480162989?text=Hello%20Green%20Nest%20Nursery,%20I%20am%20interested%20in%20Litchi%20Plants." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
          </div>
        </div>
      </article>

      <!-- Orange & Lemon -->
      <article class="plant-card" data-category="fruits">
        <div class="plant-card-media">
          <span class="plant-tag">Citrus</span>
          <img src="images/orange-lemon-plants.jpg" alt="Orange and lemon plants" loading="lazy">
        </div>
        <div class="plant-card-body">
          <h3 class="plant-card-title">Orange & Lemon Plants</h3>
          <p class="plant-card-desc">Healthy orange and lemon nursery plants in polybags. High vigour, well-developed roots for orchards and farm intercropping.</p>
          <div class="plant-card-actions">
            <a href="other-plants.html" class="btn btn-outline btn-sm">View Details &rarr;</a>
            <a href="https://wa.me/919480162989?text=Hello%20Green%20Nest%20Nursery,%20I%20am%20interested%20in%20Orange%20and%20Lemon%20Plants." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
          </div>
        </div>
      </article>

      <!-- Other Plants -->
      <article class="plant-card" data-category="fruits trees">
        <div class="plant-card-media">
          <span class="plant-tag">Variety</span>
          <img src="images/44a33b47-0cc6-458f-9d77-a4d613b9fd18.JPG" alt="Other plantation plants" loading="lazy">
        </div>
        <div class="plant-card-body">
          <h3 class="plant-card-title">Other Plantation & Fruit Plants</h3>
          <p class="plant-card-desc">Mango, Jackfruit, Guava, Sapota, Citrus, Mangosteen, Dragon Fruit, Jamun, and shade forestry saplings.</p>
          <div class="plant-card-actions">
            <a href="other-plants.html" class="btn btn-outline btn-sm">View Details &rarr;</a>
            <a href="https://wa.me/919480162989?text=Hello%20Green%20Nest%20Nursery,%20I%20am%20interested%20in%20Other%20Plants." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
          </div>
        </div>
      </article>
    </div>
  </div>
</section>

{cta_banner_html('Nursery Plants')}
"""

with open('plants.html', 'w', encoding='utf-8') as f:
    f.write(render_page(
        title="Wholesale Plants Catalogue",
        description="Explore wholesale plants available at Green Nest Nursery Kodagu including avocado, coffee, pepper, areca, silver oak, cardamom, rambutan, litchi and more.",
        canonical_url="plants.html",
        body_content=plants_body,
        active_page="plants.html"
    ))

# =============================================================
# 4. avocado-plants.html (Flagship Plant Page)
# =============================================================
avocado_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="badge-tag accent">Flagship Category</div>
    <h1>Avocado Plants for Sale in Kodagu</h1>
    <p>Wholesale avocado plants for farms, orchards, estates and commercial plantation projects across India.</p>
    <div class="breadcrumbs">
      <a href="index.html">Home</a> &gt; <a href="plants.html">Plants</a> &gt; <span>Avocado Plants</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="plant-detail-grid">
      <!-- Media Gallery -->
      <div class="plant-detail-gallery">
        <img src="images/cdce181f-6789-47a1-abcc-268d1e585baa.JPG" alt="Staked grafted avocado saplings at Green Nest Nursery" class="main-preview-img">
        <div class="thumb-row">
          <img src="images/cdce181f-6789-47a1-abcc-268d1e585baa.JPG" alt="Avocado staked saplings" class="thumb-img active">
          <img src="images/3a55609c-2e7b-493f-a146-0c8d3c32da2f.JPG" alt="Grafted avocado stem" class="thumb-img">
          <img src="images/97bb333c-1b71-43cc-a7fe-1039116c56e4.JPG" alt="Planted avocado tree with drip" class="thumb-img">
          <img src="images/b9818c5a-060d-477f-aa82-24ba31d4bec7.JPG" alt="Avocado nursery rows" class="thumb-img">
        </div>
      </div>

      <!-- Content & Specs -->
      <div>
        <div class="badge-tag">Commercial Fruit Crop</div>
        <h2>Commercial Avocado Cultivation & Nursery Supply</h2>
        <p>Avocado is a commercially valuable fruit crop increasingly cultivated in suitable tropical and subtropical regions of India. Green Nest Nursery supplies healthy avocado plants for growers planning small orchards, farm diversification and larger commercial plantations.</p>
        
        <p><strong>Commercial Varieties Available:</strong> Mexican Hass, Ettinger, Pinkerton, Pollock, Supreme Arka, Lamb Hass, and Supreme Ravi varieties are available. Our avocado plants are propagated with vigorous rootstocks and expertly grafted to ensure early bearing, true-to-type fruit quality, and superior field survival. Every plant is hardened in nursery bags with bamboo staking to support healthy upright vegetative growth.</p>

        <!-- Specifications Table -->
        <table class="plant-spec-table">
          <tbody>
            <tr>
              <th>Plant Type</th>
              <td>Avocado (Persea americana)</td>
            </tr>
            <tr>
              <th>Varieties Available</th>
              <td>Mexican Hass, Ettinger, Pinkerton, Pollock, Supreme Arka, Lamb Hass, Supreme Ravi</td>
            </tr>
            <tr>
              <th>Propagation</th>
              <td>Grafted on sturdy rootstocks with bamboo staking</td>
            </tr>
            <tr>
              <th>Container</th>
              <td>Heavy-duty UV nursery polybags with fertile potting mix</td>
            </tr>
            <tr>
              <th>Order Size</th>
              <td>Retail quantities and Commercial Wholesale Bulk Orders</td>
            </tr>
            <tr>
              <th>Planting Spacing</th>
              <td>Recommended 20x20 ft or 18x18 ft depending on orchard layout</td>
            </tr>
            <tr>
              <th>Suitable For</th>
              <td>Commercial Orchards, Estate Infilling, Agroforestry, Farms</td>
            </tr>
            <tr>
              <th>Supply Location</th>
              <td>7th Hosakote, Kushalnagar, Kodagu, Karnataka</td>
            </tr>
            <tr>
              <th>Delivery Support</th>
              <td>Commercial orders across Karnataka, Kerala, Tamil Nadu, Maharashtra and India</td>
            </tr>
          </tbody>
        </table>

        <!-- Interactive WhatsApp Calculator -->
        {whatsapp_calc_box('Avocado Plants', '300')}

        <div style="margin-top: 2rem; padding: 1.5rem; background: #ffffff; border: 1px solid var(--border); border-radius: var(--radius-md);">
          <h4 style="margin-bottom: 0.5rem;">Looking for Companion Plantation Crops?</h4>
          <p style="font-size: 0.92rem; color: var(--text-muted); margin-bottom: 0.75rem;">Growers establishing avocado orchards often plant companion crops. Explore our <a href="coffee-plants.html"><strong>Coffee Plants</strong></a>, <a href="pepper-plants.html"><strong>Pepper Plants</strong></a>, <a href="areca-plants.html"><strong>Areca Plants</strong></a>, <a href="silver-oak-plants.html"><strong>Silver Oak Plants</strong></a>, and <a href="other-plants.html"><strong>Orange & Lemon Plants</strong></a>.</p>
        </div>
      </div>
    </div>
  </div>
</section>

{cta_banner_html('Avocado Plants')}
"""

with open('avocado-plants.html', 'w', encoding='utf-8') as f:
    f.write(render_page(
        title="Avocado Plants for Sale in Kodagu | Wholesale Nursery",
        description="Green Nest Nursery supplies healthy grafted avocado plants in Kodagu for farms, orchards and commercial plantations. Bulk order availability with delivery across India.",
        canonical_url="avocado-plants.html",
        body_content=avocado_body,
        active_page="avocado-plants.html"
    ))

# =============================================================
# 5. coffee-plants.html
# =============================================================
coffee_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="badge-tag accent">Kodagu Heritage</div>
    <h1>Coffee Plants for Sale in Kodagu</h1>
    <p>Wholesale nursery-grown coffee plants for new plantation establishment, estate expansion, gap filling and replacement planting.</p>
    <div class="breadcrumbs">
      <a href="index.html">Home</a> &gt; <a href="plants.html">Plants</a> &gt; <span>Coffee Plants</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="plant-detail-grid">
      <div class="plant-detail-gallery">
        <img src="images/232ed53c-1fa7-45c0-874e-dc74da5d7133.JPG" alt="Coffee plants in nursery polybags" class="main-preview-img">
        <div class="thumb-row">
          <img src="images/232ed53c-1fa7-45c0-874e-dc74da5d7133.JPG" alt="Coffee nursery bags" class="thumb-img active">
          <img src="images/c2b814a3-9b15-44e7-91b4-c6e3e999b269.JPG" alt="Coffee seedling beds" class="thumb-img">
          <img src="images/9f9c61f7-ecd2-4fc2-a6b2-b4ba559d3ab9.JPG" alt="Holding coffee plant" class="thumb-img">
          <img src="images/546f4d9e-a8d6-44d9-9e59-c633a2c83380.JPG" alt="Coffee shipment truck" class="thumb-img">
        </div>
      </div>

      <div>
        <div class="badge-tag">Plantation Crop</div>
        <h2>High-Grade Nursery Coffee Plants in Polybags</h2>
        <p>Green Nest Nursery supplies coffee plants for new coffee plantations, estate expansion, gap filling and replacement planting across Kodagu, Chikkamagaluru, Hassan, Wayanad and other plantation regions.</p>
        
        <p>Our coffee seedlings are raised under scientifically regulated shade to encourage thick root establishment and compact, resilient stems. Polybag grown plants ensure virtually zero root disturbance during field planting, leading to higher field survival rates even during initial monsoon shifts.</p>

        <table class="plant-spec-table">
          <tbody>
            <tr>
              <th>Plant Type</th>
              <td>Coffee (Coffea arabica / Coffea canephora)</td>
            </tr>
            <tr>
              <th>Form</th>
              <td>Polybags with rich compost and local estate soil</td>
            </tr>
            <tr>
              <th>Order Quantities</th>
              <td>Bulk wholesale orders (1,000 to 50,000+ plants)</td>
            </tr>
            <tr>
              <th>Best Planting Time</th>
              <td>Pre-monsoon and monsoon seasons (June – September)</td>
            </tr>
            <tr>
              <th>Suitable Region</th>
              <td>Western Ghats, elevated hill tracts, shaded agroforestry</td>
            </tr>
            <tr>
              <th>Transport</th>
              <td>Pickup truck, open truckloads or collection at Kushalnagar nursery</td>
            </tr>
          </tbody>
        </table>

        {whatsapp_calc_box('Coffee Plants', '1000')}

        <div style="margin-top: 2rem; padding: 1.5rem; background: #ffffff; border: 1px solid var(--border); border-radius: var(--radius-md);">
          <h4 style="margin-bottom: 0.5rem;">Associated Estate Plants</h4>
          <p style="font-size: 0.92rem; color: var(--text-muted);">Complement your coffee estate with <a href="silver-oak-plants.html"><strong>Silver Oak Plants</strong></a> for shade, <a href="pepper-plants.html"><strong>Pepper Plants</strong></a> for high-revenue intercropping, and <a href="avocado-plants.html"><strong>Avocado Plants</strong></a>.</p>
        </div>
      </div>
    </div>
  </div>
</section>

{cta_banner_html('Coffee Plants')}
"""

with open('coffee-plants.html', 'w', encoding='utf-8') as f:
    f.write(render_page(
        title="Coffee Plants for Sale in Kodagu | Green Nest Nursery",
        description="Green Nest Nursery in Kodagu supplies coffee plants in bulk for coffee estates, farm expansion and replacement planting. Enquire for wholesale price.",
        canonical_url="coffee-plants.html",
        body_content=coffee_body,
        active_page="coffee-plants.html"
    ))

# =============================================================
# 6. pepper-plants.html
# =============================================================
pepper_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="badge-tag accent">High Value Spice</div>
    <h1>Pepper Plants for Wholesale Supply</h1>
    <p>Healthy black pepper planting material for estate cultivation and intercropping on silver oak and areca trees.</p>
    <div class="breadcrumbs">
      <a href="index.html">Home</a> &gt; <a href="plants.html">Plants</a> &gt; <span>Pepper Plants</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="plant-detail-grid">
      <div class="plant-detail-gallery">
        <img src="images/1d717b2f-c302-47d6-bc9c-3a795a16784f.JPG" alt="Pepper plants in polyhouse tunnel" class="main-preview-img">
        <div class="thumb-row">
          <img src="images/1d717b2f-c302-47d6-bc9c-3a795a16784f.JPG" alt="Pepper polyhouse" class="thumb-img active">
          <img src="images/354aeed0-3105-4071-8f65-a242b10a2455.JPG" alt="Pepper rooted cutting in bag" class="thumb-img">
          <img src="images/b88a9f11-ea17-406a-bb00-ff29a0d7a8ef.JPG" alt="Pepper cuttings beds" class="thumb-img">
          <img src="images/3c5e1c9a-24e8-476c-a8fe-fa28cd3dbfc3.JPG" alt="Pepper hoop house" class="thumb-img">
        </div>
      </div>

      <div>
        <div class="badge-tag">Spice Crop</div>
        <h2>Healthy Rooted Black Pepper Vine Cuttings</h2>
        <p>Black pepper (Piper nigrum) is one of the most profitable intercrops in coffee and arecanut plantations. Green Nest Nursery supplies vigorous rooted pepper cuttings grown in polythene bags under protective hoop polyhouses.</p>
        
        <p>Our cuttings are prepared from healthy runner shoots, rooted with precision moisture management, and hardened to ensure rapid climbing and establishment once trailed onto silver oak or areca standards.</p>

        <table class="plant-spec-table">
          <tbody>
            <tr>
              <th>Crop</th>
              <td>Black Pepper (Piper nigrum)</td>
            </tr>
            <tr>
              <th>Planting Material</th>
              <td>Rooted cuttings in nursery polybags</td>
            </tr>
            <tr>
              <th>Support Trees</th>
              <td>Silver Oak, Arecanut, Erythrina, Gliricidia</td>
            </tr>
            <tr>
              <th>Availability</th>
              <td>Bulk wholesale batches ready for field planting</td>
            </tr>
            <tr>
              <th>Location</th>
              <td>Kushalnagar, Kodagu, Karnataka</td>
            </tr>
          </tbody>
        </table>

        {whatsapp_calc_box('Black Pepper Plants', '500')}

        <div style="margin-top: 2rem; padding: 1.5rem; background: #ffffff; border: 1px solid var(--border); border-radius: var(--radius-md);">
          <h4 style="margin-bottom: 0.5rem;">Recommended Support Trees</h4>
          <p style="font-size: 0.92rem; color: var(--text-muted);">Pepper vines need reliable support standards. Order <a href="silver-oak-plants.html"><strong>Silver Oak Plants</strong></a> and <a href="areca-plants.html"><strong>Areca Plants</strong></a> along with your pepper order for seamless plantation establishment.</p>
        </div>
      </div>
    </div>
  </div>
</section>

{cta_banner_html('Pepper Plants')}
"""

with open('pepper-plants.html', 'w', encoding='utf-8') as f:
    f.write(render_page(
        title="Pepper Plants for Sale in Kodagu | Wholesale Supply",
        description="Source healthy rooted black pepper plants in polybags from Green Nest Nursery in Kodagu. Wholesale supply for coffee and areca plantations.",
        canonical_url="pepper-plants.html",
        body_content=pepper_body,
        active_page="pepper-plants.html"
    ))

# =============================================================
# 7. areca-plants.html
# =============================================================
areca_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="badge-tag accent">Commercial Plantation</div>
    <h1>Areca Plants for Commercial Plantations</h1>
    <p>Nursery-grown arecanut plants for commercial cultivation, replacement planting and farm development in Karnataka and India.</p>
    <div class="breadcrumbs">
      <a href="index.html">Home</a> &gt; <a href="plants.html">Plants</a> &gt; <span>Areca Plants</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="plant-detail-grid">
      <div class="plant-detail-gallery">
        <img src="images/2e8e9210-865b-4e33-b0ee-1f1a9c6ebfcd.JPG" alt="Areca nut nursery plants" class="main-preview-img">
        <div class="thumb-row">
          <img src="images/2e8e9210-865b-4e33-b0ee-1f1a9c6ebfcd.JPG" alt="Areca nursery rows" class="thumb-img active">
          <img src="images/04cfdbd5-e7c1-4679-b182-43332cce8a02.JPG" alt="Truckload of areca plants" class="thumb-img">
          <img src="images/6bbb1d1f-f80a-4ca8-bb25-2473fdf21a81.JPG" alt="Areca plants in transport bags" class="thumb-img">
          <img src="images/2a2ea4d7-0a1b-4ddf-b0f8-75f0d58c4408.JPG" alt="Areca seedlings close-up" class="thumb-img">
        </div>
      </div>

      <div>
        <div class="badge-tag">Plantation Palm</div>
        <h2>Commercial Arecanut Seedlings in Polybags</h2>
        <p>Green Nest Nursery supplies healthy, vigorous arecanut (Areca catechu) seedlings selected from high-yielding mother palms. Raised in deep nursery bags, these plants display robust root collars and vibrant fronds ready for field planting.</p>
        
        <p>Whether you are establishing a new multi-acre areca plantation or replacing older palms, we offer bulk wholesale quantities with complete vehicle loading support directly at our nursery.</p>

        <table class="plant-spec-table">
          <tbody>
            <tr>
              <th>Plant</th>
              <td>Areca Nut / Betel Nut Palm (Areca catechu)</td>
            </tr>
            <tr>
              <th>Container</th>
              <td>Heavy polybags for complete root protection</td>
            </tr>
            <tr>
              <th>Quantity</th>
              <td>Commercial wholesale volumes (truckloads available)</td>
            </tr>
            <tr>
              <th>Planting Distance</th>
              <td>Commonly 9x9 ft spacing</td>
            </tr>
            <tr>
              <th>Logistics</th>
              <td>Vehicle loading and nationwide delivery coordination</td>
            </tr>
          </tbody>
        </table>

        {whatsapp_calc_box('Areca Nut Plants', '1000')}
      </div>
    </div>
  </div>
</section>

{cta_banner_html('Areca Plants')}
"""

with open('areca-plants.html', 'w', encoding='utf-8') as f:
    f.write(render_page(
        title="Areca Plants for Sale in Karnataka | Green Nest Nursery",
        description="Buy commercial arecanut plants in bulk from Green Nest Nursery in Kodagu. Uniform, healthy polybag seedlings ready for large plantation projects.",
        canonical_url="areca-plants.html",
        body_content=areca_body,
        active_page="areca-plants.html"
    ))

# =============================================================
# 8. silver-oak-plants.html
# =============================================================
silver_oak_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="badge-tag accent">Estate Essential</div>
    <h1>Silver Oak Plants for Coffee Estates & Plantations</h1>
    <p>Popular shade and pepper support trees grown in Kodagu for coffee estates, boundaries and agroforestry plantations.</p>
    <div class="breadcrumbs">
      <a href="index.html">Home</a> &gt; <a href="plants.html">Plants</a> &gt; <span>Silver Oak Plants</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="plant-detail-grid">
      <div class="plant-detail-gallery">
        <img src="images/5a4bd5b2-bece-40cd-8943-75354d8b3944.JPG" alt="Silver oak nursery saplings" class="main-preview-img">
      </div>

      <div>
        <div class="badge-tag">Shade & Timber Tree</div>
        <h2>Vital Canopy & Pepper Support for Estates</h2>
        <p>Silver Oak (Grevillea robusta) is an indispensable species across South Indian coffee and pepper plantations. Its straight vertical growth habit provides light dappled shade that protects coffee bushes from excessive heat without competing excessively for ground nutrients.</p>
        
        <p>Additionally, its rough bark offers the ideal natural standard for black pepper vines, creating a double-yielding plantation ecosystem. Green Nest Nursery supplies sturdy, straight-stemmed silver oak saplings in polybags for high survival rates.</p>

        <table class="plant-spec-table">
          <tbody>
            <tr>
              <th>Botanical Name</th>
              <td>Grevillea robusta (Silver Oak)</td>
            </tr>
            <tr>
              <th>Role</th>
              <td>Estate Shade Tree, Pepper Support Standard, Farm Boundary, Timber</td>
            </tr>
            <tr>
              <th>Growth Rate</th>
              <td>Fast-growing, upright habit</td>
            </tr>
            <tr>
              <th>Packaging</th>
              <td>Nursery polybags for easy transit and planting</td>
            </tr>
            <tr>
              <th>Order Size</th>
              <td>Bulk quantities for estate boundaries and field blocks</td>
            </tr>
          </tbody>
        </table>

        {whatsapp_calc_box('Silver Oak Plants', '500')}
      </div>
    </div>
  </div>
</section>

{cta_banner_html('Silver Oak Plants')}
"""

with open('silver-oak-plants.html', 'w', encoding='utf-8') as f:
    f.write(render_page(
        title="Silver Oak Plants for Coffee Estates | Green Nest Nursery",
        description="Wholesale Silver Oak saplings in Kodagu for coffee estate shade and black pepper vine support. Bulk supply with delivery across India.",
        canonical_url="silver-oak-plants.html",
        body_content=silver_oak_body,
        active_page="silver-oak-plants.html"
    ))

# =============================================================
# 9. cardamom-plants.html
# =============================================================
cardamom_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="badge-tag accent">Queen of Spices</div>
    <h1>Cardamom Plants for Plantation Cultivation</h1>
    <p>Healthy nursery cardamom planting material suitable for high-rainfall, shaded plantation cultivation.</p>
    <div class="breadcrumbs">
      <a href="index.html">Home</a> &gt; <a href="plants.html">Plants</a> &gt; <span>Cardamom Plants</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="plant-detail-grid">
      <div class="plant-detail-gallery">
        <img src="images/83eec2b4-71c0-4bd3-bd58-5ec64bdb338f.JPG" alt="Cardamom nursery plants under shade net" class="main-preview-img">
        <div class="thumb-row">
          <img src="images/83eec2b4-71c0-4bd3-bd58-5ec64bdb338f.JPG" alt="Cardamom nursery plants" class="thumb-img active">
          <img src="images/d68cd26a-d13e-4aed-be7e-04cb50cd66a0.JPG" alt="Cardamom shade net house" class="thumb-img">
          <img src="images/2c272268-2ed3-431c-bc13-ce1f95e79ce4.JPG" alt="Cardamom slips" class="thumb-img">
          <img src="images/a1778f73-b88a-42df-b2f0-538598b78630.JPG" alt="Cardamom nursery bed" class="thumb-img">
        </div>
      </div>

      <div>
        <div class="badge-tag">Spice Crop</div>
        <h2>Vigorous Cardamom Slips in Polybags</h2>
        <p>Small cardamom (Elettaria cardamomum) thrives in the moist, shaded valleys and lower canopies of Kodagu and Western Ghats plantations. Green Nest Nursery nurtures cardamom plants inside dedicated shade net houses to protect foliage from sun scorch and maintain healthy tiller proliferation.</p>
        
        <p>Our plants are supplied with intact root masses in soil-filled polybags, giving growers a head start compared to bare-root suckers.</p>

        <table class="plant-spec-table">
          <tbody>
            <tr>
              <th>Botanical Name</th>
              <td>Elettaria cardamomum (Cardamom)</td>
            </tr>
            <tr>
              <th>Planting Material</th>
              <td>Healthy nursery-grown tillers in polybags</td>
            </tr>
            <tr>
              <th>Environment</th>
              <td>Dappled shade, high humidity, well-drained loamy soil</td>
            </tr>
            <tr>
              <th>Order Type</th>
              <td>Wholesale plantation orders</td>
            </tr>
            <tr>
              <th>Origin</th>
              <td>Kushalnagar, Kodagu, Karnataka</td>
            </tr>
          </tbody>
        </table>

        {whatsapp_calc_box('Cardamom Plants', '500')}
      </div>
    </div>
  </div>
</section>

{cta_banner_html('Cardamom Plants')}
"""

with open('cardamom-plants.html', 'w', encoding='utf-8') as f:
    f.write(render_page(
        title="Cardamom Plants for Plantation Cultivation | Kodagu Nursery",
        description="Source healthy nursery-grown cardamom plants in polybags from Green Nest Nursery in Kodagu. Ideal for plantation valleys and shaded estates.",
        canonical_url="cardamom-plants.html",
        body_content=cardamom_body,
        active_page="cardamom-plants.html"
    ))

# =============================================================
# 10. rambutan-plants.html
# =============================================================
rambutan_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="badge-tag accent">Exotic Fruit Crop</div>
    <h1>Rambutan Plants for Farms & Orchards</h1>
    <p>High-value grafted tropical fruit plants suitable for commercial orchards, farm diversification and agri-tourism estates.</p>
    <div class="breadcrumbs">
      <a href="index.html">Home</a> &gt; <a href="plants.html">Plants</a> &gt; <span>Rambutan Plants</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="plant-detail-grid">
      <div class="plant-detail-gallery">
        <img src="images/rambutan-plant.jpg" alt="Healthy grafted rambutan plant sapling at Green Nest Nursery" class="main-preview-img">
      </div>

      <div>
        <div class="badge-tag">Orchard Fruit</div>
        <h2>High-Yielding Grafted Rambutan Fruit Trees</h2>
        <p>Rambutan (Nephelium lappaceum) has emerged as one of the most lucrative tropical fruit crops across South India. With strong consumer demand and excellent market prices, establishing a rambutan orchard or integrating rambutan alongside avocado and coffee delivers strong financial returns.</p>
        
        <p>Green Nest Nursery supplies healthy grafted rambutan saplings in polybags. Grafted stock ensures true-to-type, sweet, juicy fruit characteristics and early fruiting within 2 to 3 years.</p>

        <table class="plant-spec-table">
          <tbody>
            <tr>
              <th>Plant</th>
              <td>Rambutan (Nephelium lappaceum)</td>
            </tr>
            <tr>
              <th>Type</th>
              <td>Grafted commercial fruit varieties</td>
            </tr>
            <tr>
              <th>Climate</th>
              <td>Warm, humid tropical climate with adequate water</td>
            </tr>
            <tr>
              <th>Supply</th>
              <td>Retail & Wholesale quantities for commercial orchards</td>
            </tr>
            <tr>
              <th>Hub</th>
              <td>Kushalnagar, Kodagu</td>
            </tr>
          </tbody>
        </table>

        {whatsapp_calc_box('Rambutan Plants', '100')}
      </div>
    </div>
  </div>
</section>

{cta_banner_html('Rambutan Plants')}
"""

with open('rambutan-plants.html', 'w', encoding='utf-8') as f:
    f.write(render_page(
        title="Rambutan Plants for Farms & Orchards | Green Nest Nursery",
        description="Commercial grafted rambutan fruit plants from Green Nest Nursery in Kodagu. Wholesale availability for commercial orchards and farm diversification.",
        canonical_url="rambutan-plants.html",
        body_content=rambutan_body,
        active_page="rambutan-plants.html"
    ))

# =============================================================
# 11. litchi-plants.html
# =============================================================
litchi_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="badge-tag accent">Commercial Orchard</div>
    <h1>Litchi Plants for Farms & Fruit Orchards</h1>
    <p>Layered and grafted litchi fruit plants suitable for commercial orchards and fruit growers.</p>
    <div class="breadcrumbs">
      <a href="index.html">Home</a> &gt; <a href="plants.html">Plants</a> &gt; <span>Litchi Plants</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="plant-detail-grid">
      <div class="plant-detail-gallery">
        <img src="images/litchi-plant.jpg" alt="Healthy litchi plant sapling at Green Nest Nursery" class="main-preview-img">
      </div>

      <div>
        <div class="badge-tag">Fruit Crop</div>
        <h2>High-Return Commercial Litchi Saplings</h2>
        <p>Litchi (Litchi chinensis) is a delicious, commercially sought-after fruit crop well suited for regions with distinct seasons and good water availability. Green Nest Nursery supplies hardened litchi plants propagated through air-layering and grafting for consistent fruit quality.</p>

        <table class="plant-spec-table">
          <tbody>
            <tr>
              <th>Crop</th>
              <td>Litchi (Litchi chinensis)</td>
            </tr>
            <tr>
              <th>Propagation</th>
              <td>Air-layered / Grafted stock in polybags</td>
            </tr>
            <tr>
              <th>Availability</th>
              <td>Subject to seasonal batch maturity</td>
            </tr>
            <tr>
              <th>Order Size</th>
              <td>Commercial wholesale and retail batches</td>
            </tr>
          </tbody>
        </table>

        {whatsapp_calc_box('Litchi Plants', '100')}
      </div>
    </div>
  </div>
</section>

{cta_banner_html('Litchi Plants')}
"""

with open('litchi-plants.html', 'w', encoding='utf-8') as f:
    f.write(render_page(
        title="Litchi Plants for Commercial Orchards | Green Nest Nursery",
        description="Buy healthy litchi fruit plants in bulk from Green Nest Nursery in Kodagu. High quality planting material for fruit growers and commercial orchards.",
        canonical_url="litchi-plants.html",
        body_content=litchi_body,
        active_page="litchi-plants.html"
    ))

# =============================================================
# 12. other-plants.html
# =============================================================
other_plants_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="badge-tag accent">Comprehensive Nursery Inventory</div>
    <h1>Other Fruit & Plantation Plants</h1>
    <p>Discover our extended selection of commercial fruit varieties including Orange & Lemon plants, spices, and estate shade trees available at Green Nest Nursery.</p>
    <div class="breadcrumbs">
      <a href="index.html">Home</a> &gt; <a href="plants.html">Plants</a> &gt; <span>Other Plants</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="badge-tag">Featured Citrus</div>
      <h2>Orange & Lemon Plants Now Available</h2>
      <p>Along with our flagship avocado, coffee, and pepper inventory, Green Nest supplies healthy, vigorous citrus plants ready for orchards, estates, and farm planting.</p>
    </div>

    <!-- Featured Spotlight: Orange & Lemon Plants -->
    <div class="spotlight-grid" style="margin-bottom: 3.5rem; background: #ffffff; padding: 2rem; border-radius: var(--radius-lg); border: 1px solid var(--border); display: grid; grid-template-columns: 1fr 1fr; gap: 2.5rem; align-items: center;">
      <div class="spotlight-image">
        <img src="images/orange-lemon-plants.jpg" alt="Healthy orange and lemon nursery plants in Kodagu" style="width: 100%; border-radius: var(--radius-md); object-fit: cover;" loading="lazy">
      </div>
      <div class="spotlight-content">
        <div class="badge-tag">Citrus Specialty</div>
        <h2>Healthy Orange & Lemon Nursery Plants</h2>
        <p>Green Nest Nursery supplies healthy nursery-grown <strong>Orange and Lemon plants</strong> in sturdy root bags. Our citrus saplings feature strong, active root systems, vibrant foliage, and robust disease resilience, acclimatized in the Kodagu microclimate.</p>
        <p>Ideal for commercial citrus orchard cultivation, intercropping in coffee and areca estates, and farm diversification projects across South India and nationwide.</p>
        <div style="margin-top: 1.5rem;">
          <a href="https://wa.me/919480162989?text=Hello%20Green%20Nest%20Nursery,%20I%20am%20interested%20in%20Orange%20and%20Lemon%20Plants.%20Please%20share%20bulk%20availability%20and%20prices." target="_blank" rel="noopener" class="btn btn-whatsapp">
            WhatsApp Orange & Lemon Enquiry
          </a>
        </div>
      </div>
    </div>

    <div class="reasons-grid" style="margin-bottom: 3.5rem;">
      <div class="reason-card">
        <div class="reason-icon">🍊</div>
        <div class="reason-content">
          <h4>Fruit & Citrus Plants</h4>
          <p>Orange and Lemon plants are actively available, alongside Mango (commercial grafted varieties), Jackfruit (All-season / gumless), Guava (Taiwan Pink, VNR Bihi), Sapota (Cricket Ball, Kalipatti), Mangosteen, Dragon Fruit, and Jamun.</p>
        </div>
      </div>

      <div class="reason-card">
        <div class="reason-icon">☕</div>
        <div class="reason-content">
          <h4>Plantation Crops</h4>
          <p>Commercial selections of Coffee, Black Pepper rooted cuttings, Arecanut, and Cardamom for commercial farm layouts.</p>
        </div>
      </div>

      <div class="reason-card">
        <div class="reason-icon">🌲</div>
        <div class="reason-content">
          <h4>Shade & Forestry Trees</h4>
          <p>Silver Oak, Albizia, native shade trees, and boundary windbreak plants to protect crops from wind and thermal stress.</p>
        </div>
      </div>
    </div>

    {whatsapp_calc_box('Other Fruit & Tree Varieties', '250')}
  </div>
</section>

{cta_banner_html('Other Plants')}
"""

with open('other-plants.html', 'w', encoding='utf-8') as f:
    f.write(render_page(
        title="Other Plantation & Fruit Plants | Green Nest Nursery Kodagu",
        description="Browse additional fruit and shade trees at Green Nest Nursery including orange, lemon, mango, jackfruit, guava, sapota, citrus and timber trees in bulk.",
        canonical_url="other-plants.html",
        body_content=other_plants_body,
        active_page="other-plants.html"
    ))

# =============================================================
# 13. wholesale-plants.html
# =============================================================
wholesale_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="badge-tag accent">B2B & Estate Scale</div>
    <h1>Wholesale Plant Nursery in Kodagu</h1>
    <p>Bulk plant supply for farmers, estate owners, agricultural businesses, orchard developers and commercial plantation projects.</p>
    <div class="breadcrumbs">
      <a href="index.html">Home</a> &gt; <span>Wholesale Supply</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="spotlight-grid" style="margin-bottom: 4rem;">
      <div class="spotlight-content" style="padding-left: 0;">
        <div class="badge-tag">Bulk Sourcing</div>
        <h2>Direct Nursery-to-Farm Bulk Plant Supply</h2>
        <p>Green Nest Nursery specialises in bulk supply of plantation and fruit plants for agricultural enterprises, plantation owners, institutions and progressive farmers.</p>
        <p>By buying directly from our wholesale nursery in Kushalnagar, growers benefit from:</p>
        <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.75rem; margin: 1.25rem 0;">
          <li style="display: flex; align-items: center; gap: 0.6rem;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="color: var(--leaf);"><polyline points="20 6 9 17 4 12"/></svg>
            <strong>Uniform Batch Maturity:</strong> Consistent plant height and root development for even orchard growth.
          </li>
          <li style="display: flex; align-items: center; gap: 0.6rem;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="color: var(--leaf);"><polyline points="20 6 9 17 4 12"/></svg>
            <strong>Volume Wholesale Pricing:</strong> Tiered discounts for large-scale estate and orchard planting.
          </li>
          <li style="display: flex; align-items: center; gap: 0.6rem;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="color: var(--leaf);"><polyline points="20 6 9 17 4 12"/></svg>
            <strong>Vehicle Loading Support:</strong> Organized truck bed loading to protect saplings during transit.
          </li>
          <li style="display: flex; align-items: center; gap: 0.6rem;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="color: var(--leaf);"><polyline points="20 6 9 17 4 12"/></svg>
            <strong>Advance Booking:</strong> Reserve upcoming batches for your planned planting season.
          </li>
        </ul>
      </div>
      <div class="spotlight-image">
        <img src="images/04cfdbd5-e7c1-4679-b182-43332cce8a02.JPG" alt="Wholesale plant truck dispatch" style="border-radius: var(--radius-md);" loading="lazy">
      </div>
    </div>

    <!-- Target Audience Cards -->
    <div class="section-head">
      <div class="badge-tag">Who We Supply</div>
      <h2>Serving Commercial Agricultural Partners</h2>
    </div>

    <div class="reasons-grid" style="margin-bottom: 3rem;">
      <div class="reason-card">
        <div class="reason-icon">👨‍🌾</div>
        <div class="reason-content">
          <h4>Commercial Farmers</h4>
          <p>Farmers expanding into high-margin fruit crops like avocado and rambutan.</p>
        </div>
      </div>
      <div class="reason-card">
        <div class="reason-icon">☕</div>
        <div class="reason-content">
          <h4>Coffee & Spice Estates</h4>
          <p>Estate owners replacing ageing coffee bushes and trailing pepper vines on silver oak.</p>
        </div>
      </div>
      <div class="reason-card">
        <div class="reason-icon">🌴</div>
        <div class="reason-content">
          <h4>Arecanut Growers</h4>
          <p>Uniform betel nut palm saplings for high-density plantation setups.</p>
        </div>
      </div>
      <div class="reason-card">
        <div class="reason-icon">🏡</div>
        <div class="reason-content">
          <h4>Farmhouse & Orchard Developers</h4>
          <p>Bulk fruit and shade tree packages for managed farmland and agri-tourism projects.</p>
        </div>
      </div>
      <div class="reason-card">
        <div class="reason-icon">🤝</div>
        <div class="reason-content">
          <h4>Agricultural Consultants</h4>
          <p>Dependable nursery partner for client orchard planning and implementation.</p>
        </div>
      </div>
      <div class="reason-card">
        <div class="reason-icon">🚛</div>
        <div class="reason-content">
          <h4>Plantation Logistics Buyers</h4>
          <p>Full truckload direct dispatch across South India and pan-India destinations.</p>
        </div>
      </div>
    </div>

    {whatsapp_calc_box('Wholesale Bulk Order', '1000')}
  </div>
</section>

{cta_banner_html('Wholesale Plant Supply')}
"""

with open('wholesale-plants.html', 'w', encoding='utf-8') as f:
    f.write(render_page(
        title="Wholesale Plant Nursery in Kodagu | Bulk Plant Supplier",
        description="Wholesale plant nursery in Kodagu supplying commercial quantities of avocado, coffee, pepper, areca and fruit plants with vehicle dispatch across India.",
        canonical_url="wholesale-plants.html",
        body_content=wholesale_body,
        active_page="wholesale-plants.html"
    ))

# =============================================================
# 14. commercial-plantation.html
# =============================================================
commercial_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="badge-tag accent">Estate Establishment</div>
    <h1>Commercial Plantation Supply & Advisory</h1>
    <p>Planning a new orchard or expanding an estate? Green Nest Nursery provides plant sourcing, spacing recommendations and bulk supply.</p>
    <div class="breadcrumbs">
      <a href="index.html">Home</a> &gt; <span>Commercial Plantation</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="spotlight-grid" style="margin-bottom: 4rem;">
      <div class="spotlight-image">
        <img src="images/97bb333c-1b71-43cc-a7fe-1039116c56e4.JPG" alt="Thriving avocado tree in commercial orchard" style="border-radius: var(--radius-md);" loading="lazy">
      </div>
      <div class="spotlight-content">
        <div class="badge-tag">Plantation Planning</div>
        <h2>Setting Up High-Performing Commercial Plantations</h2>
        <p>Whether you are establishing a new avocado orchard, expanding a coffee estate or sourcing plantation crops such as pepper, areca, cardamom or silver oak, Green Nest Nursery can assist with bulk plant requirements.</p>
        <p>Commercial plantations require careful planning, soil assessment, drainage preparation, and synchronized delivery so that saplings can be planted promptly during optimal weather windows.</p>
        
        <div style="margin-top: 1.5rem;">
          <a href="https://wa.me/919480162989?text=Hello%20Green%20Nest%20Nursery,%20I%20am%20planning%20a%20new%20commercial%20plantation%20and%20need%20bulk%20plants." target="_blank" rel="noopener" class="btn btn-whatsapp">
            Discuss Plantation Project on WhatsApp
          </a>
        </div>
      </div>
    </div>

    <!-- 4-Step Process -->
    <div class="section-head">
      <div class="badge-tag">Simple Process</div>
      <h2>How We Support Your Plantation Project</h2>
    </div>

    <div class="supply-process-grid">
      <div class="process-card">
        <div class="process-number">01</div>
        <h4>Tell us your requirement</h4>
        <p>Specify crop types (e.g. Avocado + Coffee + Pepper), total acreage or plant count, and your farm location.</p>
      </div>
      <div class="process-card">
        <div class="process-number">02</div>
        <h4>Check nursery availability</h4>
        <p>We review current nursery batches and schedule maturity to match your land preparation timetable.</p>
      </div>
      <div class="process-card">
        <div class="process-number">03</div>
        <h4>Receive quotation & terms</h4>
        <p>Clear wholesale pricing with logistics breakdown, batch reservation terms, and transport estimates.</p>
      </div>
      <div class="process-card">
        <div class="process-number">04</div>
        <h4>Coordinated supply & dispatch</h4>
        <p>Carefully packed saplings delivered to your plantation gate or loaded at our Kushalnagar nursery.</p>
      </div>
    </div>
  </div>
</section>

{cta_banner_html('Commercial Plantation Supply')}
"""

with open('commercial-plantation.html', 'w', encoding='utf-8') as f:
    f.write(render_page(
        title="Commercial Plantation Supply & Planning | Kodagu Nursery",
        description="Plan your new avocado orchard, coffee estate or spice plantation with Green Nest Nursery in Kodagu. Bulk nursery supply and delivery support across India.",
        canonical_url="commercial-plantation.html",
        body_content=commercial_body,
        active_page="commercial-plantation.html"
    ))

# =============================================================
# 15. bulk-plant-delivery.html
# =============================================================
delivery_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="badge-tag accent">Logistics & Transport</div>
    <h1>Bulk Plant Delivery Across India</h1>
    <p>Safe transportation of nursery-grown avocado, coffee, pepper, and plantation plants to farms and estates across India.</p>
    <div class="breadcrumbs">
      <a href="index.html">Home</a> &gt; <span>India Delivery</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="spotlight-grid" style="margin-bottom: 4rem;">
      <div class="spotlight-content" style="padding-left: 0;">
        <div class="badge-tag">Pan-India Supply</div>
        <h2>Safe, Coordinated Bulk Plant Transportation</h2>
        <p>Green Nest Nursery accepts commercial bulk enquiries from customers across India. Depending on the plant variety, quantity, season and destination, transportation can be arranged for suitable commercial orders.</p>
        
        <p>Plants are thoroughly watered and packed securely in open-bed or tarpaulin-shaded transport trucks to prevent root damage, stem breakage and transit shock.</p>

        <div style="background: var(--primary-soft); padding: 1.25rem; border-radius: var(--radius-sm); border: 1px solid rgba(27,67,50,0.15); margin: 1.5rem 0;">
          <p style="margin: 0; font-size: 0.92rem; color: var(--primary-dark);"><strong>Important Note:</strong> Because plant transit requires suitable weather and route planning, transportation feasibility and logistics arrangements are confirmed individually prior to dispatch.</p>
        </div>
      </div>
      <div class="spotlight-image">
        <img src="images/6a683486-e201-494a-869a-7226520f696f.JPG" alt="Commercial truck loaded with nursery plants for interstate dispatch" style="border-radius: var(--radius-md);" loading="lazy">
      </div>
    </div>

    <!-- Destinations -->
    <div class="section-head">
      <div class="badge-tag">Service Regions</div>
      <h2>Key Destinations We Serve</h2>
      <p>We regularly coordinate bulk dispatches to plantation regions and commercial farm clusters.</p>
    </div>

    <div class="reasons-grid" style="margin-bottom: 3.5rem;">
      <div class="reason-card">
        <div class="reason-icon">📍</div>
        <div class="reason-content">
          <h4>Karnataka</h4>
          <p>Kodagu, Mysuru, Hassan, Chikkamagaluru, Shivamogga, Belagavi, Bengaluru, Mandya, and coastal belts.</p>
        </div>
      </div>
      <div class="reason-card">
        <div class="reason-icon">📍</div>
        <div class="reason-content">
          <h4>Kerala</h4>
          <p>Wayanad, Idukki, Palakkad, Kannur, Kasaragod, and high-range spice/coffee tracts.</p>
        </div>
      </div>
      <div class="reason-card">
        <div class="reason-icon">📍</div>
        <div class="reason-content">
          <h4>Tamil Nadu</h4>
          <p>The Nilgiris, Ooty, Kodaikanal, Yercaud, Coimbatore, and Dindigul orchard belts.</p>
        </div>
      </div>
      <div class="reason-card">
        <div class="reason-icon">📍</div>
        <div class="reason-content">
          <h4>Goa & Maharashtra</h4>
          <p>Sindhudurg, Ratnagiri, Kolhapur, Pune, and coastal horticultural farms.</p>
        </div>
      </div>
      <div class="reason-card">
        <div class="reason-icon">📍</div>
        <div class="reason-content">
          <h4>Andhra Pradesh & Telangana</h4>
          <p>Araku Valley, Chittoor, and commercial agroforestry projects.</p>
        </div>
      </div>
      <div class="reason-card">
        <div class="reason-icon">📍</div>
        <div class="reason-content">
          <h4>Other Indian States</h4>
          <p>Bulk shipments evaluated based on quantity, distance, and direct truckload transit time.</p>
        </div>
      </div>
    </div>

    {whatsapp_calc_box('Bulk Delivery Enquiry', '500')}
  </div>
</section>

{cta_banner_html('Bulk Plant Delivery')}
"""

with open('bulk-plant-delivery.html', 'w', encoding='utf-8') as f:
    f.write(render_page(
        title="Bulk Plants Supplier in India | Green Nest Nursery Kodagu",
        description="Bulk plant supply and delivery across India from Green Nest Nursery in Kodagu. Coordinated transportation for avocado, coffee, areca and plantation plants.",
        canonical_url="bulk-plant-delivery.html",
        body_content=delivery_body,
        active_page="bulk-plant-delivery.html"
    ))

# =============================================================
# 16. gallery.html
# =============================================================
gallery_photos = [
    ("b9818c5a-060d-477f-aa82-24ba31d4bec7.JPG", "Avocado Nursery Field", "Thousands of healthy avocado saplings under shade net", "avocado nursery"),
    ("cdce181f-6789-47a1-abcc-268d1e585baa.JPG", "Grafted Avocado Saplings", "Bamboo staked avocado plants with sturdy graft unions", "avocado"),
    ("3a55609c-2e7b-493f-a146-0c8d3c32da2f.JPG", "Graft Detail", "Close-up showing successful graft union on avocado stock", "avocado"),
    ("97bb333c-1b71-43cc-a7fe-1039116c56e4.JPG", "Planted Avocado Tree", "Vigorous young avocado tree thriving with drip irrigation", "avocado"),
    ("787f90a4-7dff-4259-88f1-f6aef6c01ebb.JPG", "Nursery Staff Inspection", "Team inspecting root bag and foliage of avocado sapling", "avocado nursery"),
    ("7d9d1e84-3fef-4132-93e5-d1e9f8c1c111.JPG", "Avocado Saplings with Stakes", "Upright staked avocado plants in polyhouse bay", "avocado"),
    ("8b56e716-95a7-4afa-956a-1a763bdb1f21.JPG", "Avocado Nursery Beds", "Uniform beds of potted avocado plants", "avocado nursery"),
    ("df76ae23-ab9e-4a69-a341-6c87565f4243.JPG", "Hardened Avocado Saplings", "Ready for plantation dispatch", "avocado"),
    ("232ed53c-1fa7-45c0-874e-dc74da5d7133.JPG", "Coffee Seedlings in Bags", "Lush coffee plants in polybags", "coffee"),
    ("c2b814a3-9b15-44e7-91b4-c6e3e999b269.JPG", "Coffee Nursery Canopy", "Vast sea of healthy green coffee leaves", "coffee nursery"),
    ("IMG_0659.JPG", "Coffee Polyhouse Tunnel", "Coffee seedlings raised in protected polyhouse beds", "coffee"),
    ("9f9c61f7-ecd2-4fc2-a6b2-b4ba559d3ab9.JPG", "Single Coffee Plant", "Demonstrating root bag structure and healthy leaves", "coffee"),
    ("546f4d9e-a8d6-44d9-9e59-c633a2c83380.JPG", "Coffee Truckload Dispatch", "Pickup truck loaded with coffee seedlings for estate", "coffee dispatch"),
    ("1d717b2f-c302-47d6-bc9c-3a795a16784f.JPG", "Pepper Rooted Cuttings", "Black pepper vines in greenhouse hoop tunnels", "pepper"),
    ("354aeed0-3105-4071-8f65-a242b10a2455.JPG", "Pepper Vine Close-up", "Rooted pepper cutting ready for trailing on standards", "pepper"),
    ("b88a9f11-ea17-406a-bb00-ff29a0d7a8ef.JPG", "Pepper Polyhouse Bays", "Organised rows of rooted black pepper cuttings", "pepper nursery"),
    ("2e8e9210-865b-4e33-b0ee-1f1a9c6ebfcd.JPG", "Areca Nut Palms", "High-grade arecanut saplings in nursery", "areca"),
    ("04cfdbd5-e7c1-4679-b182-43332cce8a02.JPG", "Areca Truckload Loading", "Commercial truck stacked with areca seedlings", "areca dispatch"),
    ("6a683486-e201-494a-869a-7226520f696f.JPG", "Bulk Areca Shipment", "Wholesale truck dispatch across Karnataka", "areca dispatch"),
    ("6bbb1d1f-f80a-4ca8-bb25-2473fdf21a81.JPG", "Areca Bundles", "Saplings bundled in red transport bags", "areca dispatch"),
    ("5a4bd5b2-bece-40cd-8943-75354d8b3944.JPG", "Silver Oak Saplings", "Upright silver oak saplings on nursery pathway", "trees"),
    ("83eec2b4-71c0-4bd3-bd58-5ec64bdb338f.JPG", "Cardamom Nursery Plants", "Vigorous cardamom tillers in polybags", "cardamom"),
    ("d68cd26a-d13e-4aed-be7e-04cb50cd66a0.JPG", "Cardamom Shade Net House", "Expansive shade house for cardamom slips", "cardamom nursery"),
    ("rambutan-plant.jpg", "Grafted Rambutan Plant", "Healthy grafted rambutan sapling ready for orchard planting", "fruits"),
    ("litchi-plant.jpg", "Litchi Nursery Plant", "Air-layered litchi sapling with vigorous vegetative growth", "fruits"),
    ("orange-lemon-plants.jpg", "Orange & Lemon Nursery Plants", "Vigorous citrus orange and lemon plants in nursery bags", "fruits nursery"),
    ("830151bb-04be-430b-8763-280be6fcdea6.JPG", "Customer Nursery Visit", "Commercial growers visiting Green Nest Nursery", "nursery")
]

gallery_items_html = ""
for img, title, desc, cat in gallery_photos:
    gallery_items_html += f"""
      <div class="gallery-item" data-category="{cat}">
        <img src="images/{img}" alt="{title}" loading="lazy">
        <div class="gallery-overlay">
          <h4>{title}</h4>
          <p>{desc}</p>
        </div>
      </div>
"""

gallery_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="badge-tag accent">Visual Tour</div>
    <h1>Green Nest Nursery Photo Gallery</h1>
    <p>Authentic photographs from our nursery at Kushalnagar, Kodagu. Showing avocado saplings, coffee beds, pepper vines, areca palms and truck dispatches.</p>
    <div class="breadcrumbs">
      <a href="index.html">Home</a> &gt; <span>Gallery</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="filter-nav">
      <button class="filter-btn active" data-filter="all">All Photos</button>
      <button class="filter-btn" data-filter="avocado">Avocado</button>
      <button class="filter-btn" data-filter="coffee">Coffee</button>
      <button class="filter-btn" data-filter="pepper">Pepper</button>
      <button class="filter-btn" data-filter="areca">Areca</button>
      <button class="filter-btn" data-filter="cardamom">Cardamom</button>
      <button class="filter-btn" data-filter="dispatch">Dispatch & Delivery</button>
    </div>

    <div class="gallery-grid">
{gallery_items_html}
    </div>
  </div>
</section>

<!-- Lightbox Modal -->
<div class="lightbox-modal">
  <div class="lightbox-content">
    <button class="lightbox-close" aria-label="Close Lightbox">&times;</button>
    <img src="" alt="Enlarged photo preview">
    <div class="lightbox-caption"></div>
  </div>
</div>

{cta_banner_html('Plants')}
"""

with open('gallery.html', 'w', encoding='utf-8') as f:
    f.write(render_page(
        title="Nursery Photo Gallery | Green Nest Avocado & Coffee Nursery",
        description="Authentic photographs of avocado, coffee, pepper, areca and cardamom nursery plants and truck dispatches at Green Nest Nursery in Kodagu.",
        canonical_url="gallery.html",
        body_content=gallery_body,
        active_page="gallery.html"
    ))

# =============================================================
# 17. faq.html
# =============================================================
faq_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="badge-tag accent">Help & Guidance</div>
    <h1>Frequently Asked Questions</h1>
    <p>Clear answers to common questions about bulk plant ordering, avocado cultivation, coffee varieties, and delivery across India.</p>
    <div class="breadcrumbs">
      <a href="index.html">Home</a> &gt; <span>FAQs</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="faq-list">
      <div class="faq-item active">
        <button class="faq-question">
          <span>Do you sell avocado plants in bulk?</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
        <div class="faq-answer">
          <p>Yes. Customers can contact Green Nest Nursery regarding avocado plants for farm, orchard and commercial plantation requirements. We supply both retail quantities for trial plots and large bulk quantities for multi-acre commercial plantations. Availability depends on current nursery stock.</p>
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-question">
          <span>Do you supply coffee plants?</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
        <div class="faq-answer">
          <p>Yes. Coffee plants are available for plantation requirements including new estate development, infilling and replacement planting, subject to stock and seasonal cycles.</p>
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-question">
          <span>Can I place a commercial plant order?</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
        <div class="faq-answer">
          <p>Yes. Green Nest Nursery accepts bulk enquiries from farmers, estates, and commercial growers. We can handle orders ranging from a few hundred plants to full truckload volumes of tens of thousands of plants.</p>
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-question">
          <span>Do you deliver outside Kodagu?</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
        <div class="faq-answer">
          <p>Yes. Bulk transportation can be coordinated depending on the plant variety, quantity, and destination. We regularly supply neighbouring districts such as Mysuru, Hassan, Chikkamagaluru, and Wayanad.</p>
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-question">
          <span>Do you deliver plants across India?</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
        <div class="faq-answer">
          <p>Commercial enquiries from different parts of India can be considered. Transportation feasibility, route duration, weather, and logistics costs are confirmed before booking.</p>
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-question">
          <span>How do I get the current plant price?</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
        <div class="faq-answer">
          <p>Contact Green Nest Nursery directly through WhatsApp or phone (+91 94801 62989). Pricing can vary depending on plant variety, root bag size, order quantity, and season.</p>
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-question">
          <span>Can I enquire through WhatsApp?</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
        <div class="faq-answer">
          <p>Yes! WhatsApp is our primary communication channel. You can message us at +91 94801 62989 for rapid stock confirmation, photographs of current batches, and price quotations.</p>
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-question">
          <span>Can I visit the nursery in person?</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
        <div class="faq-answer">
          <p>Yes, growers and plantation managers are warmly welcome to visit our nursery at 7th Hosakote, Kushalnagar, Kodagu. We recommend calling ahead so our nursery manager can attend to you.</p>
        </div>
      </div>
    </div>
  </div>
</section>

{cta_banner_html('Plantation Plants')}
"""

with open('faq.html', 'w', encoding='utf-8') as f:
    f.write(render_page(
        title="Frequently Asked Questions | Green Nest Nursery Kodagu",
        description="Find answers about wholesale plant purchasing, avocado varieties, bulk quantities, pricing, and pan-India delivery from Green Nest Nursery in Kodagu.",
        canonical_url="faq.html",
        body_content=faq_body,
        active_page="faq.html"
    ))

# =============================================================
# 18. contact.html
# =============================================================
contact_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="badge-tag accent">Get in Touch</div>
    <h1>Contact Green Nest Nursery</h1>
    <p>We welcome enquiries from plantation owners, estate managers, commercial farmers and fruit growers across India.</p>
    <div class="breadcrumbs">
      <a href="index.html">Home</a> &gt; <span>Contact Us</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="contact-grid">
      <!-- Contact Information Card -->
      <div class="contact-info-card">
        <div class="badge-tag">Nursery Office</div>
        <h2>Green Nest Avocado/Coffee Nursery</h2>
        <p style="color: var(--text-muted); margin-bottom: 1.5rem;">Located at 7th Hosakote near Kushalnagar in Kodagu, Karnataka. Supplying bulk plantation and fruit plants.</p>

        <div class="contact-method-list">
          <div class="contact-method">
            <div class="contact-icon">📍</div>
            <div class="contact-text">
              <strong>Nursery Address</strong>
              <p>7th Hosakote, Kushalnagar,<br>Kodagu, Karnataka – 571237, India</p>
            </div>
          </div>

          <div class="contact-method">
            <div class="contact-icon">📞</div>
            <div class="contact-text">
              <strong>Phone Enquiries</strong>
              <a href="tel:+919480162989">+91 94801 62989</a>
              <p style="font-size: 0.82rem; color: var(--text-muted);">Available Monday to Saturday, 8:00 AM - 6:30 PM</p>
            </div>
          </div>

          <div class="contact-method">
            <div class="contact-icon">💬</div>
            <div class="contact-text">
              <strong>WhatsApp Direct</strong>
              <a href="https://wa.me/919480162989?text=Hello%20Green%20Nest%20Nursery,%20I%20would%20like%20to%20enquire%20about%20plants" target="_blank" rel="noopener">+91 94801 62989</a>
              <p style="font-size: 0.82rem; color: var(--text-muted);">Instant messaging for availability & photo verification</p>
            </div>
          </div>

          <div class="contact-method">
            <div class="contact-icon">◎</div>
            <div class="contact-text">
              <strong>Instagram</strong>
              <a href="https://instagram.com" target="_blank" rel="noopener">Follow Our Plant Highlights</a>
            </div>
          </div>
        </div>

        <div style="display: flex; gap: 0.75rem; flex-wrap: wrap; margin-top: 1.5rem;">
          <a href="tel:+919480162989" class="btn btn-primary">Call Nursery</a>
          <a href="https://wa.me/919480162989?text=Hello%20Green%20Nest%20Nursery,%20I%20would%20like%20to%20enquire%20about%20plants" target="_blank" rel="noopener" class="btn btn-whatsapp">WhatsApp Us</a>
          <a href="https://maps.google.com/?q=12.4552,75.9554" target="_blank" rel="noopener" class="btn btn-outline">Get Directions</a>
        </div>
      </div>

      <!-- Bulk Enquiry Form -->
      <div>
        {whatsapp_calc_box('General Plant Enquiry', '500')}

        <div class="map-container">
          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3896.6575747683936!2d75.9528!3d12.4552!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMTLCsDI3JzE4LjciTiA3NcKwNTcnMTIuNyJF!5e0!3m2!1sen!2sin!4v1689000000000!5m2!1sen!2sin" title="Green Nest Nursery Location Map" allowfullscreen="" loading="lazy"></iframe>
        </div>
      </div>
    </div>
  </div>
</section>
"""

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(render_page(
        title="Contact Green Nest Nursery | Kushalnagar, Kodagu",
        description="Contact Green Nest Avocado/Coffee Nursery in 7th Hosakote, Kushalnagar, Kodagu. Phone: +91 94801 62989. Call, WhatsApp, or visit our nursery facility.",
        canonical_url="contact.html",
        body_content=contact_body,
        active_page="contact.html"
    ))

# =============================================================
# 19. sitemap.xml & robots.txt
# =============================================================
pages = [
    ("", "1.0", "daily"),
    ("about.html", "0.8", "weekly"),
    ("plants.html", "0.9", "weekly"),
    ("avocado-plants.html", "0.95", "weekly"),
    ("coffee-plants.html", "0.9", "weekly"),
    ("pepper-plants.html", "0.85", "weekly"),
    ("areca-plants.html", "0.85", "weekly"),
    ("silver-oak-plants.html", "0.8", "weekly"),
    ("cardamom-plants.html", "0.8", "weekly"),
    ("rambutan-plants.html", "0.8", "weekly"),
    ("litchi-plants.html", "0.8", "weekly"),
    ("other-plants.html", "0.75", "weekly"),
    ("wholesale-plants.html", "0.9", "weekly"),
    ("commercial-plantation.html", "0.85", "weekly"),
    ("bulk-plant-delivery.html", "0.85", "weekly"),
    ("gallery.html", "0.8", "weekly"),
    ("faq.html", "0.75", "weekly"),
    ("contact.html", "0.85", "weekly"),
]

sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""

for p, priority, freq in pages:
    url = f"https://greennestnursery.com/{p}" if p else "https://greennestnursery.com/"
    sitemap_xml += f"""  <url>
    <loc>{url}</loc>
    <changefreq>{freq}</changefreq>
    <priority>{priority}</priority>
  </url>
"""

sitemap_xml += "</urlset>\n"

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_xml)

robots_txt = """User-agent: *
Allow: /

Sitemap: https://greennestnursery.com/sitemap.xml
"""

with open('robots.txt', 'w', encoding='utf-8') as f:
    f.write(robots_txt)

print("All 18 HTML pages, sitemap.xml, and robots.txt have been generated successfully!")
