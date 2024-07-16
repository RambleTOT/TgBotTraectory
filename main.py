from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from dotenv import load_dotenv
import os

# Обработчик команды /start
def start(update, context):
    user = update.message.from_user
    text = f"Привет,{user.first_name}!\nМеня зовут Алекс! Я стажер IT компании Траектория, вместе со мной ты освоишь мир цифровых технологий. О чем бы ты хотел узнать?\nЯ готов познакомить тебя с нашей системой обучения. Чтобы узнать о ней подробнее, смело нажимай кнопку Меню.\nИ не забывай пеерходить на наш сайт, чтобы получить больше информации и стать частью Траектории"
    keyboard = [InlineKeyboardButton("На сайт Траектория", url='https://traektoriya-edu.ru/')], [InlineKeyboardButton("Меню", callback_data='menu')]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('src/start_image.png', 'rb'))
    context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=reply_markup)

# Обработчик команды /menu
def menu(update, context):
    text = "Добро пожаловать в Тракторию. Мы обучаем взрослых и детей старше 7 лет. Выбери интересующую тему"
    keyboard = [
        [InlineKeyboardButton("Мероприятия", callback_data='button2')],
        [InlineKeyboardButton("Треки", callback_data='button3')],
        [InlineKeyboardButton("IT магазин", callback_data='button4')],
        [InlineKeyboardButton("Наша команда", callback_data='button5')],
        [InlineKeyboardButton("Отзывы (2GIS)", url='https://2gis.ru/yaroslavl/firm/70000001067234653/tab/reviews')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=reply_markup)

# Обработчик нажатий на кнопки
def button_click(update, context):
    query = update.callback_query
    if query.data == 'button2':
        button2(update, context)
    # if query.data == 'button1':
    #     button1(update, context)
    if query.data == 'menu' or query.data == 'back':
        menu(update, context)
    if query.data == 'button3':
        button3(update, context)
    if query.data == 'button4':
        button4(update, context)
    if query.data == 'button5':
        button5(update, context)
# Обработчик кнопки "Назад"
def back_button(update, context):
    menu(update, context)  # Возвращаемся к сообщению с меню

def button2(update, context):
    text = "Мероприятия"
    # context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    # media_group = [
    #     InputMediaPhoto(media=open('src/image_master_class_2.png', 'rb'), caption="Разработка и печать 3D модели"),
    #     InputMediaPhoto(media=open('src/image_master_class_3.png', 'rb'), caption="Создание коллекции стикеров для Telegram канала"),
    #     InputMediaPhoto(media=open('src/image_master_class_4.png', 'rb'), caption="Визуализация интерьера"),
    #     InputMediaPhoto(media=open('src/image_master_class_5.png', 'rb'), caption="Создание лендинга на Tilda"),
    #     InputMediaPhoto(media=open('src/image_master_class_6.png', 'rb'), caption="Покадровая анимация персонажа в технике Pixel Art"),
    #     InputMediaPhoto(media=open('src/image_master_class_7.png', 'rb'), caption="Создание логотипа с использованием нейросетей"),
    #     InputMediaPhoto(media=open('src/image_master_class_8.png', 'rb'), caption="Создай свою компьютерную игру в 2D"),
    #     InputMediaPhoto(media=open('src/image_master_class_9.png', 'rb'), caption="Создай анимированного персонажа в 3D"),
    #     InputMediaPhoto(media=open('src/image_master_class_10.png', 'rb'), caption="Моделирование 3D брелка"),
    #     InputMediaPhoto(media=open('src/image_master_class_11.png', 'rb'), caption="Создай комикс"),
    # ]
    # context.bot.send_media_group(chat_id=update.effective_chat.id, media=media_group)
    keyboard = [
        [InlineKeyboardButton("День открытых дверей", url='https://traektoriya-edu.ru/opendoorsday')],
        [InlineKeyboardButton("Регистрация", url='https://vk.com/trek_2022?w=app6013442_-215628262%2523form_id%253D1')],
        [InlineKeyboardButton("Назад", callback_data='back')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text="День открытых дверей в Траектори!\nВ программе вас ждет знакомство с центром, мастер-классы и презентация образовательных программ\nЖдём вас16 сентября с 10::00 до 18:00 по адресу Республиканская, 61 (3 этаж)\nДля регистрации нажмите на кнопку, которя переведет вас на форму ВК",
                             reply_markup=reply_markup)


# def button1(update, context):
#     text = "Отзывы"
#     context.bot.send_message(chat_id=update.effective_chat.id, text=text)
#     media_group = [
#         InputMediaPhoto(media=open('src/image_review_1.png', 'rb'), caption="Отзывы"),
#         InputMediaPhoto(media=open('src/image_review_2.png', 'rb'), caption="Отзывы"),
#         InputMediaPhoto(media=open('src/image_review_3.png', 'rb'), caption="Отзывы"),
#         InputMediaPhoto(media=open('src/image_review_4.png', 'rb'), caption="Отзывы"),
#         InputMediaPhoto(media=open('src/image_review_5.png', 'rb'), caption="Отзывы"),
#         InputMediaPhoto(media=open('src/image_review_6.png', 'rb'), caption="Отзывы")
#     ]
#     context.bot.send_media_group(chat_id=update.effective_chat.id, media=media_group)
#     keyboard = [
#         [InlineKeyboardButton("Перейти на сайт", url='https://traektoriya-edu.ru/reviews')],
#         [InlineKeyboardButton("Назад", callback_data='back')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Что-то об отзывах",
#                              reply_markup=reply_markup)

def button3(update, context):
    text = "Треки"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    media_group = [
        InputMediaPhoto(media=open('src/image_track_jun.png', 'rb'), caption="Младшая школа"),
        InputMediaPhoto(media=open('src/image_track_mid_1.png', 'rb'), caption="Средняя школа"),
        InputMediaPhoto(media=open('src/image_track_sen.png', 'rb'), caption="Старшая школа"),
    ]
    context.bot.send_media_group(chat_id=update.effective_chat.id, media=media_group)
    keyboard = [
        [InlineKeyboardButton("Младшая и средняя школа", url='https://traektoriya-edu.ru/middle')],
        [InlineKeyboardButton("Старшая школа", url='https://traektoriya-edu.ru/senior')],
        [InlineKeyboardButton("Назад", callback_data='back')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text="В Траектории есть обучающие программы для всех возрастов. Подробнее о каждых групах и записаться можно на сайте",
                             reply_markup=reply_markup)


def button4(update, context):
    text = "IT магазин"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    media_group = [
        InputMediaPhoto(media=open('src/image_shop_1.png', 'rb'), caption="Очки виртуальной реальности"),
        InputMediaPhoto(media=open('src/image_shop_2.png', 'rb'), caption="Графический планшет"),
        InputMediaPhoto(media=open('src/image_shop_3.png', 'rb'), caption="Гусь-обнимусь"),
        InputMediaPhoto(media=open('src/image_shop_4.png', 'rb'), caption="Настольная игра"),
        InputMediaPhoto(media=open('src/image_shop_5.png', 'rb'), caption="Магкая игрушка - Заяц")
    ]
    context.bot.send_media_group(chat_id=update.effective_chat.id, media=media_group)
    keyboard = [
        [InlineKeyboardButton("Перейти на сайт", url='https://traektoriya-edu.ru/shop')],
        [InlineKeyboardButton("Назад", callback_data='back')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Благодаря своей активности в ходе прохождения стажировки ребята заработывают очки знаний, умений и навыков. В дальнейшем они могут обменять свои накопления в ИТ магазине.\n\nОформлять заказ можно на сайте, а забрать в офисе Траектории!",
                             reply_markup=reply_markup)

def button5(update, context):
    text = "Наша команда"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    media_group = [
        InputMediaPhoto(media=open('src/Image_about_1.png', 'rb'), caption="Наши ценности"),
        InputMediaPhoto(media=open('src/Image_about_2.png', 'rb'), caption="Команда"),
        InputMediaPhoto(media=open('src/Image_about_3.png', 'rb'), caption="Команда"),
        InputMediaPhoto(media=open('src/Image_about_4.png', 'rb'), caption="Команда"),
    ]
    context.bot.send_media_group(chat_id=update.effective_chat.id, media=media_group)
    keyboard = [
        [InlineKeyboardButton("Перейти на сайт", url='https://traektoriya-edu.ru/teachers')],
        [InlineKeyboardButton("Новости", url='https://traektoriya-edu.ru/blog')],
        [InlineKeyboardButton("Назад", callback_data='back')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Наша команда - это семья, готовая развиваться и обучать учеников",
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
