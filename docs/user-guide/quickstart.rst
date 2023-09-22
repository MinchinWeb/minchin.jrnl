Quickstart
==========

Prerequisites
-------------

You will want to have `Python <https://www.python.org/downloads/>`_ and `pipx
<https://pypa.github.io/pipx/installation/>`_ installed. You also will want to
know how to pull up the terminal.


Installation
------------

The easiest way to install *minchin.jrnl* is to use ``pipx``. On the terminal::

    pipx install minchin.jrnl

The first time you run *minchin.jrnl*, it will ask you were you want to store
your journal file.

For more details on installation options, read the full :doc:`installation
instructions <installation>`.

Quickstart
----------

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
