from utils.utils import Utils


class Logger:
    __channel = None
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
    @Utils.validate_args
    def log_message(content: str, author: str, channel: str) -> None:
        Logger.__check_channel(channel)
        print(f"[{author}]: {content}")

    @staticmethod
    @Utils.validate_args
    def log_deleted_message(content: str, author: str, channel: str) -> None:
        Logger.__check_channel(channel)
        Logger.__walled_print(f"Deleted Message by {author}\n{content}")

    @staticmethod
    @Utils.validate_args
    def log_edited_message(before: str, after: str, author: str, channel: str) -> None:
        Logger.__check_channel(channel)
        Logger.__walled_print(
            f"Edited Message by {author}\nBefore Edit: {before}\n\nAfter Edit: {after}"
        )
