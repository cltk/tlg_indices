from tlg_indices.file_utils import (
    assemble_phi5_author_filepaths,
    assemble_phi5_works_filepaths,
    assemble_tlg_author_filepaths,
    assemble_tlg_works_filepaths,
)


def main() -> None:
    # TLG
    tlg_author_filepaths = assemble_tlg_author_filepaths(
        corpus_dir="~/Downloads/tlg-authors/"
    )
    print("TLG filepaths:", tlg_author_filepaths)

    tlg_works_filepaths = assemble_tlg_works_filepaths(
        corpus_dir="~/Downloads/tlg-works/"
    )
    print("TLG works filepaths:", tlg_works_filepaths)

    # PHI5
    tlg_author_filepaths = assemble_phi5_author_filepaths(
        corpus_dir="~/Downloads/phi5-authors/"
    )
    print("PHI5 filepaths:", tlg_author_filepaths)

    tlg_works_filepaths = assemble_phi5_works_filepaths(
        corpus_dir="~/Downloads/phi5-works/"
    )
    print("PHI5 works filepaths:", tlg_works_filepaths)



if __name__ == "__main__":
    main()
