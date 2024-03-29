"""
Functions in this file are standalone commands. All standalone commands are split into
two categories depending on whether they require the config to be loaded to be able to
run.

1. "preconfig" commands don't require the config at all, and can be run before the
   config has been loaded.
2. "postconfig" commands require to config to have already been loaded, parsed, and
   scoped before they can be run.

Also, please note that all (non-builtin) imports should be scoped to each function to
avoid any possible overhead for these standalone commands.
"""


import sys


def preconfig_diagnostic(_):
    from itertools import chain
    import platform

    from minchin.jrnl import __version__
    from minchin.jrnl.constants import __title__, __version_codename__
    from minchin.jrnl.plugins.meta import (
        EXPORT_FORMATS,
        IMPORT_FORMATS,
        get_exporter,
        get_importer,
    )

    print(f"{__title__}: {__version__}", end="")
    if __version_codename__:
        print(f' "{__version_codename__}"')
    print(f"Python: {sys.version}\n" f"OS: {platform.system()} {platform.release()}")

    plugin_name_length = max(
        [len(str(x)) for x in chain(IMPORT_FORMATS, EXPORT_FORMATS)]
    )

    print()
    print("Active Plugins:")
    print("    Importers:")
    for importer in IMPORT_FORMATS:
        importer_class = get_importer(importer)
        print(f"        {importer:{plugin_name_length}} : ", end="")
        print(f"{importer_class.version} from ", end="")
        print(f"{importer_class().class_path()}")
    print("    Exporters:")
    for exporter in EXPORT_FORMATS:
        exporter_class = get_exporter(exporter)
        print(f"        {exporter:{plugin_name_length}} : ", end="")
        print(f"{exporter_class.version} from ", end="")
        print(f"{exporter_class().class_path()}")


def preconfig_version(_):
    # TODO: include license text as jrnl command

    from minchin.jrnl import __version__
    from minchin.jrnl.constants import __copyright__, __title__, __version_codename__

    version_str = f"{__title__}, version {__version__}"
    if __version_codename__:
        version_str = version_str + f' "{__version_codename__}"'
    version_str = (
        version_str
        + f"""

{__copyright__}

This is free software, and you are welcome to redistribute it under certain
conditions; for details, see: https://www.gnu.org/licenses/gpl-3.0.html"""
    )

    print(version_str)


def postconfig_list(config, **kwargs):
    from .output import list_journals

    print(list_journals(config))


def postconfig_import(args, config, **kwargs):
    from .Journal import open_journal
    from .plugins import get_importer

    # Requires opening the journal
    journal = open_journal(args.journal_name, config)

    format = args.export if args.export else "jrnl"
    get_importer(format).import_(journal, args.filename)


def postconfig_encrypt(args, config, original_config, **kwargs):
    """
    Encrypt a journal in place, or optionally to a new file
    """
    from .EncryptedJournal import EncryptedJournal
    from .Journal import open_journal
    from .config import update_config
    from .install import save_config

    # Open the journal
    journal = open_journal(args.journal_name, config)

    journal.config["encrypt"] = True

    new_journal = EncryptedJournal.from_journal(journal)
    new_journal.write(args.filename)

    print(
        f"Journal encrypted to {args.filename or new_journal.config['journal']}.",
        file=sys.stderr,
    )

    # Update the config, if we encrypted in place
    if not args.filename:
        update_config(
            original_config, {"encrypt": True}, args.journal_name, force_local=True
        )
        save_config(original_config)


def postconfig_decrypt(args, config, original_config, **kwargs):
    """Decrypts into new file. If filename is not set, we encrypt the journal file itself."""
    from .Journal import PlainJournal, open_journal
    from .config import update_config
    from .install import save_config

    journal = open_journal(args.journal_name, config)
    journal.config["encrypt"] = False

    new_journal = PlainJournal.from_journal(journal)
    new_journal.write(args.filename)
    print(
        f"Journal decrypted to {args.filename or new_journal.config['journal']}.",
        file=sys.stderr,
    )

    # Update the config, if we decrypted in place
    if not args.filename:
        update_config(
            original_config, {"encrypt": False}, args.journal_name, force_local=True
        )
        save_config(original_config)
