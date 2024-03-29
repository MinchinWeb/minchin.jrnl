#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2012-2021 jrnl contributors
# License: https://www.gnu.org/licenses/gpl-3.0.html

"""
Exporter for testing and experimentation purposes.

It is not called "testing" because then it's not installed (at least by default
by pip).

The presence of this plugin is also used as a "switch" by the test suite to
decide on whether or not to run the "vanilla" test suite, or the test suite for
external plugins. The `export_entry` and `export_journal` methods are both
purposely not implemented to confirm behavior on plugins that don't implement
them.
"""

from minchin.jrnl.plugins.base import BaseExporter


class Exporter(BaseExporter):
    names = ["testing", "test"]
    version = "0.0.1"
    extension = "test"
