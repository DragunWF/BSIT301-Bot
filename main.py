import discord
import os
import interactions
import json

from discord.ext import commands
from discord_slash import SlashCommand
from pathlib import Path
from dotenv import load_dotenv


class MyClient(discord.Client):
    def __init__(self, intents):
        super().__init__(intents=intents)

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        print(f'Message from {message.author}: {message.content}')
        await message.channel.send("Hello World!")


class Main:
    @staticmethod
    def run():
        load_dotenv()

        intents = discord.Intents.default()
        intents.message_content = True

        client = MyClient(intents)
        client.run(os.getenv("TOKEN"))


if __name__ == '__main__':
    Main.run()
