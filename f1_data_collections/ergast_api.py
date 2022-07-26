import logging
from typing import List

import requests
from requests.exceptions import RequestException

from f1_data_collections.errors import ErgastApiException
from f1_data_collections.class_utils import Driver, Round

logger = logging.getLogger(__name__)

TIMEOUT_API_CALL = 5  # seconds


def get_rounds_by_year(year) -> List[Round]:
    """
    Get event names by year

    params:
        year: `int`

    returns:
        `List[Round]`


    """
    url = f"http://ergast.com/api/f1/{year}.json"

    try:
        response = requests.get(url, timeout=TIMEOUT_API_CALL)
        data = response.json()
    except RequestException as e:
        logger.error(f"Could not get data from ErgastAPI: {e}")
        raise ErgastApiException(e)

    races = data["MRData"]["RaceTable"]["Races"]
    rounds = [Round(race["round"], race["raceName"]) for race in races]
    return rounds


def get_drivers_by_year(year) -> List[Driver]:
    """
    Get drivers by year

    params:
        year: `int`

    returns:
        `List[(str, str, str)]` - list of drivers with abbreviation, Surname and number

    """

    url = f"http://ergast.com/api/f1/{year}/drivers.json"

    try:
        response = requests.get(url, timeout=TIMEOUT_API_CALL)
        data = response.json()
    except RequestException as e:
        logger.error(f"Could not get data from ErgastAPI: {e}")
        raise ErgastApiException(e)

    drivers_json = data["MRData"]["DriverTable"]["Drivers"]
    drivers = [
        Driver(driver["code"], driver["familyName"], driver["permanentNumber"])
        for driver in drivers_json
    ]

    return drivers


def get_drivers_by_team_and_year(year, team) -> List[Driver]:
    """
    Get drivers by team and year

    params:
        year: int
        team: str

    returns:
        `List[(str, str, str)]` - list of drivers with abbreviation, Surname and number

    """

    url = f"http://ergast.com/api/f1/{year}/constructors/{team}/drivers.json"

    try:
        response = requests.get(url)
        data = response.json()
    except RequestException as e:
        logger.error(f"Could not get data from ErgastAPI: {e}")
        raise ErgastApiException(e)

    drivers_json = data["MRData"]["DriverTable"]["Drivers"]
    drivers = [
        Driver(driver["code"], driver["familyName"], driver["permanentNumber"])
        for driver in drivers_json
    ]
    return drivers
