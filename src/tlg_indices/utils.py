"""Read and return data from the author index files."""

from typing import Optional, Union
from tlg_indices.author_id_to_author_name import AUTHOR_ID_TO_AUTHOR_NAME
from tlg_indices.author_ids_to_works import AUTHOR_ID_TO_WORKS
from tlg_indices.data_types import AuthorID, WorkID
from tlg_indices.date_to_author_id import MAP_DATE_TO_AUTHORS
from tlg_indices.epithet_to_author_id import MAP_EPITHET_TO_AUTHOR_IDS
from tlg_indices.female_author_ids import FEMINAE
from tlg_indices.geography_to_author_id import GEO_TO_AUTHOR_ID
from tlg_indices.tlg_indices import ALL_TLG_INDICES
# from tlg_indices.author_ids_to_work_ids_and_work_names import WORK_NUMBERS

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
_AUTHOR_NAME_INDEX_CASEFOLD: dict[str, AuthorID] = {
    name.casefold(): author_id for author_id, name in AUTHOR_ID_TO_AUTHOR_NAME.items()
}


def get_indices() -> dict[str, dict[str, str]]:
    """Return all of the TLG's indices."""
    return ALL_TLG_INDICES


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


def author_id_to_author_name() -> dict[AuthorID, str]:
    """Returns entirety of id-author TLG index."""
    return AUTHOR_ID_TO_AUTHOR_NAME


def get_author_name_from_author_id(author_id: Union[AuthorID, str]) -> Optional[str]:
    """Pass author id and return a string with the author label"""
    return AUTHOR_ID_TO_AUTHOR_NAME.get(AuthorID(author_id), None)


def get_author_id_from_author_name(name: str) -> Optional[AuthorID]:
    """Pass author name and return a string with the author id"""
    return _AUTHOR_NAME_INDEX_CASEFOLD.get(name.casefold())


def get_author_works_index() -> dict[AuthorID, dict[WorkID, str]]:
    """Returns entirety of id-author TLG index."""
    return AUTHOR_ID_TO_WORKS


def get_works_by_author_id(author_id: Union[AuthorID, str]) -> dict[WorkID, str]:
    """Pass author id and return a dictionary of its works."""
    return AUTHOR_ID_TO_WORKS[AuthorID(author_id)]


def get_work_name(
    author_id: Union[AuthorID, str], work_id: Union[WorkID, str]
) -> Optional[str]:
    """Pass author id and work id and return the work name."""
    works = AUTHOR_ID_TO_WORKS.get(AuthorID(author_id))
    if works is None:
        return None
    return works.get(WorkID(work_id))


def get_date_author() -> dict[str, list[AuthorID]]:
    """Returns entirety of date-author index."""
    return MAP_DATE_TO_AUTHORS


def get_dates():
    """Return a list of all the date epithet labels."""
    map_date_to_authors: dict[str, list[str]] = get_date_author()
    return sorted(map_date_to_authors.keys())


def get_date_of_author(_id):
    """Pass author id and return the name of its associated date."""
    map_date_to_authors: dict[str, list[str]] = get_date_author()
    for date, ids in map_date_to_authors.items():
        if _id in ids:
            return date
    return None
