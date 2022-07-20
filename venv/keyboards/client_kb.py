from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

#клиент клавиатура

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Меню')
b4 = KeyboardButton('Поделиться номером', request_contact=True)
b5 = KeyboardButton('Отправить геолокацию', request_location=True)

kb_client = ReplyKeyboardMarkup (resize_keyboard=True)

kb_client.row(b1,b2,b3).row(b4,b5)

#админ клавиатура

a1 = KeyboardButton('Отмена')
a2 = KeyboardButton ('Загрузить')
a3 = KeyboardButton ('Удалить')
kb_stop = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_stop.add(a1).row(a2,a3)
