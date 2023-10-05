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
        print(message.content)

    @client.event
    async def on_message_delete(message):
        if message.author == client.user:
            return
        Data.set_deleted_message(message.content, message.author.name)
        print("A deleted message has been stored!")

    @client.event
    async def on_message_edit(before, after):
        if before.author == client.user:
            return
        Data.set_edited_message(
            before.content, after.content, after.author.name
        )
        print("An edited message has been stored!")

    @staticmethod
    def run() -> None:
        load_dotenv()
        client.run(os.getenv("TOKEN"))
