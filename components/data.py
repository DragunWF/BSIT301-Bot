import discord
import json
from pathlib import Path
from utils.utils import Utils


class Data:
    __client = discord.Bot(intents=discord.Intents.all())
    __cwd = Path.cwd()
    __settings = json.loads(
        Path(f"{Path.cwd()}/config/settings.json").read_text()
    )
    __deleted_message = {"content": None, "author": None}
    __edited_message = {
        "content": {"after": None, "before": None},
        "author": None
    }

    @staticmethod
    def get_client() -> discord.Bot:
        return Data.__client

    @staticmethod
    def get_settings() -> dict:
        return Data.__settings

    @staticmethod
    def get_cwd() -> str:
        return Data.__cwd

    @staticmethod
    def get_guild_id() -> int:
        return Data.__settings["guild"]

    @staticmethod
    def get_channels() -> dict:
        return Data.__settings["channels"]

    @staticmethod
    def get_deleted_message() -> dict:
        return Data.__deleted_message

    @staticmethod
    # @Utils.validate_args
    def set_deleted_message(content: str, author: str) -> None:
        Data.__deleted_message["content"] = content
        Data.__deleted_message["author"] = author

    @staticmethod
    def get_edited_message() -> dict:
        return Data.__edited_message

    @staticmethod
    # @Utils.validate_args
    def set_edited_message(before: str, after: str, author: str) -> None:
        Data.__edited_message["content"]["before"] = before
        Data.__edited_message["content"]["after"] = after
        Data.__edited_message["author"] = author
