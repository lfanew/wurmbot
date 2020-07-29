from client import WurmBot
import pygetwindow as pgw
import sys


def main(args: list) -> int:
    game_window = pgw.getWindowsWithTitle('Wurm Online')[0]

    game_window.activate()
    game_window.moveTo(-7,0)

    bot = WurmBot()

    bot.load(args[1])
    bot.run(int(args[2]))

    return 0


if __name__ == "__main__":
    exit(main(sys.argv))
