import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from flask import Flask, request

TOKEN = "7922842008:AAHOchyo_fiOhaq1-7D1Ud7HSKn2rEvp6mA"  # Ganti dengan token bot kamu
WEBHOOK_URL = WEBHOOK_URL = "https://yourdomain.com/webhook"  # Ganti dengan URL Webhook (nanti kita buat)

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
    await message.answer(f"🔍 Sedang memproses klaim Anda...\nSilakan buka link ini untuk verifikasi: https://yourdomain.com/klaim?user_id={user_id}")

# Jalankan bot dengan Webhook
app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.json
    asyncio.run(dp.process_update(types.Update(**update)))
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
