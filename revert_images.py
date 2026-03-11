import glob
import os

html_files = glob.glob('d:/SSBC/*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The Hero element and about element originally used store_interior.png
    content = content.replace('"images/store_exterior_real.jpg"', '"images/store_interior.png"')
    
    # The makeup card image originally used makeup_products.png
    content = content.replace('"images/store_interior_real.jpg"', '"images/makeup_products.png"')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Images reverted back to stock.")
