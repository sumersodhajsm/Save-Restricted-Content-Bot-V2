# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "25513009"))
API_HASH = getenv("API_HASH", "33ace9b0779df4387a8ad8b7fbe6b050")
BOT_TOKEN = getenv("BOT_TOKEN", "7945680462:AAHTFepyh6j-NpTpyAIMVbNIo-zsmDf-SuA")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7068035738").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://sumersingh5688977:TGZmTpS3E803laT4@cluster0.4cikn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "4716427863")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002363366847"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "1"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "1000"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "33ace9b0779df4387a8ad8b7fbe6b050")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
