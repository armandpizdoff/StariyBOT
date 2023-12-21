import telebot
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
DATABASE = os.getenv('DATABASE')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
bot = telebot.TeleBot('TOKEN')


class DatBase:
    def __init__(self, knutify_whippers):
        conn = psycopg2.connect(database=DATABASE,
                                user=USER,
                                password=PASSWORD,
                                host=HOST,
                                port=PORT)
        cursor = conn.cursor()

    def register(message):
        # Получение информации о пользователе
        user_id = message.from_user.id
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        # Запись информации о пользователе в базу данных
        query = f"INSERT INTO users (user_id, first_name, last_name) VALUES ({user_id}, '{first_name}', '{last_name}')"
        cursor.execute(query)
        conn.commit()
        # Отправка ответа
        bot.reply_to(message, "Вы подписали контракт на кнутирование Старого. Поздравляем!")

# class DatBase:
#     def __init__(self, knutify_whippers):
#         # подключение к базе данных
#         self.connection = psycopg2.connect(database='DATABASE',
#                                            user='USER',
#                                            password='PASSWORD',
#                                            host='HOST',
#                                            port='PORT')
#         self.cursor = self.connection.cursor()



# def register(message):
#     # Получение информации о пользователе
#     user_id = message.from_user.id
#     first_name = message.from_user.first_name
#     last_name = message.from_user.last_name
#
#     # Запись информации о пользователе в базу данных
#     query = f"INSERT INTO users (user_id, first_name, last_name) VALUES ({user_id}, '{first_name}', '{last_name}')"
#     cursor.execute(query)
#     conn.commit()
#
#     # Отправка ответа
#     bot.reply_to(message, "Вы подписали контракт на кнутирование Старого. Поздравляем!")

# регистрация хлестателя
#    def add_whipper(self, user_id):
#        with self.connection:
#            self.data = data
#            query = "INSERT INTO knutify_whippers (user_id, first_name, second_name) VALUES (%s, %s, %s)"
#            self.cursor.executemany(query, [data])
#            self.connection.commit()


# проверка зарегистрирован ли хлестатель в базе
# def check_whipper(self, user_id):
#     self.user_id = user_id
#     with self.connection:
#         self.cursor.execute("SELECT *FROM viewer WHERE user_id = %s" % user_id)
#         self.connection.commit()
#         return bool(self.cursor.fetchall())
#
#
# # удаление хлестателя из базы
# def remove_whipper(self, user_id):
#     self.user_id = user_id
#     with self.connection:
#         self.cursor.execute("DELETE FROM viewer WHERE user_id = %s" % user_id)
#         self.connection.commit()


# Обработчик нажатия на кнопку
# @bot.callback_query_handler(func=lambda call: True)
# def whipper_count(call):
#     # Получение информации о пользователе
#     user_id = call.from_user.id
#
#     # Получение текущего значения счётчика пользователя
#     query = f"SELECT whipper_count FROM users WHERE user_id={user_id}"
#     cursor.execute(query)
#     count = cursor.fetchone()[0]
#
#     # Увеличение счётчика и обновление значения в базе данных
#     count += 1
#     query = f"UPDATE users SET whipper_count={count} WHERE user_id={user_id}"
#     cursor.execute(query)
#     conn.commit()

#    # Отправка ответа с обновлённым счётчиком
#    bot.send_message(call.message.chat.id, f"Количество нажатий: {count}")
