import configparser
import logging
import pandas as pd
import database

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

# Директория для загрузки приходящих файлов от пользователя
directory_path_to_file = os.path.dirname(os.path.realpath(__file__)) + '\\documents'


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
async def greeting(message: types.Message):
    await message.reply("Привет!\nЭто тестовое задание для Mayak.travel).\nКидай мне файл в формате .xlsx!")


@dp.message_handler(content_types=['document'])
async def handle_file(message: types.Message):
    """
    Загружает приходящий файл в /documents и выводит содержимое пользователю

    :param message:
    :return:
    """
    await message.document.download(directory_path_to_file+f'\\{message.document.file_name}')
    df = pd.read_excel(directory_path_to_file+f'\\{message.document.file_name}')
    await message.reply((str(df)))
    await database.save_to_db(df)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)