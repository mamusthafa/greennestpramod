#!/usr/bin/env python3
"""
Green Nest Avocado/Coffee Nursery — Site Generator
Generates all 18 production-ready HTML pages, sitemap.xml, and robots.txt
Using real photos exclusively from images/ folder.
"""

import os

# Read components
with open('_includes/header.html', 'r', encoding='utf-8') as f:
    HEADER_HTML = f.read()

with open('_includes/footer.html', 'r', encoding='utf-8') as f:
    FOOTER_HTML = f.read()

with open('_includes/sticky-contact.html', 'r', encoding='utf-8') as f:
    STICKY_HTML = f.read()

def render_page(title, description, canonical_url, body_content, active_page=''):
    header_with_active = HEADER_HTML
    # Mark active nav link
    if active_page:
        header_with_active = header_with_active.replace(
            f'href="{active_page}" class="nav-link"',
            f'href="{active_page}" class="nav-link active"'
        )
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Green Nest Nursery Kodagu</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="https://greennestnursery.com/{canonical_url}">
  <meta name="robots" content="index, follow">
  <meta name="format-detection" content="telephone=yes">

  <!-- Open Graph / Social Sharing -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title} | Green Nest Nursery Kodagu">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="https://greennestnursery.com/{canonical_url}">
  <meta property="og:site_name" content="Green Nest Avocado/Coffee Nursery">
  <meta property="og:image" content="https://greennestnursery.com/images/b9818c5a-060d-477f-aa82-24ba31d4bec7.JPG">

  <!-- Stylesheet & Favicon -->
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="assets/css/style.css">

  <!-- Structured Data: LocalBusiness -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Green Nest Avocado/Coffee Nursery",
    "image": "https://greennestnursery.com/images/b9818c5a-060d-477f-aa82-24ba31d4bec7.JPG",
    "telephone": "+919480162989",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "7th Hosakote",
      "addressLocality": "Kushalnagar, Kodagu",
      "addressRegion": "Karnataka",
      "postalCode": "571237",
      "addressCountry": "IN"
    }},
    "geo": {{
      "@type": "GeoCoordinates",
      "latitude": 12.4552,
      "longitude": 75.9554
    }},
    "url": "https://greennestnursery.com/{canonical_url}",
    "priceRange": "$$",
    "description": "Wholesale plant nursery in Kushalnagar, Kodagu specializing in avocado, coffee, pepper, areca, silver oak, cardamom, and plantation crops with bulk delivery across India."
  }}
  </script>
</head>
<body>

{header_with_active}

<main>
{body_content}
</main>

{FOOTER_HTML}
{STICKY_HTML}

<script src="assets/js/main.js" defer></script>
</body>
</html>
"""
    return html

# -------------------------------------------------------------
# 1. index.html (Homepage)
# -------------------------------------------------------------
homepage_body = """
<!-- Hero Section -->
<section class="hero">
  <div class="container">
    <div class="hero-content">
      <div class="badge-tag accent">Wholesale Plant Nursery • Kodagu, Karnataka</div>
      <h1>Wholesale Avocado, Coffee & Plantation Plants in Kodagu</h1>
      <p class="hero-lead">Green Nest Avocado/Coffee Nursery supplies healthy nursery-grown avocado, coffee, pepper, areca, silver oak, cardamom, rambutan, litchi and other plantation plants for farms, estates and commercial plantations.</p>
      <p style="color: #ffffff; font-weight: 600; margin-bottom: 2rem;">Bulk quantities available with delivery support across India.</p>
      
      <div class="hero-actions">
        <a href="plants.html" class="btn btn-primary btn-lg">View Our Plants</a>
        <a href="https://wa.me/919480162989?text=Hello%20Green%20Nest%20Nursery,%20I%20would%20like%20to%20get%20bulk%20plant%20pricing." target="_blank" rel="noopener" class="btn btn-whatsapp btn-lg">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2z"/></svg>
          WhatsApp for Bulk Price
        </a>
      </div>

      <div class="hero-trust-bar">
        <div class="trust-item">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          <span>Wholesale Plant Supply</span>
        </div>
        <div class="trust-item">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          <span>Commercial Plantation Orders</span>
        </div>
        <div class="trust-item">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          <span>Bulk Quantities in Stock</span>
        </div>
        <div class="trust-item">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          <span>Delivery Across India</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Section 8: Avocado Spotlight (Flagship Category) -->
<section class="section" style="padding-top: 1.5rem;">
  <div class="container">
    <div class="avocado-spotlight">
      <div class="spotlight-grid">
        <div class="spotlight-image">
          <img src="images/cdce181f-6789-47a1-abcc-268d1e585baa.JPG" alt="Staked grafted avocado saplings at Green Nest Nursery Kodagu" loading="lazy">
        </div>
        <div class="spotlight-content">
          <div class="badge-tag">Flagship Specialty</div>
          <h2>Premium Avocado Plants</h2>
          <p>Start or expand your avocado plantation with healthy nursery-grown avocado plants from Green Nest Nursery. We supply avocado plants for individual growers, farms, estates and commercial plantations, with bulk-order quantities available.</p>
          
          <div class="feature-badge-grid">
            <div class="feature-box">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              <span>Healthy Nursery Plants</span>
            </div>
            <div class="feature-box">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              <span>Selected Grafted Stock</span>
            </div>
            <div class="feature-box">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              <span>Bulk Availability</span>
            </div>
            <div class="feature-box">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              <span>Commercial Orders</span>
            </div>
            <div class="feature-box">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              <span>Plantation Supply</span>
            </div>
            <div class="feature-box">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              <span>Delivery Support</span>
            </div>
          </div>

          <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
            <a href="avocado-plants.html" class="btn btn-primary">Explore Avocado Plants</a>
            <a href="https://wa.me/919480162989?text=Hello%20Green%20Nest%20Nursery,%20I%20am%20interested%20in%20Avocado%20Plants.%20Please%20share%20bulk%20availability%20and%20prices." target="_blank" rel="noopener" class="btn btn-whatsapp">
              WhatsApp Avocado Enquiry
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Section 9: Main Plant Categories Grid -->
<section class="section section-bg">
  <div class="container">
    <div class="section-head">
      <div class="badge-tag">Our Inventory</div>
      <h2>Wholesale Plantation & Fruit Plants</h2>
      <p>Source high-grade nursery stock grown in the ideal elevation and microclimate of Kushalnagar, Kodagu. Ready for commercial planting.</p>
    </div>

    <div class="plants-grid">
      <!-- Avocado -->
      <article class="plant-card">
        <div class="plant-card-media">
          <span class="plant-tag">Flagship</span>
          <img src="images/3a55609c-2e7b-493f-a146-0c8d3c32da2f.JPG" alt="Grafted avocado plants in nursery bags" loading="lazy">
        </div>
        <div class="plant-card-body">
          <h3 class="plant-card-title">Avocado Plants</h3>
          <p class="plant-card-desc">Premium avocado plants for farms, estates and commercial plantations. Vigorous root system and healthy grafted scions.</p>
          <div class="plant-card-actions">
            <a href="avocado-plants.html" class="btn btn-outline btn-sm">View Details &rarr;</a>
            <a href="https://wa.me/919480162989?text=Hello%20Green%20Nest%20Nursery,%20I%20am%20interested%20in%20Avocado%20Plants." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
          </div>
        </div>
      </article>

      <!-- Coffee -->
      <article class="plant-card">
        <div class="plant-card-media">
          <span class="plant-tag">Commercial</span>
          <img src="images/232ed53c-1fa7-45c0-874e-dc74da5d7133.JPG" alt="Coffee seedlings in polybags in Kodagu" loading="lazy">
        </div>
        <div class="plant-card-body">
          <h3 class="plant-card-title">Coffee Plants</h3>
          <p class="plant-card-desc">Quality coffee plants suitable for new plantation establishment, gap filling and replacement planting across South India estates.</p>
          <div class="plant-card-actions">
            <a href="coffee-plants.html" class="btn btn-outline btn-sm">View Details &rarr;</a>
            <a href="https://wa.me/919480162989?text=Hello%20Green%20Nest%20Nursery,%20I%20am%20interested%20in%20Coffee%20Plants." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
          </div>
        </div>
      </article>

      <!-- Pepper -->
      <article class="plant-card">
        <div class="plant-card-media">
          <span class="plant-tag">Spices</span>
          <img src="images/1d717b2f-c302-47d6-bc9c-3a795a16784f.JPG" alt="Black pepper cuttings in nursery tunnel" loading="lazy">
        </div>
        <div class="plant-card-body">
          <h3 class="plant-card-title">Pepper Plants</h3>
          <p class="plant-card-desc">Healthy black pepper planting material for estate cultivation. Excellent vine vigor for trailing on silver oak and areca trees.</p>
          <div class="plant-card-actions">
            <a href="pepper-plants.html" class="btn btn-outline btn-sm">View Details &rarr;</a>
            <a href="https://wa.me/919480162989?text=Hello%20Green%20Nest%20Nursery,%20I%20am%20interested%20in%20Pepper%20Plants." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
          </div>
        </div>
      </article>

      <!-- Areca -->
      <article class="plant-card">
        <div class="plant-card-media">
          <span class="plant-tag">Plantation</span>
          <img src="images/2e8e9210-865b-4e33-b0ee-1f1a9c6ebfcd.JPG" alt="Nursery grown areca nut palms" loading="lazy">
        </div>
        <div class="plant-card-body">
          <h3 class="plant-card-title">Areca Plants</h3>
          <p class="plant-card-desc">Nursery-grown arecanut plants for commercial cultivation. Uniform growth and robust roots ready for field transplanting.</p>
          <div class="plant-card-actions">
            <a href="areca-plants.html" class="btn btn-outline btn-sm">View Details &rarr;</a>
            <a href="https://wa.me/919480162989?text=Hello%20Green%20Nest%20Nursery,%20I%20am%20interested%20in%20Areca%20Plants." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
          </div>
        </div>
      </article>

      <!-- Silver Oak -->
      <article class="plant-card">
        <div class="plant-card-media">
          <span class="plant-tag">Shade & Support</span>
          <img src="images/5a4bd5b2-bece-40cd-8943-75354d8b3944.JPG" alt="Silver oak saplings at nursery" loading="lazy">
        </div>
        <div class="plant-card-body">
          <h3 class="plant-card-title">Silver Oak Plants</h3>
          <p class="plant-card-desc">Popular shade and support trees used in coffee and pepper plantations. Rapid growth habit and strong vertical form.</p>
          <div class="plant-card-actions">
            <a href="silver-oak-plants.html" class="btn btn-outline btn-sm">View Details &rarr;</a>
            <a href="https://wa.me/919480162989?text=Hello%20Green%20Nest%20Nursery,%20I%20am%20interested%20in%20Silver%20Oak%20Plants." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
          </div>
        </div>
      </article>

      <!-- Cardamom -->
      <article class="plant-card">
        <div class="plant-card-media">
          <span class="plant-tag">Spices</span>
          <img src="images/83eec2b4-71c0-4bd3-bd58-5ec64bdb338f.JPG" alt="Cardamom nursery plants under shade net" loading="lazy">
        </div>
        <div class="plant-card-body">
          <h3 class="plant-card-title">Cardamom Plants</h3>
          <p class="plant-card-desc">Healthy cardamom planting material suitable for high-humidity plantation cultivation. Thriving tillers in nursery grow bags.</p>
          <div class="plant-card-actions">
            <a href="cardamom-plants.html" class="btn btn-outline btn-sm">View Details &rarr;</a>
            <a href="https://wa.me/919480162989?text=Hello%20Green%20Nest%20Nursery,%20I%20am%20interested%20in%20Cardamom%20Plants." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
          </div>
        </div>
      </article>

      <!-- Rambutan -->
      <article class="plant-card">
        <div class="plant-card-media">
          <span class="plant-tag">Fruit Crop</span>
          <img src="images/1c386e3c-ff0c-44f5-bba4-a6d8c00f9dc5.JPG" alt="Fruit nursery saplings" loading="lazy">
        </div>
        <div class="plant-card-body">
          <h3 class="plant-card-title">Rambutan Plants</h3>
          <p class="plant-card-desc">High-value tropical fruit plants suitable for orchards, agro-tourism farms and tropical growing conditions with irrigation.</p>
          <div class="plant-card-actions">
            <a href="rambutan-plants.html" class="btn btn-outline btn-sm">View Details &rarr;</a>
            <a href="https://wa.me/919480162989?text=Hello%20Green%20Nest%20Nursery,%20I%20am%20interested%20in%20Rambutan%20Plants." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
          </div>
        </div>
      </article>

      <!-- Litchi -->
      <article class="plant-card">
        <div class="plant-card-media">
          <span class="plant-tag">Fruit Crop</span>
          <img src="images/915e8d71-62e8-41ba-90ff-9fecaadcc242.JPG" alt="Litchi and fruit plants" loading="lazy">
        </div>
        <div class="plant-card-body">
          <h3 class="plant-card-title">Litchi Plants</h3>
          <p class="plant-card-desc">Quality fruit plants suitable for farms, commercial orchards and progressive growers seeking high-return orchard crops.</p>
          <div class="plant-card-actions">
            <a href="litchi-plants.html" class="btn btn-outline btn-sm">View Details &rarr;</a>
            <a href="https://wa.me/919480162989?text=Hello%20Green%20Nest%20Nursery,%20I%20am%20interested%20in%20Litchi%20Plants." target="_blank" rel="noopener" class="btn btn-whatsapp btn-sm">WhatsApp</a>
          </div>
        </div>
      </article>
    </div>

    <div class="text-center" style="margin-top: 3rem;">
      <a href="plants.html" class="btn btn-primary btn-lg">Explore Full Plant Catalogue &rarr;</a>
    </div>
  </div>
</section>

<!-- Section 10: Wholesale Plant Supply -->
<section class="section">
  <div class="container">
    <div class="spotlight-grid">
      <div class="spotlight-content" style="padding-left: 0;">
        <div class="badge-tag">Commercial Supply</div>
        <h2>Wholesale Plants for Farms & Estates</h2>
        <p>Green Nest Nursery specialises in bulk supply of plantation and fruit plants for farmers, estate owners, agricultural businesses and commercial plantation projects.</p>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem; margin: 1.5rem 0 2rem;">
          <div class="trust-item" style="color: var(--primary-dark);">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            <span>Bulk plant orders</span>
          </div>
          <div class="trust-item" style="color: var(--primary-dark);">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            <span>Estate requirements</span>
          </div>
          <div class="trust-item" style="color: var(--primary-dark);">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            <span>New plantation projects</span>
          </div>
          <div class="trust-item" style="color: var(--primary-dark);">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            <span>Replacement planting</span>
          </div>
          <div class="trust-item" style="color: var(--primary-dark);">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            <span>Farm development</span>
          </div>
          <div class="trust-item" style="color: var(--primary-dark);">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            <span>Nursery-to-farm supply</span>
          </div>
        </div>

        <a href="wholesale-plants.html" class="btn btn-primary">Request Wholesale Price</a>
      </div>
      <div class="spotlight-image">
        <img src="images/546f4d9e-a8d6-44d9-9e59-c633a2c83380.JPG" alt="Pickup truck stacked with nursery plants ready for wholesale delivery" style="border-radius: var(--radius-md);" loading="lazy">
      </div>
    </div>
  </div>
</section>

<!-- Section 11 & 12: Commercial Plantation & Process -->
<section class="section section-bg">
  <div class="container">
    <div class="section-head">
      <div class="badge-tag">Plantation Advisory</div>
      <h2>Planning a New Plantation?</h2>
      <p>Whether you are establishing a new avocado orchard, expanding a coffee estate or sourcing plantation crops such as pepper, areca, cardamom or silver oak, Green Nest Nursery can assist with bulk plant requirements.</p>
    </div>

    <div class="supply-process-grid">
      <div class="process-card">
        <div class="process-number">01</div>
        <h4>Tell us your requirement</h4>
        <p>Share your target plant types, approximate quantities and your land location.</p>
      </div>
      <div class="process-card">
        <div class="process-number">02</div>
        <h4>Check nursery availability</h4>
        <p>We review current nursery stock, batch maturity and dispatch schedules.</p>
      </div>
      <div class="process-card">
        <div class="process-number">03</div>
        <h4>Receive wholesale quotation</h4>
        <p>Transparent pricing tailored for commercial scale, varieties and logistics.</p>
      </div>
      <div class="process-card">
        <div class="process-number">04</div>
        <h4>Arrange supply & logistics</h4>
        <p>Collection at nursery or direct transportation arranged to your farm gate.</p>
      </div>
    </div>

    <div class="text-center" style="margin-top: 2.5rem;">
      <a href="commercial-plantation.html" class="btn btn-primary">Discuss Your Plantation Requirement</a>
    </div>
  </div>
</section>

<!-- Section 13: Why Choose Green Nest -->
<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="badge-tag">Our Strengths</div>
      <h2>Why Commercial Growers Choose Green Nest</h2>
      <p>Supplying robust plants with high field-survival rates from the heart of Kodagu's plantation belt.</p>
    </div>

    <div class="reasons-grid">
      <div class="reason-card">
        <div class="reason-icon">🌱</div>
        <div class="reason-content">
          <h4>Healthy Nursery Plants</h4>
          <p>Plants are carefully nurtured in polybags under controlled shade and polyhouse environments.</p>
        </div>
      </div>

      <div class="reason-card">
        <div class="reason-icon">🌿</div>
        <div class="reason-content">
          <h4>Wide Plant Selection</h4>
          <p>Avocado, coffee, pepper, areca, silver oak, cardamom, rambutan and litchi from a single trusted nursery.</p>
        </div>
      </div>

      <div class="reason-card">
        <div class="reason-icon">📦</div>
        <div class="reason-content">
          <h4>Bulk Availability</h4>
          <p>Equipped to fulfil large-scale plantation orders for several hundred to thousands of plants.</p>
        </div>
      </div>

      <div class="reason-card">
        <div class="reason-icon">📍</div>
        <div class="reason-content">
          <h4>Kodagu Nursery Advantage</h4>
          <p>Located at 7th Hosakote near Kushalnagar, benefiting from rich soil and optimal highland growing conditions.</p>
        </div>
      </div>

      <div class="reason-card">
        <div class="reason-icon">🚜</div>
        <div class="reason-content">
          <h4>Commercial Scale</h4>
          <p>Experienced in serving commercial growers, estate managers, agri-entrepreneurs and institutions.</p>
        </div>
      </div>

      <div class="reason-card">
        <div class="reason-icon">🚛</div>
        <div class="reason-content">
          <h4>Delivery Support Across India</h4>
          <p>Commercial orders coordinated with reliable transport networks for safe arrival at your plantation.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Section 11: India Delivery Section -->
<section class="section section-dark">
  <div class="container">
    <div class="spotlight-grid">
      <div class="spotlight-image">
        <img src="images/04cfdbd5-e7c1-4679-b182-43332cce8a02.JPG" alt="Truck loaded with wholesale saplings for delivery across India" style="border-radius: var(--radius-md);" loading="lazy">
      </div>
      <div class="spotlight-content">
        <div class="badge-tag accent">Nationwide Reach</div>
        <h2>Bulk Plant Supply Across India</h2>
        <p>Green Nest Nursery accepts commercial bulk enquiries from customers across India. Depending on the plant variety, quantity, season and destination, transportation can be arranged for suitable commercial orders.</p>
        
        <p style="color: #c9e0d2; font-size: 0.95rem; margin: 1.25rem 0;">We regularly coordinate bulk dispatches to:</p>
        <div style="display: flex; flex-wrap: wrap; gap: 0.6rem; margin-bottom: 2rem;">
          <span style="background: rgba(255,255,255,0.12); padding: 0.35rem 0.8rem; border-radius: var(--radius-full); font-size: 0.88rem;">Kodagu & Hassan</span>
          <span style="background: rgba(255,255,255,0.12); padding: 0.35rem 0.8rem; border-radius: var(--radius-full); font-size: 0.88rem;">Mysuru & Bengaluru</span>
          <span style="background: rgba(255,255,255,0.12); padding: 0.35rem 0.8rem; border-radius: var(--radius-full); font-size: 0.88rem;">Chikkamagaluru</span>
          <span style="background: rgba(255,255,255,0.12); padding: 0.35rem 0.8rem; border-radius: var(--radius-full); font-size: 0.88rem;">Kerala (Wayanad, Idukki)</span>
          <span style="background: rgba(255,255,255,0.12); padding: 0.35rem 0.8rem; border-radius: var(--radius-full); font-size: 0.88rem;">Tamil Nadu (Ooty, Kodaikanal)</span>
          <span style="background: rgba(255,255,255,0.12); padding: 0.35rem 0.8rem; border-radius: var(--radius-full); font-size: 0.88rem;">Goa & Maharashtra</span>
          <span style="background: rgba(255,255,255,0.12); padding: 0.35rem 0.8rem; border-radius: var(--radius-full); font-size: 0.88rem;">Pan-India (Commercial Orders)</span>
        </div>

        <a href="bulk-plant-delivery.html" class="btn btn-accent">Check Delivery Availability</a>
      </div>
    </div>
  </div>
</section>

<!-- Section 28: Gallery Preview -->
<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="badge-tag">Real Nursery Photos</div>
      <h2>Inside Green Nest Nursery</h2>
      <p>Take a look at our healthy avocado saplings, coffee nursery beds, pepper shade tunnels and shipment loading.</p>
    </div>

    <div class="gallery-grid">
      <div class="gallery-item">
        <img src="images/b9818c5a-060d-477f-aa82-24ba31d4bec7.JPG" alt="Avocado nursery rows at Kushalnagar Kodagu" loading="lazy">
        <div class="gallery-overlay">
          <h4>Avocado Saplings</h4>
          <p>Grafted stock ready for commercial planting</p>
        </div>
      </div>
      <div class="gallery-item">
        <img src="images/c2b814a3-9b15-44e7-91b4-c6e3e999b269.JPG" alt="Coffee nursery seedlings in Kodagu" loading="lazy">
        <div class="gallery-overlay">
          <h4>Coffee Seedling Beds</h4>
          <p>Lush, hardened plants for South India estates</p>
        </div>
      </div>
      <div class="gallery-item">
        <img src="images/1d717b2f-c302-47d6-bc9c-3a795a16784f.JPG" alt="Black pepper cuttings in polyhouse" loading="lazy">
        <div class="gallery-overlay">
          <h4>Pepper Vines</h4>
          <p>Rooted cuttings in polyhouse tunnels</p>
        </div>
      </div>
      <div class="gallery-item">
        <img src="images/2e8e9210-865b-4e33-b0ee-1f1a9c6ebfcd.JPG" alt="Areca nut palm seedlings in nursery" loading="lazy">
        <div class="gallery-overlay">
          <h4>Areca Nut Palms</h4>
          <p>Uniform plantation-grade seedlings</p>
        </div>
      </div>
      <div class="gallery-item">
        <img src="images/d68cd26a-d13e-4aed-be7e-04cb50cd66a0.JPG" alt="Cardamom nursery under green shade netting" loading="lazy">
        <div class="gallery-overlay">
          <h4>Cardamom Nursery</h4>
          <p>Healthy slips in shade house</p>
        </div>
      </div>
      <div class="gallery-item">
        <img src="images/6a683486-e201-494a-869a-7226520f696f.JPG" alt="Commercial truck dispatch of plants" loading="lazy">
        <div class="gallery-overlay">
          <h4>Wholesale Dispatch</h4>
          <p>Truckload deliveries across South India</p>
        </div>
      </div>
    </div>

    <div class="text-center" style="margin-top: 2.5rem;">
      <a href="gallery.html" class="btn btn-outline">View Complete Nursery Photo Gallery &rarr;</a>
    </div>
  </div>
</section>

<!-- Lightbox Modal Container -->
<div class="lightbox-modal">
  <div class="lightbox-content">
    <button class="lightbox-close" aria-label="Close Preview">&times;</button>
    <img src="" alt="Enlarged view">
    <div class="lightbox-caption"></div>
  </div>
</div>

<!-- Section 31: FAQ Preview -->
<section class="section section-bg">
  <div class="container">
    <div class="section-head">
      <div class="badge-tag">Got Questions?</div>
      <h2>Frequently Asked Questions</h2>
      <p>Everything you need to know about purchasing wholesale plants from Green Nest Nursery.</p>
    </div>

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
          <span>Do you deliver plants outside Kodagu and across India?</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
        <div class="faq-answer">
          <p>Yes. Bulk transportation can be coordinated depending on the plant variety, quantity, season and delivery destination. Commercial enquiries from Karnataka, Kerala, Tamil Nadu, Maharashtra, Goa, and other states across India are accepted.</p>
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-question">
          <span>How do I get the current plant wholesale price?</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
        <div class="faq-answer">
          <p>Contact Green Nest Nursery directly through WhatsApp or phone (+91 94801 62989). Pricing varies by plant variety, root bag size, order volume and seasonal availability.</p>
        </div>
      </div>
    </div>

    <div class="text-center" style="margin-top: 2rem;">
      <a href="faq.html" class="btn btn-outline btn-sm">Read All FAQs &rarr;</a>
    </div>
  </div>
</section>

<!-- Section 50: Large Conversion CTA Banner -->
<section class="section">
  <div class="container">
    <div class="cta-banner">
      <h2>Need Plants in Bulk for Your Plantation?</h2>
      <p>Tell us your required plant variety, approximate quantity and delivery location. Our nursery team will confirm current availability and share an instant wholesale quotation.</p>
      <div class="cta-banner-actions">
        <a href="https://wa.me/919480162989?text=Hello%20Green%20Nest%20Nursery,%20I%20would%20like%20to%20enquire%20about%20bulk%20plants%20for%20my%20plantation." target="_blank" rel="noopener" class="btn btn-whatsapp btn-lg">
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

<!-- Location & Map Section -->
<section class="section section-bg" style="padding-bottom: 4.5rem;">
  <div class="container">
    <div class="section-head">
      <div class="badge-tag">Visit Nursery</div>
      <h2>Located in Kushalnagar, Kodagu</h2>
      <p>7th Hosakote, Kushalnagar, Kodagu, Karnataka – 571237. Convenient road access from Mysuru, Hassan, and Madikeri.</p>
    </div>

    <div class="map-container">
      <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3896.6575747683936!2d75.9528!3d12.4552!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMTLCsDI3JzE4LjciTiA3NcKwNTcnMTIuNyJF!5e0!3m2!1sen!2sin!4v1689000000000!5m2!1sen!2sin" title="Green Nest Nursery Location" allowfullscreen="" loading="lazy"></iframe>
    </div>
  </div>
</section>
"""

# Let's save index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(render_page(
        title="Avocado & Coffee Plant Nursery in Kodagu",
        description="Green Nest Nursery in Kushalnagar, Kodagu supplies avocado, coffee, pepper, areca, cardamom, rambutan, litchi and plantation plants in bulk. Commercial orders and delivery available across India.",
        canonical_url="",
        body_content=homepage_body,
        active_page="index.html"
    ))

print("Created index.html")
