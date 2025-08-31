from pyrogram import Client, filters
from info import API_ID, API_HASH, BOT_TOKEN

print("🤖 Bot.py is starting...")

app = Client(
    "MovieBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text("Hello 👋, I’m your Movie Bot! Send me a movie name.")

print("✅ Movie Bot is running...")

app.run()
