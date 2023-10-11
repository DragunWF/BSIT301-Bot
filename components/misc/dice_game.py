import discord
from discord import Button
from discord.interactions import Interaction
from random import randint

# TODO: Implement 5 dice rolls
# TODO: Implement user points when given a positive roll and a loss when given a negative roll


class DiceView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.__rolls = 0
        self.__ROLL_LIMIT = 5
        self.__MAX_ROLL_VALUE = 12

    @discord.ui.button(label="Roll The Dice!", style=discord.ButtonStyle.primary, emoji="🎲")
    async def button_callback(self, button: Button, interaction: Interaction):
        roll = randint(1, self.__MAX_ROLL_VALUE)
        self.__rolls += 1

        if self.__rolls == self.__ROLL_LIMIT:
            button.disabled = True
            button.label = "No more rolls"
            await interaction.message.edit(view=self)
            await interaction.response.send_message("No more rolls!")
        else:
            rolls_left = self.__ROLL_LIMIT - self.__rolls
            rolls_word = "rolls" if rolls_left > 1 else "roll"
            await interaction.response.send_message(f"You rolled a **{roll}** 🎲\n\n"
                                                    + f"You have **{rolls_left}** {rolls_word} left...")


class DiceGame:
    def __init__(self, user_id: str):
        pass
