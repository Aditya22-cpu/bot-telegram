import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from flask import Flask, request

TOKEN = "1234567890:ABCDEF1234567890abcdef1234567890"  # Ganti dengan token bot kamu
WEBHOOK_URL = "https://your-repl.repl.co/webhook"  # Ganti dengan URL Replit nanti

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Logging untuk debugging
logging.basicConfig(level=logging.INFO)

# Perintah /start
@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    await message.answer("🚀 Selamat datang di Bot Marketing Freebet! Ketik /klaim untuk mendapatkan bonus.")

# Perintah /klaim
@dp.message_handler(commands=['klaim'])
async def klaim_freebet(message: Message):
    user_id = message.from_user.id
    await message.answer(f"🔍 Sedang memproses klaim Anda...\nSilakan buka link ini untuk verifikasi: https://your-repl.repl.co/klaim?user_id={user_id}")

# Webhook Flask
app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.json
    asyncio.run(dp.process_update(types.Update(**update)))
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
