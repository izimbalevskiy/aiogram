from aiogram import types, Dispatcher
from create_bot import dp,bot
from keyboards import kb_client
from data_base import sqlite_db

#@dp.message_handler(commands=['start','help'])
async def start(message:types.Message):
    try:

        await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup=kb_client)

    except:
        await message.reply('Напишите боту: \n https://t.me/BeautifulPizzaBot')

#@dp.message_handler(commands=['Режим_работы'])
async def work_time(message: types.message):
    await bot.send_message(message.from_user.id, 'Пн-Пт: с 10.00 до 22.00 \nСб-Вс: с 10.00 до 24.00')

#@dp.message_handler(commands=['Расположение'])
async def location(message: types.message):
    await bot.send_message(message.from_user.id, 'Ул. Тестовая, 1')

@dp.message_handler(commands=['Меню'])
async def pizza_menu (message: types.Message):
    await sqlite_db.sql_read(message)
    sqlite_db.sql_start()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start','help'])
    dp.register_message_handler(work_time, commands=['Режим_работы'])
    dp.register_message_handler(location, commands=['Расположение'])
    dp.register_message_handler(pizza_menu, commands=['Меню'])
