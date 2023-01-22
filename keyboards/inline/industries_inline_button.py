from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

menu_business_type = CallbackData("show", "level", "choices", "button", "k")


def make_callback_data_industries(level, choices='', button='', k=''):
    return menu_business_type.new(
        level=level, choices=choices, button=button, k=k)


async def make_industries_call(accommodation='', administrative='', construction='',
                               consumer='', education='', entertainment='',
                               farming='', financial='', government='',
                               holding='', hospitals='',
                               manufacturing='', oil='', professional='', real='',
                               retail='', technology='', transportation='',
                               utilities='', wholesale='', other_industries='', lang='en'):
    markup = InlineKeyboardMarkup(row_width=1)
    if lang == 'en':
        accommodation += "Accommodation Services"
        administrative += 'Administrative and Support Services'
        construction += 'Construction'
        consumer += 'Consumer Services'
        education += 'Education'
        entertainment += 'Entertainment'
        farming += 'Farming, Ranching, Forestry'
        financial += 'Financial Services'
        government += 'Government'
        holding += 'Holding Companies'
        hospitals += 'Hospitals and Health Care'
        manufacturing += 'Manufacturing'
        oil += 'Oil, Gas, and Mining'
        professional += 'Professional Services'
        real += 'Real Estate and Equipment Rental Services'
        retail += 'Retail'
        technology += 'Technology, Information and Media'
        transportation += 'Transportation, Logistics, Supply Chain and Storage'
        utilities += 'Utilities'
        wholesale += 'Wholesale'
        other_industries += 'Other'
        button_next = '➡ Next ➡'

    else:
        accommodation += "Услуги по размещению"
        administrative += 'Административные и вспомогательные службы'
        construction += 'Строительство'
        consumer += 'Потребительские услуги'
        education += 'Образование'
        entertainment += 'Развлечения'
        farming += 'Сельское хозяйство, Ранчо, Лесное хозяйство'
        financial += 'Финансовые услуги'
        government += 'Правительство'
        holding += 'Холдинговые компании'
        hospitals += 'Больницы и здравоохранение'
        manufacturing += 'Производство'
        oil += 'Нефть, газ и горнодобывающая промышленность'
        professional += 'Профессиональные услуги'
        real += 'Услуги по аренде недвижимости и оборудования'
        retail += 'Розничная торговля'
        technology += 'Технологии, информация и СМИ'
        transportation += 'Транспорт, логистика, цепочка поставок и хранение'
        utilities += 'Утилиты'
        wholesale += 'Оптовые продажи'
        other_industries += 'Другой'
        button_next = "➡ Далее ➡"

    markup.row(
        InlineKeyboardButton(
            text=accommodation,
            callback_data=make_callback_data_industries(
                level='level', button='accommodation', k='k'
            )
        ),
    )
    markup.row(InlineKeyboardButton(
        text=administrative,
        callback_data=make_callback_data_industries(
            level='level',
            button='administrative', k='k'
        )
    ), )
    markup.row(InlineKeyboardButton(
        text=consumer,
        callback_data=make_callback_data_industries(
            level='1',
            button='consumer', k='k'
        )
    ), )
    markup.row(InlineKeyboardButton(
        text=farming,
        callback_data=make_callback_data_industries(
            level='level',
            button='farming', k='k'
        )), )

    markup.row(InlineKeyboardButton(
        text=hospitals,
        callback_data=make_callback_data_industries(
            level='level',
            button='hospitals', k='k'
        )), )

    markup.row(InlineKeyboardButton(
        text=oil,
        callback_data=make_callback_data_industries(
            level='level',
            button='oil', k='k'
        )), )
    markup.row(InlineKeyboardButton(
        text=real,
        callback_data=make_callback_data_industries(
            level='level',
            button='real', k='k'
        )), )

    markup.row(InlineKeyboardButton(
        text=technology,
        callback_data=make_callback_data_industries(
            level='level',
            button='technology', k='k'
        )), )

    markup.row(InlineKeyboardButton(
        text=transportation,
        callback_data=make_callback_data_industries(
            level='level',
            button='transportation', k='k'
        )), )

    markup.row(
        InlineKeyboardButton(
            text=construction,
            callback_data=make_callback_data_industries(
                level='level',
                button='construction', k='k'
            )),
        InlineKeyboardButton(
            text=education,
            callback_data=make_callback_data_industries(
                level='level',
                button='education', k='k'
            )),
    )

    markup.row(
        InlineKeyboardButton(
            text=entertainment,
            callback_data=make_callback_data_industries(
                level='level',
                button='entertainment', k='k'
            )),
        InlineKeyboardButton(
            text=financial,
            callback_data=make_callback_data_industries(
                level='level',
                button='financial', k='k'
            )),
    )
    markup.row(
        InlineKeyboardButton(
            text=holding,
            callback_data=make_callback_data_industries(
                level='level',
                button='holding', k='k'
            )),
        InlineKeyboardButton(
            text=manufacturing,
            callback_data=make_callback_data_industries(
                level='level',
                button='manufacturing', k='k'
            )),
    )
    markup.row(
        InlineKeyboardButton(
            text=professional,
            callback_data=make_callback_data_industries(
                level='level',
                button='professional', k='k'
            )),
        InlineKeyboardButton(
            text=wholesale,
            callback_data=make_callback_data_industries(
                level='level',
                button='wholesale', k='k'
            )),
    )

    markup.row(
        InlineKeyboardButton(
            text=retail,
            callback_data=make_callback_data_industries(
                level='level',
                button='retail', k='k'
            )),
        InlineKeyboardButton(
            text=utilities,
            callback_data=make_callback_data_industries(
                level='level',
                button='utilities', k='k'
            )),
    )

    markup.row(
        InlineKeyboardButton(
            text=government,
            callback_data=make_callback_data_industries(
                level='level',
                button='government', k='k'
            )),
        InlineKeyboardButton(
            text=other_industries,
            callback_data=make_callback_data_industries(
                level='level',
                button='other_industries', k='k'
            )),
    )
    markup.row(InlineKeyboardButton(
        text=button_next,
        callback_data=make_callback_data_industries(
            level='level',
            button="➡ Next ➡", k='k'
        )), )

    return markup
