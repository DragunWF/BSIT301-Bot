import discord
from random import randint


class DiceView(discord.ui.View):
    @discord.ui.button(label="Roll The Dice!", style=discord.ButtonStyle.primary, emoji="🎲")
    async def button_callback(self, button, interaction):
        roll = randint(1, 6)
        await interaction.response.send_message(f"You rolled a {roll}")
