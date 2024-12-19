import sqlite3
import pandas as pd

from DBHelper import DBHelper
from working_with_database import DataBase


class DBShow:
    """Класс для отображения базы данных"""

    @staticmethod
    def print_pretty_table():
        """Выводит всю БД"""
        try:
            with DBHelper.get_connection() as conn:
                cursor = conn.cursor()

                cursor.execute("PRAGMA table_info(CollectorEngine)")
                columns = DBHelper.get_columns(DataBase.TABLE_NAME, without_first=False)
                data = list(cursor.execute("SELECT * FROM CollectorEngine"))
                df = pd.DataFrame(data, columns=columns)

                if df.empty:
                    print("База данных пустая")
                else:
                    print(df)

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)

    @staticmethod
    def show_columns_name():
        """Выводит список колонок таблицы."""
        try:
            columns = DBHelper.get_columns(DataBase.TABLE_NAME)
            print("Колонки таблицы:", columns)
        except sqlite3.Error as error:
            print("Ошибка при получении колонок:", error)

    @staticmethod
    def show_chosen_records(column):
        """Выводит выбранную колонку с именем"""
        try:
            with DBHelper.get_connection() as conn:
                cursos = conn.cursor()
                cursos.execute(f"SELECT name, {(column)} FROM {DataBase.TABLE_NAME}")
                massive = cursos.fetchall()
                columns = ['name', column]
                df = pd.DataFrame(massive, columns=columns)
                print(df)

        except sqlite3.Error as Error:
            print("Ошибка при отображении выбранных колнок:", Error)

#DBShow.print_pretty_table()
#DBShow.show_columns_name()
DBShow.show_chosen_records('Pnom')
