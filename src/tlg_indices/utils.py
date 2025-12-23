"""Read and return data from the author index files."""

from typing import Optional, Union
from tlg_indices.data_types import AuthorID
from tlg_indices.epithet_to_author_id import MAP_EPITHET_TO_AUTHOR_IDS
from tlg_indices.female_author_ids import FEMINAE
from tlg_indices.geography_to_author_id import GEO_TO_AUTHOR_ID

# Allows an O(1) lookup
_EPITHET_INDEX_CASEFOLD: dict[str, list[AuthorID]] = {
    key.casefold(): value for key, value in MAP_EPITHET_TO_AUTHOR_IDS.items()
}
# Reverse index
_AUTHOR_ID_TO_EPITHET: dict[AuthorID, str] = {
    author_id: epithet
    for epithet, author_ids in MAP_EPITHET_TO_AUTHOR_IDS.items()
    for author_id in author_ids
}
_GEO_INDEX_CASEFOLD: dict[str, list[AuthorID]] = {
    key.casefold(): value for key, value in GEO_TO_AUTHOR_ID.items()
}
_AUTHOR_ID_TO_GEO: dict[AuthorID, str] = {
    author_id: geo
    for geo, author_ids in GEO_TO_AUTHOR_ID.items()
    for author_id in author_ids
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


def get_authors_by_epithet(epithet: str) -> list[AuthorID]:
    """Pass exact name (case-insensitive) of
    epithet name, return ordered list of author ids.
    """
    ids = _EPITHET_INDEX_CASEFOLD.get(epithet.casefold())
    if ids is None:
        return list()
    return sorted(ids)


def get_epithet_of_author(author_id: Union[AuthorID, str]) -> Optional[str]:
    """Pass author id and return the name of its associated epithet."""
    return _AUTHOR_ID_TO_EPITHET.get(AuthorID(author_id))


def get_geo_index() -> dict[str, list[AuthorID]]:
    """Get entire index of geographic name (key) and
    author ids (value).
    """
    return GEO_TO_AUTHOR_ID


def get_geographies() -> list[str]:
    """Return a list of all the geography labels."""
    return sorted(GEO_TO_AUTHOR_ID.keys())


def get_authors_by_geo(geo: str) -> list[AuthorID]:
    """Pass exact name (case-insensitive) of
    geography name, return ordered list of author ids.
    """
    ids = _GEO_INDEX_CASEFOLD.get(geo.casefold())
    if ids is None:
        return list()
    return sorted(ids)


def get_geo_of_author(author_id: Union[AuthorID, str]) -> Optional[str]:
    """Pass author id and return the name of its associated geography."""
    return _AUTHOR_ID_TO_GEO.get(AuthorID(author_id))
