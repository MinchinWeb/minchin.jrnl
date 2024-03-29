from datetime import date
import json

import pytest

from minchin.jrnl import Entry, Journal
from minchin.jrnl.plugins.exporter import json as json_exporter

try:
    from jrnl.contrib.exporter import testing as testing_exporter
except:
    testing_exporter = None

if testing_exporter:

    @pytest.fixture()
    def create_entry():
        entry = Entry.Entry(
            journal=Journal.Journal(),
            text="This is the entry text",
            date=date(year=2001, month=1, day=1),
            starred=True,
        )
        yield entry

    class TestBaseExporter(testing_exporter.Exporter):
        def test_unimplemented_export(self, create_entry):
            entry = create_entry
            with pytest.raises(NotImplementedError):
                self.export_entry(entry)

    class TestJsonExporter(json_exporter.Exporter):
        def test_json_exporter_name(self):
            assert "json" in self.names

        def test_export_entry(self, create_entry):
            entry = create_entry
            exported = self.export_entry(entry)
            deserialized_export = json.loads(exported)
            assert deserialized_export["title"] == "This is the entry text"
            assert deserialized_export["date"] == "2001-01-01"
