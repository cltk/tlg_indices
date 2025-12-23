# About

This Python package facilitates the browsing of the indices of the old TLG CD-ROMs. It expects that texts have been processed by the `tlgu` package ([tlgu homepage](https://tlgu.carmen.gr/), [rehosted code](https://github.com/cltk/grc_software_tlgu)), which offers a variety of ways to convert the Beta Code of the original files into Unicode text files.

# Install

Install from PyPI with:

```bash
pip install tlg-indices
```

# Disclaimer

This repository makes no claim to ownership of the contents of the original TLG CD-ROM, which are owned by the University of California, Irvine. It is an independent effort to facilitate study of texts and does not represent or imply endorsement by the University of California, Irvine or the TLG project.

# Usage overview

The main entry point is the utility functions in `src/tlg_indices/utils.py`, which expose prebuilt indices and convenience lookups. The quickest way to see how to call these helpers is in `examples.py`, which demonstrates:

- Reading index data (epithets, geographies, dates, and author/work mappings).
- Looking up authors by epithet or geography, and reversing those lookups.
- Looking up works by author and retrieving a single work title.
- Sorting and querying date ranges using `ParsedDate` and `get_dates_in_range()`.

For a runnable walkthrough, open `examples.py` and follow the patterns there.

# Packaging

```bash
% uv build --no-sources
% uv publish --token "pypi-xxxxxxxxxxxxxxxx"
```
