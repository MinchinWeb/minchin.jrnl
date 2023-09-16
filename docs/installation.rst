Installation
============

If you an just intending to use *minchin.jrnl*, the simplest way to install is
to use pip. However, this is generally not advised (due to potentially causing
issue with your "system" Python), and so better is probably to use ``pipx``:

.. code-block:: sh
    pipx install minchin.jrnl

Upgrades can be done similarly:

.. code-block:: sh
    pipx upgrade minchin.jrnl

(c.f. `Installing pipx <https://pypa.github.io/pipx/installation/>`_.)

You will need to previously have installed Python on your system.

Development Installs
--------------------

If you are installing ``minchin.jrnl`` to hack on it, you probably want to use
a virtual environment instead of ``pipx``. On Windows, you might do something
like this; this will clone the git repo, set up and activate a virtual
environment, and install ``minchin.jrnl`` in editible mode:

.. code-block:: sh
    cd <coding/base/directory>
    git clone https://github.com/MinchinWeb/minchin.jrnl
    cd minchin.jrnl
    python -m venv .venv
    ./.venv/Scripts/activate
    pip install -e .[dev]

``minchin.jrnl`` provides three "extras", for installing optional depencies:
``dev``, ``docs``, and ``release``. The ``dev`` extra (as used in the above
example) provides the Python packages you are likely to use in development,
including linters and test frameworks. The ``docs`` extra will install the
requirements to genearte the project documentation. The ``release`` extra is
likely only useful for me, to push out releases.
