from .DailyNews import get_message_content
from .Bot import Bot
import argparse

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument("--wx-secret", type=str, default="0")

args = parser.parse_args()


if __name__ == '__main__':
    bot = Bot(args.wx_secret)
    msg = get_message_content()
    bot.send_message(msg)
