# Copyright (C) 2012-2021 jrnl contributors
# License: https://www.gnu.org/licenses/gpl-3.0.html
# Code contributed on or before April 18, 2020 and by William Minchin (any
# date) is duel licensed under the MIT license as well.

import os
import shutil
import sys

from . import Journal, __version__
from .EncryptedJournal import EncryptedJournal
from .config import is_config_json, load_config, scope_config
from .constants import __version_codename__
from .exception import UpgradeValidationException, UserAbort
from .prompt import yesno


def backup(filename, binary=False):
    print(f"  Created a backup at {filename}.backup", file=sys.stderr)
    filename = os.path.expanduser(os.path.expandvars(filename))

    try:
        with open(filename, "rb" if binary else "r") as original:
            contents = original.read()

        with open(filename + ".backup", "wb" if binary else "w") as backup:
            backup.write(contents)
    except FileNotFoundError:
        print(f"\nError: {filename} does not exist.")
        try:
            cont = yesno(f"\nCreate {filename}?", default=False)
            if not cont:
                raise KeyboardInterrupt

        except KeyboardInterrupt:
            raise UserAbort("jrnl NOT upgraded, exiting.")


def check_exists(path):
    """
    Checks if a given path exists.
    """
    return os.path.exists(path)


def upgrade_jrnl_1_2(config_path):
    """
    Upgrades jrnl configuration from version 1 to 2.

    In particular, it upgrades the configuration file from JSON to YAML.
    """

    config = load_config(config_path)

    print(
        f"""Welcome to minchin.jrnl {__version__}.

It looks like you've been using an older version of jrnl until now. That's
okay - jrnl will now upgrade your configuration and journal files. Afterwards
you can enjoy all of the great new features that come with jrnl 2:

- Support for storing your journal in multiple files
- Faster reading and writing for large journals
- New encryption back-end that makes installing jrnl much easier
- Tons of bug fixes

Please note that jrnl 1.x is NOT forward compatible with this version of jrnl.
If you choose to proceed, you will not be able to use your journals with
older versions of jrnl anymore.
"""
    )

    encrypted_journals = {}
    plain_journals = {}
    other_journals = {}
    all_journals = []

    for journal_name, journal_conf in config["journals"].items():
        if isinstance(journal_conf, dict):
            path = journal_conf.get("journal")
            encrypt = journal_conf.get("encrypt")
        else:
            encrypt = config.get("encrypt")
            path = journal_conf

        if os.path.exists(os.path.expanduser(path)):
            path = os.path.expanduser(path)
        else:
            print(f"\nError: {path} does not exist.")
            continue

        if encrypt:
            encrypted_journals[journal_name] = path
        elif os.path.isdir(path):
            other_journals[journal_name] = path
        else:
            plain_journals[journal_name] = path

    longest_journal_name = max([len(journal) for journal in config["journals"]])
    if encrypted_journals:
        print(
            f"\nFollowing encrypted journals will be upgraded to jrnl {__version__}:",
            file=sys.stderr,
        )
        for journal, path in encrypted_journals.items():
            print(
                "    {:{pad}} -> {}".format(journal, path, pad=longest_journal_name),
                file=sys.stderr,
            )

    if plain_journals:
        print(
            f"\nFollowing plain text journals will upgraded to jrnl {__version__}:",
            file=sys.stderr,
        )
        for journal, path in plain_journals.items():
            print(
                "    {:{pad}} -> {}".format(journal, path, pad=longest_journal_name),
                file=sys.stderr,
            )

    if other_journals:
        print("\nFollowing journals will be not be touched:", file=sys.stderr)
        for journal, path in other_journals.items():
            print(
                "    {:{pad}} -> {}".format(journal, path, pad=longest_journal_name),
                file=sys.stderr,
            )

    try:
        cont = yesno("\nContinue upgrading jrnl?", default=False)
        if not cont:
            raise KeyboardInterrupt
    except KeyboardInterrupt:
        raise UserAbort("jrnl NOT upgraded, exiting.")

    for journal_name, path in encrypted_journals.items():
        print(
            f"\nUpgrading encrypted '{journal_name}' journal stored in {path}...",
            file=sys.stderr,
        )
        backup(path, binary=True)
        old_journal = Journal.open_journal(
            journal_name, scope_config(config, journal_name), legacy=True
        )
        all_journals.append(EncryptedJournal.from_journal(old_journal))

    for journal_name, path in plain_journals.items():
        print(
            f"\nUpgrading plain text '{journal_name}' journal stored in {path}...",
            file=sys.stderr,
        )
        backup(path)
        old_journal = Journal.open_journal(
            journal_name, scope_config(config, journal_name), legacy=True
        )
        all_journals.append(Journal.PlainJournal.from_journal(old_journal))

    # loop through lists to validate
    failed_journals = [j for j in all_journals if not j.validate_parsing()]

    if len(failed_journals) > 0:
        print(
            "\nThe following journal{} failed to upgrade:\n{}".format(
                "s" if len(failed_journals) > 1 else "",
                "\n".join(j.name for j in failed_journals),
            ),
            file=sys.stderr,
        )

        raise UpgradeValidationException

    # write all journals - or - don't
    for j in all_journals:
        j.write()

    print("\nUpgrading config...", file=sys.stderr)

    backup(config_path)

    print("\nWe're all done here and you can start enjoying jrnl 2.", file=sys.stderr)


def is_version_1(config_path):
    """
    If the configuration file is in JSON, assume the configuration is for jrnl
    v1.
    """
    return is_config_json(config_path)


def upgrade_jrnl_legacy_phoenix(old_config_path, new_config_path):
    """
    Upgrades jrnl configuration from "Legacy" to "Phoenix".

    In particular, it changes the location on disk of the configuration file.
    """

    config = load_config(old_config_path)

    print(
        f"""Welcome to minchin.jrnl {__version__} "{__version_codename__}".

It looks like you've been using an "legacy" version of jrnl until now. Thank
you for making the change!

Minchin.jrnl will now upgrade your configuration, creating a copy for it's
own use. Your journal files will NOT be moved (but you can do this manually
and update the configuration to match).
"""
    )

    all_journals = []
    for journal_name, journal_conf in config["journals"].items():
        if isinstance(journal_conf, dict):
            path = journal_conf.get("journal")
        else:
            path = journal_conf

        if os.path.exists(os.path.expanduser(path)):
            path = os.path.expanduser(path)
        else:
            print(f"\nError: {path} does not exist.")
            continue

        all_journals[journal_name] = path

    longest_journal_name = max([len(journal) for journal in config["journals"]])

    if all_journals:
        print("\nFollowing journals will be not be touched:", file=sys.stderr)
        for journal, path in all_journals.items():
            print(
                "    {:{pad}} -> {}".format(journal, path, pad=longest_journal_name),
                file=sys.stderr,
            )

    try:
        cont = yesno("\nContinue upgrading minchin.jrnl?", default=False)
        if not cont:
            raise KeyboardInterrupt
    except KeyboardInterrupt:
        raise UserAbort("minchin.jrnl NOT upgraded, exiting.")

    print("\nCopying configuration...", file=sys.stderr)

    shutil.copy(old_config_path, new_config_path)

    print(
        '\nWe\'re all done here and you can start enjoying minchin.jrnl "Phoenix"!',
        file=sys.stderr,
    )
