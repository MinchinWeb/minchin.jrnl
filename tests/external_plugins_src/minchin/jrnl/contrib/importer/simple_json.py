# minchin\jrnl\contrib\importer\simple_json.py
import json
import sys

from minchin.jrnl import Entry
from minchin.jrnl.plugins.base import BaseImporter

__version__ = "1.0.1"


class Importer(BaseImporter):
    """JSON Importer for jrnl."""

    names = ["json"]
    version = __version__

    @staticmethod
    def import_(journal, my_input=None):
        """
        Given a nicely formatted JSON file, will add the
        contained Entries to the journal.

        This has no error checking.
        """

        old_cnt = len(journal.entries)
        if my_input:
            with open(my_input, "r", encoding="utf-8") as f:
                data = json.loads(f)
        else:
            try:
                data = sys.stdin.read()
            except KeyboardInterrupt:
                print(
                    "[Entries NOT imported into journal.]",
                    file=sys.stderr,
                )
                sys.exit(0)

        for json_entry in data:
            raw = json_entry["title"] + "/n" + json_entry["body"]
            date = json_entry["date"]
            entry = Entry.Entry(journal, date, raw)
            journal.entries.append(entry)

        new_cnt = len(journal.entries)
        print(
            "[{} entries imported to '{}' journal]".format(
                new_cnt - old_cnt, journal.name
            ),
            file=sys.stderr,
        )
