import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE = os.getenv('DATABASE')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')


class DatBase:

    def __init__(self):
        # подключение к базе данных
        self.connection = psycopg2.connect(database='DATABASE',
                                           user='USER',
                                           password='PASSWORD',
                                           host='HOST',
                                           port='PORT')
        self.cursor = self.connection.cursor()

    # регистрация хлестателя
    def add_whipper(self, 'DATABASE'):
        with self.connection:
            self.data = data
            query = "INSERT INTO knutify_whippers (user_id, first_name, second_name) VALUES (%s, %s, %s)"
            self.cursor.executemany(query, [data])
            self.connection.commit()

    # проверка зарегистрирован ли хлестатель в базе
    def check_whipper(self, user_id):
        self.user_id = user_id
        with self.connection:
            self.cursor.execute("SELECT *FROM viewer WHERE user_id = %s" % user_id)
            self.connection.commit()
            return bool(self.cursor.fetchall())

    # удаление хлестателя из базы
    def remove_whipper(self, user_id):
        self.user_id = user_id
        with self.connection:
            self.cursor.execute("DELETE FROM viewer WHERE user_id = %s" % user_id)
            self.connection.commit()
