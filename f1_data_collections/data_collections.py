"""
This files contains the data collections used in the validation module.

Preferably, the data should be gotten from the ergast API. But, if the API is
not available, the data should be gotten from the database.

Data collections inside here sare based on the current year [2022].
"""

import json
from datetime import date
from pathlib import Path
from typing import List

from f1_data_collections.errors import ErgastApiException
from f1_data_collections import ergast_api
from f1_data_collections.class_utils import Driver, Round, Session

from f1_data_collections.config import settings

CURRENT_YEAR = date.today().year

_TEAM_TRANSLATE = {
    "MER": "mercedes",
    "FER": "ferrari",
    "RBR": "red bull",
    "MCL": "mclaren",
    "APN": "alpine",
    "AMR": "aston martin",
    "ARR": "alfa romeo",
    "APT": "alphatauri",
    "HAA": "haas",
    "WIL": "williams",
}
"""Mapping of team names to theirs respective abbreviations."""

_TEAM_COLORS = {
    "mercedes": "#00d2be",
    "ferrari": "#dc0000",
    "red bull": "#0565ff",
    "mclaren": "#ff8700",
    "alpine": "#0090ff",
    "aston martin": "#006f62",
    "alfa romeo": "#900000",
    "alphatauri": "#2b4562",
    "haas": "#ffffff",
    "williams": "#005aff",
}
"""Mapping of team colors (hex color code) to team names.
(current season only)"""

_DRIVER_TEAM = {
    "LEC": "FER",
    "LECLERC": "FER",
    "SAI": "FER",
    "SAINZ": "FER",
    "VER": "RBR",
    "VERSTAPPEN": "RBR",
    "PER": "RBR",
    "PEREZ": "RBR",
    "HAM": "MER",
    "HAMILTON": "MER",
    "RUS": "MER",
    "RUSSELL": "MER",
    "RIC": "MCL",
    "RICCIARDO": "MCL",
    "NOR": "MCL",
    "NORRIS": "MCL",
    "ALO": "APN",
    "ALONSO": "APN",
    "OCO": "APN",
    "OCON": "APN",
    "VET": "AMR",
    "VETTEL": "AMR",
    "STR": "AMR",
    "STROLL": "AMR",
    "BOT": "ARR",
    "BOTTAS": "ARR",
    "ZHO": "ARR",
    "ZHOU": "ARR",
    "TSU": "APT",
    "TSUNODA": "APT",
    "GAS": "APT",
    "GASLY": "APT",
    "MSC": "HAA",
    "MSCHUMACHER": "HAA",
    "MAG": "HAA",
    "MAGNUSSEN": "HAA",
    "ALB": "WIL",
    "ALBON": "WIL",
    "LAT": "WIL",
    "LATIFI": "WIL",
}
"""Mapping of team names to theirs respective drivers."""

_DRIVER_ABBR_DICT = {
    "LECLERC": "LEC",
    "SAINZ": "SAI",
    "VERSTAPPEN": "VER",
    "PEREZ": "PER",
    "HAMILTON": "HAM",
    "RUSSELL": "RUS",
    "RICCIARDO": "RIC",
    "NORRIS": "NOR",
    "ALONSO": "ALO",
    "OCON": "OCO",
    "VETTEL": "VET",
    "STROLL": "STR",
    "BOTTAS": "BOT",
    "ZHOU": "ZHP",
    "TSUNODA": "TSU",
    "GASLY": "GAS",
    "MSCHUMACHER": "MSC",
    "MAGNUSSEN": "MAG",
    "ALBON": "ALB",
    "LATIFI": "LAT",
}
"""Mapping of the drivers surname to theirs respective abbreviation."""

_DRIVERS_LIST = [
    "ALB",
    "ALO",
    "BOT",
    "HAM",
    "HUL",
    "LAT",
    "LEC",
    "MAG",
    "NOR",
    "OCO",
    "RIC",
    "RUS",
    "GAS",
    "SAI",
    "MSC",
    "STR",
    "TSU",
    "VER",
    "VET",
    "ZHO",
    "PER",
]
"""List of all drivers in the current season."""

_SESSIONS_ABBR_DICT = {
    "FREE PRACTICE 1": "FP1",
    "FREE PRACTICE 2": "FP2",
    "FREE PRACTICE 3": "FP3",
    "QUALIFYING": "Q",
    "RACE": "R",
}
"""Mapping of all sessions to abbreviate form """

_DRIVER_NUMB_DICT = {
    1: "VER",
    3: "RIC",
    4: "NOR",
    5: "VET",
    6: "LAT",
    10: "GAS",
    11: "PER",
    14: "ALO",
    16: "LEC",
    18: "STR",
    20: "MAG",
    22: "TSU",
    23: "ALB",
    24: "ZHO",
    27: "HUL",
    31: "OCO",
    44: "HAM",
    47: "MSC",
    55: "SAI",
    63: "RUS",
    77: "BOT",
}
"""Mapping of driver number to driver name."""
# Forse si può aggiornare facendo delle chiamate dirette all'ergastAPI


def get_drivers(year: int = CURRENT_YEAR) -> List[Driver]:
    """
    Get the drivers of the given year.

    This method tries to get the drivers of the given year from the ergastAPI.
    If the request fails, it returns the drivers of the current season.

    params:
        `year`: the year of the drivers to get.

    returns:
        `List[Driver]`: A list of Driver objects or an empty list if there's some flaws in the data collection.

    """

    try:
        drivers = ergast_api.get_drivers_by_year(year)
    except ErgastApiException as e:
        drivers = [
            Driver(driver_abbr, full_name, str(number))
            for full_name, driver_abbr_ in _DRIVER_ABBR_DICT.items()
            for number, driver_abbr in _DRIVER_NUMB_DICT.items()
            if driver_abbr == driver_abbr_
        ]

    return drivers


def get_sessions() -> List[Session]:
    """
    Get the sessions for the current year.
    """

    # sessions = [(k, v) for k, v in _SESSIONS_ABBR_DICT.items()]

    sessions = [Session(session_name, session_abbr) for session_name, session_abbr in _SESSIONS_ABBR_DICT.items()]

    return sessions


def get_rounds_by_year(year: int = CURRENT_YEAR) -> List[Round]:
    """
    Get the rounds of the given year.

    This method tries to get the rounds of the given year from the ergastAPI.
    If the request fails, it returns the rounds of the current season.

    params:
        `year`: the year of the rounds to get.

    returns:
        `List[Round]`: A list of Round or an empty list if there's some flaws in the data collection.

    """

    try:
        rounds = ergast_api.get_rounds_by_year(str(year))
    except ErgastApiException as e:
        # if the request fails, try to get the rounds from the json file
        with open(Path(Path(__file__).parent, settings.TRACKS_JSON), "r") as f:
            tracks_data: dict = json.load(f)
            rounds = [
                Round(tracks_data[tr]["calendar_pos"][str(year)], race)
                for tr in tracks_data.keys()
                for race in tracks_data[tr]["raceName"]
            ]

    return rounds


def get_driver_name_from_abbr(abbr: str, year: int = CURRENT_YEAR) -> str | None:
    """
    Given an abbreviation this method tries to get the full name of the driver.

    params:
        `abbr`: the abbreviation of the driver.
        `year`: the year of the drivers to get.

    returns:
        `str`: the full name of the driver or None if the abbreviation is not found.

    """

    drivers = get_drivers(year)
    for driver in drivers:
        if driver.abbr == abbr:
            return driver.name

    # driver hasn't been found
    return None


def get_driver(full_name: str, year: int = CURRENT_YEAR) -> Driver:
    """
    Given an abbreviation this method tries to get the full name of the driver.

    params:
        `driver_abbr`: the abbreviation of the driver.
        `year`: the year of the drivers to get.

    returns:
        `Driver`: the driver object.

    """

    drivers = get_drivers(year)
    for driver in drivers:
        if full_name.upper() == driver.name.upper() or full_name.upper() == driver.abbr.upper():
            return driver

    # driver hasn't been found
    return None
