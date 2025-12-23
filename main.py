"""Example Python script for tlg_indices."""

from tlg_indices.data_types import AuthorID
from tlg_indices.utils import (
    get_epithet_of_author,
    get_female_authors,
    get_epithet_index,
    get_epithets,
    select_authors_by_epithet,
)


def main():
    female_authors: list[str] = get_female_authors()
    print("Female authors:", female_authors)

    epithets: list[str] = get_epithets()
    print("Epithets:", epithets)

    epithet_index: dict[str, list[AuthorID]] = get_epithet_index()
    print("Epithet index:", epithet_index)

    epithet: str = "Poetae Medici"
    authors: list[AuthorID] = select_authors_by_epithet(epithet=epithet)
    print(f"Authors with epithet '{epithet}':", authors)

    author_id: str = "9020"
    epithet_of_author = get_epithet_of_author(author_id=author_id)
    print(f"Epithet of author '{author_id}':", epithet_of_author)


if __name__ == "__main__":
    main()
