import requests
from PIL import Image

import telebot
from telebot import types
import dataBase

bot = telebot.TeleBot('')


@bot.message_handler(commands=["start", "Start"])
def start(message):
    name = f'Приветствую, <b>{message.from_user.first_name}</b>!'
    bot.send_message(message.chat.id, name, parse_mode='html')


@bot.message_handler(commands=["info", "Info"])
def info(message):
    bot.send_message(message.chat.id,
                     f"Номера телефона:\n   +77782185661 - Сергей\n  +77017490261 - Руслан\nАдрес: Актуальный адрес не известен\nПочта: Rus0867@Mail.Ru\nГрафик работы: Пн - Пт / 9:00 - 18:00\nСайт: comtrade.kz")


@bot.message_handler(commands=['help', 'Help'])
def help(message):
    bot.send_message(message.chat.id,
                     f'/start - Приветствие\n/info - Информация о компании\n/help - Каталог товаров\n/catalog - Доступные команды')


@bot.message_handler(commands=['catalog', 'Catalog'])
def view_catalog(message):
    bot.send_message(message.chat.id, 'Каталог', reply_markup=catalog)


infoMessage = 'Подробную информацию можно посмотреть на сайте: comtrade.kz'
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
button = types.KeyboardButton(text="Назад в каталог!")
keyboard.add(button)


@bot.callback_query_handler(func=lambda call: True)
def print_all_commands(call):
    ids = [str(i) for i in range(1, 62)]
    dictOfCategory = {"АвтоХимия": 'auto', "Антисептики, отбеливатели для древесины": 'wood',
                      "Гидроизоляционные материалы": 'hydro', "Добавки для бетона": 'biton',
                      "Лаки, краски, растворители": 'paint', "Огнебиозащитные составы": 'fire',
                      "Очистка, защита и обработка минеральных поверхностей": 'mineral',
                      "Составы для бань и саун": 'bath', "Фасадный декор": 'decor', "Химия для бассейнов": 'pool',
                      "Бытовая химия": 'life'}
    catalogList = dictOfCategory.values()
    if call.data:
        if call.data in catalogList:
            ress = []
            res = dataBase.getPic(call.data)
            preCatalog = types.InlineKeyboardMarkup(row_width=1)
            for data in res:
                ress.append(types.InlineKeyboardButton(text=data.review, callback_data=data.id))
            for i in range(len(ress)):
                preCatalog.add(ress[i])
            for key, val in dictOfCategory.items():
                if call.data == val:
                    bot.send_message(call.message.chat.id, key, reply_markup=preCatalog)
        if call.data in ids:
            res = dataBase.getPicById(call.data)
            img = Image.open(res.url)
            bot.send_photo(call.message.chat.id, img)
            bot.send_message(call.message.chat.id, str(res.review + '\n' + infoMessage), reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def getText(message):
    if message.text == 'Назад в каталог!':
        bot.send_message(message.chat.id, 'Каталог', reply_markup=catalog)
        types.ReplyKeyboardRemove()


bot.polling(none_stop=True, interval=0)

# start - Приветствие
# info - Информация о компании
# catalog - Каталог товаров
# help - Доступные команды
