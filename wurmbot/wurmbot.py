from client import WurmBot
import sys


def main(args: list) -> int:
    bot = WurmBot()

    bot.load(args[1])
    bot.run(int(args[2]))

    return 0


if __name__ == "__main__":
    exit(main(sys.argv))
