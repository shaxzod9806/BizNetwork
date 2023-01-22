from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

menu_we_would_meet = CallbackData("show", "level", "choices", "button", "k")


def make_callback_data_would_meet(level, choices='', button='', k=''):
    return menu_we_would_meet.new(
        level=level, choices=choices, button=button, k=k)


async def make_menu_we_would_meet_call(owners='', chairman='', ceo='',
                                       c_level='', departament='', mid_level='', other_we_would_meet='', lang='en'):
    button_next = ''
    if lang == "en":
        button_next += '➡ Next ➡'
        owners += "Owners/Investors"
        chairman += 'Chairman/Deputy Chairman'
        ceo += 'CEO/President'
        c_level += 'C-level CCO/CTO/CMO/CPO/CFO/CIO/CBDO/CHRO/COO/CSO/'
        departament += 'Department Directors'
        mid_level += 'Mid-level Managers'
        other_we_would_meet += 'Other'
    else:
        button_next += "➡ Далее ➡"
        owners += "Владельцы/Инвесторы"
        chairman += 'Председатель/Заместитель Председателя'
        ceo += 'генеральный директор / президент'
        c_level += 'C-уровень  CCO/CTO/CMO/CPO/CFO/CIO/CBDO/CHRO/COO/CSO/'
        departament += 'Директора департаментов'
        mid_level += 'Менеджеры среднего звена'
        other_we_would_meet += 'Другой'

    markup = InlineKeyboardMarkup(row_width=1)
    markup.row(
        InlineKeyboardButton(
            text=owners,
            callback_data=make_callback_data_would_meet(
                level='level', button='owners',
            )
        ),
    )
    markup.row(InlineKeyboardButton(
        text=chairman,
        callback_data=make_callback_data_would_meet(
            level='level',
            button='chairman',
        )
    ), )
    markup.row(InlineKeyboardButton(
        text=ceo,
        callback_data=make_callback_data_would_meet(
            level='1',
            button='ceo'
        )
    ), )
    markup.row(InlineKeyboardButton(
        text=c_level,
        callback_data=make_callback_data_would_meet(
            level='level',
            button='c_level'
        )
    )
    )
    markup.row(InlineKeyboardButton(
        text=departament,
        callback_data=make_callback_data_would_meet(
            level='level',
            button='departament'
        )
    )
    )

    markup.row(InlineKeyboardButton(
        text=mid_level,
        callback_data=make_callback_data_would_meet(
            level='level',
            button='mid_level'
        )
    )
    )

    markup.row(InlineKeyboardButton(
        text=other_we_would_meet,
        callback_data=make_callback_data_would_meet(
            level='level',
            button='other_we_would_meet'
        )
    )
    )
    markup.row(InlineKeyboardButton(
        text=button_next,
        callback_data=make_callback_data_would_meet(
            level='level',
            button="➡ Next ➡"
        )
    )
    )

    return markup
