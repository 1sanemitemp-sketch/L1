# REQUIRED CONFIG
BOT_TOKEN = "8698650812:AAG4qJ7tb6kMtrm5Ejhhjba9dWbBiWWnvV0"
OWNER_ID = 7791901419
TELEGRAM_API = 38826846
TELEGRAM_HASH = "783f4b3d1a5438032649cb5ff482f3d9"
DATABASE_URL = "mongodb+srv://sanemibot:SdhAOZaIK959Ex0g@cluster0.vewbige.mongodb.net/?appName=Cluster0"

# OPTIONAL CONFIG
DEFAULT_LANG = "en"
TG_PROXY = None  # {"scheme": ”socks5”, "hostname": ””, "port": 1234, "username": ”user”, "password": ”pass”}
USER_SESSION_STRING = ""
CMD_SUFFIX = "1"
AUTHORIZED_CHATS = "6408595259"
SUDO_USERS = ""
STATUS_LIMIT = 10
DEFAULT_UPLOAD = "rc"
STATUS_UPDATE_INTERVAL = 15
FILELION_API = ""
STREAMWISH_API = ""
ALLDEBRID_API_KEY = ""
ALLDEBRID_NO_SEED_TIMEOUT = 180
EXCLUDED_EXTENSIONS = ""
INC_TASK_NOTIFY = False
YT_DLP_OPTIONS = ""
USE_SERVICE_ACCOUNTS = False
NAME_SWAP = ""
FFMPEG_CMDS = {}
UPLOAD_PATHS = {}
WEB_ACCESS_PASSWORD = (
    ""  # Secret for deriving proxy passwords. Logs derived passwords at startup.
)

# Hyper Tg Downloader
HELPER_TOKENS = ""
STREAM_TOKENS = ""
USE_HYPER = False

# MegaAPI v4.30
MEGA_EMAIL = ""
MEGA_PASSWORD = ""
DISABLE_MEGA = True

# Disable Options
DISABLE_TORRENTS = True
DISABLE_LEECH = False
DISABLE_MIRROR = True
DISABLE_BULK = True
DISABLE_MULTI = True
DISABLE_SEED = True
DISABLE_FF_MODE = True
DISABLE_JD = True
DISABLE_NZB = True
DISABLE_SEEDR = True
DISABLE_RSS = True
DISABLE_SEARCH = True
DISABLE_STREAM = True
DISABLE_YTDLP = True
DISABLE_PLUGINS = False

# Plugins
PLUGIN_INDEXES = []

# Memory
MEM_BUDGET = 0
MEM_DEEP_STATS = False

# Telegraph
AUTHOR_NAME = "WZML-X"
AUTHOR_URL = "https://t.me/WZML_X"

# Task Limits
DIRECT_LIMIT = 50
MEGA_LIMIT = 50
TORRENT_LIMIT = 50
GD_DL_LIMIT = 50
RC_DL_LIMIT = 50
CLONE_LIMIT = 50
JD_LIMIT = 50
NZB_LIMIT = 50
SEEDR_LIMIT = 50
YTDLP_LIMIT = 50
PLAYLIST_LIMIT = 50
LEECH_LIMIT = 50
EXTRACT_LIMIT = 50
ARCHIVE_LIMIT = 50
STORAGE_LIMIT = 100

# CPU limit for background services (SABnzbd, JDownloader). Default: 20
CPU_LIMIT = 20

# CPUs given to FFmpeg. auto=60% of them, all/0=every CPU, a count like 5,
# a percentage like 75%, or an explicit taskset list like 0-4 / 0,1,2,3.
# Background services get whatever is left over.
FFMPEG_CORES = "auto"

# Throttle services during heavy ops (FFmpeg). auto=low-end only, always, never
THROTTLE_SERVICES = "auto"

# Image Search
USE_IMAGES = False
IMG_SEARCH = ""
IMG_PAGE = 1
IMG_SOURCES = ["wallpaperflare"]

# Insta video downloader api
INSTADL_API = ""

# Nzb search
HYDRA_IP = ""
HYDRA_API_KEY = ""

# Media Search
# Optional: Set IMDB_TEMPLATE to use old HTML format instead of Rich Messages.
# If empty (default), IMDb uses Rich Messages with tables and collapsible sections.
IMDB_TEMPLATE = ""

# Task Tools
FORCE_SUB_IDS = "-1004291361651"
MEDIA_STORE = True
DELETE_LINKS = False

# Limiters
BOT_MAX_TASKS = 10
USER_MAX_TASKS = 2
USER_TIME_INTERVAL = 5
VERIFY_TIMEOUT = 0
LOGIN_PASS = ""

# Crash Reporting
ENABLE_TELEMETRY = True  # Send crash reports to remote worker

# Bot Settings
BOT_PM = True
SET_COMMANDS = True
TIMEZONE = "Asia/Kolkata"

# GDrive Tools
GDRIVE_ID = ""
GD_DESP = "Uploaded with WZ Bot"
IS_TEAM_DRIVE = False
STOP_DUPLICATE = False
INDEX_URL = ""

# YT Tools
YT_DESP = "Uploaded to YouTube by WZML-X bot"
YT_TAGS = ["telegram", "bot", "youtube"]  # or as a comma-separated string
YT_CATEGORY_ID = 22
YT_PRIVACY_STATUS = "unlisted"

# Rclone
RCLONE_PATH = ""
RCLONE_FLAGS = ""
RCLONE_SERVE_URL = ""
SHOW_CLOUD_LINK = True
RCLONE_SERVE_PORT = 0
RCLONE_SERVE_USER = ""
RCLONE_SERVE_PASS = ""

# JDownloader
JD_EMAIL = ""
JD_PASS = ""

# Sabnzbd
USENET_SERVERS = [
    {
        "name": "main",
        "host": "",
        "port": 563,
        "timeout": 60,
        "username": "",
        "password": "",
        "connections": 8,
        "ssl": 1,
        "ssl_verify": 2,
        "ssl_ciphers": "",
        "enable": 1,
        "required": 0,
        "optional": 0,
        "retention": 0,
        "send_group": 0,
        "priority": 0,
    }
]

# Update
UPSTREAM_REPO = "https://github.com/SilentDemonSD/WZML-X"
UPSTREAM_BRANCH = "wzv3"
# Leech
LEECH_SPLIT_SIZE = 0
AS_DOCUMENT = False
EQUAL_SPLITS = False
MEDIA_GROUP = False
TRANSMISSION_MODE = "both"
LEECH_PREFIX = ""
LEECH_SUFFIX = ""
LEECH_FONT = "b"
LEECH_CAPTION = ""
THUMBNAIL_LAYOUT = ""
TMDB_ACCESS_TOKEN = ""
AUTO_THUMBNAIL = False

# Log Channels
LEECH_LOG_CHAT = "-1003961500919"
# Named leech dump chats, selectable per task with the -ud flag.
# The chosen chat becomes the primary upload destination for the task.
# Format: {"name": chat_id}
LEECH_DUMP_CHATS = {
    # "A": -1001234567890,
    # "B": -1009876543210,
}
LINKS_LOG_ID = "-1003961500919"
MIRROR_LOG_ID = "-1003961500919"

# qBittorrent/Aria2c
TORRENT_TIMEOUT = 120
BASE_URL = ""
WEB_PINCODE = True

# Queueing system
QUEUE_ALL = 0
QUEUE_DOWNLOAD = 0
QUEUE_UPLOAD = 0

# RSS
RSS_DELAY = 600
RSS_CHAT = ""
RSS_SIZE_LIMIT = 0

# Torrent Search
SEARCH_API_LINK = ""
SEARCH_LIMIT = 0
SEARCH_PLUGINS = [
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/piratebay.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/limetorrents.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torlock.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torrentscsv.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/eztv.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torrentproject.py",
    "https://raw.githubusercontent.com/MaurizioRicci/qBittorrent_search_engines/master/kickass_torrent.py",
    "https://raw.githubusercontent.com/MaurizioRicci/qBittorrent_search_engines/master/yts_am.py",
    "https://raw.githubusercontent.com/MadeOfMagicAndWires/qBit-plugins/master/engines/linuxtracker.py",
    "https://raw.githubusercontent.com/MadeOfMagicAndWires/qBit-plugins/master/engines/nyaasi.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/ettv.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/glotorrents.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/thepiratebay.py",
    "https://raw.githubusercontent.com/v1k45/1337x-qBittorrent-search-plugin/master/leetx.py",
    "https://raw.githubusercontent.com/nindogo/qbtSearchScripts/master/magnetdl.py",
    "https://raw.githubusercontent.com/msagca/qbittorrent_plugins/main/uniondht.py",
    "https://raw.githubusercontent.com/khensolomon/leyts/master/yts.py",
]

# Seedr (magnet mirroring via seedr.cc)
SEEDR_EMAIL = ""
SEEDR_PASSWORD = ""
SEEDR_DELETE_FOLDER = False
