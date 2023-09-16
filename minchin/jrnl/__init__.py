#!/usr/bin/env python
# Copyright (C) 2013-17, 2019-20, 2023 William Minchin
# Copyright (C) 2019-23 Jonathan Wren & Micah Jerome Ellison
# Copyright (C) 2012-17, 2019, 2021 Manuel Ebert
# Copyright (C) 2012-23 other minchin.jrnl (and jrnl) contributors
# License: https://www.gnu.org/licenses/gpl-3.0.html

# only me past 2020

__title__ = "minchin.jrnl"
__description__ = "Manage and record your thoughts, in plain text."
__url__ = "https://github.com/MinchinWeb/minchin.jrnl"
__author__ = "William Minchin"
__email__ = "w_minchin@hotmail.com"
__license__ = "GPL 3"
__copyright_years__ = "2013-17, 2019-20, 2023"
__copyright__ = "Copyright (c) {} {} & other contributors".format(
    __copyright_years__, __author__
)
try:
    from .__version__ import __version__
except ImportError:
    __version__ = "source"
__version_codename__ = "Phoenix"

ISSUES_URL = "https://github.com/MinchinWeb/minchin.jrnl/issues"

PLATFORM_DIRS_APP_NAME = __title__
PLATFORM_DIRS_APP_AUTHOR = "minchin"
# Typically `major` or `major.minor` (i.e. not patch number).
# Useful if you want multiple version of the application to be able to run
# side by side.
PLATFORM_DIRS_APP_VERSION = None
# Whether to use the roaming appdata directory on Windows.
PLATFORM_DIRS_APP_ROAMING = False
# A flag to indicating to use opinionated values.
PLATFORM_DIRS_APP_OPINION = True
# Optionally create the directory (and any missing parents) upon access if it
# does not exist. By default, no directories are created.
PLATFORM_DIRS_APP_ENSURE_EXISTS = True


# fmt: off
LEGACY_VERSIONS = [
    # as of September 14, 2023
    # does not include pre-release versions
    # https://pypi.org/project/jrnl/#history

    "0.3.0",
    "1.0.0",
    "1.5.5", "1.5.6",
    "1.6.3", "1.6.4", "1.6.5", "1.6.6",
    "1.7.1", "1.7.2",  "1.7.3",  "1.7.4",  "1.7.5",  "1.7.6",  "1.7.7",  
             "1.7.8",  "1.7.9",  "1.7.10", "1.7.12", "1.7.13", "1.7.14", 
             "1.7.15", "1.7.16", "1.7.17", "1.7.18", "1.7.19", "1.7.20",
             "1.7.22",
    "1.8.0", "1.8.1", "1.8.4", "1.8.6",
    "1.9.0", "1.9.1", "1.9.2", "1.9.3", "1.9.5", "1.9.6", "1.9.7", "1.9.8",
    "2.0.0", "2.0.1",
    "2.1.0", "2.1.1",
    "2.2.0",
    "2.3.0", "2.3.1",
    "2.4.0", "2.4.1", "2.4.2", "2.4.3", "2.4.4", "2.4.5",
    "2.5.0",
    "2.6.0",
    "2.7.0", "2.7.1",
    "2.8.0", "2.8.1", "2.8.2", "2.8.3", "2.8.4",
    "3.0.0",
    "3.1.0",
    "3.2.0",
    "3.3.0",
    "4.0.0", "4.0.1",
]
# fmt: on
