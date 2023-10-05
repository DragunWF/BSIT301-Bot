import sqlite3
import os


class Database:
    def __init__(self) -> None:
        self.__path = ""

    def update_stats(self) -> None:
        with sqlite3.connect(self.__path) as db:
            db.execute("INSERT INTO stats WHERE name = 'message_events' (?)")
