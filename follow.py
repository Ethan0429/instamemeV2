"""
    instabot example
    Workflow:
        Follow users who post medias with hashtag.
"""

import argparse
import os
import sys

sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot  # noqa: E402

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("hashtags", type=str, nargs="+", help="hashtags")
args = parser.parse_args()

bot = Bot(follow_delay=10)
bot.login(username='REDACTED', password='REDACTED', cookie_fname='cookies.txt')

for hashtag in args.hashtags:
    users = bot.get_hashtag_users(hashtag)
    bot.follow_users(users)