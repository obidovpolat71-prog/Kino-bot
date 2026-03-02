import logging
from aiogram import Bot, Dispatcher, executor, types
import os

#8791005886:AAEIz0JJX-AHKWW_Jsz62Ij6Znfrpjaj2wA
API_TOKEN = os.getenv("API_TOKEN")  # Keyin hostingda secret orqali ishlatamiz

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# /start komandasi
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("🎬 Kino bot ishlayapti! Kino kodini yuboring.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
