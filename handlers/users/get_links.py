from aiogram.dispatcher import FSMContext
from loader import dp, bot
from aiogram.types import CallbackQuery, Message

from states.personal_data import PersonalData
from filters import IsPrivate


@dp.message_handler(IsPrivate(), state=PersonalData.company_website)
async def answer_website(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    comp_website = message.text
    await state.update_data({'comp_website': comp_website})
    if lang == 'en':
        await message.answer('<b>Please enter your Instagram Username(or link) \nif your have (optional):'
                             '\ninstagram.com</b>')
    else:
        await message.answer(
            '<b>Пожалуйста, введите свое имя пользователя в Instagram (или ссылку) \nесли есть (необязательно):'
            '\ninstagram.com</b>')
    await PersonalData.instagram_link.set()


@dp.message_handler(IsPrivate(), state=PersonalData.instagram_link)
async def answer_instagram_link(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    text = message.text
    instagram_link = text if text.startswith(
                                            "https:") or text.startswith(
                                            "instagram.com"
                                            ) else "www.instagram.com/" + text

    await state.update_data({'instagram_link': instagram_link})
    if lang == 'en':
        await message.answer('<b>LinkedIn (optional):\nlinkedin.com</b>')
    else:
        await message.answer('<b>Линкедин (необязательно):\nlinkedin.com</b>')
    await PersonalData.linkedin_link.set()
