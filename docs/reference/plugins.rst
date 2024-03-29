Extending minchin.jrnl
======================

*minchin.jrnl* can be extended with custom importers and exporters.

Note that custom importers and exporters can be given the same name as a
built-in importer or exporter to override it.

Custom Importers and Exporters are traditional Python packages, and are
installed (into *minchin.jrnl*) simply by installing them so they are available
to the Python interpreter that is running *minchin.jrnl*.

Exporter are also used as “formatters” when entries are written to the command
line.


Rational
--------

I added this feature because *minchin.jrnl* was overall working well for me,
but I found myself maintaining a private fork so I could have a slightly
customized export format. Implementing (import and) export plugins was seen as
a way to maintain my custom exporter without the need to maintaining my private
fork.

This implementation tries to keep plugins as light as possible, and as free of
boilerplate code as reasonable. As well, internal importers and exporters are
implemented in almost exactly the same way as custom importers and exporters,
and so it is hoped that plugins can be moved from “contributed” to “internal”
easily, or that internal plugins can serve as a base and/or a demonstration for
external plugins.

-- @MinchinWeb, May 2021


Entry Class
-----------

Both the Importers and the Exporters work on the ``Entry`` class. Below
is a (selective) description of the class, it's properties and
functions:

-  **Entry** (class) at ``minchin.jrnl.Entry.Entry``.

   -  **title** (string): a single line that represents a entry's title.
   -  **date** (datetime.datetime): the date and time assigned to an entry.
   -  **body** (string): the main body of the entry. Can be basically any
      length. *jrnl* assumes no particular structure here.
   -  **starred** (boolean): is an entry starred? Presumably, starred entries
      are of particular importance.
   -  **tags** (list of strings): the tags attached to an entry. Each tag
      includes the pre-facing “tag symbol”.
   -  **\__init__(journal, date=None, text="", starred=False)**: contractor
      method

      -  **journal** (*minchin.jrnl.Journal.Journal*): a link to an existing
         Journal class. Mainly used to access it’s configuration.
      -  **date** (datetime.datetime)
      -  **text** (string): assumed to include both the title and the body.
         When the title, body, or tags of an entry are requested, this text
         will the parsed to determine the tree.
      -  **starred** (boolean)

Entries also have “advanced” metadata if they are using the DayOne backend, but
we'll ignore that for the purposes of this demo.


Custom Importer
---------------

If you have a (custom) datasource that you want to import into your jrnl
(perhaps like a blog export), you can write a custom importer to do this.

An importer takes the source data, turns it into Entries and then appends those
entries to a Journal. Here is a basic Importer, assumed to be provided with a
nicely formatted JSON file:

.. include:: ../tests/external_plugins_src/minchin/jrnl/contrib/importer/simple_json.py
   :literal:

Note that the above is very minimal, doesn't do any error checking, and doesn't
try to import all possible entry metadata.

Another potential use of a custom importer is to effectively create a scripted
entry creator. For example, maybe each day you want to create a journal entry
that contains the answers to specific questions; you could create a custom
“importer” that would ask you the questions, and then create an entry
containing the answers provided.

Some implementation notes:

-  The importer class must be named **Importer**, and should sub-class
   **minchin.jrnl.plugins.base.BaseImporter**.
-  The importer module must be within the **minchin.jrnl.contrib.importer**
   namespace.
-  The importer must not have any ``__init__.py`` files in the base directories
   (but you can have one for your importer base directory if it is in a
   directory rather than a single file).
-  The importer must be installed as a Python package available to the same
   Python interpreter running jrnl.
-  The importer must expose at least the following the following members:

   -  **version** (string): the version of the plugin. Displayed to help the
      user debug their installations.
   -  **names** (list of strings): these are the “names” that can be passed to
      the CLI to involve your importer. If you specify one used by a built-in
      plugin, it will overwrite it (effectively making the built-in one
      unavailable).
   -  **import_(journal, input=None)**: the actual importer. Must append
      entries to the journal passed to it. It is recommended to accept either a
      filename or standard input as a source.


Custom Exporter
---------------

Custom exporters are useful to make *minchin.jrnl* 's data available to other
programs. One common usecase would to generate the input to be used by a static
site generator or blogging engine.

An exporter take either a whole journal or a specific entry and exports it.
Below is a basic JSON Exporter; note that a more extensive JSON exporter is
included in *minchin.jrnl* and so this (if installed) would override the built
in exporter.

.. include:: ../tests/external_plugins_src/minchin/jrnl/contrib/exporter/custom_json.py
   :literal:

Note that the above is very minimal, doesn't do any error checking, and doesn't
export all entry metadata.

Some implementation notes:

-  the exporter class must be named **Exporter** and should sub-class
   **jrnl.plugins.base.BaseExporter**.
-  the exporter module must be within the **minchin.jrnl.contrib.exporter**
   namespace.
-  The exporter must not have any ``__init__.py`` files in the base directories
   (but you can have one for your exporter base directory if it is in a
   directory rather than a single file).
-  The exporter must be installed as a Python package available to the same
   Python interpreter running jrnl.
-  the exporter should expose at least the following the following members
   (there are a few more you will need to define if you don't subclass
   ``minchin.jrnl.plugins.base.BaseExporter``):

   -  **version** (string): the version of the plugin. Displayed to help the
      user debug their installations.
   -  **names** (list of strings): these are the “names” that can be passed to
      the CLI to invole your exporter. If you specific one used by a built-in
      plugin, it will overwrite it (effectively making the built-in one
      unavailable).
   -  **extension** (string): the file extention used on exported entries.
   -  **export_entry(entry)**: given an entry, returns a string of the
      formatted, exported entry.
   -  **export_journal(journal)**: (optional) given a journal, returns a string
      of the formatted, exported entries of the journal. If not implemented,
      *jrnl* will call **export_entry()** on each entry in turn and then
      concatenate the results together.

Special Exporters
~~~~~~~~~~~~~~~~~

There are a few “special” exporters, in that they are called by *minchin.jrnl*
in situations other than a traditional export. They are:

-  **short** -- called by ``jrnl --short``. Displays each entry on a single
   line. The default is to print the timestamp of the entry, followed by the
   title. The built-in (default) plugin is at
   ``minchin.jrnl.plugins.exporter.short``.
-  **default** -- called when a different format is not specified. The built-in
   (default) plugin is at ``minchin.jrnl.plugins.exporter.pretty``.

Development Tips
----------------

-  Editable installs (``pip install -e ...``) don't seem to (always?) play nice
   with the namespace layout. If your plugin isn't appearing, try a
   non-editable install of both *minchin.jrnl* and your plugin. If that still
   doesn't work, try re-creating your virtual environment.
-  If you run *minchin.jrnl* from the main project root directory (the one that
   contains *minchin.jrnl*\ 's source code), namespace plugins won't be
   recognized. This is (I suspect) because the Python interpreter will find
   your *minchin* source directory (which doesn't contain your namespace
   plugins) before it find your “site-packages” directory (i.e. installed
   packages, which will recognize namespace packages).
-  Don't name your plugin file ``testing.py`` or it won't be installed (at least
   automatically) by pip.
-  For examples, you can look to the *minchin.jrnl*\ 's internal importers and
   exporters. As well, there are some basic external examples included in
   *minchin.jrnl*\ 's git repo at ``tests/external_plugins_src`` (including the
   example code above).
- overwrite ``def make_filename(cls, entry)`` (class method) to change the
  exported files' filenames.
