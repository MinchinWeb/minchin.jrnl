# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import re

import minchin.jrnl

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = minchin.jrnl.__title__
copyright = "{} {} & other contributors".format(
    minchin.jrnl.__copyright_years__, minchin.jrnl.__author__
)

author = minchin.jrnl.__author__

release = minchin.jrnl.__version__
p = re.compile("\d+\.\d+")
versionmatch = p.match(release)
version = versionmatch.group()

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.githubpages",  # produces .nojekyll file
    # 'releases',
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

## Others

releases_github_path = "minchinweb/minchin.jrnl"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "favicon.ico"

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# Output file base name for HTML help builder.
htmlhelp_basename = minchin.jrnl.__title__ + "doc"
