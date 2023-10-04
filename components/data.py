import json
from pathlib import Path


class Data:
    __cwd = Path.cwd()
    __settings = json.loads(
        Path(f"{Path.cwd()}/config/settings.json").read_text()
    )
    __deleted_message = {"content": None, "author": None}

    def get_settings() -> dict:
        return Data.__settings

    def get_cwd() -> str:
        return Data.__cwd

    def get_deleted_message() -> dict:
        return Data.__deleted_message

    def set_deleted_message(content: str, author: str) -> None:
        Data.__deleted_message["content"] = content
        Data.__deleted_message["author"] = author
