import telebot
import psycopg2

# Создание соединения с базой данных
conn = psycopg2.connect(database="your_database", user="your_user",
                        password="your_password", host="your_host", port="your_port")
cursor = conn.cursor()

# Создание экземпляра бота
bot = telebot.TeleBot("YOUR_TELEGRAM_TOKEN")


# Обработчик команды /register
@bot.message_handler(commands=['register'])
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
    bot.reply_to(message, "Вы успешно зарегистрированы!")


# Обработчик нажатия на кнопку
@bot.callback_query_handler(func=lambda call: True)
def button_click(call):
    # Получение информации о пользователе
    user_id = call.from_user.id

    # Получение текущего значения счётчика пользователя
    query = f"SELECT button_click_count FROM users WHERE user_id={user_id}"
    cursor.execute(query)
    count = cursor.fetchone()[0]

    # Увеличение счётчика и обновление значения в базе данных
    count += 1
    query = f"UPDATE users SET button_click_count={count} WHERE user_id={user_id}"
    cursor.execute(query)
    conn.commit()

    # Отправка ответа с обновлённым счётчиком
    bot.send_message(call.message.chat.id, f"Количество нажатий: {count}")


# Запуск бота
bot.polling()

Обрати внимание, что в этом коде использованы фиктивные значения для подключения к базе данных:
your_database, your_user, your_password, your_host и your_port. Замени их на реальные значения своей базы
данных PostgreSQL. Также обязательно создай таблицу users со столбцами user_id, first_name, last_name и
button_click_count в базе данных.
После того, как ты запустишь бота, он будет регистрировать пользователей при команде /register
и считать количество нажатий на кнопку для каждого пользователя отдельно.