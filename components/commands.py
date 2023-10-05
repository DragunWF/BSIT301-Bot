import discord

from .bot import client
from .data import Data
from utils.utils import Utils
from datetime import datetime


class Commands:
    __guilds = Data.get_settings()["guilds"]

    @client.slash_command(guild_ids=__guilds,
                          description="For testing purposes")
    async def test(ctx):
        print(ctx)
        await ctx.respond("This is a test message")

    @client.slash_command(guild_ids=__guilds,
                          description="Snipes recently deleted messages")
    async def snipe(ctx):
        deleted_message = Data.get_deleted_message()
        if deleted_message["author"] is None:
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

    @client.slash_command(guild_ids=__guilds,
                          description="Snipes recently edited messages")
    @Utils.validate_args
    async def esnipe(ctx):
        edited_message = Data.get_edited_message()
        if edited_message["author"] is None:
            await ctx.respond("There are no edited messages recorded!")
        else:
            after = edited_message["content"]["after"]
            before = edited_message["content"]["before"]
            embed = discord.Embed(
                title="Edited Message",
                description=f"Before:\n{before}\nAfter:\n{after}",
                color=discord.Colour.blurple(),
                timestamp=datetime.now()
            )
            embed.set_footer(
                text=f"Author: {edited_message['author']}"
            )
            await ctx.respond(embed=embed)
