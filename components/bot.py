import os
import discord

from dotenv import load_dotenv
from discord import Message
from components.data import Data
from utils.cli_log import Logger

client = Data.get_client()


class Bot:
    @client.event
    async def on_ready():
        print(f"Logged in as {client.user}")

    @client.event
    async def on_message(message: Message):
        if message.author == client.user or message.author.bot:
            return
        Logger.log_message(
            message.content, message.author.name, message.channel.name
        )

    @client.event
    async def on_message_delete(message: Message):
        if message.author == client.user or message.author.bot:
            return
        await Logger.log_deleted_message(
            message.content, message.author.name, message.channel.name
        )
        Data.set_deleted_message(message.content, message.author.name)

    @client.event
    async def on_message_edit(before: Message, after: Message):
        if before.author == client.user or before.author.bot:
            return
        await Logger.log_edited_message(
            before.content, after.content,
            after.author.name, after.channel.name
        )
        Data.set_edited_message(
            before.content, after.content,
            after.author.name
        )

    @staticmethod
    def run() -> None:
        load_dotenv()
        client.run(os.getenv("TOKEN"))
