from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "18145443"))
API_HASH = getenv("API_HASH", "dc90da21390582736a9d5b4ffce8b5bb")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","Misscutie music")
BOT_USERNAME = getenv("BOT_USERNAME", "")
OWNER_USERNAME = getenv("OWNER_USERNAME", "surya12p")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Misscuitesupport")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
START_IMG = getenv("START_IMG", "")
PING_IMG = getenv("PING_IMG", "")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5150456401").split()))
