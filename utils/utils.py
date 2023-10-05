import discord
from datetime import datetime


class Utils:
    def validate_args(*args, **kwargs) -> bool:
        if all(args) and all(kwargs):
            return True
        ERROR_MESSAGE = "Function call contains one or more invalid arguments!"
        try:
            raise Exception(ERROR_MESSAGE)
        except Exception:
            print(ERROR_MESSAGE)
        return False

    @staticmethod
    @validate_args
    def get_snipe_embed(title: str, description: str, author: str) -> discord.Embed:
        embed = discord.Embed(
            title=title,
            description=description,
            color=discord.Colour.blurple(),
            timestamp=datetime.now()
        )
        embed.set_footer(f"Author: {author}")
        return embed

    @staticmethod
    def get_random_embed_color() -> None:
        # TODO: Implement random embed color
        pass
