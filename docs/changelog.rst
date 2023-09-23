Changelog for *minchin.jrnl* v. |release|
=========================================

*This starts with v7. Future plans are to add the changelog of previous
versions at a later date to this format.*

- :bug:`- major` allow exporting files to nested directories.
- :bug:`- major` Work with updated (v4 or greater)`tzlocal` API. (DayOne
  classic journal particular issue.) c.f. legacy `Pull Request #1528
  <https://github.com/jrnl-org/jrnl/pull/1528>`_.
- :feature:`-` allow top-level ``__version__`` without use of an
  ``__init__.py`` file. c.f. legacy `Pull Request #1296
  <https://github.com/jrnl-org/jrnl/pull/1296>`_. This had (previously?) been
  required for namespace plugins to load.
- :feature:`-` merge external plugin support, as per legacy `Pull Request #1216
  <https://github.com/jrnl-org/jrnl/pull/1216>`_. Also merges relevant parts of
  legacy `Pull Request #1115 <https://github.com/jrnl-org/jrnl/pull/1115>`_;
  c.f. legacy `Pull Request #1281
  <https://github.com/jrnl-org/jrnl/pull/1281>`_.
- :release:`7.0.0 <2023-9-19>`
- :support:`-` add GitHub dependabot congifuration (to keep GitHub
  actions up to date).
- :support:`-` switch from *poetry* to *setuptools* and *pip-tools*
  to manage project dependencies. Update GitHub automated tested as needed.
- :support:`-` move from poetry specific ``pyproject.toml`` project
  metadata to "generic" metadata. Packaging is now done with *setuptools*.
- :support:`-` remove *poetry* as a task running, and start moving
  to *invoke* (incomplete). Also, remove ``Makefile``.
- :support:`-` move release process from GitHub action to
  *minchin.releaser*.
- :support:`3` start reworking documentation, moving them from *MKDocs* to
  *Sphinx* (incomplete). Also, remove automatic generation of the Changelog
  through GitHub Actions. *Sphinx* documentation is live online at
  `<http://minchin.ca/minchin.jrnl/>`_.
- :support:`-` update Code of Conduct, Contributing, Readme.
- :support:`-` change *isort* profile.
- :support:`-` remove (user unfriendly) stale bot (used on GitHub
  issues and pull requests).
- :support:`2` **BREAKING CHANGE**: move on disk location of configuration, and
  configuration filename (now ``minchin.jrnl.yaml``). The included upgrade
  process should automatically manage this, if you are upgrading.
- :support:`1` **BREAKING CHANGE**: move code from ``jrnl`` namespace to
  ``minchin.jrnl`` namespace.
- :feature:`-` remove upper Python limit (was previously 3.9)
- :bug:`- major` update project URLs throughout.

- :release:`2.6.0 <2020-12-19>`
- :support:`-` *This is the base release from* ``jnrl-org/jrnl`` *that I'm
  using.*


The changelog is managed with `Releases`_.

Git History Comparisions
------------------------

- `7.0.0 to (development) head
  <https://github.com/MinchinWeb/minchin.jrnl/compare/7.0.0...phoenix>`_
- `2.6.0 (last "legacy" release) to 7.0.0
  <https://github.com/MinchinWeb/minchin.jrnl/compare/legacy/v2.6.0...7.0.0>`_

.. _Releases: https://releases.readthedocs.io/en/latest/index.html
