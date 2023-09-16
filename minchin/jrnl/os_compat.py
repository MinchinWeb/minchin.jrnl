# Copyright (C) 2012-2021 jrnl contributors
# License: https://www.gnu.org/licenses/gpl-3.0.html
# Code contributed on or before April 18, 2020 and by William Minchin (any
# date) is duel licensed under the MIT license as well.

from sys import platform

ON_WINDOWS = "win32" in platform

DEFAULT_WINDOWS_EDITOR = "notepad.exe"
# Default editor on Linux?
