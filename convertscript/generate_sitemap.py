import os
import xml.etree.ElementTree as ET
import urllib.parse
# This is intended to be run in the web root directory.
# List of indexable file extensions
INDEXABLE_EXTENSIONS = {
    ".html", ".htm", ".php", ".asp", ".jsp", ".aspx", ".xml", ".json", ".txt"
}

def generate_sitemap(base_url, output_file="sitemap.xml"):
    # Create the root element of the sitemap
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    # Walk through the current working directory
    for root, _, files in os.walk(os.getcwd()):
        # Skip the `convertscript/` directory
        if "convertscript" in os.path.relpath(root, os.getcwd()).split(os.sep):
            continue
        
        for file in files:
            # Check if the file has an indexable extension
            _, ext = os.path.splitext(file)
            if ext.lower() not in INDEXABLE_EXTENSIONS:
                continue
            
            # Generate the relative path of the file
            file_path = os.path.relpath(os.path.join(root, file), os.getcwd())
            
            # Create a URL element
            url = ET.SubElement(urlset, "url")
            
            # Build the full URL and entity escape it
            loc = ET.SubElement(url, "loc")
            loc.text = urllib.parse.urljoin(base_url, urllib.parse.quote(file_path.replace("\\", "/")))

    # Write the sitemap to a file
    tree = ET.ElementTree(urlset)
    with open(output_file, "wb") as f:
        tree.write(f, encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    # Replace with your site's base URL
    base_url = "https://pypositron.github.io/"
    generate_sitemap(base_url)
    print("Sitemap generated successfully!")
