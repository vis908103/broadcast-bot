#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  Name     : broadcast-bot [ Telegram ]
#  Repo     : https://github.com/m4mallu/broadcast-bot
#  Author   : Renjith Mangal [ https://t.me/space4renjith ]
#  Licence  : GPL-3


import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):
    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7592341037:AAExV2-M-x9AiQlbityNXHgDKt_kLBoaXuE")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "26657288"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "00536e431477dbb16583d5b85813aa72")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "http://eg3skk3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

    # Group / channel username of the support chat
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "@Anime_india_divine")

    # List of admin user ids for special functions(Storing as an array)
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
