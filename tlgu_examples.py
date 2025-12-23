"""Examples how to convert files using `tlgu`."""

from tlg_indices.tlgu import tlgu_convert_corpus, tlgu_convert_file


def main() -> None:
    # Convert a single TLG file into author file
    tlgu_convert_file(
        orig_txt_path="/Users/kylepjohnson/tlg/TLG_E/TLG0007.TXT",
        target_txt_path="/Users/kylepjohnson/Downloads/0007.txt",
        corpus="tlg",
        grouping="author",
        overwrite=True,
    )

    # Convert a single TLG file into works files
    tlgu_convert_file(
        orig_txt_path="/Users/kylepjohnson/tlg/TLG_E/TLG0007.TXT",
        target_txt_path="/Users/kylepjohnson/Downloads/0007",
        corpus="tlg",
        grouping="work",
        overwrite=True,
    )

    # Convert entire TLG corpus into author files
    tlgu_convert_corpus(
        orig_txt_dir="/Users/kylepjohnson/tlg/TLG_E",
        target_txt_dir="/Users/kylepjohnson/Downloads/tlg-authors",
        corpus="tlg",
        grouping="author",
        overwrite=True,
    )

    # Convert entire TLG corpus into work files
    tlgu_convert_corpus(
        orig_txt_dir="/Users/kylepjohnson/tlg/TLG_E",
        target_txt_dir="/Users/kylepjohnson/Downloads/tlg-works",
        corpus="tlg",
        grouping="work",
        overwrite=True,
    )

    # Convert a single PHI5 file into author file
    tlgu_convert_file(
        orig_txt_path="/Users/kylepjohnson/tlg/PHI5/LAT1254.TXT",
        target_txt_path="/Users/kylepjohnson/Downloads/1254.txt",
        corpus="phi5",
        grouping="author",
        overwrite=True,
    )

    # Convert a single PHI5 file into works files
    tlgu_convert_file(
        orig_txt_path="/Users/kylepjohnson/tlg/PHI5/LAT1254.TXT",
        target_txt_path="/Users/kylepjohnson/Downloads/1254",
        corpus="phi5",
        grouping="work",
        overwrite=True,
    )

    # Convert entire PHI5 corpus into author files
    tlgu_convert_corpus(
        orig_txt_dir="/Users/kylepjohnson/tlg/PHI5",
        target_txt_dir="/Users/kylepjohnson/Downloads/phi5-authors",
        corpus="phi5",
        grouping="author",
        overwrite=True,
    )

    # Convert entire PHI5 corpus into work files
    tlgu_convert_corpus(
        orig_txt_dir="/Users/kylepjohnson/tlg/PHI5",
        target_txt_dir="/Users/kylepjohnson/Downloads/phi5-works",
        corpus="phi5",
        grouping="work",
        overwrite=True,
    )


if __name__ == "__main__":
    main()
