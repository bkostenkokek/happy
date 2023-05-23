import asyncio
import os
import logging
from dotenv import load_dotenv
from aiogram.types.web_app_info import WebAppInfo
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, Dispatcher, executor, types
import database as db
from keyboards import key

load_dotenv()

logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)

TOKEN = os.environ.get('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


async def on_startup(_):
    await db.db_start()
    logger.info('База даних створена')


class FormState(StatesGroup):
    name = State()
    age = State()
    gender = State()


@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await db.init_user(message.from_user.id, message.from_user.username)
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("add_birthday", web_app=WebAppInfo(url="https://bkostenkokek.github.io/happy/")))
    await message.answer(f'Привіт {message.from_user.username}! \nБот створений для слідкування за днями народження!',
                         reply_markup=markup)


@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    await message.answer(message.web_app_data.data)
# @dp.message_handler(commands=['add_birthday'])
# async def hello(message: types.Message):
#     await message.answer(f'{message.from_user.id}  ку ')
#
#     # await db.add_birthday(telegram_id=message.from_user.id, name, date)
#
#
# @dp.message_handler(commands=['get_birthdays'])
# async def hello(message: types.Message):
#     await message.answer(f'{message.from_user.username}  ку ')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, on_startup=on_startup)
