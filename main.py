import discord
from dotenv import load_dotenv
import os


class MyClient(discord.Client):
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
        intents = discord.Intents.default()
        intents.message_content = True
        load_dotenv()

        client = MyClient(intents=intents)
        client.run(os.getenv("TOKEN"))


if __name__ == '__main__':
    Main.run()
