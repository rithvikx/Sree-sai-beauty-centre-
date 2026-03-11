import glob
import os

html_files = glob.glob('d:/SSBC/*.html')

images_to_replace = {
    # Store interior images
    'images/store_interior.png': 'images/store_exterior_real.jpg',  # We'll use the exterior of the beautiful building for the hero
    'images/makeup_products.png': 'images/store_interior_real.jpg',   # Show the interior shelf instead of stock makeup
}

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The Hero element and about element uses store_interior.png stock placeholder
    content = content.replace('"images/store_interior.png"', '"images/store_exterior_real.jpg"')
    
    # Replace makeup card image with the cool Lakme stand inside the store
    content = content.replace('"images/makeup_products.png"', '"images/store_interior_real.jpg"')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Images replaced.")
