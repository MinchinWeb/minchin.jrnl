# Install `invoke` to make use of these commands
from invoke import task

try:
    from minchin.releaser import make_release  # noqa: F401
except ImportError:
    print("[WARN] minchin.releaser not installed.")

DOC_DIR = "docs"

# TODO: move these tasks to a submodule of minchin.jrnl to allow them to be
# documented by Sphinx?


@task
def build_docs(ctx, color=True):
    """
    Build Sphinx documentation.

    Args:
        --color / --no-color:  Whether to force color mode (default is on)
    """

    color_cli = ""
    if color:
        color_cli = "--color "

    ctx.run(f"sphinx-build -b dirhtml {color_cli}{DOC_DIR} {DOC_DIR}/_build")


@task
def serve_docs(ctx):
    """Start a local webserver to review documentation."""

    print("Go to localhost:8000")
    ctx.run(f"python -m http.server -d {DOC_DIR}/_build")


@task
def lint(ctx, color=True):
    """
    Lint codebase: Run `isort` and `black`.

    Args:
        --color / --no-color:  Whether to force color mode (default is on)
    """

    color_cli = ""
    if color:
        color_cli = " --color"

    ctx.run(f"isort tasks.py ./docs ./features ./minchin ./tests{color_cli}")
    ctx.run(f"black tasks.py ./docs ./features ./minchin ./tests{color_cli}")


@task
def test_style(ctx, color=True):
    """
    Tests codebase for style issues. Runs `flake8`.

    Args:
        --color / --no-color:  Whether to force color mode (default is on)
    """

    if color:
        color_cli = "--color always"
    else:
        color_cli = "--color never"

    ctx.run(f"flake8 tasks.py ./docs ./features ./minchin ./tests {color_cli}")
