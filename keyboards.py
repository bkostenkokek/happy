from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

key = ReplyKeyboardMarkup(resize_keyboard=True)
key.add('').add('Показати Дні народження').add('Видатили День народження')

markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(
    KeyboardButton("Додати День народження", web_app=WebAppInfo(url="https://bkostenkokek.github.io/happy"))).add(
    'Показати Дні народження').add('Видатили День народження')
