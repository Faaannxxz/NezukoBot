from os import environ, path

from dotenv import load_dotenv

if path.exists("config.env"):
    load_dotenv("config.env")

BOT_TOKEN = environ.get("5701341223:AAHQL19XLCpyNXHtHmoLDMAvirFYEKZbahc", None)
API_ID = int(environ.get("14314614",)
API_HASH = environ.get("7f030d708946ee907bf0944c05c8cc09", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
SUDO_USERS_ID = [int(x) for x in environ.get("5035563632", "").split()]
LOG_GROUP_ID = int(environ.get("-1001729421519", None))
GBAN_LOG_GROUP_ID = int(environ.get("-1001729421519", None))
MESSAGE_DUMP_CHAT = int(environ.get("-1001729421519", None))
WELCOME_DELAY_KICK_SEC = int(environ.get("WELCOME_DELAY_KICK_SEC", None))
MONGO_URL = environ.get("mongodb+srv://maticnemanja:kucingkawin@cluster0.qhwwh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", None)
ARQ_API_URL = environ.get("ARQ_API_URL", None)
ARQ_API_KEY = environ.get("KHJZGM-OXGZRB-WLJFAW-VKMQOV-ARQ", None)
RSS_DELAY = int(environ.get("RSS_DELAY", None))
UPSTREAM_REPO = environ.get(
    "UPSTREAM_REPO", "https://github.com/rozari0/NezukoBot.git"
)
