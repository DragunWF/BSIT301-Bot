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
            await ctx.respond(embed=Utils.get_snipe_embed(
                title="Deleted Message",
                description=deleted_message["content"],
                author=deleted_message["author"]
            ))

    @client.slash_command(guild_ids=__guilds,
                          description="Snipes recently edited messages")
    async def esnipe(ctx):
        edited_message = Data.get_edited_message()
        if edited_message["author"] is None:
            await ctx.respond("There are no edited messages recorded!")
        else:
            after = edited_message["content"]["after"]
            before = edited_message["content"]["before"]
            await ctx.respond(embed=Utils.get_snipe_embed(
                title="Edited Message",
                description=f"Before:\n{before}\nAfter:\n{after}",
                author=edited_message["author"]
            ))
