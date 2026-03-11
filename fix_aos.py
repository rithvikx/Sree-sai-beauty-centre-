import glob
import re

html_files = glob.glob('d:/SSBC/*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the existing AOS script tag wherever it is
    content = re.sub(r'\s*<script src="https://unpkg\.com/aos@2\.3\.1/dist/aos\.js"></script>', '', content)
    
    # Insert it right before main.js
    content = content.replace('<script src="js/main.js"></script>', '<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>\n    <script src="js/main.js"></script>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Fixed script order in {len(html_files)} files.")
