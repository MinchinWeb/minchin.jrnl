"""
This project uses the Semantic Versioning scheme in conjunction with PEP 0440:

    <http://semver.org/>
    <https://www.python.org/dev/peps/pep-0440>

Major versions introduce significant changes to the API, and backwards
compatibility is not guaranteed. Minor versions are for new features and other
backwards-compatible changes to the API. Patch versions are for bug fixes and
internal code changes that do not affect the API.

Certain version numbers will be skipped, to try and avoid confusion with
jrnl-org/jrnl ("legacy") releases.
"""
import sys

__version__ = "7.1.0"


# this makes the version available at `minchin.jrnl.__version__` without
# requiring a `__init__.py` file in the *jrnl* root directory
sys.modules["minchin.jrnl.__version__"] = __version__
