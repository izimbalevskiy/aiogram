from create_bot import dp
from aiogram.utils import executor
from handlers import client, admin, other
from data_base import sqlite_db





client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)



executor.start_polling(dp, skip_updates=True, )
