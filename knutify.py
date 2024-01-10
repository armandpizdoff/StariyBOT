import telebot
import random
import os
import time
import phrases
import psycopg2
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('TOKEN')
PIC = os.getenv('PIC')
CRUEL = os.getenv('CRUEL')
bot = telebot.TeleBot(TOKEN)
DATABASE = os.getenv('DATABASE')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')


def knutirovanie(call):
    if call.data == 'knut':
        markup = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text='Лёгкое⚡', callback_data='junior')
        button2 = telebot.types.InlineKeyboardButton(text='Среднее♿⚡', callback_data='middle')
        button3 = telebot.types.InlineKeyboardButton(text='Старое⚡♿⚡', callback_data='senior')
        button4 = telebot.types.InlineKeyboardButton(text='👨‍🦼👨‍🦼Кнутирование 4-го уровня👨‍🦼👨‍🦼',
                                                     callback_data='senior2')
        button5 = telebot.types.InlineKeyboardButton(text='Обоссывание🚾💦', callback_data='clarify')
        button6 = telebot.types.InlineKeyboardButton(text='Отмена кнутирования', callback_data='back')
        markup.row(button1, button2, button3)
        markup.row(button4)
        markup.row(button5, button6)
        bot.send_message(call.message.chat.id, text='Пожалуйста, выберите тип кнутирования:', reply_markup=markup)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif call.data == 'clarify':
        markup = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text='Да', callback_data='obossali')
        button2 = telebot.types.InlineKeyboardButton(text='Нет', callback_data='mercy')
        markup.row(button1, button2)
        bot.send_message(call.message.chat.id, "Вы что, и в правду хотите обоссать меня, Сэр? ¯\_(ツ)_/¯",
                         reply_markup=markup)
    elif call.data == 'obossali':
        user_id = call.from_user.id
        conn = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
        cursor = conn.cursor()
        with conn:
            cursor.execute('SELECT *FROM knutify_whippers WHERE user_id = %s' % user_id)
            conn.commit()
            if bool(cursor.fetchall()):
                markup = telebot.types.InlineKeyboardMarkup()
                markup.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data='knut'))
                bot.send_message(call.message.chat.id, text='{0.first_name} ({0.last_name} который), '
                                                            'нунинаадааа!'.format(call.from_user, bot.get_me()))
                bot.send_message(call.message.chat.id, 'глолгоглгогл!')
                bot.send_animation(call.message.chat.id,
                                   animation=open(PIC + 'obossal i otstraponil/obossal.gif', 'rb'),
                                   reply_markup=markup)
            else:
                bot.send_message(call.message.chat.id, 'Стоять, дружок-пирожок. Ты не имеешь права меня '
                                                       'обоссывать, пока не заключишь со мной контракт. '
                                                       '\nЧтобы подписать контракт, нажми /whipperreg')
            cursor.close()
            conn.close()
    elif call.data == 'mercy':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data='back'))
        bot.send_message(call.message.chat.id, text=':)')
        time.sleep(1)
        bot.send_message(call.message.chat.id, text='Вы пощадили Старого... на этот раз.')
        time.sleep(1)
        bot.send_message(call.message.chat.id, text=phrases.digital_stariy, reply_markup=markup)
    elif call.data == 'junior':
        user_id = call.from_user.id
        conn = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
        cursor = conn.cursor()
        with conn:
            cursor.execute('SELECT *FROM knutify_whippers WHERE user_id = %s' % user_id)
            conn.commit()
            if bool(cursor.fetchall()):
                bot.send_message(call.message.chat.id, 'Простите, Сэр! Вы не имеете права.')
            else:
                bot.send_message(call.message.chat.id, 'Стоять, дружок-пирожок. Ты не имеешь права меня '
                                                       'кнутировать, пока не заключишь со мной контракт. '
                                                       '\nЧтобы подписать контракт, нажми /whipperreg')
            cursor.close()
            conn.close()
    elif call.data == 'middle':
        user_id = call.from_user.id
        conn = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
        cursor = conn.cursor()
        with conn:
            cursor.execute('SELECT *FROM knutify_whippers WHERE user_id = %s' % user_id)
            conn.commit()
            if bool(cursor.fetchall()):
                bot.send_message(call.message.chat.id, 'Нет, я не дам себя в обиду. Руки! ')
                time.sleep(1)
                bot.send_message(call.message.chat.id, 'А то малява на Ваше имя уже завтра будет в мусарне...')
                time.sleep(2)
                bot.send_message(call.message.chat.id, 'Да, я мусарнусь.')
            else:
                bot.send_message(call.message.chat.id, 'Стоять, дружок-пирожок. Ты не имеешь права меня '
                                                       'кнутировать, пока не заключишь со мной контракт. '
                                                       '\nЧтобы подписать контракт, нажми /whipperreg')
            cursor.close()
            conn.close()
    elif call.data == 'senior':
        user_id = call.from_user.id
        conn = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
        cursor = conn.cursor()
        with conn:
            cursor.execute('SELECT *FROM knutify_whippers WHERE user_id = %s' % user_id)
            conn.commit()
            if bool(cursor.fetchall()):
                markup = telebot.types.InlineKeyboardMarkup()
                markup.add(telebot.types.InlineKeyboardButton(text='Пиздануть ещё раз', callback_data='senior'))
                markup.add(telebot.types.InlineKeyboardButton(text='Главное меню', callback_data='back'))
                rimage = random.choice(os.listdir(CRUEL))
                rscream = random.choice(['Да блять! ', 'АЙ БЛЯТЬ!!! ', 'А-А-А-А!!! ', 'КАЛЕНВАЛ? ', 'ЙОБАНЫЙ ВРОТ! ',
                                         'МОЙ АНАЛ, МОЙ АНАЛ! ', 'НОГА, НОГААА! ', 'Что, опять избиение? ', '*вопли* '])
                rscream2 = random.choice(['*звук адского хлыста* ', 'АЙ БЛЯТЬ, МОИ ЯЙЦА! ', 'ЙОБАНЫЙ ВРОТ! ', '(ооо, даа...) ',
                                          'УХ БЛЯ ', 'Равиолли с сыром, пожалуйста! ', 'СЖАЛЬСЯ, ГАНДОН! ',
                                          'ТОЛЬКО НЕ КАЛЕНВАЛ! ', '*звуки насилия* ', 'кто-нибудь, подберите мои зубы! '])
                rscream3 = random.choice(['*ахегао* ', 'УМОЛЯЮ! ', 'ГЛБГЛБГЛБГЛГЛБ ', 'СЭР! У меня лопатка оторвалась! ',
                                          'ХРЕБЕ-Е-ЕТ!!! ', 'МОЙ ПЕНИС! БОЖЕ! ', 'Пальцевые слайсы?! ', 'А-АЙ, жооопа! ',
                                          'А-А-А-А!!! ', 'Кто-нибудь, подберите мою скальп!!! '])
                bot.send_message(call.message.chat.id, rscream + rscream2)
                time.sleep(1)
                bot.send_message(call.message.chat.id, rscream3)
                bot.send_photo(call.message.chat.id, photo=open(CRUEL + rimage, 'rb'))
                bot.send_message(call.message.chat.id, "МММММММММ!!! ММММММММММММММММММММММ!", reply_markup=markup)
            else:
                bot.send_message(call.message.chat.id, 'Стоять, дружок-пирожок. Ты не имеешь права меня '
                                                       'кнутировать, пока не заключишь со мной контракт. '
                                                       '\nЧтобы подписать контракт, нажми /whipperreg')
            cursor.close()
            conn.close()
    elif call.data == 'senior2':
        user_id = call.from_user.id
        conn = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
        cursor = conn.cursor()
        with conn:
            cursor.execute('SELECT *FROM knutify_whippers WHERE user_id = %s' % user_id)
            conn.commit()
            if bool(cursor.fetchall()):
                markup = telebot.types.InlineKeyboardMarkup()
                markup.add(telebot.types.InlineKeyboardButton(text='Продолжать уродовать выблядка 👨‍🦼',
                                                              callback_data='senior2'))
                markup.add(telebot.types.InlineKeyboardButton(text='Главное меню', callback_data='back'))
                rimage = random.choice(os.listdir(CRUEL))
                rscream = random.choice(['Да блять! ', 'АЙ БЛЯТЬ!!! ', 'А-А-А-А!!! ', 'КАЛЕНВАЛ? ', 'ЙОБАНЫЙ ВРОТ! ',
                                         'МОЙ АНАЛ, МОЙ АНАЛ! ', 'НОГА, НОГААА! ', 'Что, опять избиение? ', '*вопли* ',
                                         'А-АЙ, жооопа! '])
                rscream2 = random.choice(['*звук адского хлыста* ', 'АЙ БЛЯТЬ, МОИ ЯЙЦА! ', 'ЙОБАНЫЙ ВРОТ! ', '(ооо, даа...) ',
                                          'УХ БЛЯ ', 'ПОЖАЛУЙСТА!! ', 'СЖАЛЬСЯ, ГАНДОН! ', 'ТОЛЬКО НЕ КАЛЕНВАЛ! ',
                                          '*звуки насилия* ', 'кто-нибудь, подберите мои зубы! ',
                                          'Только не равиолли с сыром в анал! ТОЛЬКО НЕ РАВИОЛЛИ С СЫРОМ В АНАЛ! НЕЕЕЕЕЕАТ! '])
                rscream3 = random.choice(['*слёзы* ', '*ахегао* ', 'УМОЛЯЮ! ', 'ГЛБГЛБГЛБГЛГЛБ ', 'ХРЕБЕ-Е-ЕТ!!! ',
                                          'МОЙ ПЕНИС! БОЖЕ! ', 'Пальцевые слайсы?! ', 'А-АЙ, жооопа! ',
                                          'А-А-А-А!!! ', 'СЭР! У меня лопатка оторвалась! ',
                                          'Кто-нибудь, подберите мою скальп!!! '])
                rscream4 = random.choice(['АРХГХРХХХХ ', 'СЭР! ОНО НЕ ВЛЕЗАЕТ МНЕ В АНАЛ! ',
                                          'КНУТ РАССЁК МОЁ ПРАВОЕ ЯИЦО! ААА! ', 'Нет, я не носил парик! Моя Скальп!!! '])
                bot.send_message(call.message.chat.id, 'О, нет, Господин {0.first_name}, СЖАЛЬТЕСЬ! Только не снова! '
                                                       '\nОЙ! Остановитесь! Умоляю, не нужно!'
                                 .format(call.from_user, bot.get_me()))
                time.sleep(2)
                bot.send_photo(call.message.chat.id, photo=open(CRUEL + rimage, 'rb'))
                time.sleep(2)
                bot.send_message(call.message.chat.id, rscream2 + rscream)
                time.sleep(2)
                bot.send_message(call.message.chat.id, rscream4 + rscream3)
                time.sleep(2)
                bot.send_message(call.message.chat.id, 'ААААЙ!')
                time.sleep(2)
                rimage2 = random.choice(os.listdir(CRUEL))
                bot.send_photo(call.message.chat.id, photo=open(CRUEL + rimage2, 'rb'))
                bot.send_message(call.message.chat.id, "МММММММММ!!! ММММММММММММММММММММММ!", reply_markup=markup)
            else:
                bot.send_message(call.message.chat.id, 'Стоять, дружок-пирожок. Ты не имеешь права меня '
                                                       'кнутировать, пока не заключишь со мной контракт. '
                                                       '\nЧтобы подписать контракт, нажми /whipperreg')
            cursor.close()
            conn.close()
