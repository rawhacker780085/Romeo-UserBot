from os import getenv

API_ID = int(getenv("API_ID", "28372387"))
API_HASH = getenv("API_HASH", "11edc85521fb2d8f75e751bb284507e1")
BOT_TOKEN = getenv("BOT_TOKEN", "8008903575:AAHIsqouHROwJoNPKyMMSjBz2blYBBfJhHo")
OWNER_ID = int(getenv("OWNER_ID", "STINER_KING_OP"))
STRING_SESSION = getenv("STRING_SESSION", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5392070730").split()))
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/a62b9c7d9848afde0569e.jpg")
REPO_URL = getenv("REPO_URL", "https://github.com/RRomeo-RJ/Romeo-UserBot")
BRANCH = getenv("BRANCH", "main")
