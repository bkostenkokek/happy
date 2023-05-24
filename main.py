import os
import json
import logging

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import database as db
from keyboards import markup

load_dotenv()

logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)

TOKEN = os.environ.get('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
storage = MemoryStorage()


class DeleteStatesGroup(StatesGroup):
    entry_id = State()


async def on_startup(_):
    await db.db_start()
    logger.info('База даних створена')


@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await db.init_user(message.from_user.id, message.from_user.username)
    await message.answer(f'Привіт {message.from_user.username}!', reply_markup=markup)


@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    data = message.web_app_data.data
    await db.insert_data(telegram_id=message.from_user.id,
                         name=json.loads(data)['name'],
                         date=json.loads(data)['date'])


@dp.message_handler(text="Побачити дні народження")
async def birthday_handler(message: types.Message):
    user_id = message.from_user.id
    birthdays = db.get_birthdays_by_telegram_id(user_id)
    await message.answer(f"Дні народження:\n{birthdays}")


@dp.message_handler(text="Видатили День народження")
async def birthday_handler(message: types.Message):
    await message.reply("Введите ID записи, которую вы хотите удалить:")
    await DeleteStatesGroup.entry_id.set()


@dp.message_handler(content_types=['text'], state=DeleteStatesGroup.entry_id)
async def delete_entry_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['entry_id'] = message
        print(data)
    await state.finish()
    await message.reply("Удалено")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, on_startup=on_startup)
