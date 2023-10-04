import json
from pathlib import Path


class Data:
    __cwd = Path.cwd()
    __settings = json.loads(
        Path(f"{Path.cwd()}/config/settings.json").read_text()
    )

    def get_settings() -> dict:
        return Data.__settings

    def get_cwd() -> str:
        return Data.__cwd
