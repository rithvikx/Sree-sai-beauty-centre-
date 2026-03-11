/* =============================================
   Sri Sai Beauty Centre - JavaScript
   ============================================= */

const WHATSAPP_NUM = "919949241212";
const WHATSAPP_BASE = `https://wa.me/${WHATSAPP_NUM}`;

/* ---- Navbar scroll effect ---- */
const navbar = document.getElementById("navbar");
window.addEventListener("scroll", () => {
  if (navbar) {
    navbar.classList.toggle("scrolled", window.scrollY > 40);
  }
});

/* ---- Hamburger menu ---- */
const hamburger = document.getElementById("hamburger");
const mobileNav = document.getElementById("mobileNav");
if (hamburger && mobileNav) {
  hamburger.addEventListener("click", () => {
    hamburger.classList.toggle("open");
    mobileNav.classList.toggle("open");
  });
  // Close on link click
  mobileNav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      hamburger.classList.remove("open");
      mobileNav.classList.remove("open");
    });
  });
}

/* ---- Active nav link ---- */
function setActiveNav() {
  const current = window.location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav-links a, .mobile-nav a").forEach((link) => {
    const href = link.getAttribute("href");
    if (href === current || (current === "" && href === "index.html")) {
      link.classList.add("active");
    }
  });
}
setActiveNav();

/* ---- Initialize AOS ---- */
if (typeof AOS !== 'undefined') {
  AOS.init({
    once: true,
    offset: 50,
    duration: 800
  });
}

/* ---- WhatsApp helpers ---- */
function waLink(msg = "") {
  const encoded = encodeURIComponent(msg);
  return `${WHATSAPP_BASE}?text=${encoded}`;
}

function openWhatsApp(
  msg = "Hello! I am interested in your products at Sri Sai Beauty Centre. Please share more details.",
) {
  window.open(waLink(msg), "_blank");
}

/* ---- Product inquiry ---- */
document.querySelectorAll("[data-wa-product]").forEach((btn) => {
  btn.addEventListener("click", () => {
    const product = btn.getAttribute("data-wa-product");
    const msg = `Hello Sri Sai Beauty Centre! I would like to inquire about *${product}*. Please share pricing and availability details. Thank you!`;
    window.open(waLink(msg), "_blank");
  });
});

/* ---- Contact form ---- */
const contactForm = document.getElementById("contactForm");
if (contactForm) {
  contactForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const name = document.getElementById("cf-name")?.value || "";
    const phone = document.getElementById("cf-phone")?.value || "";
    const msg = document.getElementById("cf-message")?.value || "";
    const type = document.getElementById("cf-type")?.value || "General Inquiry";

    const waMsg = `Hello Sri Sai Beauty Centre!\n\nName: ${name}\nPhone: ${phone}\nInquiry Type: ${type}\n\n${msg}\n\nThank you!`;
    window.open(waLink(waMsg), "_blank");
  });
}

/* ---- Ticker duplication for seamless loop ---- */
const ticker = document.querySelector(".ticker-content");
if (ticker) {
  // Duplicate content for smooth loop
  ticker.innerHTML += ticker.innerHTML;
}

/* ---- Counter animation ---- */
function animateCounters() {
  document.querySelectorAll("[data-count]").forEach((el) => {
    const target = parseInt(el.getAttribute("data-count"));
    const duration = 1500;
    const step = target / (duration / 16);
    let current = 0;
    const timer = setInterval(() => {
      current = Math.min(current + step, target);
      el.textContent = Math.round(current).toLocaleString();
      if (current >= target) clearInterval(timer);
    }, 16);
  });
}

const statsSection = document.querySelector(".hero-stats");
if (statsSection) {
  const statsObserver = new IntersectionObserver(
    (entries) => {
      if (entries[0].isIntersecting) {
        animateCounters();
        statsObserver.disconnect();
      }
    },
    { threshold: 0.3 },
  );
  statsObserver.observe(statsSection);
}

/* ---- Smooth scroll for anchor links ---- */
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", (e) => {
    const href = anchor.getAttribute("href");
    if (href === "#") return;
    const target = document.querySelector(href);
    if (target) {
      e.preventDefault();
      const offset = 80;
      const top =
        target.getBoundingClientRect().top + window.pageYOffset - offset;
      window.scrollTo({ top, behavior: "smooth" });
    }
  });
});
