from .bot import client
from .data import Data


class Commands:
    __guilds = Data.get_settings()["guilds"]

    @client.slash_command(guild_ids=__guilds)
    async def test(ctx):
        print(ctx)
        await ctx.respond("Why hello there!")
