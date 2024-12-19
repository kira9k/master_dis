import sqlite3


class DBHelper:
    """Класс для доп функций для базы данных"""
    DATABASE_NAME = "my_database.db"

    @staticmethod
    def get_connection():
        """Возвращает соединение с базой данных."""
        return sqlite3.connect(DBHelper.DATABASE_NAME)

    @staticmethod
    def get_columns(table_name, without_first=False):
        """Получает таблицу с данными из БД"""
        with DBHelper.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({table_name});")
            if without_first:
                columns = [col[1] for col in cursor.fetchall() if col[1] != "id"]
            else:
                columns = [col[1] for col in cursor.fetchall()]
        return columns
