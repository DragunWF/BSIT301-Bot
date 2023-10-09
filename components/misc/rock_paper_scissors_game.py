import discord
from random import randint
from utils.utils import Utils

# TODO: Find a way to grab the user id from the user that has clicked the button


class RockPaperScissorsGame(discord.ui.View):
    @discord.ui.button(label="Rock", style=discord.ButtonStyle.primary, emoji="🎲")
    async def button_callback(self, button, interaction):
        # TODO: Implement button callback
        pass

    @discord.ui.button(label="Paper", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction):
        # TODO: Implement button callback
        pass

    @discord.ui.button(label="Scissors", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction):
        # TODO: Implement button callback
        pass


class GameState:
    __choices = ("rock", "paper", "scissors")
    __MAX_POINTS = 5
    __states = []

    def __init__(self, player_id: str) -> None:
        if player_id is None:
            raise Exception("Argument cannot be a NoneType!")
        self.__player_id = player_id
        self.__player_points = 0
        self.__opponent_points = 0
        self.__ties = 0
        self.__winner = None

    @Utils.validate_args
    def game_loop(self, player_choice: str) -> None:
        ai_choice = self.__ai_choice()
        if player_choice == ai_choice:
            self.__ties += 1
        elif (player_choice == "rock" and ai_choice == "paper" or
              player_choice == "paper" and ai_choice == "scissors" or
              player_choice == "scissors" and ai_choice == "rock"):
            self.__opponent_points += 1
        else:
            self.__player_points += 1
        self.__check_win()

    def end_game(self) -> None:
        # TODO: Implement game aftermath
        pass

    def get_player_id(self) -> str:
        return self.__player_id

    @Utils.validate_args
    def find_game_state(self, player_id: str) -> object:
        for game_state in GameState.__states:
            if game_state.get_player_id() == player_id:
                return game_state
        return None

    def __check_win(self) -> bool:
        if self.__player_points >= GameState.__MAX_POINTS:
            self.__winner = "player"
            return True
        elif self.__opponent_points >= GameState.__MAX_POINTS:
            self.__winner = "opponent"
            return True
        return False

    def __ai_choice(self) -> str:
        return GameState.__choices[randint(0, len(GameState.__choices))]

    @staticmethod
    @Utils.validate_args
    def add_game_state(player_id: str):
        GameState.__states.append(GameState(player_id))
