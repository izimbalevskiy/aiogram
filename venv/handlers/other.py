from aiogram import types, Dispatcher
import json, string
from create_bot import dp


# @dp.message_handler()
async def filtr_mes(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('exception.json')))) != set():
        await message.reply('сам такой')
        await message.delete()



def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(filtr_mes)
