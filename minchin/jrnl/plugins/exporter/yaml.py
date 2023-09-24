from minchin.jrnl.plugins.exporter.pelican import (  # noqa: E401
    Exporter as PelicanExporter,
)


class Exporter(PelicanExporter):
    """
    This Exporter can convert entries and journals into Markdown formatted text
    with YAML front matter.

    For now, it is an exact copy of the ``pelican`` exporter (although that may
    change in future version.)
    """

    names = ["yaml"]
