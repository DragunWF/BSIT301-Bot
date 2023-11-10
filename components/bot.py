import os
import discord

from dotenv import load_dotenv
from discord import Message
from discord import Member

from components.data import Data
from utils.cli_log import Logger
from utils.utils import Utils

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

    @client.event
    async def on_member_join(member: Member):
        welcome_channel = client.get_channel(Data.get_channels()["welcome"])
        guild = client.get_guild(Data.get_guild_id())
        await welcome_channel.send(f"Welcome to BSIT301! <@{member.id}>, You are the {Utils.get_ordinal(guild.member_count)}")

    @staticmethod
    def run() -> None:
        load_dotenv()
        client.run(os.getenv("TOKEN"))
