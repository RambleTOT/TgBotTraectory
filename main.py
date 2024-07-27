from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv
import os

# Обработчик команды /start
def start(update, context):
    user = update.message.from_user
    text = f"Привет, {user.first_name}!\nМеня зовут Алекс! Я - стажер IT компании Траектория, вместе со мной ты освоишь мир цифровых технологий. Хочешь узнать о нашей системе обучения ? Тогда смело нажимай кнопку «Меню».\nА еще не забывай переходить на наш сайт, там для тебя много актуальной информации."
    keyboard = [InlineKeyboardButton("На сайт Траектория", url='https://traektoriya-edu.ru/')], [InlineKeyboardButton("Меню", callback_data='menu')]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('src/start_image.png', 'rb'))
    context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=reply_markup)

# Обработчик команды /menu
def menu(update, context):
    text = "Добро пожаловать в Центр дополнительного образования «Траектория» 🙌🏼! Здесь обучаются взрослые и дети школьного возраста. А ты уже учишься у нас?"

    keyboard = [
        [InlineKeyboardButton("Да, обучаюсь", callback_data='yes')],
        [InlineKeyboardButton("Планирую свое обучение", callback_data='no')],
        [InlineKeyboardButton("Информация о центре", callback_data='info')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=reply_markup)

# Обработчик нажатий на кнопки
def button_click(update, context):
    query = update.callback_query
    if query.data == "yes":
        buttonYes(update, context)
    if query.data == "no":
        buttonNo(update, context)
    if query.data == 'button2':
        button2(update, context)
    if query.data == 'menu' or query.data == 'back':
        menu(update, context)
    if query.data == 'backNo':
        buttonNo(update, context)
    if query.data == 'backYes':
        buttonYes(update, context)
    if query.data == 'button3':
        button3(update, context)
    if query.data == 'buttonQuestion':
        buttonQuestion(update, context)
    if query.data == 'info':
        buttonInfo(update, context)
    if query.data == 'buttonContact':
        buttonContact(update, context)
    if query.data == 'buttonConsultation':
        buttonConsultation(update, context)


# Обработчик кнопки "Назад"
def back_button(update, context):
    menu(update, context)  # Возвращаемся к сообщению с меню

def buttonYes(update, context):
    text = "Информация для наших учеников"
    keyboard = [
        [InlineKeyboardButton("Треки", url='https://traektoriya-edu.ru/middle')],
        [InlineKeyboardButton("Расписание групп", url='https://traektoriya-edu.ru/timetable')],
        [InlineKeyboardButton("Задать вопрос в учебную часть", callback_data='buttonQuestion')],
        [InlineKeyboardButton("Внеучебные мероприятия", url='https://vk.com/trek_2022')],
        [InlineKeyboardButton("Оформить заказ в ИТ магазине ", url='https://traektoriya-edu.ru/shop')],
        [InlineKeyboardButton("Назад", callback_data='back')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=reply_markup)

def back_button_no(update, context):
    buttonNo(update, context)

def buttonNo(update, context):
    text = "Информация для будущих учеников"
    keyboard = [
        [InlineKeyboardButton("Отзывы (2GIS)", url='https://2gis.ru/yaroslavl/firm/70000001067234653/tab/reviews')],
        [InlineKeyboardButton("Записаться на пробный урок ", url='https://vk.com/app6013442_-215628262#form_id=1')],
        [InlineKeyboardButton("Образовательные треки", callback_data='button3')],
        [InlineKeyboardButton("Расписание учебных групп", url='https://traektoriya-edu.ru/timetable')],
        [InlineKeyboardButton("Получить консультацию", callback_data='buttonConsultation')],
        [InlineKeyboardButton("Назад", callback_data='back')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=reply_markup)


def buttonQuestion(update, context):
    text = "Чтобы задать вопрос в учебную часть, вы можете написать на WhatsApp по номеру телефона:\n89806588070"
    keyboard = [
        [InlineKeyboardButton("Назад", callback_data='buttonYes')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=reply_markup)

def button2(update, context):
    keyboard = [
        [InlineKeyboardButton("День открытых дверей", url='https://traektoriya-edu.ru/opendoorsday')],
        [InlineKeyboardButton("Регистрация", url='https://vk.com/trek_2022?w=app6013442_-215628262%2523form_id%253D1')],
        [InlineKeyboardButton("Назад", callback_data='backNo')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text="День открытых дверей в Траектори!\nВ программе вас ждет знакомство с центром, мастер-классы и презентация образовательных программ\nЖдём вас16 сентября с 10::00 до 18:00 по адресу Республиканская, 61 (3 этаж)\nДля регистрации нажмите на кнопку, которя переведет вас на форму ВК",
                             reply_markup=reply_markup)


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
        [InlineKeyboardButton("Младшая школа", url='https://traektoriya-edu.ru/junior')],
        [InlineKeyboardButton("Средняя школа", url='https://traektoriya-edu.ru/middle')],
        [InlineKeyboardButton("Старшая школа", url='https://traektoriya-edu.ru/senior')],
        [InlineKeyboardButton("Назад", callback_data='backNo')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text="В Траектории есть обучающие программы для всех возрастов. Подробнее о каждых групах и записаться можно на сайте",
                             reply_markup=reply_markup)



def buttonInfo(update, context):
    text = "Траектория - это обучение ИТ и КОВОРКИНГ в современном бизнес-центре Ярославля"
    keyboard = [
        [InlineKeyboardButton("ВК сообщество", url='https://vk.com/trek_2022')],
        [InlineKeyboardButton("Фотогаллерея", url='https://yandex.ru/maps/org/trayektoriya/236265512900/?ll=39.877877%2C57.626381&z=15')],
        [InlineKeyboardButton("Внеучебные мероприятия", url='https://traektoriya-edu.ru/events')],
        [InlineKeyboardButton("Позвонить нам", callback_data='buttonContact')],
        [InlineKeyboardButton("Как добраться", url='https://2gis.ru/yaroslavl/firm/70000001067234653/tab/reviews')],
        [InlineKeyboardButton("Назад", callback_data='menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=text,
                             reply_markup=reply_markup)


def buttonContact(update, context):
    text = "Для связи с нами вы можете использовать номер телефона 8 (962) 181-54-29"
    keyboard = [
        [InlineKeyboardButton("Назад", callback_data='info')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=text,
                             reply_markup=reply_markup)

def buttonConsultation(update, context):
    text = "Чтобы с вами связались для консультации, вы должны оставить свои ФИО и номер телфеона"
    keyboard = [
        [InlineKeyboardButton("Назад", callback_data='backNo')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=text,
                             reply_markup=reply_markup)
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))


def echo(update: Update, context: CallbackContext) -> None:
    # Получаем текст сообщения от пользователя
    user_message = 'Данные для консультации:\n' + update.message.text

    # Отправляем сообщение на другой аккаунт
    context.bot.send_message(chat_id=os.getenv('CHAT_TOKEN'), text=user_message)


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
