import re
from os import environ
from Script import script

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if str(value).lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif str(value).lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Main
SESSION = environ.get("SESSION", "Movie_area")
API_ID = int(environ.get("API_ID", "20035684"))
API_HASH = environ.get("API_HASH", "987a8b7ee93d55e76bb29fce4d8ebf52")
BOT_TOKEN = environ.get("BOT_TOKEN", "8315587555:AAEB8hCCcXn_FN6SHWyUA_ZWuMWcZf6V8ts")
PORT = environ.get("PORT", "8080")

# Owners
ADMINS = [
    int(admin) if id_pattern.search(admin) else admin
    for admin in environ.get("ADMINS", "5234918257").split()
]
OWNER_USERNAME = environ.get("OWNER_USERNAME", "riteshkumarsingh437")
USERNAME = environ.get("USERNAME", "riteshkumarsingh437")

# Database Channel
CHANNELS = [
    int(ch) if id_pattern.search(ch) else ch
    for ch in environ.get("CHANNELS", "-1002918425042 -1002804180914").split()
]

# ForceSub Channel & Log Channels
AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1002918425042"))
AUTH_REQ_CHANNEL = int(environ.get("AUTH_REQ_CHANNEL", "-1002804180914"))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002984344864"))
LOG_API_CHANNEL = int(environ.get("LOG_API_CHANNEL", "-1002984344864"))
LOG_VR_CHANNEL = int(environ.get("LOG_VR_CHANNEL", "-1002984344864"))

# MongoDB
DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://riteshkumarsingh:iX9Eeca9iRTH3buu@cluster0.sqrcqji.mongodb.net/moviecollection?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get("DATABASE_NAME", "mongodb")

# Files index database url
FILES_DATABASE = environ.get("FILES_DATABASE", DATABASE_URI)
COLLECTION_NAME = environ.get("COLLECTION_NAME", "movies")

# Other Channels
SUPPORT_GROUP = int(environ.get("SUPPORT_GROUP", "-1002918425042"))
DELETE_CHANNELS = int(environ.get("DELETE_CHANNELS", "0"))
request_channel = environ.get("REQUEST_CHANNEL", "-1002896274382")
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
MOVIE_UPDATE_CHANNEL = int(environ.get("MOVIE_UPDATE_CHANNEL", "-1002896274382"))

# Added Link Here Not Id
SUPPORT_CHAT = environ.get("SUPPORT_CHAT", "https://t.me/moviesupportchats437")
MOVIE_GROUP_LINK = environ.get("MOVIE_GROUP_LINK", "https://t.me/moviearea_437")

# Verification
IS_VERIFY = is_enabled("IS_VERIFY", True)
TUTORIAL = environ.get("TUTORIAL", "https://t.me/ninjamodz437/121")
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://t.me/ninjamodz437/121")
TUTORIAL_3 = environ.get("TUTORIAL_3", "https://t.me/ninjamodz437/121")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")

# Shorteners
SHORTENER_API = environ.get("SHORTENER_API", "ef9e633750559cdcc7b4dc6e544b53370a5116f0")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "earnlinks.in")

# Gap for verification
TWO_VERIFY_GAP = int(environ.get("TWO_VERIFY_GAP", "14400"))
THREE_VERIFY_GAP = int(environ.get("THREE_VERIFY_GAP", "14400"))

# Language & Quality & Season & Year
LANGUAGES = ["hindi","english","telugu","tamil","kannada","malayalam","bengali","marathi","gujarati","punjabi","marathi"]
QUALITIES = ["HdRip","web-dl","bluray","hdr","fhd","240p","360p","480p","540p","720p","960p","1080p","1440p","2K","2160p","4k","5K","8K"]
YEARS = [f"{i}" for i in range(2025, 2002, -1)]
SEASONS = [f"season {i}" for i in range(1, 23)]

# Pictures
START_IMG = (environ.get("START_IMG","https://i.ibb.co/qpxpGmC/image.jpg https://i.ibb.co/DQ35zLZ/image.jpg",)).split()
FORCESUB_IMG = environ.get("FORCESUB_IMG", "https://i.ibb.co/ZNC1Hnb/ad3f2c88a8f2.jpg")

# Other Settings
FILE_AUTO_DEL_TIMER = int(environ.get("FILE_AUTO_DEL_TIMER", "600"))
AUTO_FILTER = is_enabled("AUTO_FILTER", True)
AUTO_DELETE = is_enabled("AUTO_DELETE", True)
DELETE_TIME = int(environ.get("DELETE_TIME", 1200))
SPELL_CHECK = is_enabled("SPELL_CHECK", True)
LINK_MODE = is_enabled("LINK_MODE", True)

TMDB_API_KEY = environ.get("TMDB_API_KEY", "")

# Streaming
STREAM_MODE = bool(environ.get("STREAM_MODE", True))
