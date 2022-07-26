from pathlib import Path

from pydantic import BaseSettings


class F1DataCollection(BaseSettings):
    """
    This class is used to store the settings for the application.
    """

    current_dir = Path(__file__).parent
    TRACKS_JSON = Path(current_dir, "json/f1_tracks.json")


settings = F1DataCollection()