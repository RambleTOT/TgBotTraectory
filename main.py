from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from dotenv import load_dotenv
import os

# Обработчик команды /start
def start(update, context):
    text = "Привет, я Алекс! Я представитель центра дополнительного образования Траектория, и я готов помочь с поиском нужной информации. Для того, чтобы перейти к ней, нажми кнопку Меню"
    keyboard = [InlineKeyboardButton("Меню", callback_data='menu')], [InlineKeyboardButton("На сайт Траектория", url='https://traektoriya-edu.ru/')]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('test_photo (2).png', 'rb'))
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
    if query.data == 'button1':
        text = "Вы нажали кнопку 1. Здесь кратинки и текст."
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('test_photo (2).png', 'rb'))
        keyboard = [
            [InlineKeyboardButton("Перейти на сайт", url='http://example.com')],
            [InlineKeyboardButton("Назад", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Дополнительная информация.", reply_markup=reply_markup)

    if query.data == 'button2':
        text = "Мастер классы"
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('test_photo (2).png', 'rb'))
        keyboard = [
            [InlineKeyboardButton("Перейти на сайт", url='https://traektoriya-edu.ru/master-class')],
            [InlineKeyboardButton("Назад", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Что-то о мастер классах", reply_markup=reply_markup)
    if query.data == 'menu':
        menu(update, context)
# Обработчик кнопки "Назад"
def back_button(update, context):
    menu(update, context)  # Возвращаемся к сообщению с меню

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