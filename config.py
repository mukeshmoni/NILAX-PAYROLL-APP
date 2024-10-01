import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = int(getenv("API_ID", "24274375"))
API_HASH = getenv("API_HASH", "9d88affc9ab571a6695e069cef5d363b")
# ------------------------------------------------------

BOT_TOKEN = getenv("BOT_TOKEN", "6582609535:AAFpTkuhQiZ-t5wWHUTICICUefJ_H3AbZbE")

# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME", "KingofAtttitude")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "AmmuMusic_bot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , "AmmuMusic")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "Owner_of_aishu")
# ---------------------------------------------------------


#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://moni:monieee@cluster0.cei6n.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "17894614560000000000000"))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID", "-1001886289537"))
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", " 7290811275 1054522004 6094755630"))
# -----------------------------------------------------------------
# -----------------------------------------------------------------

# ----------------------------------------------------------------
# ----------------------------------------------------------------
## Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://telegra.ph/file/65470847d88dad800596c.jpg",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # ----------------------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/teamwednesdayssupportchannel")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/teamwednesdayssupport")
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = getenv("STRING_SESSION", "BQEk7oIAU7O2t3zs6BxB1CvJbo41U7flhZc55oCsZgxx6iBdnmJLWfPzXe_Y1DMJkTZRVTWLoX9P41GaBKuhZyGDJ3SLrD74VDtnSJmCdKZmuAWH1c6db9wa_W4qzVDhCsioTl0jE6DEqfCnKPVGfiJHexwf3F_H2Ws8OFaS5NtICDti9JOPf_1IaZKWLMX-GSDrRSmG_grVZVCQPbzhUZieoW0JQzCqQz5Bbi73zzdtxfWrrSyJRPbcb2FFwYLWMOvjQZsn6X0BRmC0JbU1NqnKPX64b32lM_x6UZN2j7Ihwi0XrjKnyx1xXTBjs1_fG3bjr7Ya4RMcZEAA9eynp5JAmNV7kgAAAAEq1MfAAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = getenv(
    "START_IMG_URL", "https://i.ibb.co/1qC3CZX/2552da9992e9.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://i.ibb.co/QbM7CL5/cb538d6a1906.jpg"
)
PLAYLIST_IMG_URL = "https://i.ibb.co/9V9FjGt/e24148ae6904.jpg"
TELEGRAM_AUDIO_URL = "https://i.ibb.co/YbsSmKX/0e0d080f7ad3.jpg"
TELEGRAM_VIDEO_URL = "https://i.ibb.co/Mff2sBn/7dd1e5ae0e25.jpg"
STREAM_IMG_URL = "https://i.ibb.co/4MVKbTZ/ad0c15244bdf.jpg"
SOUNCLOUD_IMG_URL = "https://i.ibb.co/jLQTzYR/6ed2ba839238.jpg"
YOUTUBE_IMG_URL = "https://i.ibb.co/FwvLXNx/c30c239d63e5.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://i.ibb.co/bFTCJHt/2197feb915be.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://i.ibb.co/4jhF2JM/fa433827323c.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://i.ibb.co/FBkc1Mj/a0e720db9e4d.jpg"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
