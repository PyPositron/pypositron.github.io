# PyPositron Docs Converter

This utility converts Markdown documentation files into static HTML pages for the PyPositron website. It uses a template system to ensure a consistent look and includes automatic sidebar navigation.

## Features

- Converts all `.md` files in the working directory to HTML
- Uses GitHub-flavored Markdown rendering
- Automatically generates sidebar links for navigation
- Outputs HTML files into a `converted/` directory, each in its own subfolder

## Prerequisites

- Python 3.x installed
- Required Python packages:
  - `markdown-it-py`
  - `linkify-it-py`

Install dependencies:
```bash
pip install markdown-it-py linkify-it-py
```

## Usage

1. **Prepare your files:**
    - Place your Markdown files (e.g. `usage.md`, `api.md`) in the same directory as `docs_converter.py`.
      To get the Markdown files from the Wiki, use `git clone https://github.com/itzmetanjim/py-positron.wiki.git`
    - You should download the `template.html` from this directory for consistency.
      If you are making a new tempplate or editing the existing one, your new template should include:
      - `<!--INSERT CONVERTED HTML HERE-->` : placeholder for the main content, converted by the script. This won't have any styling.
      - `<!--INSERT SIDEBAR LINKS HERE-->` : placeholder for sidebar navigation.

2. **Run the script:**
    ```bash
    python docs_converter.py
    ```
    (from within the `convertscript` directory)

3. **Find your output:**
    - Converted HTML files will be saved in the `converted/` directory.
    - Each Markdown file will have its own subfolder, e.g. `converted/usage/index.html`.
    - Just upload everything in `converted` into the root directory of the web repo (as a PR).

## Example Workflow

```bash
cd convertscript
python docs_converter.py
```

If you have `usage.md` and `api.md`, you’ll get:
- `converted/usage/index.html`
- `converted/api/index.html`

## Notes

- The sidebar is generated automatically with links to all markdown files in the directory.
- The script prints progress and info messages during the conversion process.
