#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2012-2021 jrnl contributors
# License: https://www.gnu.org/licenses/gpl-3.0.html

from minchin.jrnl.plugins.base import BaseExporter

from ... import __version__  # deliberate relative import


class Exporter(BaseExporter):
    """This Exporter can convert entries and journals into text files."""

    names = ["text", "txt"]
    extension = "txt"
    version = __version__

    @classmethod
    def export_entry(cls, entry):
        """Returns a string representation of a single entry."""
        return str(entry)
