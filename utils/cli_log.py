import discord
from utils.utils import Utils
from components.bot import Data
from datetime import datetime

client = Data.get_client()


class Logger:
    __deleted_messages_channel = client.get_channel(111)
    __edited_messages_channel = client.get_channel(111)
    __wall = "-" * 20  # For ASCII art

    @staticmethod
    def __walled_print(text: str) -> None:
        print(f"{Logger.__wall}\n{text}\n{Logger.__wall}")

    @staticmethod
    def __check_channel(channel: str) -> None:
        if Logger.__channel != channel:
            Logger.__channel = channel
            Logger.__walled_print(f"# {channel}")

    @staticmethod
    # @Utils.validate_args
    def log_message(content: str, author: str, channel: str) -> None:
        Logger.__check_channel(channel)
        print(f"[{author}]: {content}")

    @staticmethod
    # @Utils.validate_args
    def log_deleted_message(content: str, author: str, channel: str) -> None:
        embed = Utils.get_snipe_embed(
            title="Deleted Message",
            description=content,
            author=author
        )
        Logger.__check_channel(channel)
        Logger.__walled_print(f"Deleted Message by {author}\n{content}")
        Logger.__deleted_messages_channel.send(embed=embed)

    @staticmethod
    # @Utils.validate_args
    def log_edited_message(before: str, after: str, author: str, channel: str) -> None:
        content = f"Before Edit: {before}\n\nAfter Edit: {after}"
        embed = Utils.get_snipe_embed(
            title="Edited Message",
            description=content,
            author=author
        )
        Logger.__check_channel(channel)
        Logger.__walled_print(f"Edited Message by {author}\n{content}")
        Logger.__edited_messages_channel.send(embed=embed)
