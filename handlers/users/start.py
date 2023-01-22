from aiogram.dispatcher import FSMContext
from keyboards.default.request_location import get_keyboard
from keyboards.inline.lang_keyboard import language_keyboard
from loader import dp, bot
from aiogram import types
from aiogram.types import CallbackQuery, Message
from states.personal_data import PersonalData
from filters import IsPrivate
from pathlib import Path

download_path = Path().joinpath("dowlands", "path")
download_path.mkdir(parents=True, exist_ok=True)


@dp.message_handler(IsPrivate(), state='*', text='/start')
async def bot_start(message: types.Message):
    text = f"""
            Please select a language ⬇\nПожалуйста, выберите язык ⬇
    """
    await message.answer(text, reply_markup=language_keyboard)
    await PersonalData.language.set()


@dp.message_handler(IsPrivate(), state=PersonalData.language)
async def start_uz(message: types.Message, state: FSMContext):
    lang = 'en' if message.text == '🇬🇧 English' else 'ru'
    txt_en = """<b>
    Please kindly register and answer to the questions </b>"""
    txt_ru = """<b>
    Пожалуйста, зарегистрируйтесь и ответьте на вопросы
     </b>"""
    if lang == 'en':
        await message.answer(txt_en)
        await message.answer('<b>Upload your photo:</b>', reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer(txt_ru)
        await message.answer('<b>Загрузите свою фотографию:</b>', reply_markup=types.ReplyKeyboardRemove())
    await PersonalData.photo.set()
    await state.update_data({
        'language': lang
    })


@dp.message_handler(IsPrivate(), state=PersonalData.photo, content_types='photo')
async def answer_photo(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    print('=================================')
    await message.photo[-1].download(destination_dir=download_path)
    photo_id = message.photo[-1].file_id
    # await message.answer_photo(photo_id)
    await state.update_data(
        {'photo_id': photo_id,
         })
    if lang == 'en':
        reply = f"<b>Full name:</b>"
    else:
        reply = "<b>ФИО:</b>"
    await message.answer(reply)
    await PersonalData.fullname.set()


@dp.message_handler(IsPrivate(), state=PersonalData.fullname)
async def answer_fullname(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    fullname = message.text
    print(fullname)
    await state.update_data(
        {'name': fullname,
         'chat_id': message.from_user.id,
         'username': message.from_user.username
         })
    if lang == 'en':
        reply = f"<b>📌 Select your residential address on the map\n or\n" \
                "Click the button below to share your current location:</b>"
    else:
        reply = "<b>📌 Выберите свой адрес проживания на карте\n или\n" \
                "Нажмите кнопку ниже, чтобы поделиться своим текущим местоположением:</b>"
    await message.answer(reply, reply_markup=get_keyboard())
    await PersonalData.live_address.set()
