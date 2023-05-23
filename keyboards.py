from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

markup = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Видатили День народження")],
        [KeyboardButton(text="Додати День народження WebApp",
                        web_app=WebAppInfo(url="https://bkostenkokek.github.io/happy"))
                        # web_app=WebAppInfo(url="https://massonnn.github.io/just-test-pages/"))
         ]],
    resize_keyboard=True)
