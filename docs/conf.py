# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

copyright = '2024, David Nicholson'
author = 'David Nicholson'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx_copybutton',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx_design',
    'sphinxext.opengraph',
    'sphinx_tabs.tabs',
]

templates_path = ['_templates']
source_suffix = ['.rst', '.md']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = ""
html_theme = 'pydata_sphinx_theme'
html_theme_options = {
    "logo": {
        "text": "",
        "image_light": "",
        "image_dark": "",
    },
    "secondary_sidebar_items": [],
}
html_sidebars = {
  "index": [],
}

html_static_path = ['_static']

myst_enable_extensions = [
    "colon_fence",
    "html_admonition",
    "html_image",
]
