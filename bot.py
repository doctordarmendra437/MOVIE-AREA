from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pymongo import MongoClient
from info import API_ID, API_HASH, BOT_TOKEN, DATABASE_URI, DATABASE_NAME, OWNER_USERNAME, SUPPORT_CHAT, MOVIE_GROUP_LINK
from utils import shorten_url


# Bot client
bot = Client(
    "MovieBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# MongoDB connection
mongo = MongoClient(DATABASE_URI)
db = mongo[DATABASE_NAME]
files_col = db["movies"]  # collection name


@bot.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text(
        f"👋 Hello {message.from_user.mention}!\n\n"
        "I am your Movie Bot 🎬\n\n"
        "🔎 Send me the name of any movie and I’ll fetch it for you with links.",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("📢 Updates", url=MOVIE_GROUP_LINK),
                InlineKeyboardButton("👨‍💻 Owner", url=f"https://t.me/{OWNER_USERNAME}")
            ],
            [
                InlineKeyboardButton("💬 Support", url=SUPPORT_CHAT)
            ]]
        )
    )


@bot.on_message(filters.text & ~filters.command(["start"]))
async def search_movie(client, message):
    query = message.text.strip()

    if len(query) < 3:
        return await message.reply_text("⚠️ Please enter at least 3 characters to search.")

    results = files_col.find({"file_name": {"$regex": query, "$options": "i"}}).limit(10)

    if results.count() == 0:
        return await message.reply_text("❌ No movies found, try another name.")

    buttons = []
    text = f"🔎 Results for: **{query}**\n\n"

    for file in results:
        file_name = file.get("file_name", "Unknown File")
        chat_id = file.get("chat_id")
        msg_id = file.get("msg_id")

        if chat_id and msg_id:
            # Telegram message link
            movie_link = f"https://t.me/c/{str(chat_id)[4:]}/{msg_id}"
            short_link = shorten_url(movie_link)

            buttons.append([InlineKeyboardButton(file_name[:50], url=short_link)])

    reply_markup = InlineKeyboardMarkup(buttons)

    await message.reply_text(
        text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


print("🤖 Movie Bot is running...")
bot.run()
