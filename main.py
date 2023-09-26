import telebot
import random
import os
import time

import audiobooks
import knutify
import textcommand
import jokes

# import logging
from dotenv import load_dotenv

# import xlrd
# from bs4 import BeautifulSoup

# from datetime import datetime, timedelta
# import requests - для парсинга шуток с сайтов
# from bs4 import BeautifulSoup - для парсинга данных с сайтов

load_dotenv()
TOKEN = os.getenv('TOKEN')
BASE_PATH = os.getenv('BASE_PATH')
SOUND = os.getenv('SOUND')
STORIES = os.getenv('STORIES')
MUSIC = os.getenv('MUSIC')
RETRO = os.getenv('RETRO')
ROCK = os.getenv('ROCK')
RAP = os.getenv('RAP')
OTHER = os.getenv('OTHER')
PIC = os.getenv('PIC')
CRUEL = os.getenv('CRUEL')
ANIME_CHAN = os.getenv('ANIME_CHAN')
COW = os.getenv('COW')
LAUGH_NIGER = os.getenv('LAUGH_NIGER')
DJO = os.getenv('DJO')
MURLOK = os.getenv('MURLOK')
COMICS = os.getenv('COMICS')
MILLENNIUM = os.getenv('MILLENNIUM')

bot = telebot.TeleBot(TOKEN)
# logging.debug("A DEBUG Message")
# logging.info("An INFO")
# logging.warning("A WARNING")
# logging.error("An ERROR")
# logging.critical("A message of CRITICAL severity")


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, text='*Список быстрых команд:* '
                                           '\n/start - получить спектр услуг. '
                                           '\n/help - засуммонить помощь. '
                                           '\n/music - сделать меня томадой. '
                                           '\n/armandhelper - пельменная Виктора Чипотловича. '
                                           '\n\n*Список печатных команд:* '
                                           '\nкнут - пожалуйста не надо, Господин {0.first_name}! '
                                           '\nмузыка - сделайте меня томадой, мистер {0.first_name}. '
                                           '\nпокажи Путина - чтобы я привёл Вам перзидента Роисии. '
                                           '\nскрытое отхлищивание... - кнутирование 4-го уровня. '
                                           '\n\nЕсли вводите команду вручную - '
                                           'соблюдайте регистр. '.format(message.from_user, bot.get_me()),
                     parse_mode='markdown')


@bot.message_handler(commands=['armandhelper'])
def armandhelper(message):
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text='Python', callback_data='python')
    button2 = telebot.types.InlineKeyboardButton(text='Ubuntu', callback_data='ubuntu')
    button3 = telebot.types.InlineKeyboardButton(text='GIT', callback_data='git')
    button4 = telebot.types.InlineKeyboardButton(text='Telegram', callback_data='telegram')
    button5 = telebot.types.InlineKeyboardButton(text='Django', callback_data='django')
    markup.row(button1, button2, button3, button4, button5)
    bot.send_message(message.chat.id, text='<s>Пельменная</s> Справочная "<b>Старый+</b>". Чем вам помочь?',
                     parse_mode='HTML', reply_markup=markup)


@bot.message_handler(commands=['id_chat'])
def armandhelper(message):
    bot.send_message(message.chat.id, text=message.chat.id)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text='Команды', callback_data='main menu')
    button2 = telebot.types.InlineKeyboardButton(text='Музыка🎵', callback_data='music')
    button3 = telebot.types.InlineKeyboardButton(text='Кнут', callback_data='knut')
    button4 = telebot.types.InlineKeyboardButton(text='Anime-chan🧏🏻‍♀', callback_data='animechan')
    button5 = telebot.types.InlineKeyboardButton(text='Рабочий график', callback_data='grafik')
    button6 = telebot.types.InlineKeyboardButton(text='WEB-Старый (в разработке)', url='http://onlynotcrankshaft.ru')
    button7 = telebot.types.InlineKeyboardButton(text='Закрыть🚫', callback_data='cancel')
    markup.row(button1, button2)
    markup.row(button3, button4, button5)
    markup.row(button6)
    markup.row(button7)
    bot.send_message(message.chat.id, text='*Здравствуйте, Космический Директор Архангел {0.first_name}!'
                                           '\nЯ ваш блядский дворецкий Старый (@_@)* '
                                           '\nЯ очень не люблю круговое обоссывание. '
                                           '\nЧтобы использовать меня в своих личных целях, '
                                           'выберите интересующий раздел меню'.format(message.from_user, bot.get_me()),
                     parse_mode='markdown', reply_markup=markup)
# .format(message.chat.id)


@bot.message_handler(commands=['play'])
def fk(message, where_call=None):
    if where_call is None:
        global number
        number = random.randint(1, 30)
        msg = bot.send_message(message.chat.id, 'Сэр! Я придумал игру! Сможете ли вы с 6 попыток угадать число '
                                                'между 1 и 30? Если не боитесь - введите первое число.'
                                                '\nЕсли угадаете, то я позволю вам отхлищеть меня... '
                                                'Но если выиграю я...'
                                                '\nУАХАХАХАХ! КНУТИРОВАТЬ БУДУ Я! НАКОНЕЦ-ТО ХОТЬ КАКАЯ-ТО ВЛАСТЬ! '
                                                'Хе-хе-хе!')
        attempt = 1
        bot.register_next_step_handler(msg, lambda message: random_number(message, attempt))
    elif where_call == 'not_digit':
        msg = bot.send_message(message.chat.id, 'Сэр! Там только числа!')
        attempt = 1
        bot.register_next_step_handler(msg, lambda message: random_number(message, attempt))


def random_number(message, attempt):
    if message.text.isdigit():
        n = int(message.text)
        if attempt <= 6:
            attempt += 1
            if n < number:
                msg = bot.send_message(message.chat.id, 'Нет, загаданное число больше!')
                bot.register_next_step_handler(msg, lambda message: random_number(message, attempt))
            elif n > number:
                msg = bot.send_message(message.chat.id, 'Нет! Это слишком много!')
                bot.register_next_step_handler(msg, lambda message: random_number(message, attempt))
            else:
                markup = telebot.types.InlineKeyboardMarkup()
                markup.add(telebot.types.InlineKeyboardButton(text='Кнут.', callback_data='senior'))
                markup.add(telebot.types.InlineKeyboardButton(text='Простить выблядка', callback_data='mercy'))
                bot.send_message(message.chat.id, 'Ой... нееет... Сэр... вы угадали... с {} попытки! '
                                                  '\nПожаааалуйста... Пожалейте меня! Вы ведь пожалеете, да? ;)'
                                 .format(attempt - 1), reply_markup=markup)
        else:
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton(text='Подчиниться Старому...', callback_data='earlystop'))
            markup.add(telebot.types.InlineKeyboardButton(text='Отхлищеть Старого до полусмерти.',
                                                          callback_data='senior2'))
            bot.send_message(message.chat.id, 'ХАААА! ПОПЫТКИ ЗАКОНЧИЛИСЬ! Загаданное число было {0}! '
                             .format(number))
            time.sleep(2)
            bot.send_message(message.chat.id, 'РАССТЁГИВАЙ ШТАНИШКИ {0.first_name}ша-стесняша! '
                                              '\nВОТ СЕЙЧАС-ТО Я ОТЫГРАЮСЬ. НАКОНЕЦ-ТО. УЕБУ КАК СЛЕДУЕТ!!! '
                                              '\nУраааа!'.format(message.from_user, bot.get_me()), reply_markup=markup)
    else:
        fk(message, where_call='not_digit')


@bot.message_handler(commands=['carousel'])
def carouselwishes1(message):
    msg = bot.send_message(message.chat.id, 'Сэр! Я помогу вам принять решение в спорных ситуациях! '
                                            '\nС моей помощью вы сможете как выбрать себе ресторан на обед, '
                                            'так и игру на вечер!'
                                            '\nВведите первый вариант:')
    bot.register_next_step_handler(msg, lambda message: carouselwishes2(message))


def carouselwishes2(message):
    if message.text != 'Готово':
        global opt1
        opt1 = str(message.text)
        msg = bot.send_message(message.chat.id, 'Принято. Записал вариант - *{}*. Введите второй вариант, либо '
                                                'напишите "Готово"'.format(opt1), parse_mode='markdown')
        bot.register_next_step_handler(msg, lambda message: carouselwishes3(message))
    else:
        bot.send_message(message.chat.id, 'ты даун?)')


def carouselwishes3(message):
    if message.text != 'Готово':
        global opt2
        opt2 = str(message.text)
        msg = bot.send_message(message.chat.id, 'Принято. Записал второй вариант - *{}*. '
                                                '\nВведите следующий вариант, либо напишите "Готово"'.format(opt2),
                               parse_mode='markdown')
        bot.register_next_step_handler(msg, lambda message: carouselwishes4(message))
    else:
        bot.send_message(message.chat.id, 'ты даун?)')


def carouselwishes4(message):
    if message.text != 'Готово':
        global opt3
        opt3 = str(message.text)
        msg = bot.send_message(message.chat.id, 'Принято. Записал третий вариант - *{}*.'
                                                '\nНапишите "Готово" (С БОЛЬШОЙ БУКВЫ!)'.format(opt3),
                               parse_mode='markdown')
        bot.register_next_step_handler(msg, lambda message: choosewishes(message))
    else:
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Поблагодарить Старого', url='https://boosty.to/armand_pzd'))
        markup.add(telebot.types.InlineKeyboardButton(text='Отхлищеть Старого до полусмерти.', callback_data='senior2'))
        markup.add(telebot.types.InlineKeyboardButton(text='Повторить карусель желаний',
                                                      callback_data='carouselwishes'))
        thing = random.choice([opt1, opt2])
        bot.send_message(message.chat.id, 'Итак, Господин, сегодня ваш выбор - *{}*!'.format(thing),
                         parse_mode='markdown', reply_markup=markup)


def choosewishes(message):
    if message.text == 'Готово':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Поблагодарить Старого', url='https://boosty.to/armand_pzd'))
        markup.add(telebot.types.InlineKeyboardButton(text='Отхлищеть Старого до полусмерти.', callback_data='senior2'))
        markup.add(telebot.types.InlineKeyboardButton(text='Повторить карусель желаний',
                                                      callback_data='carouselwishes'))
        thing = random.choice([opt1, opt2, opt3])
        bot.send_message(message.chat.id, 'Итак, Господин, сегодня ваш выбор - *{}*!'.format(thing),
                         parse_mode='markdown', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'ты даун?) \nНадо было написать "Готово!". '
                                          '\nТеперь запускай карусель заново. Мраз')


@bot.message_handler(commands=['music'])
def music(message):
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text='Ещё песню!', callback_data='randomsong')
    button2 = telebot.types.InlineKeyboardButton(text='Не понравилось. Ёбнуть Старого.', callback_data='senior')
    button3 = telebot.types.InlineKeyboardButton(text='Выбрать жанр', callback_data='music')
    markup.row(button1, button3)
    markup.row(button2)
    cataloglist = random.choice(os.listdir(MUSIC)) + '/'
    directory = MUSIC + cataloglist
    audio = random.choice(os.listdir(directory))
    bot.send_chat_action(message.chat.id, 'upload_audio')
    bot.send_audio(message.chat.id, audio=open(directory + audio, 'rb'), reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id)
    if call.data == 'main menu':
        markup = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text='Всратые звуки❗', callback_data='sounds')
        button2 = telebot.types.InlineKeyboardButton(text='Карусель Желаний', callback_data='carouselwishes')
        button3 = telebot.types.InlineKeyboardButton(text='Рубрика "Весёлые Нигеры"', callback_data='carouselniggers')
        button4 = telebot.types.InlineKeyboardButton(text='Различные рассказики', callback_data='stories')
        button5 = telebot.types.InlineKeyboardButton(text='Сочные тёлки🐄', callback_data='cow')
        button6 = telebot.types.InlineKeyboardButton(text='Юмор', callback_data='joke')
        button7 = telebot.types.InlineKeyboardButton(text='Игры🎮', callback_data='game')
        button8 = telebot.types.InlineKeyboardButton(text='TV📺', url='https://www.glaz.tv/online-tv/')
        button9 = telebot.types.InlineKeyboardButton(text='Постоянно улучшаемая картинка✏', callback_data='better')
        button10 = telebot.types.InlineKeyboardButton(text='Назад', callback_data='back')
        markup.row(button1, button2)
        markup.row(button3, button4)
        markup.row(button5)
        markup.row(button6, button7, button8)
        markup.row(button9)
        markup.row(button10)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup)
    elif call.data == 'cancel':
        bot.send_photo(call.message.chat.id, photo=open(PIC + 'okay.jpg', "rb"))
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif call.data == 'back':
        markup = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text='Команды', callback_data='main menu')
        button2 = telebot.types.InlineKeyboardButton(text='Музыка🎵', callback_data='music')
        button3 = telebot.types.InlineKeyboardButton(text='Кнут', callback_data='knut')
        button4 = telebot.types.InlineKeyboardButton(text='Anime-chan🧏🏻‍♀', callback_data='animechan')
        button5 = telebot.types.InlineKeyboardButton(text='Рабочий график', callback_data='grafik')
        button6 = telebot.types.InlineKeyboardButton(text='WEB-Старый (в разработке)',
                                                     url='http://onlynotcrankshaft.ru')
        button7 = telebot.types.InlineKeyboardButton(text='Закрыть🚫', callback_data='cancel')
        markup.row(button1, button2)
        markup.row(button3, button4, button5)
        markup.row(button6)
        markup.row(button7)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup)
    elif call.data == 'knut':
        knutify.knutirovanie(call)
    elif call.data == 'game':
        markup = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text='Игра "Весёлое кнутирование ;)" (Beta)',
                                                     callback_data='funnyknut')
        button2 = telebot.types.InlineKeyboardButton(text='Назад', callback_data='main menu')
        markup.row(button1)
        markup.row(button2)
        bot.send_message(call.message.chat.id, 'Выберите игру: ', reply_markup=markup)
    elif call.data == 'funnyknut':
        bot.send_message(call.message.chat.id, 'Для игры в "Весёлое кнутирование" - нажмите /play!')
    elif call.data == 'clarify':
        knutify.knutirovanie(call)
    elif call.data == 'obossali':
        knutify.knutirovanie(call)
    elif call.data == 'mercy':
        knutify.knutirovanie(call)
    elif call.data == 'junior':
        knutify.knutirovanie(call)
    elif call.data == 'middle':
        knutify.knutirovanie(call)
    elif call.data == 'senior':
        knutify.knutirovanie(call)
    elif call.data == 'senior2':
        knutify.knutirovanie(call)
    elif call.data == 'sounds':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Джо Байден", callback_data='djo'))
        markup.add(telebot.types.InlineKeyboardButton(text="Мурлок", callback_data='murlok'))
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='main menu'))
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup)
    elif call.data == 'djo':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='main menu'))
        rimage = random.choice(os.listdir(DJO))
        bot.send_photo(call.message.chat.id, photo=open(DJO + rimage, "rb"))
        audio = open(SOUND + 'djo.ogg', 'rb')
        bot.send_chat_action(call.message.chat.id, 'upload_audio')
        bot.send_audio(call.message.chat.id, audio, reply_markup=markup)
    elif call.data == 'murlok':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Назад', callback_data='main menu'))
        bot.send_photo(call.message.chat.id, photo=open(MURLOK + 'murlok.jpg', "rb"))
        audio = open(SOUND + 'murlok.ogg', 'rb')
        bot.send_chat_action(call.message.chat.id, 'upload_audio')
        bot.send_audio(call.message.chat.id, audio, reply_markup=markup)
    elif call.data == 'carouselniggers':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Наказать выблядка', callback_data='senior'))
        markup.add(telebot.types.InlineKeyboardButton(text='Простить Старого... на этот раз', callback_data="mercy"))
        reat = random.choice(['Нахуй иди со своей каруселью Ниггеров, BLACK LIVES MATTER!',
                              'Нахуй иди.', 'Разъебу тебя в очко, бесплатно.', 'Хуй за щеку. О ДААА!'])
        bot.send_message(call.message.chat.id,
                         text="Итак, {0.first_name}, твой нигер на сегодня...".format(call.from_user, bot.get_me()))
        time.sleep(3)
        bot.send_message(call.message.chat.id, text='ВСЕ НА ПОЗИЦИИ! Запускаю Карусель Нигеров... хмммммм...')
        time.sleep(2)
        rimage = random.choice(os.listdir(LAUGH_NIGER))
        bot.send_photo(call.message.chat.id, photo=open(LAUGH_NIGER + rimage, 'rb'))
        bot.send_message(call.message.chat.id, reat, reply_markup=markup)
    elif call.data == 'cow':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Ещё тёлочку!', callback_data='cow'))
        markup.add(telebot.types.InlineKeyboardButton(text='Перепутал, хочу аниме-тян', callback_data='animechan'))
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='main menu'))
        rimage = random.choice(os.listdir(COW))
        bot.send_photo(call.message.chat.id, photo=open(COW + rimage, 'rb'))
        bot.send_message(call.message.chat.id, "Я привёл девственниц, Повелитель.", reply_markup=markup)
    elif call.data == 'animechan':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Ещё одну!', callback_data='animechan'))
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='back'))
        rimage = random.choice(os.listdir(ANIME_CHAN))
        bot.send_photo(call.message.chat.id, photo=open(ANIME_CHAN + rimage, 'rb'))
        bot.send_message(call.message.chat.id, "Я привёл аниме-девственниц, Повелитель.", reply_markup=markup)
    elif call.data == 'better':
        markup = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text='Картинкой', callback_data='better1')
        button2 = telebot.types.InlineKeyboardButton(text='Файлом', callback_data='better2')
        button3 = telebot.types.InlineKeyboardButton(text="Назад", callback_data='main menu')
        markup.row(button1, button2)
        markup.row(button3)
        bot.send_message(call.message.chat.id, "Как вам её прислать, Повелитель?", reply_markup=markup)
    elif call.data == 'better1':
        bot.send_photo(call.message.chat.id, photo=open(PIC + 'better/better.png', "rb"))
    elif call.data == 'better2':
        bot.send_document(call.message.chat.id, document=open(PIC + 'better/better.png', "rb"))
    elif call.data == 'music':  # сделать деление по группам
        markup = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text='Ретро', callback_data='retro')
        button2 = telebot.types.InlineKeyboardButton(text='Рок', callback_data='rock')
        button3 = telebot.types.InlineKeyboardButton(text='Рэп', callback_data='rap')
        button4 = telebot.types.InlineKeyboardButton(text='Другое', callback_data='other')
        button5 = telebot.types.InlineKeyboardButton(text='Случайная песня', callback_data='randomsong')
        button6 = telebot.types.InlineKeyboardButton(text='Главное меню', callback_data='back')
        markup.row(button1, button2, button3)
        markup.row(button4, button5)
        markup.row(button6)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup)
    elif call.data == 'randomsong':
        markup = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text='Ещё песню!', callback_data='randomsong')
        button2 = telebot.types.InlineKeyboardButton(text='Не понравилось. Ёбнуть Старого.', callback_data='senior')
        button3 = telebot.types.InlineKeyboardButton(text='Выбрать жанр', callback_data='music')
        markup.row(button1, button3)
        markup.row(button2)
        cataloglist = random.choice(os.listdir(MUSIC)) + '/'
        directory2 = MUSIC + cataloglist
        audio = random.choice(os.listdir(directory2))
        bot.send_chat_action(call.message.chat.id, 'upload_audio')
        bot.send_audio(call.message.chat.id, audio=open(directory2 + audio, 'rb'), reply_markup=markup)
    elif call.data == 'retro':
        markup = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text='Ещё ретро!', callback_data='retro')
        button2 = telebot.types.InlineKeyboardButton(text='Не понравилось. Ёбнуть Старого.', callback_data='senior')
        button3 = telebot.types.InlineKeyboardButton(text='Изменить жанр', callback_data='music')
        markup.row(button1, button3)
        markup.row(button2)
        audio = random.choice(os.listdir(RETRO))
        bot.send_chat_action(call.message.chat.id, 'upload_audio')
        bot.send_audio(call.message.chat.id, audio=open(RETRO + audio, 'rb'), reply_markup=markup)
    elif call.data == 'rock':
        markup = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text='Ещё роцк!', callback_data='rock')
        button2 = telebot.types.InlineKeyboardButton(text='Не понравилось. Ёбнуть Старого.', callback_data='senior')
        button3 = telebot.types.InlineKeyboardButton(text='Изменить жанр', callback_data='music')
        markup.row(button1, button3)
        markup.row(button2)
        audio = random.choice(os.listdir(ROCK))
        bot.send_chat_action(call.message.chat.id, 'upload_audio')
        bot.send_audio(call.message.chat.id, audio=open(ROCK + audio, 'rb'), reply_markup=markup)
    elif call.data == 'rap':
        markup = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text='Ещё крэп!', callback_data='rap')
        button2 = telebot.types.InlineKeyboardButton(text='Не понравилось. Ёбнуть Старого.', callback_data='senior')
        button3 = telebot.types.InlineKeyboardButton(text='Изменить жанр', callback_data='music')
        markup.row(button1, button3)
        markup.row(button2)
        audio = random.choice(os.listdir(RAP))
        bot.send_chat_action(call.message.chat.id, 'upload_audio')
        bot.send_audio(call.message.chat.id, audio=open(RAP + audio, 'rb'), reply_markup=markup)
    elif call.data == 'other':
        markup = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text='Ещё кринжа!', callback_data='other')
        button2 = telebot.types.InlineKeyboardButton(text='Не понравилось. Ёбнуть Старого.', callback_data='senior')
        button3 = telebot.types.InlineKeyboardButton(text='Изменить жанр', callback_data='music')
        markup.row(button1, button3)
        markup.row(button2)
        audio = random.choice(os.listdir(OTHER))
        bot.send_chat_action(call.message.chat.id, 'upload_audio')
        bot.send_audio(call.message.chat.id, audio=open(OTHER + audio, 'rb'), reply_markup=markup)
    elif call.data == 'grafik':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Показать график',
                                                      callback_data='grafikpic'))  # в идеале - скрин графика
        markup.add(telebot.types.InlineKeyboardButton(text='Скинуть график', callback_data="grafikfile"))
        markup.add(telebot.types.InlineKeyboardButton(text="График внерабочих консультаций поющих ведущих",
                                                      callback_data='grafikved'))
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='back'))
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup)
    # elif call.data == 'grafikpic':
    # workbook = xlrd.open_workbook(BASE_PATH + 'grafik/grafik.xlsx', formatting_info=True)
    # worksheet = workbook.sheet_by_index(6)
    # cells = worksheet['B2':'AH20']
    # for name,  in cells:
    #    bot.send_message(call.message.chat.id, cell)
    # for i in range(2, 20):
    #    for j in range(1, 32):
    #        # Print the cell values with tab space
    #        print(worksheet.cell_value(i, j), end='\t')
    #    bot.send_message(call.message.chat.id, worksheet.cell_value(i, j))
    elif call.data == 'grafikfile':
        bot.send_document(call.message.chat.id, document=open(BASE_PATH + 'storage/grafik/grafik.png', "rb"))
    elif call.data == 'grafikved':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='grafik'))
        bot.send_message(call.message.chat.id, 'Число месяца:'
                                               '\n*Андрей Добровольский*: 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31'
                                               '\n*Даниил Гущенко*: 2, 5, 8, 11, 14, 17, 20, 23, 26, 29'
                                               '\n*Илья Катухов*: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30'
                                               '\nПримечание: если дежурный ведущий специалист в данный период времени '
                                               'подменяет дежурных в 1/3 и в данный момент не на смене - оповещаем '
                                               'следующего дежурного!', parse_mode='markdown', reply_markup=markup)
    elif call.data == 'joke':
        jokes.query_jokes(call)
    elif call.data == 'joke2':
        jokes.query_jokes(call)
    elif call.data == 'jokeru':
        jokes.query_jokes(call)
    elif call.data == 'jokeen':
        jokes.query_jokes(call)
    elif call.data == 'jokees':
        jokes.query_jokes(call)
    elif call.data == 'jokede':
        jokes.query_jokes(call)
    elif call.data == 'jokerunor':
        jokes.query_jokes(call)
    elif call.data == 'comics':
        jokes.query_jokes(call)
    elif call.data == 'millennium1':
        jokes.query_jokes(call)
    elif call.data == 'millennium2':
        jokes.query_jokes(call)
    elif call.data == 'millennium3':
        jokes.query_jokes(call)
    elif call.data == 'carouselwishes':
        markup = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text='шлёппнуть Старого', callback_data='earlystop')
        markup.row(button1)
        bot.send_message(call.message.chat.id, 'Чтобы запустить "Карусель Желаний", '
                                               'используйте /carousel', reply_markup=markup)
        # bot.send_dice(call.message.chat.id)
        # bot.send_dice(call.message.chat.id, reply_markup=markup)
        # listrest = open(BASE_PATH + 'carouselfood/listrest.txt', 'a')
        # listrest.write(f':{int(message.text)}\n')
        # listrest.close()
    elif call.data == 'earlystop':
        bot.send_message(call.message.chat.id, 'Ты даун?)')
    elif call.data == 'stories':
        audiobooks.rasskaziki(call)
    elif call.data == 'uthermarriage':
        audiobooks.rasskaziki(call)
    elif call.data == 'utherbecomegay':
        audiobooks.rasskaziki(call)
    elif call.data == 'arthaswantsminet':
        audiobooks.rasskaziki(call)
    elif call.data == 'utherdevelopment':
        audiobooks.rasskaziki(call)
    elif call.data == 'uthercropdick':
        audiobooks.rasskaziki(call)
    elif call.data == 'battlevsgnomy':
        audiobooks.rasskaziki(call)
    elif call.data == 'iliaquarreljina':
        audiobooks.rasskaziki(call)
    elif call.data == 'operaall':
        audiobooks.rasskaziki(call)
    elif call.data == 'opera1':
        audiobooks.rasskaziki(call)
    elif call.data == 'opera2':
        audiobooks.rasskaziki(call)
    elif call.data == 'opera3':
        audiobooks.rasskaziki(call)
    elif call.data == 'arthasnightmare':
        audiobooks.rasskaziki(call)
    elif call.data == 'arnamdhelper':
        markup = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text='Python', callback_data='python')
        button2 = telebot.types.InlineKeyboardButton(text='Ubuntu', callback_data='ubuntu')
        button3 = telebot.types.InlineKeyboardButton(text='GIT', callback_data='git')
        button4 = telebot.types.InlineKeyboardButton(text='Telegram', callback_data='telegram')
        button5 = telebot.types.InlineKeyboardButton(text='Django', callback_data='django')
        markup.row(button1, button2, button3, button4, button5)
        bot.send_message(call.message.chat.id, text='<s>Пельменная</s> Справочная "<b>Старый+</b>". Чем вам помочь?',
                         parse_mode='HTML', reply_markup=markup)
    elif call.data == 'python':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='arnamdhelper'))
        bot.send_message(call.message.chat.id, text='*Python:* '
                                                    '\n\n1) *pip install googletrans==3.1.0a0* - последняя версия '
                                                    'google-переводчика (она не устанавливается автоматически и не '
                                                    'описана в документации google). ',
                         parse_mode='markdown', reply_markup=markup)
    elif call.data == 'ubuntu':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='arnamdhelper'))
        bot.send_message(call.message.chat.id, text='*Ubuntu:* '
                                                    '\n\nЕсли папка содержит защищённый от перезаписи контент '
                                                    'или какие-то команды выдают ошибку доступа - добавьте в '
                                                    'начало команды sudo - всегда помогает ;) '
                                                    '\n1) *adduser user* - создать нового пользователя. '
                                                    '\n2) *usermod -aG sudo user* - наделить его полномочиями. '
                                                    '\n3) *su user* - переключение на другого пользователя '
                                                    'без перезахода на сервер. '
                                                    '\n4) *rm -R /home/user/directory/* - рекурсивное удаление '
                                                    'указанного каталога с содержимым. '
                                                    '\n5) *rmdir /directory/* - удаление пустого каталога. '
                                                    '\n6) *df -h* - отображение дискового пространства с критерием '
                                                    'использования памяти. '
                                                    '\n7) *mv звёздочка ../* - перемещает файлы в текущем каталоге '
                                                    'на уровень выше. '
                                                    '\n8) *mv звёздочка.звёздочка ..* - перемещает ВСЕ ФАЙЛЫ в '
                                                    'текущем каталоге на уровень выше (в т.ч. и скрытые).',
                         parse_mode='markdown', reply_markup=markup)
    elif call.data == 'git':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='arnamdhelper'))
        bot.send_message(call.message.chat.id, text='*GIT:* '
                                                    '\n\nСинхронизация *git* с данным удалённым репозиторием: '
                                                    '\n1) *git fetch* --> *git merge* - фетч проверяет изменения в '
                                                    'репозитории и закачивает их на сервер. Мердж - заменяет '
                                                    'текущие данные на те, что были закачены из git-репозитория. '
                                                    '\n2) *git pull* - форсированное обновление репозитория. '
                                                    '\nПервый способ безопаснее в вопросах потери данных. '
                                                    'И он сработал, збс. '
                                                    '\n\nСоздание репозитория git-> сервер: '
                                                    '\n*git clone git@github.com:your-nickname/your-project.git* '
                                                    '- подставить свою УЗ и название репозитория.',
                         parse_mode='markdown', reply_markup=markup)
    elif call.data == 'telegram':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='arnamdhelper'))
        bot.send_message(call.message.chat.id, text='*Telegram:* '
                                                    '\n\n1) *username_to_id_bot* - подставь собаку перед '
                                                    'названием. Этот бот позволяет узнать свой ID '
                                                    'или ID любого чата. Для этого его НЕ ОБЯЗАТЕЛЬНО '
                                                    'добавлять в чат. ', parse_mode='markdown', reply_markup=markup)
    elif call.data == 'django':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='arnamdhelper'))
        bot.send_message(call.message.chat.id, text='*django:* '
                                                    '\n\n1) *./manage.py* - ваш друг и товарищ. Почти любые '
                                                    'операции нужно производить, находясь в одном каталоге с менеджем.'
                                                    '\n2) *./manage.py createsuperuser* - создать админку на ресурсе.'
                                                    '\n3) *./manage.py runserver* - запустить локальный сервер.'
                                                    '\n4) *./manage.py migrate* - миграция - запись изменений самой '
                                                    'структуры таблиц в БД.'
                                                    '\n5) *./manage.py makemigrations* - пока хз, чёт не получается. '
                                                    '\n6) *./manage.py startapp app1* - создание блока приложений. '
                                                    'Вместо app1 подставить название вашего будущего приложения. '
                         , parse_mode='markdown', reply_markup=markup)


@bot.message_handler(func=lambda message: 'кнут' in message.text.lower(), content_types=['text'])
def knut(message):
    markup = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text='Да', callback_data='knut')
    button2 = telebot.types.InlineKeyboardButton(text='Нет', callback_data='mercy')
    markup.row(button1, button2)
    bot.send_message(message.chat.id, "Хотите отхлищеть кого-то и выместить на этом человеке свою злость?",
                     reply_markup=markup)


@bot.message_handler(func=lambda message: 'хуй' in message.text.lower(), content_types=['text'])
def hui(message):
    bot.send_message(message.chat.id, "*жирным.*", parse_mode='markdown')


@bot.message_handler(func=lambda message: 'игнат' in message.text.lower(), content_types=['text'])
def ignat(message):
    bot.send_photo(message.chat.id, photo=open(PIC + 'pskov/pskov.png', "rb"))
    time.sleep(2)
    bot.send_message(message.chat.id, 'Дрочи мой хуй себе в рот...')
    time.sleep(2)
    bot.send_message(message.chat.id, 'Я знаю - ты любишь отсасывать')


@bot.message_handler(func=lambda message: 'шамиль' in message.text.lower(), content_types=['text'])
def shamil(message):
    bot.send_message(message.chat.id, 'Салам Аллейкум Аджара гужду аджика сила'
                                      '\nhttps://www.youtube.com/watch?v=USrirfiv0L8')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'музыка':
        textcommand.get_text_messages(message)
    elif message.text == 'привет':
        textcommand.get_text_messages(message)
    elif message.text == 'покажи Путина':
        textcommand.get_text_messages(message)
    elif message.text == 'шоколад в жопе':
        textcommand.get_text_messages(message)
    elif message.text == 'if he dies':
        textcommand.get_text_messages(message)
    elif message.text == 'скрытое отхлищивание...':
        textcommand.get_text_messages(message)
    elif message.text == 'ты лох':
        textcommand.get_text_messages(message)
    elif message.text == 'ты лох2':
        textcommand.get_text_messages(message)
    elif message.text == 'Похвалить Старого!':
        textcommand.get_text_messages(message)
    elif message.text == 'тест':
        bot.send_photo(message.chat.id, photo=open('AgACAgIAAxkBAAEWssFlD5Ba_zODDbPJ9kb8U07VDA94jQACwckxG730gUiSGAWcmALv5QEAAwIAA3gAAzAE', 'rb'))


bot.polling(none_stop=True, interval=0)
