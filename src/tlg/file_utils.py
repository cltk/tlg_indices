"""Higher-level (i.e., user-friendly) functions for quickly reading
TLG data after it has been processed by ``TLGU()``.
"""

import os
from typing import Union

import re
from re import Pattern

from .tlg_index import TLG_INDEX, TLG_WORKS_INDEX


def tlg_plaintext_cleanup(
    text: str, rm_punctuation: bool = False, rm_periods: bool = False
) -> str:
    """Remove and substitute post-processing for Greek TLG text.
    TODO: Surely more junk to pull out. Please submit bugs!
    """
    # Note: flag was removed, is necessary?
    remove_comp: Pattern[str] = re.compile(
        r"-\n|[«»<>〈〉\(\)‘’_—:!\?\'\"\*]|{[[:print:][:space:]]+?}|\[[[:print:][:space:]]+?\]|[a-zA-Z0-9]",
    )
    text = remove_comp.sub("", text)

    if rm_punctuation:
        punct_comp: Pattern[str] = re.compile(r",|·")
        text = punct_comp.sub("", text)

    if rm_periods:
        period_comp: Pattern[str] = re.compile(r"\.|;")
        text = period_comp.sub("", text)

    # replace line breaks w/ space
    replace_comp: Pattern[str] = re.compile(r"\n")
    text = replace_comp.sub(" ", text)

    comp_space: Pattern[str] = re.compile(r"\s+")
    text = comp_space.sub(" ", text)

    return text


# TODO: Update
# def assemble_tlg_author_filepaths() -> list[str]:
#     """Reads TLG index and builds a list of absolute filepaths."""
#     plaintext_dir: str = make_cltk_path("grc/text/tlg/plaintext/")
#     filepaths: list[str] = [os.path.join(plaintext_dir, x + ".TXT") for x in TLG_INDEX]
#     return filepaths

# TODO: Update
# def assemble_tlg_works_filepaths() -> list[str]:
#     """Reads TLG index and builds a list of absolute filepaths."""
#     plaintext_dir: str = make_cltk_path("grc/text/tlg/individual_works/")
#     all_filepaths: list[str] = list()
#     for author_code in TLG_WORKS_INDEX:
#         author_data: dict[str, Union[list[str], str]] = TLG_WORKS_INDEX[author_code]
#         works: Union[list[str], str] = author_data["works"]
#         for work in works:
#             filepath: str = os.path.join(
#                 plaintext_dir, author_code + ".TXT" + "-" + work + ".txt"
#             )
#             all_filepaths.append(filepath)
#     return all_filepaths
