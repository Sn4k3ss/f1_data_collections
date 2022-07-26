from dataclasses import dataclass


@dataclass
class Round:
    round_number: int
    round_name: str

    def __init__(self, round_number, round_name):
        self.round_number = round_number
        self.round_name = round_name


@dataclass
class Session:
    abbr: str
    name: str

    def __init__(self, name, abbr):
        self.abbr: str = abbr
        self.name: str = name


@dataclass
class Driver:
    abbr: str
    name: str
    number: str

    def __init__(self, abbr, name, number):
        self.abbr: str = abbr
        self.name: str = name
        self.number: str = number
