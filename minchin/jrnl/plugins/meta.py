#!/usr/bin/env python
# encoding: utf-8

"""
This file ("meta") uses that title in the reflexive sense; i.e. it is the
collection of code that allows plugins to deal with themselves. In particular,
the code here collects the list of imports and exporters, both internal and
external, and tells the main program which plugins are available. Actual
calling of the plugins is done directly and works because given plugin
functions are importable/callable at predetermined (code) locations. Internal
plugins are located in the `minchin.jrnl.plugins` namespace, and external
plugins are located in the `minchin.jrnl.contrib` namespace.
"""

import importlib
import pkgutil

import minchin.jrnl.contrib.exporter
import minchin.jrnl.contrib.importer
import minchin.jrnl.plugins.exporter
import minchin.jrnl.plugins.importer

__exporters_builtin = list(
    pkgutil.iter_modules(
        minchin.jrnl.plugins.exporter.__path__,
        minchin.jrnl.plugins.exporter.__name__ + ".",
    )
)
__exporters_contrib = list(
    pkgutil.iter_modules(
        minchin.jrnl.contrib.exporter.__path__,
        minchin.jrnl.contrib.exporter.__name__ + ".",
    )
)

__importers_builtin = list(
    pkgutil.iter_modules(
        minchin.jrnl.plugins.importer.__path__,
        minchin.jrnl.plugins.importer.__name__ + ".",
    )
)
__importers_contrib = list(
    pkgutil.iter_modules(
        minchin.jrnl.contrib.importer.__path__,
        minchin.jrnl.contrib.importer.__name__ + ".",
    )
)

__exporter_types_builtin = {
    name: importlib.import_module(plugin.name)
    for plugin in __exporters_builtin
    for name in importlib.import_module(plugin.name).Exporter.names
}
__exporter_types_contrib = {
    name: importlib.import_module(plugin.name)
    for plugin in __exporters_contrib
    for name in importlib.import_module(plugin.name).Exporter.names
}


__importer_types_builtin = {
    name: importlib.import_module(plugin.name)
    for plugin in __importers_builtin
    for name in importlib.import_module(plugin.name).Importer.names
}
__importer_types_contrib = {
    name: importlib.import_module(plugin.name)
    for plugin in __importers_contrib
    for name in importlib.import_module(plugin.name).Importer.names
}

__exporter_types = {
    **__exporter_types_builtin,
    **__exporter_types_contrib,
}
__importer_types = {**__importer_types_builtin, **__importer_types_contrib}

EXPORT_FORMATS = sorted(__exporter_types.keys())
"""list of stings: all available export formats."""
IMPORT_FORMATS = sorted(__importer_types.keys())
"""list of stings: all available import formats."""


def get_exporter(my_format):
    """
    Given an export format, returns the (callable) class of the corresponding exporter.
    """
    try:
        return __exporter_types[my_format].Exporter
    except (AttributeError, KeyError):
        return None


def get_importer(my_format):
    """
    Given an import format, returns the (callable) class of the corresponding importer.
    """
    try:
        return __importer_types[my_format].Importer
    except (AttributeError, KeyError):
        return None
