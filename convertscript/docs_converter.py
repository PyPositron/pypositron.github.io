import markdown_it
import linkify_it
import os
import re
md = markdown_it.MarkdownIt("gfm-like")
md_string="""
# This is an example
```python
print("Hello, World!")
```
[Link to Python](https://www.python.org)
# Another section
## This is a heading
### Basic Selectors

*   `"#myId"`: Selects element with id="myId"
*   `".myClass"`: Selects all elements with class="myClass"
*   `"div"`: Selects all `<div>` elements
*   `"*"`: Selects all elements
```html
<div id="myId" class="myClass">Content</div>
```
"""
"""Commented out test code
print(md.render(md_string))
with open("template.html", "r", encoding="utf-8") as f:
    template = f.read()
docsfile = template.replace("<!--INSERT CONVERTED HTML HERE-->", md.render(md_string))
with open("converteddocs.html", "w", encoding="utf-8") as f:
    f.write(docsfile)
print("Converted docs saved to converteddocs.html")
"""

def convert_markdown_to_html(md_string, sidebar_links, template_path="template.html"):
    md = markdown_it.MarkdownIt("gfm-like")
    rendered_html = md.render(md_string)
    
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
    
    rendered_html = re.sub(
        r'<a href="(?!https?://|http://|/)([^"]+)"',
        r'<a href="/\1"',
        rendered_html
    )
    docsfile = template.replace("<!--INSERT CONVERTED HTML HERE-->", rendered_html).replace("<!--INSERT SIDEBAR LINKS HERE-->", sidebar_links)
    return docsfile
def sidebar_link(filename):
    formatted_filename = filename.replace(".md", "").replace("-", " ").replace("_", " ").title()
    return f'<a href="/{filename.replace(".md", "")}" class="sidebar-link">{formatted_filename}</a>'
def generate_sidebar_links(filenames):
    sidebar_links = []
    for filename in filenames:
        if filename.endswith(".md"):
            sidebar_links.append(sidebar_link(filename))
    return "\n".join(sidebar_links)

markdown_files = []
ld=os.listdir(".")
for file in ld:
    if file.endswith(".md"):
        markdown_files.append(file)
print("[INFO] Markdown files found:", "\n".join(markdown_files))
converted_paths=[]
for i in markdown_files:
    converted_paths.append("converted/"+i.replace(".md", "")+"/index.html")
sidebar_links = generate_sidebar_links(markdown_files)
print("[INFO] Generated sidebar links:", sidebar_links)
for i,j in zip(markdown_files,converted_paths):
    print(f"[INFO] Converting {i} to {j}")
    with open(i, "r", encoding="utf-8") as f:
        md_string = f.read()
    converted_html = convert_markdown_to_html(md_string, sidebar_links)
    print(f"       Converted HTML for {i}")
    os.makedirs(os.path.dirname(j), exist_ok=True)
    with open(j, "w", encoding="utf-8") as f:
        f.write(converted_html)
    print(f"       Saved converted HTML to {j}\n")
print("\n[INFO] Conversion complete. HTML files saved in 'converted' directory.")
