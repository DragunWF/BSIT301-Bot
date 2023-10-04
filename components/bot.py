import os
import discord
import json

from dotenv import load_dotenv
from pathlib import Path

client = discord.Bot()


class Bot:
    @client.event
    async def on_ready():
        print(f"Logged in as {client.user}")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

    @staticmethod
    def run() -> None:
        load_dotenv()
        client.run(os.getenv("TOKEN"))
