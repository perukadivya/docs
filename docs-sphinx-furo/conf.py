# Sphinx Configuration File
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# -- Project information -----------------------------------------------------
project = 'Data Engineering Docs'
copyright = '2024, Data Engineering Team'
author = 'Data Engineering Team'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx_copybutton',           # Copy button for code blocks
    'sphinxcontrib.mermaid',       # Mermaid diagrams
    'myst_parser',                 # Markdown support
    'sphinx_design',               # Cards, grids, tabs
]

# Markdown support
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# MyST Markdown settings
myst_enable_extensions = [
    'colon_fence',
    'deflist',
    'tasklist',
    'html_admonition',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'venv']

# -- Options for HTML output -------------------------------------------------
html_theme = 'furo'

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#7C3AED",
        "color-brand-content": "#7C3AED",
    },
    "dark_css_variables": {
        "color-brand-primary": "#A78BFA",
        "color-brand-content": "#A78BFA",
    },
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
    "top_of_page_button": "edit",
}

html_static_path = ['_static']
html_title = "Data Engineering Docs"

# -- Copy button settings ----------------------------------------------------
copybutton_prompt_text = r">>> |\$ |In \[\d*\]: |\.\.\.: "
copybutton_prompt_is_regexp = True
copybutton_remove_prompts = True

# -- Mermaid settings --------------------------------------------------------
mermaid_version = "10.6.1"
