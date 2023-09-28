import sqlite3

# Устанавливаем соединение с базой данных
import pandas as pd

connection = sqlite3.connect('product_info.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Информация (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
site TEXT NOT NULL,
price REAL
)
''')

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()

# слой вызова асинхронных функций, работающие с асинхронным драйвером БД
import aiosqlite


async def save_to_db(excel_info: pd.DataFrame):
    excel_info = excel_info.reset_index()
    info_to_db = []
    for index, row in excel_info.iterrows():
        info_to_db.append((row['Товар'], row['Сайт'], row['Цена']))
    async with aiosqlite.connect('product_info.db') as db:
        await db.executemany('INSERT INTO Информация (name, site, price) VALUES (?, ?, ?)',
                             info_to_db)
        await db.commit()


async def average_price():
    async with aiosqlite.connect('product_info.db') as db:
        results = await db.execute_fetchall('SELECT site, AVG(price) AS avg_price FROM Информация GROUP BY site')
        avg_prices = []
        for row in results:
            site = row[0]
            avg_price = row[1]
            avg_prices.append(f"{site}: {avg_price}")
        return avg_prices