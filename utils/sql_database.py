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

    def get_users(self) -> dict:
        with sqlite3.connect(self.__path) as db:
            # TODO: Implement users select query from database
            pass

    def get_stats(self) -> dict:
        with sqlite3.connect(self.__path) as db:
            # TODO: Implement stats select query from database
            pass
