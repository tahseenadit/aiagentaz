# -*- coding: utf-8 -*-
#
# aiagentaz documentation build configuration file

import importlib
import inspect
import os
import sys
from pathlib import Path

import aiagentaz

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
sys.path.insert(0, os.path.abspath("."))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here
extensions = [
    "sphinx.ext.autodoc",
    "numpydoc",
    "sphinx.ext.linkcode",
]

# Add any paths that contain templates here. Uncomment when there are something in the directory.
# templates_path = ["_templates"]
autodoc_mock_imports = ["openai", "google.generativeai"]

# The suffix of source filenames
source_suffix = ".rst"

# The master toctree document
master_doc = "index"

# General information about the project
project = "aiagentaz"
copyright = "2024, aiagentaz developers"

# The version info for the project
version = aiagentaz.__version__[:3]
release = aiagentaz.__version__

# List of patterns to ignore when looking for source files
exclude_patterns = ["_build", "_autosummary"]

# The name of the Pygments style to use
pygments_style = "sphinx"

# Function to generate source links pointing to GitHub
def linkcode_resolve(domain, info):
    if domain != "py":
        return None

    obj = importlib.import_module(info["module"])
    source_file = Path(inspect.getsourcefile(obj))
    file_path = "/" + "/".join(info["module"].split("."))

    # Try to get a better file path
    add_linenumbers = False
    for part in info["fullname"].split("."):
        try:
            obj = getattr(obj, part)
        except AttributeError:
            break

        try:
            source_file = Path(inspect.getsourcefile(obj))
        except TypeError:
            break

        path_elements = [source_file.name]
        for parent in source_file.parents:
            path_elements = [parent.name] + path_elements
            if parent.name == "aiagentaz":
                break

        file_path = "/".join(path_elements)
    else:
        add_linenumbers = True

    source_url = (
        f"https://github.com/tahseenadit/aiagentaz/blob/v{aiagentaz.__version__}/{file_path}"
    )

    if add_linenumbers:
        try:
            source_lines, start = inspect.getsourcelines(obj)
        except OSError:
            pass
        else:
            end = start + len(source_lines) - 1
            source_url += f"#L{start}-L{end}"

    return source_url

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Pages
html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "external_links": [],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/tahseenadit/aiagentaz",
            "icon": "fab fa-github-square",
        },
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/aiagentaz/",
            "icon": "fas fa-box",
        },
    ],
    "use_edit_page_button": True,
}

html_context = {
    "github_user": "tahseenadit",
    "github_repo": "aiagentaz",
    "github_version": "main",
    "doc_path": "docs/",
}

# Add any paths that contain custom static files.  Uncomment when there are something in the directory.
# html_static_path = ["_static"]

# Output file base name for HTML help builder
htmlhelp_basename = "aiagentazdoc"

# -- Options for LaTeX output --------------------------------------------------

latex_documents = [
    (
        "index",
        "aiagentaz.tex",
        "aiagentaz Documentation",
        "aiagentaz developers",
        "manual",
    )
]

# -- Options for manual page output --------------------------------------------

man_pages = [
    (
        "index", 
        "aiagentaz", 
        "aiagentaz Documentation",
        ["aiagentaz developers"], 
        1
    )
]

# -- Options for Texinfo output ------------------------------------------------

texinfo_documents = [
    (
        "index",
        "aiagentaz",
        "aiagentaz Documentation",
        "aiagentaz developers",
        "aiagentaz",
        "A Python package for interacting with various AI services.",
        "Miscellaneous",
    )
]

# Example configuration for intersphinx
intersphinx_mapping = {"http://docs.python.org/": None}
