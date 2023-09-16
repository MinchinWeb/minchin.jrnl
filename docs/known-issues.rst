Known Issues
============

Windows Store version of Python
-------------------------------

When using the Windows Store version of Python, several filepaths, include the
``%APPDATA%`` folder where configuration is kept, are redirected on disk. So
``C:\Users\<user>\AppData\Local`` becomes (something like)
``C:\Users\<user>\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\Local\``.
This is common to all Windows Store applications, and is part of their security
model. See `https://docs.python.org/3/using/windows.html#windows-store`_ for
more details.

This may become an issue if you change how Python is installed on your machine
(i.e. switch from the Python.org installer to the Windows Store version, or
vis versa), or if you have both installed on your machine and try and run
*minchin.jrnl* from both.

I am also unsure how upgrades to Python will be handled. Please report back
issues if you upgrade the Windows Store version of Python and loose access to
your configuration.


Behave Tests Don't Pass
-----------------------

The ``behave`` tests don't currently pass on GitHub Actions, and I'm not sure
they're ever reliably passed on my local (Windows) machine.

I know at one point ``behave`` had basically been abandoned, but I think the
project has been revived or a new fork exists. I want to investigate the
project's current status before spending a lot of time re-working the tests.


Tests Stomp on Local Journal
----------------------------

Running the tests locally seems to stomp on my default journal file.

Test isolation from the local system needs to be investigated.


Ongoing GPLv3 --> MIT License Migration
---------------------------------------

On of the goals of the project is to move from the (current) GPLv3 license back
to the original MIT license.

The license change (from MIT --> GPLv3) was done with
`Pull Request #918 <https://github.com/jrnl-org/jrnl/pull/918>`_, dated April
18, 2020. Therefore, any code before that and any pull requests submitted
before that can be assumed to be available under the MIT license. Code
contributed or changed after that date will need to be replaced, unless it has
been written by me.

This work is ongoing.
