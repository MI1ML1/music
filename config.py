from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("22044610"))
API_HASH = getenv("77fd99b0e50e1bdae484edf844f8cb4d")

BOT_TOKEN = getenv("8485480436:AAHR--ysY4wiJi2pQx88GXydFNwjCIl9HGM", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("6070781640"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/5948678d1dcbc98e11d49.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/5948678d1dcbc98e11d49.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/mi3i11")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/fo78v")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "3823637201").split()))


FAILED = "https://graph.org/file/5948678d1dcbc98e11d49.jpg"
