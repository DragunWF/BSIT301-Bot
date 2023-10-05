from utils.utils import Utils


class Logger:
    __channel = None
    __wall = "-" * 20  # For ASCII art

    @staticmethod
    def __check_channel(channel: str) -> None:
        if Logger.__channel != channel:
            Logger.__channel = channel
            print(f"# {channel}")

    @staticmethod
    @Utils.validate_args
    def log_message(content: str, author: str, channel: str) -> None:
        Logger.__check_channel(channel)
        print(f"[{author}]: {content}")

    @staticmethod
    @Utils.validate_args
    def log_deleted_message(content: str, author: str, channel: str) -> None:
        Logger.__check_channel(channel)
        print(Logger.__wall)
        print(f"Deleted Message by {author}\n{content}")
        print(Logger.__wall)

    @staticmethod
    @Utils.validate_args
    def log_edited_message(before: str, after: str, author: str, channel: str) -> None:
        Logger.__check_channel(channel)
        print(Logger.__wall)
        print(f"Edited Message by {author}")
        print(f"Before Edit: {before}\n\nAfter Edit: {after}")
        print(Logger.__wall)
