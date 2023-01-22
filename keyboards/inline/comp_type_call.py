from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

company_type_keyboard_en = InlineKeyboardMarkup(
    inline_keyboard=[
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
        # [
        #     InlineKeyboardButton(text='⬅', callback_data='⬅'),
        #     InlineKeyboardButton(text='➡', callback_data='➡'),
        # ],
    ]
)

company_type_keyboard_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Сервисы', callback_data='services'),
        ],
        [
            InlineKeyboardButton(text='производитель', callback_data='manufacturer'),

        ],
        [
            InlineKeyboardButton(text='распределитель', callback_data='distributor'),

        ],
        [
            InlineKeyboardButton(text='инвестор', callback_data='investor'),

        ],
        [
            InlineKeyboardButton(text='НПО', callback_data='NGO'),

        ],
        [
            InlineKeyboardButton(text='правительство', callback_data='government'),
        ],
        [
            InlineKeyboardButton(text='Другой', callback_data='other')

        ],
        # [
        #     InlineKeyboardButton(text='⬅', callback_data='⬅'),
        #     InlineKeyboardButton(text='➡', callback_data='➡'),
        # ],
    ]
)
