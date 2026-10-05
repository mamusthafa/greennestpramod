/**
 * Green Nest Avocado/Coffee Nursery — Main JavaScript
 * Handles Navigation, Filtering, WhatsApp Lead Generation, Lightbox & Interactive Components
 */

document.addEventListener('DOMContentLoaded', () => {
  initMobileDrawer();
  initFaqAccordion();
  initCategoryFilter();
  initPlantGallerySwitcher();
  initLightbox();
  initWhatsAppForms();
});

/* Mobile Drawer */
function initMobileDrawer() {
  const toggleBtn = document.querySelector('.mobile-toggle');
  const drawer = document.querySelector('.mobile-drawer');
  const backdrop = document.querySelector('.drawer-backdrop');
  const closeBtn = document.querySelector('.drawer-close');

  if (!toggleBtn || !drawer || !backdrop) return;

  function openDrawer() {
    drawer.classList.add('open');
    backdrop.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    drawer.classList.remove('open');
    backdrop.classList.remove('open');
    document.body.style.overflow = '';
  }

  toggleBtn.addEventListener('click', openDrawer);
  if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
  backdrop.addEventListener('click', closeDrawer);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && drawer.classList.contains('open')) {
      closeDrawer();
    }
  });
}

/* FAQ Accordion */
function initFaqAccordion() {
  const faqItems = document.querySelectorAll('.faq-item');
  if (!faqItems.length) return;

  faqItems.forEach((item) => {
    const questionBtn = item.querySelector('.faq-question');
    if (!questionBtn) return;

    questionBtn.addEventListener('click', () => {
      const isActive = item.classList.contains('active');
      faqItems.forEach((other) => other.classList.remove('active'));
      if (!isActive) {
        item.classList.add('active');
      }
    });
  });
}

/* Category Filter (for plants.html & gallery.html) */
function initCategoryFilter() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const filterItems = document.querySelectorAll('[data-category]');

  if (!filterBtns.length || !filterItems.length) return;

  filterBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      filterBtns.forEach((b) => b.classList.remove('active'));
      btn.classList.add('active');

      const target = btn.getAttribute('data-filter');

      filterItems.forEach((item) => {
        const itemCat = item.getAttribute('data-category');
        if (target === 'all' || itemCat.includes(target)) {
          item.style.display = '';
          item.style.animation = 'fadeIn 0.3s ease forwards';
        } else {
          item.style.display = 'none';
        }
      });
    });
  });
}

/* Plant Detail Page Thumbnail Switcher */
function initPlantGallerySwitcher() {
  const mainImg = document.querySelector('.main-preview-img');
  const thumbs = document.querySelectorAll('.thumb-img');

  if (!mainImg || !thumbs.length) return;

  thumbs.forEach((thumb) => {
    thumb.addEventListener('click', () => {
      thumbs.forEach((t) => t.classList.remove('active'));
      thumb.classList.add('active');
      mainImg.src = thumb.src;
      mainImg.alt = thumb.alt;
    });
  });
}

/* Lightbox Modal */
function initLightbox() {
  const galleryItems = document.querySelectorAll('.gallery-item');
  const modal = document.querySelector('.lightbox-modal');
  if (!galleryItems.length || !modal) return;

  const modalImg = modal.querySelector('.lightbox-content img');
  const modalCaption = modal.querySelector('.lightbox-caption');
  const closeBtn = modal.querySelector('.lightbox-close');

  galleryItems.forEach((item) => {
    item.addEventListener('click', () => {
      const img = item.querySelector('img');
      const title = item.querySelector('.gallery-overlay h4');
      const desc = item.querySelector('.gallery-overlay p');

      if (img && modalImg) {
        modalImg.src = img.src;
        modalImg.alt = img.alt;
      }
      if (modalCaption) {
        modalCaption.textContent = title ? title.textContent + (desc ? ' — ' + desc.textContent : '') : '';
      }
      modal.classList.add('open');
      document.body.style.overflow = 'hidden';
    });
  });

  function closeModal() {
    modal.classList.remove('open');
    document.body.style.overflow = '';
  }

  if (closeBtn) closeBtn.addEventListener('click', closeModal);
  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeModal();
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('open')) closeModal();
  });
}

/* WhatsApp Interactive Enquiry Generator */
function initWhatsAppForms() {
  const forms = document.querySelectorAll('.whatsapp-form');
  const phone = '919480162989';

  forms.forEach((form) => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();

      const name = form.querySelector('[name="name"]')?.value.trim() || 'Grower';
      const userPhone = form.querySelector('[name="phone"]')?.value.trim() || '';
      const plant = form.querySelector('[name="plant"]')?.value.trim() || 'Avocado Plants';
      const quantity = form.querySelector('[name="quantity"]')?.value.trim() || 'Bulk Requirement';
      const location = form.querySelector('[name="location"]')?.value.trim() || 'Karnataka';
      const delivery = form.querySelector('[name="delivery"]')?.value.trim() || location;
      const message = form.querySelector('[name="message"]')?.value.trim() || '';

      let text = `Hello Green Nest Nursery,\n\nI would like to enquire about plants:\n- Plant: ${plant}\n- Quantity: ${quantity}\n- My Location: ${location}\n- Delivery Destination: ${delivery}`;

      if (userPhone) text += `\n- Contact Number: ${userPhone}`;
      if (name) text += `\n- Name: ${name}`;
      if (message) text += `\n- Notes: ${message}`;

      text += `\n\nPlease share current nursery availability and wholesale quotation.`;

      const encoded = encodeURIComponent(text);
      window.open(`https://wa.me/${phone}?text=${encoded}`, '_blank');
    });
  });
}
