from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

meeting_times = CallbackData("show", "level", "choices", "button", "k")


def make_callback_data_meeting_times(level, choices='', button='', k=''):
    return meeting_times.new(
        level=level, choices=choices, button=button, k=k)


async def make_menu_meeting_times_call(january='', february='', march='', april='',
                                       may='', june='', july='', august='',
                                       september='', october='', november='',
                                       december='', soonest_time='',
                                       other_meeting_times='', lang='en'
                                       ):
    button_next = ''
    if lang == 'en':
        january += 'January'
        february += 'February'
        march += 'March'
        april += 'April'
        may += 'May'
        june += 'June'
        july += 'July'
        august += 'August'
        september += 'September'
        october += 'October'
        november += 'November'
        december += 'December'
        soonest_time += 'Soonest time'
        other_meeting_times += 'Other'
        button_next += '➡ Next ➡'
    else:
        january += 'Январь.'
        february += 'Февраль'
        march += 'Маршировать'
        april += 'Апреля'
        may += 'Может'
        june += 'Июнь'
        july += 'Июль'
        august += 'Август'
        september += 'Сентябрь'
        october += 'Октябрь'
        november += 'Ноябрь'
        december += 'Декабрь'
        soonest_time += 'Ближайшее время'
        other_meeting_times += 'Другой'
        button_next = "➡ Далее ➡"
    markup = InlineKeyboardMarkup(row_width=1)
    markup.row(
        InlineKeyboardButton(
            text=january,
            callback_data=make_callback_data_meeting_times(
                level='level', button='january',
            )
        ),
        InlineKeyboardButton(
            text=february,
            callback_data=make_callback_data_meeting_times(
                level='level', button='february',
            )
        ),
    )
    markup.row(
        InlineKeyboardButton(
            text=march,
            callback_data=make_callback_data_meeting_times(
                level='level',
                button='march',
            )
        ),
        InlineKeyboardButton(
            text=april,
            callback_data=make_callback_data_meeting_times(
                level='level',
                button='april',
            )
        ), )
    markup.row(
        InlineKeyboardButton(
            text=may,
            callback_data=make_callback_data_meeting_times(
                level='1',
                button='may'
            )
        ),
        InlineKeyboardButton(
            text=june,
            callback_data=make_callback_data_meeting_times(
                level='1',
                button='june'
            )
        ), )

    markup.row(
        InlineKeyboardButton(
            text=july,
            callback_data=make_callback_data_meeting_times(
                level='1',
                button='july'
            )
        ),
        InlineKeyboardButton(
            text=august,
            callback_data=make_callback_data_meeting_times(
                level='1',
                button='august'
            )
        ), )

    markup.row(
        InlineKeyboardButton(
            text=september,
            callback_data=make_callback_data_meeting_times(
                level='1',
                button='september'
            )
        ),
        InlineKeyboardButton(
            text=october,
            callback_data=make_callback_data_meeting_times(
                level='1',
                button='october'
            )
        ), )

    markup.row(
        InlineKeyboardButton(
            text=november,
            callback_data=make_callback_data_meeting_times(
                level='1',
                button='november'
            )
        ),
        InlineKeyboardButton(
            text=december,
            callback_data=make_callback_data_meeting_times(
                level='1',
                button='december'
            )
        ), )

    markup.row(
        InlineKeyboardButton(
            text=soonest_time,
            callback_data=make_callback_data_meeting_times(
                level='level',
                button='soonest_time'
            )
        ),
        InlineKeyboardButton(
            text=other_meeting_times,
            callback_data=make_callback_data_meeting_times(
                level='level',
                button='other_meeting_times'
            )
        )
    )
    markup.row(InlineKeyboardButton(
        text=button_next,
        callback_data=make_callback_data_meeting_times(
            level='level',
            button='➡ Next ➡'
        )
    )
    )
    return markup
