from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

meeting_formats = CallbackData("show", "level", "choices", "button", "k")


def make_callback_data_meeting_formats(level, choices='', button='', k=''):
    return meeting_formats.new(
        level=level, choices=choices, button=button, k=k)


async def make_menu_meeting_formats_call(offline='', online='',
                                         combined='', other_meeting_formats='', lang='en'):
    button_next = ''
    if lang == "en":
        offline += 'Offline'
        online += 'Online'
        combined += 'Combined'
        other_meeting_formats += 'Other'
        button_next = '➡ Next ➡'
    else:
        offline += 'Не в сети'
        online += 'Онлайн'
        combined += 'Комбинированный'
        other_meeting_formats += 'Другой'
        button_next += "➡ Далее ➡"
    markup = InlineKeyboardMarkup(row_width=1)
    markup.row(
        InlineKeyboardButton(
            text=offline,
            callback_data=make_callback_data_meeting_formats(
                level='level', button='offline',
            )
        ),
    )
    markup.row(InlineKeyboardButton(
        text=online,
        callback_data=make_callback_data_meeting_formats(
            level='level',
            button='online',
        )
    ), )
    markup.row(InlineKeyboardButton(
        text=combined,
        callback_data=make_callback_data_meeting_formats(
            level='1',
            button='combined'
        )
    ), )

    markup.row(InlineKeyboardButton(
        text=other_meeting_formats,
        callback_data=make_callback_data_meeting_formats(
            level='level',
            button='other_meeting_formats'
        )
    )
    )
    markup.row(InlineKeyboardButton(
        text=button_next,
        callback_data=make_callback_data_meeting_formats(
            level='level',
            button='➡ Next ➡'
        )
    )
    )

    return markup
