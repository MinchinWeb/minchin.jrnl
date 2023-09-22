# Copyright (C) 2012-2021 jrnl contributors
# License: https://www.gnu.org/licenses/gpl-3.0.html
# Code contributed on or before April 18, 2020 and by William Minchin (any
# date) is duel licensed under the MIT license as well.

import logging
import os

from rich.console import Console
from rich.text import Text


def deprecated_cmd(old_cmd, new_cmd, callback=None, **kwargs):
    import sys
    import textwrap

    from .color import RESET_COLOR, WARNING_COLOR

    warning_msg = f"""
    The command {old_cmd} is deprecated and will be removed from jrnl soon.
    Please use {new_cmd} instead.
    """
    warning_msg = textwrap.dedent(warning_msg)
    logging.warning(warning_msg)
    print(f"{WARNING_COLOR}{warning_msg}{RESET_COLOR}", file=sys.stderr)

    if callback is not None:
        callback(**kwargs)


def list_journals(config):
    from .install import CONFIG_FILEPATH

    # resolve Microsoft Store version of Python redirects on Windows
    # https://docs.python.org/3/using/windows.html#windows-store
    MY_CONFIG_FILEPATH = os.path.realpath(CONFIG_FILEPATH)

    """List the journals specified in the configuration file"""
    result = f'Journals defined in "{MY_CONFIG_FILEPATH}"\n\n'
    max_length = min(max(len(k) for k in config["journals"]), 20)
    result = result + "\n".join(
        [
            f''' * {journal:{max_length}} -> "{cfg['journal'] if isinstance(cfg, dict) else cfg}"'''
            for journal, cfg in config["journals"].items()
        ]
    )
    return result


def ansi_wrap(text, width):
    """Wrap text while passing through ANSI colour codes."""
    ansi_text = Text.from_ansi(text, no_wrap=False, tab_size=None)

    console = Console(width=width)
    with console.capture() as capture:
        console.print(ansi_text, sep="", end="")
    return capture.get()
