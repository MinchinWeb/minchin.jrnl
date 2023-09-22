#!/usr/bin/env python
# Copyright (C) 2012-2021 jrnl contributors
# License: https://www.gnu.org/licenses/gpl-3.0.html
# Code contributed on or before April 18, 2020 and by William Minchin (any
# date) is duel licensed under the MIT license as well.


import glob
import logging
import os
from pathlib import Path
import sys

from platformdirs import user_config_dir, user_documents_dir
import xdg.BaseDirectory  # for Legacy file locations
import yaml

from . import __version__
from .config import load_config, verify_config_colors
from .constants import (
    ISSUES_URL,
    PLATFORM_DIRS_APP_AUTHOR,
    PLATFORM_DIRS_APP_ENSURE_EXISTS,
    PLATFORM_DIRS_APP_NAME,
    PLATFORM_DIRS_APP_ROAMING,
    PLATFORM_DIRS_APP_VERSION,
    __title__,
)
from .exception import UserAbort
from .os_compat import DEFAULT_WINDOWS_EDITOR, ON_WINDOWS
from .prompt import yesno
from .upgrade import is_version_1

DEFAULT_JOURNAL_FILENAME = "journal.txt"
DEFAULT_JOURNAL_KEY = "default"

USER_HOME = Path(os.path.expanduser("~"))

DEFAULT_CONFIG_NAME = "minchin.jrnl.yaml"
CONFIG_DIR = Path(
    os.path.expanduser(
        user_config_dir(
            appname=PLATFORM_DIRS_APP_NAME,
            appauthor=PLATFORM_DIRS_APP_AUTHOR,
            version=PLATFORM_DIRS_APP_VERSION,
            roaming=PLATFORM_DIRS_APP_ROAMING,
            ensure_exists=PLATFORM_DIRS_APP_ENSURE_EXISTS,
        )
    )
) or (USER_HOME / PLATFORM_DIRS_APP_NAME)

JOURNAL_BASE_DIR = (
    Path(os.path.expanduser(user_documents_dir() or USER_HOME)) / PLATFORM_DIRS_APP_NAME
)
CONFIG_FILEPATH = CONFIG_DIR / DEFAULT_CONFIG_NAME
CONFIG_FILEPATH_FALLBACK = USER_HOME / ".minchin.jrnl.config"
DEFAULT_JOURNAL_FILEPATH = JOURNAL_BASE_DIR / DEFAULT_JOURNAL_FILENAME

LEGACY_DEFAULT_CONFIG_NAME = "jrnl.yaml"
LEGACY_XDG_RESOURCE = "jrnl"

LEGACY_CONFIG_PATH = (
    xdg.BaseDirectory.save_config_path(LEGACY_XDG_RESOURCE) or USER_HOME
)
LEGACY_CONFIG_FILE_PATH = os.path.join(LEGACY_CONFIG_PATH, LEGACY_DEFAULT_CONFIG_NAME)
LEGACY_CONFIG_FILE_PATH_FALLBACK = os.path.join(USER_HOME, ".jrnl_config")

LEGACY_JOURNAL_PATH = xdg.BaseDirectory.save_data_path(LEGACY_XDG_RESOURCE) or USER_HOME
LEGACY_JOURNAL_FILE_PATH = os.path.join(LEGACY_JOURNAL_PATH, DEFAULT_JOURNAL_FILENAME)


default_config = {
    "version": __version__,
    "journals": {"default": DEFAULT_JOURNAL_FILEPATH},
    "editor": os.getenv("VISUAL")
    or os.getenv("EDITOR")
    or (DEFAULT_WINDOWS_EDITOR if ON_WINDOWS else ""),
    "encrypt": False,
    "template": False,
    "default_hour": 9,
    "default_minute": 0,
    "timeformat": "%Y-%m-%d %H:%M",
    "tagsymbols": "@",
    "highlight": True,
    "linewrap": 79,
    "indent_character": "|",
    "colors": {
        "date": "none",
        "title": "none",
        "body": "none",
        "tags": "none",
    },
}


def upgrade_config(config):
    """
    Checks if there are keys missing in a given config dict, and if so, updates
    the config file accordingly. This essentially automatically ports jrnl
    installations if new config parameters are introduced in later versions.
    """
    missing_keys = set(default_config).difference(config)
    if missing_keys:
        for key in missing_keys:
            config[key] = default_config[key]
        save_config(config)
        print(
            f"[Configuration updated to newest version at {CONFIG_FILEPATH}]",
            file=sys.stderr,
        )


def save_config(config):
    config["version"] = __version__

    # make sure the base folder already exists
    CONFIG_FILEPATH.parent.mkdir(exist_ok=True, parents=True)

    with open(CONFIG_FILEPATH, "w") as f:
        yaml.safe_dump(
            config, f, encoding="utf-8", allow_unicode=True, default_flow_style=False
        )


def load_or_install_jrnl():
    """
    If jrnl is already installed, loads and returns a config object.
    Else, perform various prompts to install jrnl.
    """

    MY_CONFIG_FILEPATH = (
        CONFIG_FILEPATH if CONFIG_FILEPATH.exists() else CONFIG_FILEPATH_FALLBACK
    )

    LEGACY_CONFIG_PATH = (
        LEGACY_CONFIG_FILE_PATH
        if os.path.exists(LEGACY_CONFIG_FILE_PATH)
        else LEGACY_CONFIG_FILE_PATH_FALLBACK
    )

    if MY_CONFIG_FILEPATH.exists():
        logging.debug("Reading configuration from file %s", LEGACY_CONFIG_PATH)
        config = load_config(MY_CONFIG_FILEPATH)

        # upgrade, if needed??

        upgrade_config(config)
        verify_config_colors(config)

    elif os.path.exists(LEGACY_CONFIG_PATH) and not MY_CONFIG_FILEPATH.exists():
        from . import upgrade

        logging.debug("Reading configuration from file %s", LEGACY_CONFIG_PATH)
        config = load_config(LEGACY_CONFIG_PATH)

        if is_version_1(LEGACY_CONFIG_PATH):
            try:
                upgrade.upgrade_jrnl_1_2(LEGACY_CONFIG_PATH)
            except upgrade.UpgradeValidationException:
                print("Aborting upgrade.", file=sys.stderr)
                print(
                    "Please tell us about this problem at the following URL:",
                    file=sys.stderr,
                )
                print(
                    f"{ISSUES_URL}/new?title=UpgradeValidationException",
                    file=sys.stderr,
                )
                print("Exiting.", file=sys.stderr)
                sys.exit(1)

        # assumed to be "Legacy" version
        try:
            upgrade.upgrade_jrnl_legacy_phoenix(LEGACY_CONFIG_PATH, MY_CONFIG_FILEPATH)
        except upgrade.UpgradeValidationException:
            print("Aborting upgrade.", file=sys.stderr)
            print(
                "Please tell us about this problem at the following URL:",
                file=sys.stderr,
            )
            print(
                f"{ISSUES_URL}/new?title=UpgradeValidationException",
                file=sys.stderr,
            )
            print("Exiting.", file=sys.stderr)
            sys.exit(1)

        if MY_CONFIG_FILEPATH.exists():
            logging.debug("Reading configuration from file %s", MY_CONFIG_FILEPATH)
            config = load_config(MY_CONFIG_FILEPATH)

        upgrade_config(config)
        verify_config_colors(config)

    else:
        logging.debug(f"Configuration file not found, installing {__title__}...")
        try:
            config = install()
        except KeyboardInterrupt:
            raise UserAbort("Installation aborted")

    logging.debug('Using configuration "%s"', config)
    return config


def install():
    _initialize_autocomplete()

    # Where to create the journal?
    path_query = (
        f'Path to your journal file (leave blank for "{DEFAULT_JOURNAL_FILEPATH}"): '
    )
    MY_JOURNAL_PATH = os.path.abspath(
        input(path_query).strip() or DEFAULT_JOURNAL_FILEPATH
    )
    default_config["journals"][DEFAULT_JOURNAL_KEY] = os.path.expanduser(
        os.path.expandvars(MY_JOURNAL_PATH)
    )

    # If the folder doesn't exist, create it
    path = os.path.split(default_config["journals"][DEFAULT_JOURNAL_KEY])[0]
    try:
        os.makedirs(path)
    except OSError:
        pass

    # Encrypt it?
    encrypt = yesno(
        "Do you want to encrypt your journal? (You can always change this later.)",
        default=False,
    )
    if encrypt:
        default_config["encrypt"] = True
        print("Journal will be encrypted.", file=sys.stderr)
    print()

    save_config(default_config)
    return default_config


def _initialize_autocomplete():
    # readline is not included in Windows Active Python and perhaps some other distributions
    if sys.modules.get("readline"):
        import readline

        readline.set_completer_delims(" \t\n;")
        readline.parse_and_bind("tab: complete")
        readline.set_completer(_autocomplete_path)


def _autocomplete_path(text, state):
    expansions = glob.glob(os.path.expanduser(os.path.expandvars(text)) + "*")
    expansions = [e + "/" if os.path.isdir(e) else e for e in expansions]
    expansions.append(None)
    return expansions[state]
