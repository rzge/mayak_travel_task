import configparser
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
# Считываем конфиг

config = configparser.ConfigParser()
config.read("config.ini")

API_TOKEN = config['Telegram']['api_token']

# Задаём уровень логгирования
logging.basicConfig(level=logging.INFO)

# Иницализируем бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЭто тестовое задание для Mayak.travel).\nКидай мне файл в формате .xlsx!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)