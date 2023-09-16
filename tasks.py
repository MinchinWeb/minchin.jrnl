# Install `invoke` to make use of these commands

try:
    from minchin.releaser import make_release
except ImportError:
    print("[WARN] minchin.releaser not installed.")
