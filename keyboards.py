from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

markup = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Додати День народження WebApp",
                        web_app=WebAppInfo(url="https://bkostenkokek.github.io/happy"))
         ],
        [KeyboardButton(text="Побачити дні народження")],
        [KeyboardButton(text="Видатили День народження")],
    ],
    resize_keyboard=True)
