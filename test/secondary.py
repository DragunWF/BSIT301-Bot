import os
import discord
from discord import Option
from dotenv import load_dotenv

bot_guilds = ["1158349118897397813"]
bot = discord.Bot()


class Main:
    @bot.event
    async def on_ready():
        print(f"Ready as {bot.user}")

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        print(message)
        if message.author.name == "dragunwf":
            await message.channel.send("Hello there, Master!")
        else:
            await message.channel.send("Greetings")

    @bot.slash_command(guild_ids=bot_guilds)
    async def hello(ctx, member: Option(discord.Member, "", required=True)):
        await ctx.respond(f"Hello {member}")


load_dotenv()
bot.run(os.getenv("TOKEN"))
