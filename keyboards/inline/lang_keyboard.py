from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

language_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🇬🇧 English'),
            KeyboardButton(text='🇷🇺 Русский'),
        ],
    ],
    resize_keyboard=True
)
