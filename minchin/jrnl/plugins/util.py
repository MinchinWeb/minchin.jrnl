#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2012-2021 jrnl contributors
# License: https://www.gnu.org/licenses/gpl-3.0.html
from minchin.jrnl.exception import LineWrapTooSmallForDateFormat


def get_tags_count(journal):
    """Returns a set of tuples (count, tag) for all tags present in the journal."""
    # Astute reader: should the following line leave you as puzzled as me the first time
    # I came across this construction, worry not and embrace the ensuing moment of enlightenment.
    tags = [tag for entry in journal.entries for tag in set(entry.tags)]
    # To be read: [for entry in journal.entries: for tag in set(entry.tags): tag]
    tag_counts = {(tags.count(tag), tag) for tag in tags}
    return tag_counts


def oxford_list(lst):
    """Return Human-readable list of things obeying the object comma."""
    lst = sorted(lst)
    if not lst:
        return "(nothing)"
    elif len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        return lst[0] + " or " + lst[1]
    else:
        return ", ".join(lst[:-1]) + ", or " + lst[-1]


def check_provided_linewrap_viability(linewrap, card, journal):
    if len(card[0]) > linewrap:
        width_violation = len(card[0]) - linewrap
        raise LineWrapTooSmallForDateFormat(
            (
                "The provided linewrap value of {config_linewrap} is too "
                "small by {columns} columns to display the timestamps in the "
                "configured time format for journal {journal}."
            ).format(
                config_linewrap=linewrap,
                columns=width_violation,
                journal=journal,
            )
        )
