Requirements
============

General
-------

The main *minchin.jrnl* program, has the following dependencies:

.. include:: ../.requirements/base.in
   :literal:


.. note:: Multiple extras (as detailed below) can be installed at the same
          time; i.e. ``pip install minchin.jrnl[docs,dev,release]``.

Testing
-------

Testing *minchin.jrnl* requires:

.. include:: ../.requirements/dev.in
   :start-line: 9
   :end-line: 17
   :literal:

(This can be installed with the *dev* extra, e.g. ``pip install
minchin.jrnl[dev]``.)

For unit test, then run (from the base directory)::

    pytest

For integration tests, run (from the base directory)::

    behave

.. note:: The behave test suite is currently failing for me, and so
          failures here are permitted.

For code-style "tests" (aka linting), then run (from the base directory)::

    isort
    black


Documentation Generation
------------------------

To generation the documentation (i.e. this) for *minchin.jrnl*, *minchin.jrnl*
itself must be installed (it is imported in the process of building the
documentation). The following dependencies are also required:

.. include:: ../.requirements/docs.in
   :literal:

(This can be installed with the *docs* extra, e.g. ``pip install
minchin.jrnl[docs]``.)

Then run (on Windows) (from the base directory)::

    sphinx-build -b dirhtml ./docs ./docs/_build

.. To upload the documention, then run ...


Release Generation
------------------

To push a release, the following dependencies are also required:

.. include:: ../.requirements/release.in
   :start-line: 2
   :literal:

(This can be installed with the *release* extra, e.g. ``pip install
minchin.jrnl[release]``.)

Releases are managed by *minchin.releaser*.

To push a release, run (from the base directory)::

    invoke make-release

and follow the interactive prompts, make any additions or changes as needed.

.. To push a release...
