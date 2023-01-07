from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

language_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇸 English", callback_data="en"),
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data="ru"),
        ],
    ]
)
