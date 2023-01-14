from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# language_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="🇺🇸 English", callback_data="en"),
#             InlineKeyboardButton(text="🇷🇺 Русский", callback_data="ru"),
#         ],
#     ]
# )
language_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🇺🇸 English'),
            KeyboardButton(text='🇷🇺 Русский'),
        ],
    ],
    resize_keyboard=True
)
