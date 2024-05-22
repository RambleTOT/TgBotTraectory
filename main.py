from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from dotenv import load_dotenv
import os

# Обработчик команды /start
def start(update, context):
    text = "Привет, я Алекс! Я представитель центра дополнительного образования Траектория, и я готов помочь с поиском нужной информации. Для того, чтобы перейти к ней, нажми кнопку Меню"
    keyboard = [InlineKeyboardButton("Меню", callback_data='menu')], [InlineKeyboardButton("На сайт Траектория", url='https://traektoriya-edu.ru/')]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('src/start_image.png', 'rb'))
    context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=reply_markup)

# Обработчик команды /menu
def menu(update, context):
    text = "Добро пожаловать в меню. Здесь ты сможешь узнать больше информации о нашем центре. Для этого нужно просто нажать на кнопку интересующей темы"
    keyboard = [
        [InlineKeyboardButton("Отызвы", callback_data='button1')],
        [InlineKeyboardButton("Мастер классы", callback_data='button2')],
        [InlineKeyboardButton("Треки", callback_data='button3')],
        [InlineKeyboardButton("Магазин", callback_data='button4')],
        [InlineKeyboardButton("О нас", callback_data='button5')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=reply_markup)

# Обработчик нажатий на кнопки
def button_click(update, context):
    query = update.callback_query
    if query.data == 'button2':
        button2(update, context)
    if query.data == 'button1':
        button1(update, context)
    if query.data == 'menu' or query.data == 'back':
        menu(update, context)
    if query.data == 'button4':
        button4(update, context)
# Обработчик кнопки "Назад"
def back_button(update, context):
    menu(update, context)  # Возвращаемся к сообщению с меню

def button2(update, context):
    text = "Мастер классы"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    media_group = [
        InputMediaPhoto(media=open('src/image_master_class_2.png', 'rb'), caption="Разработка и печать 3D модели"),
        InputMediaPhoto(media=open('src/image_master_class_3.png', 'rb'), caption="Создание коллекции стикеров для Telegram канала"),
        InputMediaPhoto(media=open('src/image_master_class_4.png', 'rb'), caption="Визуализация интерьера"),
        InputMediaPhoto(media=open('src/image_master_class_5.png', 'rb'), caption="Создание лендинга на Tilda"),
        InputMediaPhoto(media=open('src/image_master_class_6.png', 'rb'), caption="Покадровая анимация персонажа в технике Pixel Art"),
        InputMediaPhoto(media=open('src/image_master_class_7.png', 'rb'), caption="Создание логотипа с использованием нейросетей"),
        InputMediaPhoto(media=open('src/image_master_class_8.png', 'rb'), caption="Создай свою компьютерную игру в 2D"),
        InputMediaPhoto(media=open('src/image_master_class_9.png', 'rb'), caption="Создай анимированного персонажа в 3D"),
        InputMediaPhoto(media=open('src/image_master_class_10.png', 'rb'), caption="Моделирование 3D брелка"),
        InputMediaPhoto(media=open('src/image_master_class_11.png', 'rb'), caption="Создай комикс"),
    ]
    context.bot.send_media_group(chat_id=update.effective_chat.id, media=media_group)
    keyboard = [
        [InlineKeyboardButton("Перейти на сайт", url='https://traektoriya-edu.ru/master-class')],
        [InlineKeyboardButton("Назад", callback_data='back')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Что-то о мастер классах",
                             reply_markup=reply_markup)


def button1(update, context):
    text = "Отзывы"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    media_group = [
        InputMediaPhoto(media=open('src/image_review_1.png', 'rb'), caption="Отзывы"),
        InputMediaPhoto(media=open('src/image_review_2.png', 'rb'), caption="Отзывы"),
        InputMediaPhoto(media=open('src/image_review_3.png', 'rb'), caption="Отзывы"),
        InputMediaPhoto(media=open('src/image_review_4.png', 'rb'), caption="Отзывы"),
        InputMediaPhoto(media=open('src/image_review_5.png', 'rb'), caption="Отзывы"),
        InputMediaPhoto(media=open('src/image_review_6.png', 'rb'), caption="Отзывы")
    ]
    context.bot.send_media_group(chat_id=update.effective_chat.id, media=media_group)
    keyboard = [
        [InlineKeyboardButton("Перейти на сайт", url='https://traektoriya-edu.ru/reviews')],
        [InlineKeyboardButton("Назад", callback_data='back')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Что-то об отзывах",
                             reply_markup=reply_markup)

def button4(update, context):
    text = "Магазин"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    media_group = [
        InputMediaPhoto(media=open('src/image_review_1.png', 'rb'), caption="Отзывы"),
        InputMediaPhoto(media=open('src/image_review_2.png', 'rb'), caption="Отзывы"),
        InputMediaPhoto(media=open('src/image_review_3.png', 'rb'), caption="Отзывы"),
        InputMediaPhoto(media=open('src/image_review_4.png', 'rb'), caption="Отзывы"),
        InputMediaPhoto(media=open('src/image_review_5.png', 'rb'), caption="Отзывы"),
        InputMediaPhoto(media=open('src/image_review_6.png', 'rb'), caption="Отзывы")
    ]
    context.bot.send_media_group(chat_id=update.effective_chat.id, media=media_group)
    keyboard = [
        [InlineKeyboardButton("Перейти на сайт", url='https://traektoriya-edu.ru/shop')],
        [InlineKeyboardButton("Назад", callback_data='back')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Благодаря своей активности в ходе прохождения стажировки ребята заработывают очки знаний, умений и навыков. В дальнейшем они могут обменять свои накопления в ИТ магазине. \n Оформлять заказ можно на сайте, а забрать в офисе Траектории!",
                             reply_markup=reply_markup)


load_dotenv()
# Создание и запуск бота
updater = Updater(os.getenv('TOKEN'), use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('menu', menu))
dispatcher.add_handler(CallbackQueryHandler(button_click))
dispatcher.add_handler(CallbackQueryHandler(back_button, pattern='back'))

updater.start_polling()
updater.idle()
