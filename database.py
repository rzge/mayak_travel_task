import sqlite3

# Устанавливаем соединение с базой данных
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