import discord
from datetime import datetime


class Utils:
    def validate_args(*args, **kwargs) -> bool:
        return all(args) and all(kwargs)

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
