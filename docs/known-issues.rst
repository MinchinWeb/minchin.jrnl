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
