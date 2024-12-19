import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS CollectorEngine (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type INT NOT NULL,
    Pnom REAL NOT NULL,
    Mnom REAL NOT NULL,
    nnom REAL NOT null,
    Unom REAL NOT NULL,
    Inom REAL NOT NULL,
    R REAL NOT NULL,
    J REAL NOT NULL,
    m REAL NOT NULL,
    Price REAL NOT NULL,
    Plan BLOB
)
''')

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()
