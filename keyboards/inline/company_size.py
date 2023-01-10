from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

company_size_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text='0-499$K', callback_data='0-499$K'),
    ],
        [
            InlineKeyboardButton(text='500$K-999$K', callback_data='500$K-999$K'),

        ],
        [
            InlineKeyboardButton(text='1$M-9.9$M', callback_data='1$M-9.9$M'),

        ],
        [
            InlineKeyboardButton(text='10$M-99$M', callback_data='10$M-99$M'),

        ],
        [
            InlineKeyboardButton(text='100$M-499$M', callback_data='100$M-499$M'),

        ],
        [
            InlineKeyboardButton(text='500$M-999$M', callback_data='500$M-999$M'),
        ],
        [
            InlineKeyboardButton(text='1$B-9.9$B', callback_data='1$B-9.9$B')

        ],
        [
            InlineKeyboardButton(text='10$B+', callback_data='10$B+')

        ],
        [
            InlineKeyboardButton(text='Other', callback_data='Other')

        ],
        [
            InlineKeyboardButton(text='⬅', callback_data='⬅'),
            InlineKeyboardButton(text='➡', callback_data='➡'),
        ]
    ]
)
