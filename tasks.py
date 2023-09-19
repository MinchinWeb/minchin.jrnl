# Install `invoke` to make use of these commands
from invoke import task

try:
    from minchin.releaser import make_release
except ImportError:
    print("[WARN] minchin.releaser not installed.")

DOC_DIR = "docs"

# TODO: move these tasks to a submodule of minchin.jrnl to allow them to be
# documented by Sphinx?


@task
def build_docs(ctx):
    """Build Sphinx documentation."""

    ctx.run(f"sphinx-build -b dirhtml {DOC_DIR} {DOC_DIR}/_build")


@task
def serve_docs(ctx):
    """Start a local webserver to review documentation."""

    print("Go to localhost:8000")
    ctx.run(f"python -m http.server -d {DOC_DIR}/_build")


@task
def lint(ctx):
    """Lint codebase: Run `isort` and `black`."""

    ctx.run("isort tasks.py ./docs ./features ./minchin ./tests")
    ctx.run("black tasks.py ./docs ./features ./minchin ./tests")
