import requests
from PIL import Image

import telebot
from telebot import types
import dataBase

bot = telebot.TeleBot('5125730563:AAFr0-wAfF8eas0EcPqnmZ6W2MpHrCgV_vU')


@bot.message_handler(commands=["start", "Start"])
def start(message):
    name = f'Приветствую, <b>{message.from_user.first_name}</b>!'
    bot.send_message(message.chat.id, name, parse_mode='html')


@bot.message_handler(commands=["info", "Info"])
def info(message):
    bot.send_message(message.chat.id,
                     f"Номер телефона:\n   +77782185661\n  +77017490261\nАдрес: Брюсова 4/35 офис 1\nПочта: Rus0867@Mail.Ru\nГрафик работы: Пн - Пт / 9:00 - 18:00\nСайт:comtrade.kz")


@bot.message_handler(commands=['help', 'Help'])
def help(message):
    bot.send_message(message.chat.id,
                     f'/start - Приветствие\n/info - Информация о компании\n/help - Каталог товаров\n/catalog - Доступные команды')


@bot.message_handler(commands=['catalog', 'Catalog'])
def view_catalog(message):
    bot.send_message(message.chat.id, 'Каталог', reply_markup=catalog)


catalog = types.InlineKeyboardMarkup(row_width=1)
autochem = types.InlineKeyboardButton(text="АвтоХимия", callback_data='auto')
wood = types.InlineKeyboardButton(text="Антисептики, отбеливатели для древесины", callback_data='wood')
household = types.InlineKeyboardButton(text="Бытовая химия", callback_data='life')
hydro = types.InlineKeyboardButton(text="Гидроизоляционные материалы", callback_data='hydro')
biton = types.InlineKeyboardButton(text="Добавки для бетона", callback_data='biton')
paint = types.InlineKeyboardButton(text="Лаки, краски, растворители", callback_data='paint')
fire = types.InlineKeyboardButton(text="Огнебиозащитные составы", callback_data='fire')
mineral = types.InlineKeyboardButton(text="Очистка, защита и обработка минеральных поверхностей",
                                         callback_data='mineral')
bath = types.InlineKeyboardButton(text="Составы для бань и саун", callback_data='bath')
decor = types.InlineKeyboardButton(text="Фасадный декор", callback_data='decor')
pool = types.InlineKeyboardButton(text="Химия для бассейнов", callback_data='pool')
catalog.add(autochem, wood, household, hydro, biton, paint, fire, mineral, bath, decor, pool)

keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
button = types.KeyboardButton(text="Назад!")
keyboard.add(button)

@bot.callback_query_handler(func=lambda call: True)
def print_all_commands(call):
    if call.data:
        res = dataBase.getPic(call.data)

        for data in res:
            img = Image.open(data.url)
            bot.send_chat_action(call.message.chat.id, 'upload_photo')
            bot.send_photo(call.message.chat.id, img)
            bot.send_message(call.message.chat.id, str(data.review), reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def getText(message):
    if message.text == 'Назад!':
        bot.send_message(message.chat.id, 'Каталог', reply_markup=catalog)
        types.ReplyKeyboardRemove()



bot.polling(none_stop=True, interval=0)

# start - Приветствие
# info - Информация о компании
# catalog - Каталог товаров
# help - Доступные команды
