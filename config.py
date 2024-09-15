# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "18991521"))
API_HASH = getenv("API_HASH", "0c1086e0013e5f6633ad3b4bae13238b")
BOT_TOKEN = getenv("BOT_TOKEN", "7516196344:AAF5FVbcSLK7Zat-JjR6TO8SAP3fdoqlsWY")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1633416742").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://hehup:hehup18@cluster0.ema1k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002139381519")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002145995438"))
