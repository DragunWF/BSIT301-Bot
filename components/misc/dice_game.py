import discord
from random import randint

# TODO: Implement 5 dice rolls
# TODO: Implement user points when given a positive roll and a loss when given a negative roll


class DiceView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.__rolls = 0
        self.__ROLL_LIMIT = 5

    @discord.ui.button(label="Roll The Dice!", style=discord.ButtonStyle.primary, emoji="🎲")
    async def button_callback(self, button, interaction):
        roll = randint(1, 6)
        self.__rolls += 1

        if self.__rolls == self.__ROLL_LIMIT:
            button.disabled = True
            button.label = "No more rolls"
            await interaction.response.send_message("No more rolls!")
        else:
            await interaction.response.send_message(f"You rolled a {roll} 🎲.\n"
                                                    + f"You have {self.__ROLL_LIMIT - self.__rolls} rolls left")


class DiceGame:
    def __init__(self, user_id: str):
        pass
