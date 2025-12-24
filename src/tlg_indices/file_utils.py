"""Higher-level (i.e., user-friendly) functions for quickly reading
TLG data after it has been processed by ``TLGU()``.
"""

import os
from typing import Union

import re
from re import Pattern

from tlg_indices.data_types import AuthorID
from tlg_indices.tlg_index_utils import get_all_authors_ids

from tlg_indices.indices.author_id_to_name import TLG_INDEX, TLG_WORKS_INDEX
from tlg_indices.indices.phi5_author_id_to_name import MAP_PHI5_AUTHOR_ID_TO_NAME
from tlg_indices.indices.phi5_author_id_to_works import MAP_PHI5_AUTHOR_ID_TO_WORKS


def assemble_tlg_author_filepaths(corpus_dir: str) -> list[str]:
    """Reads TLG index and builds a list of absolute filepaths.
    This expects that files have been translated by `tlgu` and are at
    a path something like `"grc/text/tlg/plaintext/"`
    """
    corpus_dir = os.path.expanduser(corpus_dir)
    if not os.path.exists(corpus_dir):
        raise FileNotFoundError(f"Directory {corpus_dir} does not exist.")
    all_author_ids: list[AuthorID] = get_all_authors_ids()
    filepaths: list[str] = [
        os.path.join(corpus_dir, x + ".TXT") for x in all_author_ids
    ]
    return filepaths


def assemble_tlg_works_filepaths(corpus_dir: str) -> list[str]:
    """Reads TLG index and builds a list of absolute filepaths."""
    corpus_dir = os.path.expanduser(corpus_dir)
    if not os.path.exists(corpus_dir):
        raise FileNotFoundError(f"Directory {corpus_dir} does not exist.")
    all_filepaths: list[str] = list()
    for author_code in TLG_WORKS_INDEX:
        author_data: dict[str, Union[list[str], str]] = TLG_WORKS_INDEX[author_code]
        works: Union[list[str], str] = author_data["works"]
        for work in works:
            filepath: str = os.path.join(
                corpus_dir, author_code[3:] + "-" + work + ".txt"
            )
            all_filepaths.append(filepath)
    return all_filepaths


def assemble_phi5_author_filepaths(corpus_dir: str) -> list[str]:
    """Reads PHI5 index and builds a list of absolute filepaths.
    This expects that files have been translated by `tlgu` and are at
    a path something like `"lat/text/phi5/plaintext/"`
    """
    corpus_dir = os.path.expanduser(corpus_dir)
    if not os.path.exists(corpus_dir):
        raise FileNotFoundError(f"Directory {corpus_dir} does not exist.")
    all_author_ids: list[AuthorID] = sorted(MAP_PHI5_AUTHOR_ID_TO_NAME.keys())
    filepaths: list[str] = [
        os.path.join(corpus_dir, x + ".txt") for x in all_author_ids
    ]
    return filepaths


def assemble_phi5_works_filepaths(corpus_dir: str) -> list[str]:
    """Reads PHI5 index and builds a list of absolute filepaths."""
    corpus_dir = os.path.expanduser(corpus_dir)
    if not os.path.exists(corpus_dir):
        raise FileNotFoundError(f"Directory {corpus_dir} does not exist.")
    all_filepaths: list[str] = list()
    for author_id, works in MAP_PHI5_AUTHOR_ID_TO_WORKS.items():
        for work_id in works:
            filepath: str = os.path.join(corpus_dir, f"{author_id}-{work_id}.txt")
            all_filepaths.append(filepath)
    return all_filepaths
