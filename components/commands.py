from .bot import client
from .data import Data


class Commands:
    __guilds = Data.get_settings()["guilds"]

    @client.slash_command(guild_ids=__guilds)
    async def test(ctx):
        print(ctx)
        await ctx.respond("Why hello there!")

    @client.slash_command(guild_ids=__guilds)
    async def snipe(ctx):
        # barebones functionality
        # TODO: add more like embed messages and show message author
        deleted_message = Data.get_previous_deleted_message()
        if deleted_message is None:
            await ctx.respond("There are no deleted messages recorded!")
        else:
            await ctx.respond(f"Deleted Message: {deleted_message}")
