from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.check_keyboard import check_keyboard_en, check_keyboard_ru
from keyboards.default.request_location import get_keyboard
from keyboards.inline.callback_buttons import company_type_keyboard
from keyboards.inline.company_size import company_size_keyboard
from keyboards.inline.lang_keyboard import language_keyboard
from loader import dp, bot
from aiogram import types
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove

from states.personal_data import PersonalData
from utils.get_address import get_address_name


@dp.message_handler(text='/start')
async def bot_start(message: types.Message):
    # await message.answer(f"Salom, {message.from_user.full_name}!")
    text = f"""
            Please select a language ⬇\nПожалуйста, выберите язык ⬇
    """
    await message.answer(text, reply_markup=language_keyboard)

    await PersonalData.language.set()


@dp.callback_query_handler(state=PersonalData.language)
async def start_uz(call: CallbackQuery, state: FSMContext):
    lang = call.data
    # фамилия
    # Имя
    txt_en = """
    Sign up
    Now you will be asked some questions.
    Please, answer each one.
    In the end, if everything is correct,
    click YES and 
    your application will be sent to Admin."""
    txt_ru = """
    Зарегистрироваться
     Сейчас вам зададут несколько вопросов.
     Пожалуйста, ответьте на каждый.
     В конце концов, если все правильно,
     нажмите ДА и
     Ваша заявка будет отправлена администратору.
     """
    if lang == 'en':
        await call.message.answer(txt_en)
        await call.message.answer('<b>✍ Please enter your Full Name:</b>')
    else:
        await call.message.answer(txt_ru)
        await call.message.answer('<b>✍ Пожалуйста введите свое полное имя:</b>')
    await PersonalData.fullname.set()
    await state.update_data({
        'language': call.data
    })


@dp.message_handler(state=PersonalData.fullname)
async def answer_fullname(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    fullname = message.text
    await state.update_data(
        {'name': fullname,
         'chat_id': message.from_user.id,
         'username': message.from_user.username
         })
    if lang == 'en':
        reply = "<b>Enter your company Name:</b>"
    else:
        reply = "<b>📌 Выберите свой адрес проживания на карте\n или\n" \
                "Нажмите кнопку ниже, чтобы поделиться своим текущим местоположением:</b>"
    await message.answer(reply)
    await PersonalData.company_name.set()


@dp.message_handler(state=PersonalData.company_name)
async def answer_company_name(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    company_name = message.text
    await state.update_data({'company_name': company_name})
    if lang == 'en':
        await message.answer('<b>📌 Enter your company location:</b>', reply_markup=get_keyboard())
    else:
        await message.answer('<b>Введите свое рабочее место:</b>')
    await PersonalData.company_address.set()


@dp.message_handler(content_types=['text'], state=PersonalData.company_address)
async def answer_re_location(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    if lang == 'en':
        await message.answer(
            '<b>Re-enter your details:\nShare your location:</b>',
            reply_markup=get_keyboard())
    else:
        await message.answer(
            '<b>Повторно введите свои данные:\nПоделитесь своим местоположением:</b>',
            reply_markup=types.ReplyKeyboardRemove())
    # await PersonalData.fullname.set()
    # await answer_company_name(message, state)


@dp.message_handler(content_types=['location'], state=PersonalData.company_address)
async def answer_location(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    lat = message.location.latitude
    lon = message.location.longitude
    address_name = get_address_name(lon, lat)
    if lang == 'en':
        await message.answer('<b>Enter your company website:</b>', reply_markup=types.ReplyKeyboardRemove())
        await message.answer(address_name, reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer('<b>Введите свой возраст:</b>', reply_markup=types.ReplyKeyboardRemove())

    await state.update_data({
        'location': {'lon': lon, 'lat': lat},
        'country': address_name.get('country'),
        'city': address_name.get('city')
    })
    await PersonalData.company_website.set()


@dp.message_handler(state=PersonalData.company_website)
async def answer_company_website(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    company_website = message.text
    await state.update_data({'company_website': company_website})
    if lang == 'en':
        await message.answer('<b> Enter your email:</b>')
    else:
        await message.answer('<b>Введите свою работу:</b>')
    await PersonalData.email.set()


@dp.message_handler(state=PersonalData.email)
async def answer_email(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    email = message.text
    await state.update_data({'email': email})
    if lang == 'en':
        await message.answer('<b>Enter your phone number:</b> \n\nEx: +998934445566')
    else:
        await message.answer('<b>Введите свой номер телефона:</b> \n\nEx: +998934445566')
    await PersonalData.phone_number.set()


@dp.message_handler(state=PersonalData.phone_number)
async def answer_phone_number(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    phone_number = message.text
    await state.update_data({'phone_number': phone_number})
    if lang == 'en':
        await message.answer('<b>Enter number of expected meetings:</b>')
    else:
        await message.answer('<b>Введите адрес электронной почты:</b>')
    await PersonalData.expected_meetings.set()


# data = await state.get_data()
# lang = data.get('language')
# if lang == 'en':
#     msg = f'<b>The following information has been received:</b>\n'
#     msg += f"<b>📝 Fullname:</b>  {data.get('name')}\n"
#     msg += f"<b>🌐 Country:</b>   {data.get('country')}\n"
#     msg += f"<b>🌆 City:</b>  {data.get('city')}\n"
#     msg += f"<b>⚡ Age:</b>   {data.get('age')}\n"
#     msg += f"<b>🏢 Workplace:</b> {data.get('workplace')}\n"
#     msg += f"<b>‍💻 Job:</b>  {data.get('job')}\n"
#     msg += f"<b>📞 Phone number:</b>  {data.get('phone_number')}\n"
#     msg += f"<b>🌀 Telegram:</b>  @{data.get('username')}\n"
#     msg += f"<b>📧 Email:</b> {data.get('email')}\n"
#     await message.answer(msg)
#     await message.answer("<b>Is all the information correct?</b>", reply_markup=check_keyboard_en)
#     await bot.send_message(chat_id=1047359359, text=msg)
# else:
#     msg = f'<b>Получена следующая информация:</b>\n'
#     msg += f"<b>📝 Полное имя:</b>    {data.get('name')}\n"
#     msg += f"<b>🌐 Страна:</b>    {data.get('country')}\n"
#     msg += f"<b>🌆 Город:</b>   {data.get('city')}\n"
#     msg += f"<b>⚡ Возраст:</b>   {data.get('age')}\n"
#     msg += f"<b>🏢 Рабочее место:</b>    {data.get('workplace')}\n"
#     msg += f"<b>‍💻 Задание:</b>  {data.get('job')}\n"
#     msg += f"<b>📞 Номер телефона:</b>    {data.get('phone_number')}\n"
#     msg += f"<b>🌀 Telegram:</b>   @{data.get('username')}\n"
#     msg += f"<b>📧 Электронная почта:</b>     {data.get('email')}\n"
#     await message.answer(msg)
#     await message.answer("<b>Вся ли информация верна?</b>", reply_markup=check_keyboard_ru)
#     await bot.send_message(chat_id=1047359359, text=msg)
# await PersonalData.check.set()
# await call.message.edit_text(r_markup[1])
# await bot.answer_callback_query(call.id, text=text_delete)
@dp.message_handler(state=PersonalData.check)
async def answer_check(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    resp = message.text
    if lang == 'en':
        if resp == '✅ YES':
            await message.answer('<b>We have received your personal information successfully.\n Thank you</b>',
                                 reply_markup=types.ReplyKeyboardRemove()
                                 )
            await state.finish()
        else:
            await message.answer('<b>Not accepted</b>',
                                 reply_markup=types.ReplyKeyboardRemove())
            await message.answer('<b>Re-enter your information</b>')
            await message.answer('<b>✍ Please enter your fullname:</b> ')
            await PersonalData.fullname.set()

    else:
        if resp == '✅ ДА':
            await message.answer('<b>Accepted</b>',
                                 reply_markup=types.ReplyKeyboardRemove())
            await state.finish()
        else:
            await message.answer('<b>Not accepted</b>',
                                 reply_markup=types.ReplyKeyboardRemove())
            await message.answer('<b>Повторно введите свою информацию</b>')
            await message.answer('<b>✍ Пожалуйста введите свое полное имя:</b>')
            await PersonalData.fullname.set()
