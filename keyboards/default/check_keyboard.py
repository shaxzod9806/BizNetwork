from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

check_keyboard_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✅ YES'),
            KeyboardButton(text='❌ NO'),
        ],
    ],
    resize_keyboard=True
)

check_keyboard_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✅ ДА'),
            KeyboardButton(text='❌ НЕТ'),
        ],
    ],
    resize_keyboard=True
)
