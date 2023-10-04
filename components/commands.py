import discord

from .bot import client
from .data import Data
from datetime import datetime


class Commands:
    __guilds = Data.get_settings()["guilds"]

    @client.slash_command(guild_ids=__guilds)
    async def test(ctx):
        print(ctx)
        await ctx.respond("Why hello there!")

    @client.slash_command(guild_ids=__guilds)
    async def snipe(ctx):
        deleted_message = Data.get_deleted_message()
        if deleted_message["content"] is None:
            await ctx.respond("There are no deleted messages recorded!")
        else:
            embed = discord.Embed(
                title="Deleted Message",
                description=deleted_message["content"],
                color=discord.Colour.blurple(),
                timestamp=datetime.now()
            )
            embed.set_footer(
                text=f"Author: {deleted_message['author']}",
            )
            await ctx.respond(embed=embed)
