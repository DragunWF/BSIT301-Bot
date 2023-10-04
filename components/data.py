import json
from pathlib import Path


class Data:
    __cwd = Path.cwd()
    __settings = json.loads(
        Path(f"{Path.cwd()}/config/settings.json").read_text()
    )
    __previous_deleted_message = None

    def get_settings() -> dict:
        return Data.__settings

    def get_cwd() -> str:
        return Data.__cwd

    def get_previous_deleted_message() -> object:
        return Data.__previous_deleted_message
