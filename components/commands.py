from .bot import client
from .data import Data


class Commands:
    @client.slash_command(guild_ids=Data.settings.guilds)
    async def test(ctx):
        print(ctx)
        await ctx.respond("Why hello there!")
