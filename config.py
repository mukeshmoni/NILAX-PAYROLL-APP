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

BOT_TOKEN = getenv("BOT_TOKEN", "7369094787:AAFLCZ6QjCi2YvYOp_T-emU7ZEWPjIA73Hw")

# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME", "Mr_king008")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "Kanazhagi_bot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , "ꞏ─𓆩‌🌼‌⃝⃪👀ᤌᰢᮀᰪᰢᰪഴᤌ᭄آ‌🐾 ⃝")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "Salim0204")
# ---------------------------------------------------------


#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://mukeshnitttr1626:mukeshmoninitttr1626@cluster0.e27s9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "17894614560000000000000"))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID", "-1001770039008"))
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", "5444362033"))
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
    "https://github.com/mukeshmoni/AnieMusicbot2.0",
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
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TMK_MUSICCHANNEL")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TMK_MUSICSUPPORT")
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
STRING1 = getenv("STRING_SESSION", "BQEk7oIAMcCaHLZm0QQ-5X7muMXlRHtDpQm12waq0wINsG483lMcTuB7nOEhWAEqnAMSttX3b-Y4cKT08F3aX9Yf2wXXwosm0ZI6fvq1o-JRSngTbh11n03WoIMEgxD8bsZO6HkAPPwqx2U3OqAY1G4uu7T4QaptXsX-HeHqoS0PBfcGrv4BYnPIDSzly7HaGtluAO68stBdctd-tBojTzMI6HIZtRzm90jyd156F9DEFXnNvQKF-FA21bhs6BttnCtVokThPKe4foB7AY4Eh7ZRjIgjc7VO8pEtJ9q9Xi7AQtdBwKNvAs6G2Qc_03FIiGWH95zAl-MJRmn49ywlkh9kdjAh4gAAAAFEgl8xAA")
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
    "START_IMG_URL", "https://telegra.ph/file/65470847d88dad800596c.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/65470847d88dad800596c.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/65470847d88dad800596c.jpg"
STATS_IMG_URL = "https://telegra.ph/file/65470847d88dad800596c.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/65470847d88dad800596c.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/65470847d88dad800596c.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/65470847d88dad800596c.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/65470847d88dad800596c.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/65470847d88dad800596c.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/65470847d88dad800596c.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/65470847d88dad800596c.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/65470847d88dad800596c.jpg"

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
