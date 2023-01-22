from aiogram.dispatcher import FSMContext

from handlers.users.start import answer_fullname
from loader import dp, bot
from aiogram import types
from aiogram.types import CallbackQuery, Message
from states.personal_data import PersonalData
from utils.get_address import get_address_name
from filters import IsPrivate


@dp.message_handler(IsPrivate(), state=PersonalData.live_address)
async def answer_re_location(message: Message, state: FSMContext):
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
    await answer_fullname(message, state)


@dp.message_handler(IsPrivate(), content_types='location', state=PersonalData.live_address)
async def answer_location(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    lat = message.location.latitude
    lon = message.location.longitude
    address_name = get_address_name(lon, lat)
    if lang == 'en':
        await message.answer('<b>Which city did you born:</b>', reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer('<b>В каком городе ты родился:</b>', reply_markup=types.ReplyKeyboardRemove())

    await state.update_data({
        'location': {'lon': lon, 'lat': lat},
        'country': address_name.get('country'),
        'city': address_name.get('city')
    })
    await PersonalData.born_address.set()


@dp.message_handler(IsPrivate(), state=PersonalData.born_address)
async def answer_born_address(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    born_address = message.text
    await state.update_data({'born_address': born_address})
    if lang == 'en':
        await message.answer('<b>Enter your  company name:</b>')
    else:
        await message.answer('<b>Введите название вашей компании:</b>')

    await PersonalData.company_name.set()
