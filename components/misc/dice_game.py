import discord
from random import randint

# TODO: Implement 5 dice rolls
# TODO: Implement user points when given a positive roll and a loss when given a negative roll


class DiceView(discord.ui.View):
    @discord.ui.button(label="Roll The Dice!", style=discord.ButtonStyle.primary, emoji="🎲")
    async def button_callback(self, button, interaction):
        roll = randint(1, 6)
        await interaction.response.send_message(f"You rolled a {roll} 🎲")


class DiceGame:
    def __init__(self, user_id: str):
        pass
