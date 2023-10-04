from components.bot import Bot
import components.commands  # To load the commands


class Main:
    @staticmethod
    def run() -> None:
        Bot.run()


if __name__ == '__main__':
    Main.run()
