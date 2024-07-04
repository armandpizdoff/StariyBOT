import telebot
import random
import time
import os
from dotenv import load_dotenv
import phrases

bot = telebot.TeleBot('5923409986:AAGh_or9NPf2wv_2DqI7BksTH3T2WMf9DQA')
load_dotenv()
MUSIC = os.getenv('MUSIC')
SOUND = os.getenv('SOUND')
CRUEL = os.getenv('CRUEL')
PIC = os.getenv('PIC')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'музыка':
        cataloglist = random.choice(os.listdir(MUSIC)) + '/'
        directory = MUSIC + cataloglist
        audio = random.choice(os.listdir(directory))
        bot.send_chat_action(message.chat.id, 'upload_audio')
        bot.send_audio(message.chat.id, audio=open(directory + audio, 'rb'))
    elif message.text == 'привет':
        bot.send_message(message.chat.id, 'Всем привет! Я Игнат')
    elif message.text == 'покажи Путина':
        bot.send_message(message.chat.id, 'Будет исполнено...')
        time.sleep(2)
        bot.send_chat_action(message.chat.id, 'upload_audio')
        bot.send_animation(message.chat.id, animation=open(PIC + 'putin.mp4', "rb"))
        bot.send_audio(message.chat.id, audio=open(SOUND + 'song for denise.mp3', "rb"))
    elif message.text == 'шоколад в жопе':
        bot.send_message(message.chat.id, '😉😉😉')
        time.sleep(3)
        bot.send_photo(message.chat.id, photo=open(PIC + 'vertlib.jpg', 'rb'))
    elif message.text == 'if he dies':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Отомстить Старому за Апполо Крида...',
                                                      callback_data='senior2'))
        bot.send_message(message.chat.id, '... he dies.', reply_markup=markup)
    elif message.text == 'скрытое отхлищивание...':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Продолжать уродовать выблядка 👨‍🦼',
                                                      callback_data='senior2'))
        markup.add(telebot.types.InlineKeyboardButton(text='Главное меню', callback_data='back'))
        rimage = random.choice(os.listdir(CRUEL))
        rscream = random.choice(['Да блять! ', 'АЙ БЛЯТЬ!!! ', 'А-А-А-А!!! ', 'КАЛЕНВАЛ? ', 'ЙОБАНЫЙ ВРОТ! ',
                                 'МОЙ АНАЛ, МОЙ АНАЛ! ', 'НОГА, НОГААА! ', 'Что, опять избиение? ', '*вопли* '])
        rscream2 = random.choice(['*звук адского хлыста* ', 'АЙ БЛЯТЬ, МОИ ЯЙЦА! ', 'ЙОБАНЫЙ ВРОТ! ', '(ооо, даа...) ',
                                  'УХ БЛЯ ', 'ПОЖАЛУЙСТА!! ', 'СЖАЛЬСЯ, ГАНДОН! ', 'ТОЛЬКО НЕ КАЛЕНВАЛ! ',
                                  '*звуки насилия* ', 'кто-нибудь, подберите мои зубы! ',
                                  'Только не равиолли с сыром в анал! ТОЛЬКО НЕ РАВИОЛЛИ С СЫРОМ В АНАЛ! НЕЕЕЕЕЕАТ! '])
        rscream3 = random.choice(['*ахегао* ', 'УМОЛЯЮ! ', 'ГЛБГЛБГЛБГЛГЛБ ', 'СЭР! У меня лопатка оторвалась! ',
                                  'ХРЕБЕ-Е-ЕТ!!! ', 'МОЙ ПЕНИС! БОЖЕ! ', 'Пальцевые слайсы?! ', 'А-АЙ, жооопа! ',
                                  'А-А-А-А!!! ', 'Кто-нибудь, подберите мою скальп!!! '])
        rscream4 = random.choice(['АРХГХРХХХХ ', 'СЭР! ОНО НЕ ВЛЕЗАЕТ МНЕ В АНАЛ! ',
                                  'КНУТ РАССЁК МОЁ ПРАВОЕ ЯИЦО! ААА! ', 'Нет, я не носил парик! Моя Скальп!!! '])
        bot.send_message(message.chat.id, 'О, нет, Господин {0.first_name}, так нечестно! Мы же договаривались! '
                                          '\nОЙ! Остановитесь! Умоляю, не нужно!'
                         .format(message.from_user, bot.get_me()))
        time.sleep(2)
        bot.send_photo(message.chat.id, photo=open(CRUEL + rimage, 'rb'))
        time.sleep(2)
        bot.send_message(message.chat.id, rscream2 + rscream)
        time.sleep(2)
        bot.send_message(message.chat.id, rscream4 + rscream3)
        time.sleep(2)
        bot.send_message(message.chat.id, 'ААААЙ!')
        time.sleep(2)
        rimage2 = random.choice(os.listdir(CRUEL))
        bot.send_photo(message.chat.id, photo=open(CRUEL + rimage2, 'rb'))
        bot.send_message(message.chat.id, 'МММММММММ!!! ММММММММММММММММММММММ!', reply_markup=markup)
    elif message.text == 'ты лох':
        bot.send_message(chat_id='-1001892218052', text='Запомните, твари: Я не сломаюсь..nahui')
    elif message.text == 'ты лох2':
        bot.send_message(chat_id='-1001892218052', text='<b>Давтян не дежурный, ошибка системы/b>')
    elif message.text == 'Похвалить Старого!':
        bot.send_message(message.chat.id, text=phrases.digital_stariy)
