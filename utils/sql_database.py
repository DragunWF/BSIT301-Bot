import sqlite3
import os


class Database:
    def __init__(self) -> None:
        self.__path = ""

    def update_stats(self) -> None:
        with sqlite3.connect(self.__path) as db:
            # TODO: Implement stats updating from database
            db.execute("INSERT INTO stats WHERE name = 'message_events' (?)")

    def update_users(self) -> None:
        with sqlite3.connect(self.__path) as db:
            # TODO: Implement users update for points in database
            pass

    def reward_points(self, user_id: str, points: int) -> None:
        # TODO: Implement reward points for finishing games with the bot
        pass

    def get_users(self, sort_by_points=False) -> dict:
        with sqlite3.connect(self.__path) as db:
            # TODO: Implement users select query from database
            if sort_by_points:
                # Implement logic with sorted data
                pass
            else:
                # Implement logic with no sorting
                pass

    def get_leaderboard(self):
        # TODO: Replace bubble sort with quick sort
        users = self.get_users()
        for i in range(len(users) - 1):
            for j in range(len(users) - 1):
                if users[j]["points"] > users[j + 1]["points"]:
                    users[j], users[j + 1] = users[j + 1], users[j]

    def get_stats(self) -> dict:
        with sqlite3.connect(self.__path) as db:
            # TODO: Implement stats select query from database
            pass
