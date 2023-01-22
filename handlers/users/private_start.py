from aiogram.dispatcher import FSMContext

from keyboards.inline.business_type_call import make_business_type_call
from keyboards.inline.comp_type_call import company_type_keyboard_en, company_type_keyboard_ru

from keyboards.inline.company_size import company_size_keyboard
from loader import dp, bot
from aiogram import types
from aiogram.types import CallbackQuery, Message
from states.personal_data import PersonalDataPrivate


# @dp.message_handler(text="/I_want", state="*")
@dp.message_handler(text="I'm Interested", state="*")
async def answer_check(message: Message, state: FSMContext):
    await message.answer(f"What is your company Type", reply_markup=company_type_keyboard_en)
    await PersonalDataPrivate.company_type.set()
    await state.update_data({
        "language": "en"
    })


@dp.message_handler(text="Мне это интересно", state="*")
async def answer_check(message: Message, state: FSMContext):
    await message.answer("Тип вашей компании", reply_markup=company_type_keyboard_ru)
    await PersonalDataPrivate.company_type.set()
    await state.update_data({
        "language": "ru"
    })


@dp.callback_query_handler(state=PersonalDataPrivate.company_type)
async def answer_company_type(call: CallbackQuery, state: FSMContext):
    company_type = call.data
    data = await state.get_data()
    lang = data.get('language')
    await call.message.delete()
    if lang == "en":
        await call.message.answer(f"<b>What is your company website?</b>",
                                  reply_markup=types.ReplyKeyboardRemove())
    else:
        await call.message.answer("<b>Какой сайт у вашей компании?</b>",
                                  reply_markup=types.ReplyKeyboardRemove())
    await state.update_data({
        "comp_type": company_type
    })
    await PersonalDataPrivate.company_website.set()


@dp.message_handler(state=PersonalDataPrivate.company_website)
async def answer_company_website(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    website = message.text
    if lang == 'en':
        await message.answer("<b>Email</b>")
    else:
        await message.answer("<b>Эл. адрес</b>")
    await state.update_data({
        "website": website
    })
    await PersonalDataPrivate.email.set()


@dp.message_handler(state=PersonalDataPrivate.email)
async def answer_email(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    email = message.text
    if lang == 'en':
        await message.answer("<b>Enter your birthday:</b>\n"
                             "dd.mm.yyyy\n\n"
                             "Example: 31.12.1990")
    else:
        await message.answer("<b>Введите свой день рождения</b>\n"
                             "дд.мм.гггг\n\n"
                             "Пример: 31.12.1990")
    await state.update_data({
        "email": email
    })
    await PersonalDataPrivate.birthday.set()


@dp.message_handler(state=PersonalDataPrivate.birthday)
async def answer_birthday(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    birthday = message.text
    if lang == 'en':
        await message.answer("<b>Mobile number:</b>\n\n"
                             "Example: +998903334466")
    else:
        await message.answer("<b>Мобильный номер:</b>\n\n"
                             "Пример: +998903334466")
    await state.update_data({
        "birthday": birthday
    })
    await PersonalDataPrivate.phone_number.set()


@dp.message_handler(state=PersonalDataPrivate.phone_number)
async def answer_phone_number(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    print(lang)
    phone_number = message.text
    keyboard = await company_size_keyboard(lang)
    if lang == 'en':
        await message.answer("<b>Your Company Annual Turnover in USD</b>",
                             reply_markup=keyboard)
    else:
        await message.answer("<b>Годовой оборот вашей компании в долларах США</b>",
                             reply_markup=keyboard)
    await state.update_data({
        "phone_number": phone_number
    })
    await PersonalDataPrivate.company_size.set()


@dp.callback_query_handler(state=PersonalDataPrivate.company_size)
async def answer_company_size(call: CallbackQuery, state: FSMContext):
    await state.update_data({
        'B2B': "  B2B", "B2G": "  B2G", "B2C": "  B2C"
    })
    data = await state.get_data()
    print(data)
    lang = data.get('language')
    company_size = call.data
    print(company_size)
    b2b = data.get("B2B")
    b2g = data.get('B2G')
    b2c = data.get('B2C')
    if lang == 'en':
        await call.message.edit_text("<b>We are interested in following Matchmaking</b>")
        keyboard = await make_business_type_call(b2b, b2g, b2c, lang)
        await call.message.edit_reply_markup(
            reply_markup=keyboard)
    else:
        keyboard = await make_business_type_call(b2b, b2g, b2c, lang)
        await call.message.edit_text("<b>Мы заинтересованы в том, чтобы следить за сватовством</b>")
        await call.message.edit_reply_markup(reply_markup=keyboard)

    await state.update_data({
        "company_size": company_size
    })
    print('await state.get_data()')
    print(await state.get_data())
    await PersonalDataPrivate.business_type.set()
    print('await state.get_data()')
