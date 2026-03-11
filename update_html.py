import os
import glob
import re

html_files = glob.glob('d:/SSBC/*.html')

emoji_map = {
    '💄': '<i class="fa-solid fa-wand-magic-sparkles"></i>',
    '🛍️': '<i class="fa-solid fa-bag-shopping"></i>',
    '📞': '<i class="fa-solid fa-phone"></i>',
    '📍': '<i class="fa-solid fa-location-dot"></i>',
    '⭐': '<i class="fa-solid fa-star"></i>',
    '🌟': '<i class="fa-solid fa-star"></i>',
    '💬': '<i class="fa-brands fa-whatsapp"></i>',
    '📸': '<i class="fa-solid fa-camera"></i>',
    'ℹ️': '<i class="fa-solid fa-circle-info"></i>',
    '🏠': '<i class="fa-solid fa-house"></i>',
    '🏷️': '<i class="fa-solid fa-tags"></i>',
    '✨': '<i class="fa-solid fa-sparkles"></i>',
    '💰': '<i class="fa-solid fa-coins"></i>',
    '🚚': '<i class="fa-solid fa-truck-fast"></i>',
    '🌿': '<i class="fa-solid fa-leaf"></i>',
    '💋': '<i class="fa-solid fa-heart"></i>',
    '🌸': '<i class="fa-solid fa-spa"></i>',
    '💆': '<i class="fa-solid fa-user"></i>',
    '🕐': '<i class="fa-regular fa-clock"></i>',
    '✅': '<i class="fa-solid fa-check"></i>',
    '✂️': '<i class="fa-solid fa-scissors"></i>',
    '💅': '<i class="fa-solid fa-hand-sparkles"></i>',
    '🏪': '<i class="fa-solid fa-shop"></i>',
    '🧴': '<i class="fa-solid fa-bottle-droplet"></i>',
    '📅': '<i class="fa-regular fa-calendar"></i>',
    '✦': '<i class="fa-solid fa-star-of-life"></i>'
}

def replace_classes(match):
    classes = match.group(1)
    
    delay = None
    if 'fade-in-delay-1' in classes:
        delay = '100'
        classes = classes.replace('fade-in-delay-1', '')
    elif 'fade-in-delay-2' in classes:
        delay = '200'
        classes = classes.replace('fade-in-delay-2', '')
    elif 'fade-in-delay-3' in classes:
        delay = '300'
        classes = classes.replace('fade-in-delay-3', '')
        
    has_fade = False
    if 'fade-in' in classes:
        has_fade = True
        classes = classes.replace('fade-in', '')
        
    classes = ' '.join(classes.split())
    
    res = f'class="{classes}"'
    if has_fade:
        res += ' data-aos="fade-up"'
    if delay:
        res += f' data-aos-delay="{delay}"'
        
    if 'class=""' in res:
        res = res.replace('class="" ', '')
        
    return res

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. CDNs
    if "font-awesome/6.4.0/" not in content:
        content = content.replace('</head>', '  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />\n    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet" />\n  </head>')
    
    if "aos.js" not in content:
        content = content.replace('</body>', '  <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>\n  </body>')

    # 2. Add AOS classes
    content = re.sub(r'class="([^"]*fade-in[^"]*)"', replace_classes, content)

    # 3. Floating Whatsapp SVG -> FA
    svg_pattern = r'<svg viewBox="0 0 24 24".*?</svg>'
    content = re.sub(svg_pattern, '<i class="fa-brands fa-whatsapp" style="font-size: 32px; color: white;"></i>', content, flags=re.DOTALL)

    # 4. Emojis
    for emoji, tag in emoji_map.items():
        content = content.replace(emoji, tag)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# 5. Fix main.js for AOS initialization
js_file = 'd:/SSBC/js/main.js'
with open(js_file, 'r', encoding='utf-8') as f:
    js_content = f.read()

# remove old intersection observer
old_fade = """/* ---- Fade-in on scroll ---- */
const fadeEls = document.querySelectorAll(".fade-in");
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
      }
    });
  },
  { threshold: 0.1, rootMargin: "0px 0px -40px 0px" },
);

fadeEls.forEach((el) => observer.observe(el));"""

js_content = js_content.replace(old_fade, "/* ---- Initialize AOS ---- */\nif (typeof AOS !== 'undefined') {\n  AOS.init({\n    once: true,\n    offset: 50,\n    duration: 800\n  });\n}")

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Updated {len(html_files)} HTML files and main.js.")
