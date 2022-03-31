import telebot
from telebot import types

bot = telebot.TeleBot('5125730563:AAFr0-wAfF8eas0EcPqnmZ6W2MpHrCgV_vU')


@bot.message_handler(commands=["start", "Start"])
def start(message):
    name = f'Приветствую, <b>{message.from_user.first_name}</b>!'
    bot.send_message(message.chat.id, name, parse_mode='html')


@bot.message_handler(commands=["info", "Info"])
def info(message):
    bot.send_message(message.chat.id, f"Номер телефона:\n   +77782185661\n  +77017490261\nАдрес: Брюсова 4/35 офис 1\nПочта: Rus0867@Mail.Ru\nГрафик работы: Пн - Пт / 9:00 - 18:00\nСайт:comtrade.kz")


@bot.message_handler(commands=['help', 'Help'])
def help(message):
    bot.send_message(message.chat.id, f'/start - Приветствие\n/info - Информация о компании\n/help - Каталог товаров\n/catalog - Доступные команды')


@bot.message_handler(commands=['catalog', 'Catalog'])
def view_catalog(message):
    catalog = types.InlineKeyboardMarkup()
    autochem = types.InlineKeyboardButton(text="АвтоХимия", callback_data='auto')
    wood = types.InlineKeyboardButton(text="Антисептики, отбеливатели для древесины", callback_data='wood')
    household = types.InlineKeyboardButton(text="Бытовая химия", callback_data='life')
    hydro = types.InlineKeyboardButton(text="Гидроизоляционные материалы", callback_data='hydro')
    biton = types.InlineKeyboardButton(text="Добавки для бетона", callback_data='biton')
    paint = types.InlineKeyboardButton(text="Лаки, краски, растворители", callback_data='paint')
    fire = types.InlineKeyboardButton(text="Огнебиозащитные составы", callback_data='fire')
    mineral = types.InlineKeyboardButton(text="Очистка, защита и обработка минеральных поверхностей",callback_data='mineral')
    bath = types.InlineKeyboardButton(text="Составы для бань и саун", callback_data='bath')
    decor = types.InlineKeyboardButton(text="Фасадный декор", callback_data='decor')
    pool = types.InlineKeyboardButton(text="Химия для бассейнов", callback_data='pool')
    catalog.add(autochem, wood, household, hydro, biton, paint, fire, mineral, bath, decor, pool)
    bot.send_message(message.chat.id, 'Каталог', reply_markup=catalog)


bot.polling(none_stop=True, interval=0)



# start - Преветствие
# info - Информация о компании
# catalog - Каталог товаров
# help - Доступные команды