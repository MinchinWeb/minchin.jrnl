Changelog for *minchin.jrnl* v. |release|
=========================================

*This starts with v7. Future plans are to add the changelog of previous
versions at a later date to this format.*

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
- :support:`-` start reworking documentation, moving them from *MKDocs* to
  *Sphinx* (incomplete). Also, remove automatic generation of the Changelog
  through GitHub Actions. *Sphinx* documentation is live online at
  `<http://minchin.ca/minchin.jrnl/>`_.
- :support:`-` update Code of Conduct, Contributing, Readme.
- :support:`-` change *isort* profile.
- :support:`-` remove (user unfriendly) stale bot (used on GitHub
  issues and pull requests).
- :support:`-` **BREAKING CHANGE**: move on disk location of configuration, and
  configuration filename (now ``minchin.jrnl.yaml``). The included upgrade
  process should automatically manage this, if you are upgrading.
- :support:`-` **BREAKING CHANGE**: move code from ``jrnl`` namespace to
  ``minchin.jrnl`` namespace.
- :feature:`-` remove upper Python limit (was previously 3.9)
- :bug:`- major` update project URLs throughout.

- :release:`2.6.0 <2020-12-19>`
- :support:`-` *This is the base release from* ``jnrl-org/jrnl`` *that I'm
  using.*


The changelog is managed with `Releases`_.

.. _Releases: https://releases.readthedocs.io/en/latest/index.html
