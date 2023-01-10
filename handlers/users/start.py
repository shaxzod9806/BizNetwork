from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.check_keyboard import check_keyboard_en, check_keyboard_ru
from keyboards.default.request_location import get_keyboard
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
        await call.message.answer('<b>✍ Please enter your fullname:</b>')
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
        reply = "<b>📌 Select your residential address on the map\n or\n" \
                "Click the button below to share your current location:</b>"
    else:
        reply = "<b>📌 Выберите свой адрес проживания на карте\n или\n" \
                "Нажмите кнопку ниже, чтобы поделиться своим текущим местоположением:</b>"
    await message.answer(reply, reply_markup=get_keyboard())
    await PersonalData.live_address.set()


@dp.message_handler(state=PersonalData.live_address)
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


@dp.message_handler(content_types='location', state=PersonalData.live_address)
async def answer_location(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    lat = message.location.latitude
    lon = message.location.longitude
    address_name = get_address_name(lon, lat)
    if lang == 'en':
        await message.answer('<b>Which city did you born:</b>', reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer('<b>Введите свой возраст:</b>', reply_markup=types.ReplyKeyboardRemove())

    await state.update_data({
        'location': {'lon': lon, 'lat': lat},
        'country': address_name.get('country'),
        'city': address_name.get('city')
    })
    await PersonalData.born_address.set()


@dp.message_handler(state=PersonalData.born_address)
async def answer_born_address(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    born_address = message.text
    await state.update_data({'born_address': born_address})
    if lang == 'en':
        await message.answer('<b>Enter your  company name :</b>')
    else:
        await message.answer('<b>Введите свое рабочее место:</b>')

    await PersonalData.company_name.set()


@dp.message_handler(state=PersonalData.company_name)
async def answer_company_name(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    company_name = message.text
    await state.update_data({'company_name': company_name})
    if lang == 'en':
        await message.answer('<b>Enter your  company position:</b>')
    else:
        await message.answer('<b>Введите свою работу:</b>')
    await PersonalData.company_position.set()


@dp.message_handler(state=PersonalData.company_position)
async def answer_company_position(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    company_position = message.text
    await state.update_data({'company_position': company_position})
    if lang == 'en':
        reply = "<b>📌 Select your company address on the map\n or\n" \
                "Click the button below to share your current location:</b>"
    else:
        reply = "<b>📌 Выберите свой адрес проживания на карте\n или\n" \
                "Нажмите кнопку ниже, чтобы поделиться своим текущим местоположением:</b>"
    await message.answer(reply, reply_markup=get_keyboard())
    await PersonalData.company_address.set()


@dp.message_handler(state=PersonalData.company_address)
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


@dp.message_handler(content_types='location', state=PersonalData.company_address)
async def answer_location(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    lat = message.location.latitude
    lon = message.location.longitude
    address_name = get_address_name(lon, lat)
    if lang == 'en':
        await message.answer('<b>Your Hobbies:</b>', reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer('<b>Введите свой возраст:</b>', reply_markup=types.ReplyKeyboardRemove())

    await state.update_data({
        'comp_location': {'lon': lon, 'lat': lat},
        'comp_country': address_name.get('country'),
        'comp_city': address_name.get('city')
    })
    await PersonalData.hobbies.set()


@dp.message_handler(state=PersonalData.hobbies)
async def answer_hobbies(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    hobbies = message.text
    await state.update_data({'hobbies': hobbies})
    if lang == 'en':
        await message.answer('<b>The reason that you joined to this chat:</b>')
    else:
        await message.answer('<b>Введите адрес электронной почты:</b>')
    await PersonalData.reason_chat.set()


@dp.message_handler(state=PersonalData.reason_chat)
async def answer_reason_chat(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    reason_chat = message.text
    await state.update_data({'your superpower': reason_chat})
    if lang == 'en':
        await message.answer('<b>Enter your superpower:</b>')
    else:
        await message.answer('<b>Введите адрес электронной почты:</b>')
    await PersonalData.your_superpower.set()


@dp.message_handler(state=PersonalData.your_superpower)
async def answer_your_superpower(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    your_superpower = message.text
    await state.update_data({'your_superpower': your_superpower})
    if lang == 'en':
        await message.answer('<b>How you can be helpful to this community?:</b>')
    else:
        await message.answer('<b>Введите адрес электронной почты:</b>')
    await PersonalData.your_value.set()


@dp.message_handler(state=PersonalData.your_value)
async def answer_your_value(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    your_value = message.text
    await state.update_data({'your_value': your_value})
    if lang == 'en':
        await message.answer('<b>What kind of help you need from Business Community?:</b>')
    else:
        await message.answer('<b>Введите адрес электронной почты:</b>')
    await PersonalData.help_community.set()


@dp.message_handler(state=PersonalData.help_community)
async def answer_help_community(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    help_community = message.text
    await state.update_data({'your_value': help_community})
    if lang == 'en':
        await message.answer('<b>Enter instagram link:</b>')
    else:
        await message.answer('<b>Введите адрес электронной почты:</b>')
    await PersonalData.instagram_link.set()


@dp.message_handler(state=PersonalData.instagram_link)
async def answer_instagram_link(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    instagram_link = message.text
    await state.update_data({'instagram_link': instagram_link})
    if lang == 'en':
        await message.answer('<b>Enter linkedin link:</b>')
    else:
        await message.answer('<b>Введите адрес электронной почты:</b>')
    await PersonalData.linkedin_link.set()


@dp.message_handler(state=PersonalData.linkedin_link)
async def answer_linkedin_link(message: Message, state: FSMContext):
    linkedin_link = message.text
    await state.update_data({'linkedin_link': linkedin_link})
    data = await state.get_data()
    lang = data.get('language')
    if lang == 'en':
        msg = f'<b>The following information has been received:</b>\n'
        msg += f"<b> fullname:</b>  {data.get('fullname')}\n"
        msg += f"<b> born_address:</b>   {data.get('born_address')}\n"
        msg += f"<b> live_address:</b>  {data.get('live_address')}\n"
        msg += f"<b> company_name:</b>   {data.get('company_name')}\n"
        msg += f"<b> company_position:</b> {data.get('company_position')}\n"
        msg += f"<b> company_address:</b>  {data.get('company_address')}\n"
        msg += f"<b> hobbies :</b>  {data.get('hobbies')}\n"
        msg += f"<b> Telegram:</b>  @{data.get('username')}\n"
        msg += f"<b> reason_chat:</b> {data.get('reason_chat')}\n"
        msg += f"<b> your_superpower:</b> {data.get('your_superpower')}\n"
        msg += f"<b> your_value:</b> {data.get('your_value')}\n"
        msg += f"<b> help_community:</b> {data.get('help_community')}\n"
        msg += f"<b> instagram_link:</b> {data.get('instagram_link')}\n"
        msg += f"<b> linkedin_link:</b> {data.get('linkedin_link')}\n"
        # photo = State()
        #     fullname = State()
        #     born_address = State()
        #     live_address = State()
        #     company_name = State()
        #     company_position = State()
        #     company_address = State()
        #     hobbies = State()
        #     reason_chat = State()
        #     your_superpower = State()
        #     your_value = State()
        #     help_community = State()
        #     instagram_link = State()
        #     linkedin_link = State()
        await message.answer(msg)
        await message.answer("<b>Is all the information correct?</b>", reply_markup=check_keyboard_en)
    else:
        msg = f'<b>Получена следующая информация:</b>\n'
        msg += f"<b>📝 Полное имя:</b>    {data.get('name')}\n"
        msg += f"<b>🌐 Страна:</b>    {data.get('country')}\n"
        msg += f"<b>🌆 Город:</b>   {data.get('city')}\n"
        msg += f"<b>⚡ Возраст:</b>   {data.get('age')}\n"
        msg += f"<b>🏢 Рабочее место:</b>    {data.get('workplace')}\n"
        msg += f"<b>‍💻 Задание:</b>  {data.get('job')}\n"
        msg += f"<b>📞 Номер телефона:</b>    {data.get('phone_number')}\n"
        msg += f"<b>🌀 Telegram:</b>   @{data.get('username')}\n"
        msg += f"<b>📧 Электронная почта:</b>     {data.get('email')}\n"
        await message.answer(msg)
        await message.answer("<b>Вся ли информация верна?</b>", reply_markup=check_keyboard_ru)
    await PersonalData.check.set()


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