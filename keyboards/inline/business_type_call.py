
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

menu_business_type = CallbackData("show", "level", "choices", "button", "k")


def make_callback_data_business_type(level, choices, button, k):
    return menu_business_type.new(
        level=level, choices=choices, button=button, k=k)


async def make_business_type_call(b2b, b2g, b2c, lang):
    button_b2b = b2b
    button_b2g = b2g
    button_b2c = b2c
    button_next = '➡ Next ➡' if lang == 'en' else "➡ Далее ➡"
    markup = InlineKeyboardMarkup(row_width=1)
    markup.row(
        InlineKeyboardButton(
            text=button_b2b,
            callback_data=make_callback_data_business_type(
                level='level', choices=button_b2b, button='B2B', k='k'
            )
        ),
    )
    markup.row(InlineKeyboardButton(
        text=button_b2g,
        callback_data=make_callback_data_business_type(
            level='level',
            choices=button_b2g, button='B2G', k='k'
        )
    ), )
    markup.row(InlineKeyboardButton(
        text=button_b2c,
        callback_data=make_callback_data_business_type(
            level='1',
            choices=button_b2c, button='B2C', k='k'
        )
    ), )
    markup.row(InlineKeyboardButton(
        text=button_next,
        callback_data=make_callback_data_business_type(
            level='level',
            choices='➡ Next ➡', button='➡ Next ➡', k='k'
        )
    )
    )
    return markup
