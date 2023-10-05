import os
import discord

from dotenv import load_dotenv
from components.data import Data
from utils.cli_log import Logger

client = discord.Bot(intents=discord.Intents.all())


class Bot:
    @client.event
    async def on_ready():
        print(f"Logged in as {client.user}")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        Logger.log_message(message.content, message.author.name)

    @client.event
    async def on_message_delete(message):
        if message.author == client.user:
            return
        Logger.log_deleted_message(message.content, message.author.name)
        Data.set_deleted_message(message.content, message.author.name)

    @client.event
    async def on_message_edit(before, after):
        if before.author == client.user:
            return
        Logger.log_edited_message(
            before.content, after.content, after.author.name
        )
        Data.set_edited_message(
            before.content, after.content, after.author.name
        )

    @staticmethod
    def run() -> None:
        load_dotenv()
        client.run(os.getenv("TOKEN"))
