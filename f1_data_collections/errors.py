"""
    Base error class for the application.
"""


class MyException(Exception):
    """Base exception class for this project

    Ideally speaking, this could be caught to handle any exceptions raised from this project.
    """


class ErgastApiException(MyException):
    """An exception that is raised when the ergast api returns an error"""

    def __init__(self, message: str):
        if message:
            self.message = message
        else:
            self.message = "Ergast API returned an error"
        super().__init__(self.message)