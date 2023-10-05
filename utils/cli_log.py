from utils.utils import Utils


class Logger:
    @staticmethod
    @Utils.validate_args
    def log_message(content: str, author: str) -> None:
        pass

    @staticmethod
    @Utils.validate_args
    def log_deleted_message(content: str, author: str) -> None:
        pass

    @staticmethod
    @Utils.validate_args
    def log_edited_message(before: str, after: str, author: str) -> None:
        pass
