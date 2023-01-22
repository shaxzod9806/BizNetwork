from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

menu_hobbies = CallbackData("show", "level", "choices", "button", "k")


def make_callback_data_menu_hobbies(level, choices='', button='', k=''):
    return menu_hobbies.new(
        level=level, choices=choices, button=button, k=k)


async def make_hobbies_call(sports='', mindfulness='', outdoor='',
                            health_wellness='', startups='', entrepreneurship='',
                            investments='', business_breakfasts='', b2b_meetings='',
                            business_traveling='', self_development='', international_relations='',
                            professional_networking='', business_games='',
                            other_hobbies='', lang='en'):
    markup = InlineKeyboardMarkup(row_width=1)
    if lang == 'en':
        sports += 'Sports'
        mindfulness += 'Mindfulness'
        outdoor += 'Outdoor'
        health_wellness += 'Health & Wellness'
        startups += 'Startups'
        entrepreneurship += 'Entrepreneurship'
        investments += 'Investments'
        business_breakfasts += 'Business Breakfasts'
        b2b_meetings += 'B2B Meetings'
        business_traveling += 'Business Traveling'
        self_development += 'Self Development'
        international_relations += 'International Relations'
        professional_networking += 'Professional Networking'
        business_games += 'Business Games'
        other_hobbies += 'Other'
        button_next = "➡ Next ➡"
    else:
        sports += 'Спорт'
        mindfulness += 'Внимательность'
        outdoor += 'Открытый'
        health_wellness += 'Здоровье и благополучие'
        startups += 'Стартапы'
        entrepreneurship += 'Предпринимательство'
        investments += 'Инвестиции'
        business_breakfasts += 'Деловые завтраки'
        b2b_meetings += 'Встречи B2B'
        business_traveling += 'Деловые поездки'
        self_development += 'Саморазвитие'
        international_relations += 'Международные отношения'
        professional_networking += 'Профессиональное общение'
        business_games += 'Деловые игры'
        other_hobbies += 'Другое'

        button_next = '➡ Далее ➡'

    markup.row(
        InlineKeyboardButton(
            text=sports,
            callback_data=make_callback_data_menu_hobbies(
                level='level', button='sports', k='k'
            )
        ),
        InlineKeyboardButton(
            text=mindfulness,
            callback_data=make_callback_data_menu_hobbies(
                level='level', button='mindfulness', k='k'
            )
        ),
    )
    markup.row(InlineKeyboardButton(
        text=outdoor,
        callback_data=make_callback_data_menu_hobbies(
            level='level',
            button='outdoor', k='k'
        )
    ),
        InlineKeyboardButton(
            text=health_wellness,
            callback_data=make_callback_data_menu_hobbies(
                level='level',
                button='health_wellness', k='k'
            )
        ), )
    markup.row(InlineKeyboardButton(
        text=startups,
        callback_data=make_callback_data_menu_hobbies(
            level='1',
            button='startups', k='k'
        )
    ),
        InlineKeyboardButton(
            text=entrepreneurship,
            callback_data=make_callback_data_menu_hobbies(
                level='1',
                button='entrepreneurship', k='k'
            )
        ), )
    markup.row(InlineKeyboardButton(
        text=investments,
        callback_data=make_callback_data_menu_hobbies(
            level='level',
            button='investments', k='k'
        )),
        InlineKeyboardButton(
            text=business_breakfasts,
            callback_data=make_callback_data_menu_hobbies(
                level='level',
                button='business_breakfasts', k='k'
            )), )

    markup.row(InlineKeyboardButton(
        text=b2b_meetings,
        callback_data=make_callback_data_menu_hobbies(
            level='level',
            button='b2b_meetings', k='k'
        )),
        InlineKeyboardButton(
            text=business_traveling,
            callback_data=make_callback_data_menu_hobbies(
                level='level',
                button='business_traveling', k='k'
            )), )

    markup.row(InlineKeyboardButton(
        text=self_development,
        callback_data=make_callback_data_menu_hobbies(
            level='level',
            button='self_development', k='k'
        )),
        InlineKeyboardButton(
            text=international_relations,
            callback_data=make_callback_data_menu_hobbies(
                level='level',
                button='international_relations', k='k'
            )), )
    markup.row(InlineKeyboardButton(
        text=professional_networking,
        callback_data=make_callback_data_menu_hobbies(
            level='level',
            button='professional_networking', k='k'
        )),
        InlineKeyboardButton(
            text=business_games,
            callback_data=make_callback_data_menu_hobbies(
                level='level',
                button='business_games', k='k'
            )), )
    markup.row(InlineKeyboardButton(
        text=other_hobbies,
        callback_data=make_callback_data_menu_hobbies(
            level='level',
            button='other_hobbies', k='k'
        )), )
    markup.row(InlineKeyboardButton(
        text=button_next,
        callback_data=make_callback_data_menu_hobbies(
            level='level',
            button='➡ Next ➡', k='k'
        )), )

    return markup
