import discord
import os
import interactions
import json

from discord import app_commands
from discord.ext import commands
from pathlib import Path
from dotenv import load_dotenv


class MyClient(commands.Bot):
    def __init__(self, intents) -> None:
        super().__init__(token=os.getenv("TOKEN"))

    async def on_ready(self) -> None:
        print(f'Logged on as {self.user}!')

    async def on_message(self, message) -> None:
        if message.author == self.user:
            return
        print(f'Message from {message.author}: {message.content}')
        await message.channel.send("Hello World!")


class Bot:
    pass

class Main:
    @staticmethod
    def run() -> None:
        load_dotenv()

        intents = discord.Intents.default()
        intents.message_content = True

        client = MyClient(intents)
        client.start()


if __name__ == '__main__':
    Main.run()
