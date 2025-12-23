"""Read and return data from the author index files."""

from tlg_indices.data_types import AuthorID
from tlg_indices.epithet_to_author_id import MAP_EPITHET_TO_AUTHOR_IDS
from tlg_indices.female_author_ids import FEMINAE

# Allows an O(1) lookup
_EPITHET_INDEX_CASEFOLD: dict[str, list[AuthorID]] = {
    key.casefold(): value for key, value in MAP_EPITHET_TO_AUTHOR_IDS.items()
}


def get_female_authors() -> list[str]:
    """Open female authors index and return sorted list of author ids."""
    return sorted(FEMINAE)


def get_epithet_index() -> dict[str, list[AuthorID]]:
    """Return dict of epithets (key) to a set of all
    author ids of that epithet (value).
    """
    return MAP_EPITHET_TO_AUTHOR_IDS


def get_epithets() -> list[str]:
    """Return a list of all the epithet labels."""
    return sorted(MAP_EPITHET_TO_AUTHOR_IDS.keys())


def select_authors_by_epithet(epithet: str) -> list[AuthorID]:
    """Pass exact name (case-insensitive) of
    epithet name, return ordered list of author ids.
    """
    ids = _EPITHET_INDEX_CASEFOLD.get(epithet.casefold())
    if ids is None:
        return list()
    return sorted(ids)


# def get_epithet_of_author(_id: str) -> str:
#     """Pass author id and return the name of its associated epithet."""
#     for epithet, ids in MAP_EPITHET_TO_AUTHOR_IDS.items():
#         if _id in ids:
#             return epithet
