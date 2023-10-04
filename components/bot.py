import os
import discord

from dotenv import load_dotenv
from components.data import Data

client = discord.Bot(intents=discord.Intents.all())


class Bot:
    @client.event
    async def on_ready():
        print(f"Logged in as {client.user}")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.author.name == "dragunwf":
            pass
            # await message.channel.send("Hello!")
        print(type(message.content))
        print(message.content)

    @client.event
    async def on_message_delete(message):
        if message.author == client.user:
            return
        Data.set_deleted_message(message.content, message.author.name)

    @client.event
    async def on_message_edit(before, after):
        if before.author == client.user:
            return

    @staticmethod
    def run() -> None:
        load_dotenv()
        client.run(os.getenv("TOKEN"))
