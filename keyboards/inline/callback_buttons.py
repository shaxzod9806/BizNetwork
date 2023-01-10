from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

company_type_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🔎 search', switch_inline_query_current_chat='yuk'),
        ],
        [
            InlineKeyboardButton(text='services', callback_data='services'),
        ],
        [
            InlineKeyboardButton(text='manufacturer', callback_data='manufacturer'),

        ],
        [
            InlineKeyboardButton(text='distributor', callback_data='distributor'),

        ],
        [
            InlineKeyboardButton(text='investor', callback_data='investor'),

        ],
        [
            InlineKeyboardButton(text='NGO', callback_data='NGO'),

        ],
        [
            InlineKeyboardButton(text='government', callback_data='government'),
        ],
        [
            InlineKeyboardButton(text='other', callback_data='other')

        ],
        [
            InlineKeyboardButton(text='⬅', callback_data='⬅'),
            InlineKeyboardButton(text='➡', callback_data='➡'),
        ],
    ]
)

business_type_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text='B2B', callback_data='B2B'),
    ],
        [
            InlineKeyboardButton(text='B2G', callback_data='B2G'),

        ],
        [
            InlineKeyboardButton(text='B2C', callback_data='B2C'),

        ],
        [
            InlineKeyboardButton(text='⬅', callback_data='⬅'),
            InlineKeyboardButton(text='➡', callback_data='➡'),
        ],
    ]
)
