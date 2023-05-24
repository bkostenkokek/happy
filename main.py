import os
import logging
from dotenv import load_dotenv
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, Dispatcher, executor, types
import database as db
from keyboards import markup

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

    await message.answer(f'Привіт {message.from_user.username}!', reply_markup=markup)


@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    data = await message.answer(message.web_app_data.data)
    # await db.insert_data(telegram_id=data['chat']['id'],
    #                      username=data['chat']['username'],
    #                      name=,
    #                      date=)
    print(data)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, on_startup=on_startup)
