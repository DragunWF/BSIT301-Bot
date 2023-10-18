import discord

# Has future use for type hinting (Option): Check documentation to learn
from discord import Option
from discord.commands.context import ApplicationContext
from datetime import datetime
from random import randint

from .bot import client
from .data import Data
from .misc.dice_game import DiceView
from .misc.rps import RockPaperScissorsGame, GameState
from utils.utils import Utils
from utils.sql_database import Database


class Commands:
    __guilds = Data.get_settings()["guilds"]
    __commands = ("help", "info", "snipe", "esnipe")

    @client.slash_command(guild_ids=__guilds,
                          description="Testing purpose for the developer of this bot")
    async def test(ctx: ApplicationContext):
        print(ctx)
        await ctx.respond("This is a test message")

    @client.slash_command(guild_ids=__guilds,
                          description="Display all commands from BSIT301-Bot")
    async def help(ctx: ApplicationContext):
        command_list = "## List:\n"
        for name in Commands.__commands:
            command_list += f"- `/{name}`\n"
        embed = discord.Embed(
            title="Commands",
            description=command_list,
            color=discord.Colour.blurple(),
            timestamp=datetime.now()
        )
        embed.set_footer(text=Data.get_settings()["web_link"])
        await ctx.respond(embed=embed)

    @client.slash_command(guild_ids=__guilds,
                          description="Display information about BSIT301-Bot")
    async def info(ctx: ApplicationContext):
        embed = discord.Embed(
            title="Information about BSIT301-Bot",
            description=f"This bot is programmed and developed by {Data.get_settings()['master_name']}",
            color=discord.Colour.blurple(),
            timestamp=datetime.now()
        )
        # TODO: Make a replit web server then replace this placeholder link with a real one
        embed.set_footer(text=Data.get_settings()["web_link"])
        # TODO: Set image to bot profile picture
        embed.set_image(Data.get_settings()["profile_image"])
        await ctx.respond(embed=embed)

    async def stats(ctx: ApplicationContext):
        embed = discord.Embed(
            title="BSIT301-Bot Statistics",
            description="",
            color=discord.Colour.blurple(),
            timestamp=datetime.now()
        )
        embed.set_image(Data.get_settings()["profile_image"])
        embed.set_footer(text=Data.get_settings()["web_link"])

    @client.slash_command(guild_ids=__guilds,
                          description="Snipes recently deleted messages")
    async def snipe(ctx: ApplicationContext):
        deleted_message = Data.get_deleted_message()
        if deleted_message["author"] is None:
            await ctx.respond("There are no deleted messages recorded!")
        else:
            await ctx.respond(embed=Utils.get_snipe_embed(
                title="Deleted Message",
                description=deleted_message["content"],
                author=deleted_message["author"]
            ))

    @client.slash_command(guild_ids=__guilds,
                          description="Snipes recently edited messages")
    async def esnipe(ctx: ApplicationContext):
        edited_message = Data.get_edited_message()
        if edited_message["author"] is None:
            await ctx.respond("There are no edited messages recorded!")
        else:
            after = edited_message["content"]["after"]
            before = edited_message["content"]["before"]
            await ctx.respond(embed=Utils.get_snipe_embed(
                title="Edited Message",
                description=f"**Before:**\n{before}\n\n**After:**\n{after}",
                author=edited_message["author"]
            ))

    @client.slash_command(guild_ids=__guilds,
                          description="Displays the player leaderboard by points")
    async def leaderboard(ctx: ApplicationContext):
        # TODO: Implement leaderboards
        embed = discord.Embed()
        await ctx.respond(embed=embed)

    @client.slash_command(guild_ids=__guilds,
                          description="Play a game of dice!")
    async def dice(ctx: ApplicationContext):
        # TODO: Implement dice mini-game
        await ctx.respond("Try out your luck with a dice roll!", view=DiceView())

    @client.slash_command(guild_ids=__guilds,
                          description="Let the bot choose a random name from your list of names. " +
                          "Ex: nameOne,nameTwo,nameThree")
    async def name_picker(ctx: ApplicationContext, names: str):
        wheel_of_names = tuple(map(str.strip, names.split(",")))
        if len(wheel_of_names) <= 1:
            await ctx.respond("You must choose more than one name!")
        else:
            chosen_name = wheel_of_names[randint(0, len(wheel_of_names))]
            await ctx.respond(f"{chosen_name} has been chosen!")

    @client.slash_command(guild_ids=__guilds,
                          description="Play a game of rock paper scissors against A.I!")
    async def rock_paper_scissors(ctx: ApplicationContext):
        pass
