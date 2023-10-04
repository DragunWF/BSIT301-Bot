import os
import discord
import json

from dotenv import load_dotenv
from pathlib import Path
from components.data import Data

client = discord.Bot(intents=discord.Intents.default())


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
        print("delete message event")
        print(message)
        if message.author == client.user:
            return
        print("down here")
        Data.set_previous_deleted_message(message.content)
        print(Data.get_previous_deleted_message())

    @client.event
    async def on_message_edit(before, after):
        if before.author == client.user:
            return

    @staticmethod
    def run() -> None:
        load_dotenv()
        client.run(os.getenv("TOKEN"))
