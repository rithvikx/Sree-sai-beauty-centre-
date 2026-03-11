import glob

html_files = glob.glob('d:/SSBC/*.html')

bad_favicon = """href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'><i class="fa-solid fa-wand-magic-sparkles"></i></text></svg>\""""
good_favicon = """href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>💄</text></svg>\""""

# Sometimes it might be split across lines, let's use a regex or string replacement.
# In index.html:
#       href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'><i class="fa-solid fa-wand-magic-sparkles"></i></text></svg>"
# In others:
#   <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'><i class="fa-solid fa-wand-magic-sparkles"></i></text></svg>" />

import re

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The issue is exactly: <i class="fa-solid fa-wand-magic-sparkles"></i> inside the SVG.
    # We can just replace it specifically inside the data:image/svg string:
    pattern = r'(data:image/svg\+xml,<svg[^>]+><text[^>]+>)<i class="fa-solid fa-wand-magic-sparkles"></i>(</text></svg>)'
    
    content = re.sub(pattern, r'\g<1>💄\g<2>', content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Fixed favicons in {len(html_files)} files.")
