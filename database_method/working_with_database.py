import sqlite3
import pandas as pd

from charachteristics_collector_engine import engine
from DBHelper import DBHelper


class DataBase:
    TABLE_NAME = "CollectorEngine"

    @staticmethod
    def load_to_database(record):
        """Вставляет одну запись в таблицу."""
        try:
            with DBHelper.get_connection() as conn:
                cursor = conn.cursor()
                columns = DBHelper.get_columns(DataBase.TABLE_NAME, without_first=True)
                columns_str = ", ".join(columns)
                placeholders = ", ".join(["?"] * len(columns))
                cursor.execute(f"SELECT COUNT(*) FROM {DataBase.TABLE_NAME} WHERE name = ?", (record[0],))
                if cursor.fetchone()[0] == 0:
                    query = f"INSERT INTO {DataBase.TABLE_NAME} ({columns_str}) VALUES ({placeholders})"
                    cursor.execute(query, record)
                print("Записи успешно добавлены.")
                conn.commit()
        except sqlite3.Error as error:
            print("Ошибка при вставке записей:", error)

    @staticmethod
    def delete_record(delete_name):
        """Удаляет запись из таблицы по имени."""
        try:
            with DBHelper.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(f"DELETE FROM {DataBase.TABLE_NAME} WHERE name = ?", (delete_name,))
                print("Запись успешно удалена.")
        except sqlite3.Error as error:
            print("Ошибка при удалении записи:", error)

    @staticmethod
    def insert_multiple_records(records):
        """Вставляет несколько записей в таблицу."""
        try:
            with DBHelper.get_connection() as conn:
                cursor = conn.cursor()
                columns = DBHelper.get_columns(DataBase.TABLE_NAME, without_first=True)
                columns_str = ", ".join(columns)
                placeholders = ", ".join(["?"] * len(columns))
                for record in records:
                    cursor.execute(f"SELECT COUNT(*) FROM {DataBase.TABLE_NAME} WHERE name = ?", (record[0],))
                    if cursor.fetchone()[0] == 0:
                        query = f"INSERT INTO {DataBase.TABLE_NAME} ({columns_str}) VALUES ({placeholders})"
                        cursor.execute(query, record)
                #cursor.executemany(query, records)
                print("Записи успешно добавлены.")
                conn.commit()
        except sqlite3.Error as error:
            print("Ошибка при вставке записей:", error)

    @staticmethod
    def clear_database():
        """Очистка базы данных"""
        try:
            with DBHelper.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM CollectorEngine;")
                conn.commit()
                print("Все записи были успешно удалены.")

        except sqlite3.Error as error:
            print("Ошибка при очистки базы данных:", error)

#DataBase.insert_multiple_records(engine)
#DataBase.load_to_database(engine[1])
#DataBase.delete_record("Constar 0615N5M 01-122-3.0")
#DataBase.clear_database()
