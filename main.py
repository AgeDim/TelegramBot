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
                     f"Номера телефона:\n   +77782185661 - Сергей\n  +77017490261 - Руслан\nАдрес: Актуальный адрес не известен\nПочта: Rus0867@Mail.Ru\nГрафик работы: Пн - Пт / 9:00 - 18:00\nСайт: comtrade.kz")


@bot.message_handler(commands=['help', 'Help'])
def help(message):
    bot.send_message(message.chat.id,
                     f'/start - Приветствие\n/info - Информация о компании\n/help - Каталог товаров\n/catalog - Доступные команды')


@bot.message_handler(commands=['catalog', 'Catalog'])
def view_catalog(message):
    bot.send_message(message.chat.id, 'Каталог', reply_markup=catalog)


catalog = types.InlineKeyboardMarkup(row_width=1)
autochem = types.InlineKeyboardButton(text="АвтоХимия", callback_data='АвтоХимия')
wood = types.InlineKeyboardButton(text="Антисептики, отбеливатели для древесины",
                                  callback_data='Антисептики, отбеливатели для древесины')
household = types.InlineKeyboardButton(text="Бытовая химия", callback_data='Бытовая химия')
hydro = types.InlineKeyboardButton(text="Гидроизоляционные материалы", callback_data='Гидроизоляционные материалы')
biton = types.InlineKeyboardButton(text="Добавки для бетона", callback_data='Добавки для бетона')
paint = types.InlineKeyboardButton(text="Лаки, краски, растворители", callback_data='Лаки, краски, растворители')
fire = types.InlineKeyboardButton(text="Огнебиозащитные составы", callback_data='Огнебиозащитные составы')
mineral = types.InlineKeyboardButton(text="Очистка, защита и обработка минеральных поверхностей",
                                     callback_data='Очистка, защита и обработка минеральных поверхностей')
bath = types.InlineKeyboardButton(text="Составы для бань и саун", callback_data='Составы для бань и саун')
decor = types.InlineKeyboardButton(text="Фасадный декор", callback_data='Фасадный декор')
pool = types.InlineKeyboardButton(text="Химия для бассейнов", callback_data='Химия для бассейнов')
catalog.add(autochem, wood, household, hydro, biton, paint, fire, mineral, bath, decor, pool)

keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
button = types.KeyboardButton(text="Назад!")
keyboard.add(button)


@bot.callback_query_handler(func=lambda call: True)
def print_all_commands(call):
    catalogList = ["АвтоХимия", "Антисептики, отбеливатели для древесины", "Бытовая химия",
                   "Гидроизоляционные материалы", "Добавки для бетона", "Лаки, краски, растворители",
                   "Огнебиозащитные составы", "Очистка, защита и обработка минеральных поверхностей",
                   "Составы для бань и саун", "Фасадный декор", "Химия для бассейнов"]
    if call.data:
        if call.data in catalogList:
            ress = []
            res = dataBase.getPic(call.data)
            preCatalog = types.InlineKeyboardMarkup(row_width=1)
            for data in res:
                ress.append(types.InlineKeyboardButton(text=data.review, callback_data=data.id))
            for i in range(len(ress)):
                preCatalog.add(ress[i])
            bot.send_message(call.message.chat.id, call.data, reply_markup=preCatalog)

        # for data in res:
        #     img = Image.open(data.url)
        #     bot.send_chat_action(call.message.chat.id, 'upload_photo')
        #     bot.send_photo(call.message.chat.id, img)
        #     bot.send_message(call.message.chat.id, str(data.review), reply_markup=keyboard)


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
