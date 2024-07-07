import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("23626691", 0)
API_HASH = os.getenv("751ddd3e8ddb254be1fd8df914a4f687", "")
BOT_TOKEN = os.getenv("6802359058:AAHWoRtY2v8u2yDoDR4FiXRYaYHDvbckGhQ", None)
SUDOERS = list(map(int, os.getenv("1321338802", 0).split()))
MONGO_URL = os.getenv("mongodb+srv://<redbn32>:<qawsed00>@cluster0.l6ty5ue.mongodb.net/", None)
LOG_GROUP_ID = os.getenv("-1002025820201", None)
MUST_JOIN = os.getenv("X_YI1I", "")
DISABLED = os.getenv("abj", "").split()

if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")

if not MONGO_URL:
    print("MONGO_URL environment variable Is Empty Bot")

# Convert the LOG_GROUP_ID variable to an integer if it is not None
if LOG_GROUP_ID:
    LOG_GROUP_ID = int(LOG_GROUP_ID)
