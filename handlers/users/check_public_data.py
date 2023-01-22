from aiogram.dispatcher import FSMContext

from keyboards.default.check_keyboard import check_keyboard_en, start_private_en, start_private_ru, check_keyboard_ru
from keyboards.inline.comp_type_call import company_type_keyboard_en, company_type_keyboard_ru
from loader import dp, bot
from aiogram import types
from aiogram.types import CallbackQuery, Message

from states.personal_data import PersonalData, PersonalDataPrivate
from utils.db_api.sql_alchemy import add_user
from filters import IsPrivate


@dp.message_handler(IsPrivate(), state=PersonalData.linkedin_link)
async def answer_linkedin_link(message: Message, state: FSMContext):
    linkedin_link = message.text
    await state.update_data({'linkedin_link': linkedin_link})
    data = await state.get_data()
    print(data)
    lang = data.get('language')
    photo = data.get('photo_id')
    fullname = data.get('name')
    born_address = data.get('born_address')
    residential_country = data.get('country')
    residential_city = data.get('city')
    hobbies = data.get('hobbies')
    username = '@' + str(data.get('username'))
    reasons_chat = data.get('reason_chat')
    your_superpower = data.get('your_superpower')
    your_value = data.get('your_value')
    help_community = data.get('help_community')
    instagram_link = data.get('instagram_link')
    linkedin_link = data.get('linkedin_link')
    comp_name = data.get('comp_name')
    comp_position = data.get('comp_position')
    comp_country = data.get('comp_country')
    comp_city = data.get('comp_city')
    comp_website = data.get('comp_website')

    if lang == 'en':
        msg = f' <b>\nThe following information has been received:</b>\n\n'
        msg += f"<b> Fullname:</b>  {fullname}\n"
        msg += f"<b> Born address:</b>   {born_address}\n"
        msg += f"<b> Residential address:</b>  {residential_country} ,{residential_city}\n"

        msg += f"<b> Company name:</b>  {comp_name}\n"
        msg += f"<b> Company position:</b>  {comp_position}\n"
        msg += f"<b> Company located country:</b>  {comp_country}\n"
        msg += f"<b> Company located city:</b>  {comp_city}\n"
        msg += f"<b> Company Website:</b>  {comp_website}\n"

        msg += f"<b> Hobbies :</b>  {hobbies}\n"
        msg += f"<b> Telegram:</b>  {username}\n"
        msg += f"<b> Reason chat:</b> {reasons_chat}\n"
        msg += f"<b> Your superpower:</b> {your_superpower}\n"
        msg += f"<b> Your value:</b> {your_value}\n"
        msg += f"<b> Help community:</b> {help_community}\n"
        msg += f"<b> Instagram link:</b> {instagram_link}\n"
        msg += f"<b> Linkedin link:</b> {linkedin_link}\n"

        await message.answer_photo(photo=photo, caption=msg)
        await state.update_data({
            "msg_en": msg
        })

        await message.answer(
            "<b>We have received your personal information successfully.\n "
            "you agree to data processing\n"
            "Your information is transmitted to the Network Group</b>",
            reply_markup=check_keyboard_en)
    else:
        msg = f'<b>Получена следующая информация:</b>\n'
        msg += f"<b> Полное имя:</b> {fullname}\n"
        msg += f"<b> Адрес рождения:</b> {born_address}\n"
        msg += f"<b> Адрес проживания:</b> {residential_city} ,{residential_city}\n"
        msg += f"<b> Название компании:</b> {comp_name}\n"
        msg += f"<b> Должность компании:</b> {comp_position}\n"
        msg += f"<b> Страна местонахождения компании:</b> {comp_country}\n"
        msg += f"<b> Город местонахождения компании:</b> {comp_city}\n"
        msg += f"<b> Веб-сайт компании:</b> {comp_website}\n"
        msg += f"<b> Хобби :</b> {hobbies}\n"
        msg += f"<b> Телеграм:</b> {username}\n"
        msg += f"<b> Чат причин:</b> {reasons_chat}\n"
        msg += f"<b> Ваша суперсила:</b> {your_superpower}\n"
        msg += f"<b> Ваше значение:</b> {your_value}\n"
        msg += f"<b> Справочное сообщество:</b> {help_community}\n"
        msg += f"<b> Cсылка на Instagram:</b> {instagram_link}\n"
        msg += f"<b> Cсылка на Linkedin:</b> {linkedin_link}\n"

        await message.answer_photo(photo=photo, caption=msg)
        await state.update_data({
            "msg_ru": msg
        })

        await message.answer(
            "<b>Мы успешно получили вашу личную информацию.\n "
            "вы соглашаетесь на обработку данных\n"
            "Ваша информация передается в сетевую группу</b>",
            reply_markup=check_keyboard_ru)
    await PersonalData.check.set()


@dp.message_handler(IsPrivate(), state=PersonalData.check)
async def answer_check(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    resp = message.text

    photo = data.get('photo_id')
    fullname = data.get('name')
    born_address = data.get('born_address')
    residential_country = data.get('country')
    residential_city = data.get('city')
    hobbies = data.get('hobbies')
    username = '@' + str(data.get('username'))
    reasons_chat = data.get('reason_chat')
    your_superpower = data.get('your_superpower')
    your_value = data.get('your_value')
    help_community = data.get('help_community')
    instagram_link = data.get('instagram_link')
    linkedin_link = data.get('linkedin_link')
    comp_name = data.get('comp_name')
    comp_position = data.get('comp_position')
    comp_country = data.get('comp_country')
    comp_city = data.get('comp_city')
    comp_website = data.get('comp_website')
    chat_id = message.from_user.id

    if lang == 'en':
        if resp == '✅ YES':
            photo = data.get('photo_id')
            msg = f"Welcome {fullname}\n" \
                  f"Born in {born_address}\n" \
                  f"Lives in {residential_city}, {residential_country}\n" \
                  f"Works as {comp_position} in {comp_name}, \n{comp_city},  {comp_country}\n" \
                  f"Company website: {comp_website}\n" \
                  f"Hobbies & Interests: {hobbies}\n" \
                  f"Telegram: {username}\n" \
                  f"Reason why joined to community {reasons_chat}\n" \
                  f"Superpower: {your_superpower}\n" \
                  f"Can be helpful to our community {your_value}\n" \
                  f"Needs help on {help_community}\n" \
                  f"Instagram: {instagram_link}\n" \
                  f"Linked: {linkedin_link}"

            await bot.send_photo(chat_id=-1001895105606, photo=photo, caption=msg)
            await message.answer("<b>\n"
                                 "Are you interested in B2B meetings?\n"
                                 "This information will not be shared to the public\n\n"
                                 "Your link for Biz Network group:\nhttps://t.me/+KNC5z2sG44AxNWZi"
                                 "</b>",
                                 reply_markup=start_private_en)
            user_data = await add_user(
                fullname=fullname,
                born_address=born_address,
                residential_country=residential_country,
                residential_city=residential_city, hobbies=hobbies,
                telegram=username, reason_chat=reasons_chat,
                your_superpower=your_superpower, your_value=your_value,
                help_community=help_community, instagram_link=instagram_link,
                linkedin_link=linkedin_link, chat_id=chat_id,
                company_city=comp_city, company_country=comp_country,
                company_name=comp_name, company_position=comp_position,
                company_website=comp_website
            )
            print(user_data)
            await state.finish()
        elif resp == "❌ NO":
            await message.answer('<b>Not accepted</b>',
                                 reply_markup=types.ReplyKeyboardRemove())
            await message.answer('<b>Re-enter your information</b>')
            await message.answer('<b>✍ Please download your photo:</b> ')
            await PersonalData.photo.set()

    else:
        if resp == '✅ ДА':
            await message.answer("<b>\n"
                                 "Вас интересуют встречи B2B?\n"
                                 "Эта информация не будет опубликована\n\n"
                                 "Ваша ссылка на группу Biz Network:\nhttps://t.me/+KNC5z2sG44AxNWZi"
                                 "</b>",
                                 reply_markup=start_private_ru)
            msg = data.get('msg_ru')
            photo = data.get('photo_id')
            await bot.send_photo(chat_id=-1001895105606, photo=photo, caption=msg)
            user_data = await add_user(
                fullname=fullname,
                born_address=born_address,
                residential_country=residential_country,
                residential_city=residential_city, hobbies=hobbies,
                telegram=username, reason_chat=reasons_chat,
                your_superpower=your_superpower, your_value=your_value,
                help_community=help_community, instagram_link=instagram_link,
                linkedin_link=linkedin_link, chat_id=chat_id,
                company_city=comp_city, company_country=comp_country,
                company_name=comp_name, company_position=comp_position,
                company_website=comp_website
            )
            print(user_data)
            await state.finish()
        else:
            await message.answer('<b>Not accepted</b>',
                                 reply_markup=types.ReplyKeyboardRemove())
            await message.answer('<b>Повторно введите свою информацию</b>')
            await message.answer('<b>✍ Пожалуйста, загрузите свою фотографию:</b>')
            await PersonalData.photo.set()
