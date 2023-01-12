from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.check_keyboard import check_keyboard_en, check_keyboard_ru, add_company_en
from keyboards.default.request_location import get_keyboard
from keyboards.inline.lang_keyboard import language_keyboard
from loader import dp, bot
from aiogram import types
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove, ContentType

from states.personal_data import PersonalData
from utils.get_address import get_address_name

user_data = {}


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
        await call.message.answer('<b>✍ Please enter your image:</b>')
    else:
        await call.message.answer(txt_ru)
        await call.message.answer('<b>✍ Пожалуйста введите свое полное имя:</b>')
    await PersonalData.photo.set()
    await state.update_data({
        'language': call.data
    })


from pathlib import Path

download_path = Path().joinpath("dowlands", "path")
download_path.mkdir(parents=True, exist_ok=True)


@dp.message_handler(state=PersonalData.photo, content_types='photo')
async def answer_photo(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    print('=================================')
    await message.photo[-1].download(destination_dir=download_path)
    photo_id = message.photo[-1].file_id
    await message.answer_photo(photo_id)
    await message.answer_photo(photo_id)
    await state.update_data(
        {'photo_id': photo_id,
         })
    if lang == 'en':
        reply = f"<b>📌 Enter your fullname:</b>"
    else:
        reply = "<b>:</b>"
    await message.answer(reply)
    await PersonalData.fullname.set()


@dp.message_handler(state=PersonalData.fullname)
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
    comp_name = message.text
    user_id = str(message.from_user.id) + "n"
    global user_data
    # user_data = {user_id: {'comp_name': comp_name}}
    user_data.update({user_id: [{'comp_name': comp_name}]})
    print(user_data)
    # await state.update_data({'company': {'company_name': company_name}})
    if lang == 'en':
        await message.answer(f'<b>Enter your  company position:</b>')
    else:
        await message.answer('<b>Введите свою работу:</b>')
    await PersonalData.company_position.set()


@dp.message_handler(state=PersonalData.company_position)
async def answer_company_position(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    comp_position = message.text
    # await state.update_data({'company_position': company_position})
    user_id = str(message.from_user.id) + "p"
    # user_data[user_id]['company_position'] = company_position
    global user_data
    user_data.update({user_id: [{'comp_position': comp_position}]})
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


@dp.message_handler(state=PersonalData.company_address, content_types='location')
async def answer_location(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    lat = message.location.latitude
    lon = message.location.longitude
    address_name = get_address_name(lon, lat)
    if lang == 'en':
        await message.answer('<b>Do you add company:</b>', reply_markup=add_company_en)
    else:
        await message.answer('<b>Введите свой возраст:</b>', reply_markup=types.ReplyKeyboardRemove())

    # await state.update_data({
    #     'comp_location': {'lon': lon, 'lat': lat},
    #     'comp_country': address_name.get('country'),
    #     'comp_city': address_name.get('city')
    # })
    user_id = str(message.from_user.id)
    global user_data

    print(user_data)
    pos = user_id + "p"
    name = user_id + "n"
    comp_data = [{
        'comp_location': {'lon': lon, 'lat': lat},
        'comp_country': address_name.get('country'),
        'comp_city': address_name.get('city'),
        'comp_position': user_data[pos][0],
        'comp_name': user_data[name][0],

    }, ]
    await state.update_data({
        "comp_data": comp_data
    })
    print(comp_data)
    print(state.get_data('comp_data'))
    # user_data.pop(user_id)
    # user_data[user_id]['company_position'] = company_position
    await PersonalData.add_company.set()


@dp.message_handler(state=PersonalData.add_company)
async def answer_add_company(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    add_company = message.text
    print(add_company)
    if lang == 'en':
        if add_company == '✅ YES':
            await message.answer('<b>Enter your  company name :</b>')
            await PersonalData.company_name.set()
            # await answer_company_name(message, state)
        if add_company == '❌ NO':
            print('no')
            await message.answer('Your Hobbies')
            await PersonalData.hobbies.set()
    else:
        pass


# Your Hobbies
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
    await state.update_data({'reason_chat': reason_chat})
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
        await message.answer('<b>What kind of help you need from Business Community?</b>')
    else:
        await message.answer('<b>Введите адрес электронной почты:</b>')
    await PersonalData.help_community.set()


@dp.message_handler(state=PersonalData.help_community)
async def answer_help_community(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    help_community = message.text
    await state.update_data({'help_community': help_community})
    if lang == 'en':
        await message.answer('<b>Enter your instagram link:</b>')
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
        await message.answer('<b>Enter Linkedin link:</b>')
    else:
        await message.answer('<b>Введите адрес электронной почты:</b>')
    await PersonalData.linkedin_link.set()


@dp.message_handler(state=PersonalData.linkedin_link)
async def answer_linkedin_link(message: Message, state: FSMContext):
    linkedin_link = message.text
    await state.update_data({'linkedin_link': linkedin_link})
    data = await state.get_data()
    lang = data.get('language')
    photo = data.get('photo_id')
    print(photo)
    if lang == 'en':
        msg = f'<b>The following information has been received:</b>\n'
        msg += f"<b> Fullname:</b>  {data.get('name')}\n"
        msg += f"<b> Born address:</b>   {data.get('born_address')}\n"
        msg += f"<b> Residential address:</b>  {data.get('country')} ,{data.get('city')}\n"
        comp_data = data.get('comp_data')
        comp = ''
        print(comp_data)
        for i in comp_data:
            comp += f"<b>Company country: {i['comp_country']}</b>\n"
            comp += f"<b>Company city: {i['comp_city']}\n</b>"
            comp += f"<b>Company position: {i['comp_position']['comp_position']}</b>\n"
            comp += f"<b>Company name: {i['comp_name']['comp_name']}</b>\n"
        print(comp)
        msg += comp
        msg += f"<b> Hobbies :</b>  {data.get('hobbies')}\n"
        msg += f"<b> Telegram:</b>  @{data.get('username')}\n"
        msg += f"<b> Reason_chat:</b> {data.get('reason_chat')}\n"
        msg += f"<b> Your_superpower:</b> {data.get('your_superpower')}\n"
        msg += f"<b> Your_value:</b> {data.get('your_value')}\n"
        msg += f"<b> Help_community:</b> {data.get('help_community')}\n"
        msg += f"<b> Instagram_link:</b> {data.get('instagram_link')}\n"
        msg += f"<b> linkedin_link:</b> {data.get('linkedin_link')}\n"

        await message.answer(msg)
        await message.answer_photo(photo=photo, caption=msg)

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
