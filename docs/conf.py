# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import re

# import minchin.jrnl
import minchin.jrnl.constants

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = minchin.jrnl.constants.__title__
copyright = " {} {} & other contributors".format(
    minchin.jrnl.constants.__copyright_years__, minchin.jrnl.constants.__author__
)

author = minchin.jrnl.constants.__author__

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = minchin.jrnl.__version__
# The short X.Y version.
_p = re.compile(r"\d+\.\d+")
_versionmatch = _p.match(release)
version = _versionmatch.group()

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# location of "master" Table of Contents, as added to the sidebar
master_doc = "contents"

extensions = [
    "sphinx.ext.githubpages",  # produces .nojekyll file
    "releases",
]

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

# -- Others ------------------------------------------------------------------

releases_github_path = "minchinweb/minchin.jrnl"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.ico"

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# Output file base name for HTML help builder.
htmlhelp_basename = minchin.jrnl.constants.__title__ + "doc"


# for releases
# releases_release_uri =
# releases_issue_uri =
releases_github_path = "MinchinWeb/minchin.jrnl"
# see debug output while building your docs
# releases_debug = True
