from pyrogram import Client, filters
from pymongo import MongoClient
from info import API_ID, API_HASH, BOT_TOKEN, DATABASE_URI, DATABASE_NAME, CHANNELS


# Bot Client
bot = Client(
    "MovieIndexer",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# MongoDB connection
mongo = MongoClient(DATABASE_URI)
db = mongo[DATABASE_NAME]
files_col = db["movies"]  # collection name


@bot.on_message(filters.chat(CHANNELS) & (filters.document | filters.video))
async def index_movies(client, message):
    """
    Automatically index movies from given Telegram channels into MongoDB.
    """
    try:
        file_name = None
        file_id = None
        file_size = None

        if message.document:
            file_name = message.document.file_name
            file_id = message.document.file_id
            file_size = message.document.file_size
        elif message.video:
            file_name = message.video.file_name or "Video File"
            file_id = message.video.file_id
            file_size = message.video.file_size

        if file_id:
            # Avoid duplicates
            if not files_col.find_one({"file_id": file_id}):
                files_col.insert_one({
                    "file_name": file_name,
                    "file_id": file_id,
                    "file_size": file_size,
                    "caption": message.caption or "",
                    "chat_id": message.chat.id,
                    "msg_id": message.id
                })
                print(f"[INDEXED] {file_name}")
            else:
                print(f"[SKIPPED] Already exists - {file_name}")

    except Exception as e:
        print(f"[ERROR] Indexing failed: {e}")


print("📥 Movie Indexer is running... Waiting for new files.")
bot.run()
