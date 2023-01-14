import os
import subprocess
import sys

sys.path.insert(0, os.path.abspath("fake/"))


project = "rollNW"
extensions = [
    'sphinx_tabs.tabs',
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "enum_tools.autoenum",
]

# Check if we're running on Read the Docs' servers
read_the_docs_build = os.environ.get('READTHEDOCS', None) == 'True'

if not read_the_docs_build:
    html_theme = "sphinx_rtd_theme"

breathe_projects = {}
