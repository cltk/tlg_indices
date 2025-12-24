from tlg_indices.tlgu import tlgu_convert_corpus
from tlg_indices.file_utils import assemble_tlg_works_filepaths

# Convert entire TLG corpus into author files
conveted_tlg_dir: str = "~/Downloads/tlg-works"
tlgu_convert_corpus(
    orig_txt_dir="~/tlg/TLG_E",
    target_txt_dir=conveted_tlg_dir,
    corpus="tlg",
    grouping="work",
    overwrite=False,
)

# Get filepaths of converted TLG works
tlg_works_filepaths: list[str] = assemble_tlg_works_filepaths(
    corpus_dir=conveted_tlg_dir
)
# print("TLG works filepaths:", tlg_works_filepaths)

# Open files
for filepath in tlg_works_filepaths:
    print(f"Processing: {filepath}")
    with open(filepath, "r") as file:
        content = file.read()
        print(f"Content of {filepath}: {content[:100]}")  # Print first 100 characters
