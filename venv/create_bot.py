from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token='5566324578:AAFwZ3G5HwajVVfR4hefk_o3nApkfBBPrhY')
dp = Dispatcher(bot, storage=storage)
