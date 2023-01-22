from aiogram.dispatcher import FSMContext
from keyboards.default.request_location import get_keyboard
from keyboards.inline.hobbies_callback_button import make_hobbies_call
from loader import dp, bot
from aiogram import types
from aiogram.types import CallbackQuery, Message

from states.personal_data import PersonalData
from utils.get_address import get_address_name
from filters import IsPrivate


@dp.message_handler(IsPrivate(), state=PersonalData.company_name)
async def answer_company_name(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    comp_name = message.text
    await state.update_data({'comp_name': comp_name})
    if lang == 'en':
        await message.answer(f'<b>What is your position in the company:</b>')
    else:
        await message.answer('<b>Введите позицию вашей компании:</b>')
    await PersonalData.company_position.set()


@dp.message_handler(IsPrivate(), state=PersonalData.company_position)
async def answer_company_position(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    comp_position = message.text
    await state.update_data({'comp_position': comp_position})
    if lang == 'en':
        reply = "<b>📌 Select your company address on the map\n or\n" \
                "Click the button below to share your current location:</b>"
    else:
        reply = "<b>📌 Выберите свой адрес проживания на карте\n или\n" \
                "Нажмите кнопку ниже, чтобы поделиться своим текущим местоположением:</b>"
    await message.answer(reply, reply_markup=get_keyboard())
    await PersonalData.company_address.set()


@dp.message_handler(IsPrivate(), state=PersonalData.company_address)
async def answer_re_location_comp(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    if lang == 'en':
        await message.answer(
            '<b>Re-enter your details:\nShare your location:</b>',
            reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer(
            '<b>Повторно введите свои данные:\nПоделитесь своим местоположением:</b>',
            reply_markup=types.ReplyKeyboardRemove())
    await answer_company_position(message, state)


@dp.message_handler(IsPrivate(), state=PersonalData.company_address, content_types='location')
async def answer_location(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    lat = message.location.latitude
    lon = message.location.longitude
    address_name = get_address_name(lon, lat)
    await state.update_data({'sports': '',
                             'mindfulness': '',
                             'outdoor': '',
                             'health_wellness': '',
                             'startups': '',
                             'entrepreneurship': '',
                             'investments': '',
                             'business_breakfasts': '',
                             'b2b_meetings': '',
                             'business_traveling': '',
                             'self_development': '',
                             'international_relations': '',
                             'professional_networking': '',
                             'business_games': '',
                             'other_hobbies': '',
                             })
    keyboard = await make_hobbies_call(lang=lang)
    if lang == 'en':

        await message.answer('<b>Your Hobbies:</b>', reply_markup=keyboard)
    else:
        await message.answer('<b>Ваше хобби:</b>', reply_markup=keyboard)

    await state.update_data({
        'comp_location': {'lon': lon, 'lat': lat},
        'comp_country': address_name.get('country'),
        'comp_city': address_name.get('city')
    })
    await PersonalData.hobbies.set()
