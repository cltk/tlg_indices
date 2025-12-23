"""For loading TLG .json files and searching, then pulling author ids."""

import json
import os
from typing import Optional

import re
from re import Pattern


__author__ = [
    "Kyle P. Johnson <kyle@kyle-p-johnson.com>",
    "Stephen Margheim <stephen.margheim@gmail.com>",
    "Martín Pozzi <marpozzi@gmail.com>",
]

# THIS_DIR = os.path.dirname(os.path.abspath(__file__))


# def open_json(_file):
#     """Loads the json file as a dictionary and returns it."""
#     with open(_file) as f:
#         return json.load(f)


# def _get_epoch(_str) -> Optional[str]:
#     """Take incoming string, return its epoch."""
#     _return = None
#     if _str.startswith("A.D. "):
#         _return = "ad"
#     elif _str.startswith("a. A.D. "):
#         _return = None  # ?
#     elif _str.startswith("p. A.D. "):
#         _return = "ad"
#     elif re.match(r"^[0-9]+ B\.C\. *", _str):
#         _return = "bc"
#     elif re.match(r"^a\. *[0-9]+ B\.C\. *", _str):
#         _return = "bc"
#     elif re.match(r"^p\. *[0-9]+ B\.C\. *", _str):
#         _return = None  # ?
#     elif _str == "Incertum" or _str == "Varia":
#         _return = _str
#     return _return


# def _check_number(_str) -> bool:
#     """check if the string contains only a number followed by ?"""
#     if re.match(r"^[0-9]+\?*", _str):
#         return True
#     return False


# def _handle_splits(_str: str) -> dict[str, Optional[str]]:
#     """Check if incoming date has a '-' or '/', if so do stuff."""
#     _str = _str.replace("/", "-")
#     _tmp_dict: dict[str, Optional[str]] = dict()
#     if "-" in _str:
#         start, stop = _str.split("-")
#         if _check_number(start):
#             start = re.sub(r"[0-9]+\?*", start, stop)
#         elif _check_number(stop):
#             stop = re.sub(r"[0-9]+\?*", stop, start)
#     else:
#         start = _str
#         stop = _str
#     _tmp_dict["start_raw"] = start
#     _tmp_dict["stop_raw"] = stop
#     _tmp_dict["start_epoch"] = _get_epoch(start)
#     _tmp_dict["stop_epoch"] = _get_epoch(stop)
#     return _tmp_dict


# def normalize_dates():
#     """Experiment to make sense of TLG dates.
#     TODO: start here, parse everything with pass
#     """
#     map_date_to_authors: dict[str, list[str]] = get_date_author()
#     for tlg_date in map_date_to_authors:
#         date = {}
#         if tlg_date == "Varia":
#             # give a homer-to-byz date for 'varia'
#             pass
#         elif tlg_date == "Incertum":
#             # ?
#             pass
#         else:
#             tmp_date = _handle_splits(tlg_date)
#             date.update(tmp_date)
#         print(date)
