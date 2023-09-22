.. image:: https://raw.githubusercontent.com/MinchinWeb/minchin.jrnl/phoenix/docs/_static/minchin.jrnl-logo-4x.png
   :alt: minchin.jrnl
   :align: center

``minchin.jrnl`` is a simple journal application for the command line.

You can use it to easily create, search, and view journal entries. Journals are
stored as human-readable plain text, and can also be encrypted using `AES
encryption <http://en.wikipedia.org/wiki/Advanced_Encryption_Standard>`_.

|Version| |Changelog| |Pythons| |License| |Testing| |Downloads|

*To get help,* `submit an
issue <https://github.com/MinchinWeb/minchin.jrnl/issues/new/choose>`_ *on
Github.*

In a Nutshell
-------------

To make a new entry, just enter

.. code:: sh

   jrnl yesterday: Called in sick. Used the time to clean the house and write
   my book.

``yesterday:`` is interpreted by ``minchin.jrnl`` as a timestamp. Everything
until the first sentence ending (either ``.``, ``?``, or ``!``) is interpreted
as the title, and the rest as the body. In your journal file, the result will
look like this:

::

   [2012-03-29 09:00] Called in sick.
   Used the time to clean the house and write my book.

If you just call ``jrnl``, you will be prompted to compose your entry - but you
can also configure *minchin.jrnl* to use your external editor.

Installation
------------

::

   pip install minchin.jrnl

(The above assumes you already have Python installed.)

Documentation
-------------

Full documentation is available at http://minchin.ca/minchin.jrnl/

Changelog
---------

Release notes are on my blog at https://blog.minchin.ca/label/minchinjrnl/

Full changelog is available at http://minchin.ca/minchin.jrnl/changelog/


Links
-----

- Code, on GitHub: https://github.com/MinchinWeb/minchin.jrnl
- Report a Bug! https://github.com/MinchinWeb/minchin.jrnl/issues
- Documentation: http://minchin.ca/minchin.jrnl/
- Listing on PyPI: https://pypi.python.org/pypi/minchin.jrnl
- Release Notes: https://blog.minchin.ca/label/minchinjrnl/

License
-------

The project is licensed under GPLv3.

Code contributed on or before April 18, 2020 and by William Minchin (any date)
is duel licensed under the MIT license as well. One of the long term projects
of the goal is to remove or replace any GPLv3 code, and move the entire project
to the MIT license.


Contributors
------------

Maintainers
~~~~~~~~~~~

Our maintainers help keep the lights on for the project:

-  William Minchin (`minchinweb <https://github.com/MinchinWeb>`_)

Please thank them if you like ``minchin.jrnl``!

Code Contributors
~~~~~~~~~~~~~~~~~

This project is made with love by the many `fabulous people
<https://github.com/MinchinWeb/minchin.jrnl/graphs/contributors>`_ who have
contributed. ``minchin.jrnl`` couldn't exist without each and every one of you!

If you'd also like to help make ``minchin.jrnl`` better, please see our
`contributing documentation <CONTRIBUTING.md>`_.


.. |Version| image:: http://img.shields.io/pypi/v/minchin.jrnl.svg?style=flat
   :target: https://pypi.python.org/pypi/minchin.jrnl/
   :alt: PyPI version number

.. |Testing| image:: https://github.com/MinchinWeb/minchin.jrnl/workflows/Testing/badge.svg
   :target: https://github.com/MinchinWeb/minchin.jrnl/actions?query=workflow%3ATesting
   :alt: GitHub Workflow Status

.. |Downloads| image:: https://pepy.tech/badge/minchin.jrnl
   :target: https://pepy.tech/project/minchin.jrnl
   :alt: Download Count

.. |Changelog| image:: https://img.shields.io/badge/-Changelog-success
   :target: http://minchin.ca/minchin.jrnl/changelog/
   :alt: Changelog

.. |License| image:: https://img.shields.io/pypi/l/minchin.jrnl.svg?style=flat
   :target: https://github.com/MinchinWeb/minchin.jrnl/blob/phoenix/LICENSE.rst

.. |Pythons| image:: https://img.shields.io/pypi/pyversions/minchin.jrnl?style=flat
   :target: https://pypi.python.org/pypi/minchin.jrnl/
   :alt: Supported Python versions
