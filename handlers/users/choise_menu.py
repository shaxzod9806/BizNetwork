from aiogram.dispatcher import FSMContext
from keyboards.inline.callback_buttons import company_type_keyboard, business_type_keyboard
from keyboards.inline.company_size import company_size_keyboard
from loader import dp, bot
from aiogram import types
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from states.personal_data import PersonalData


@dp.message_handler(text='/a')
# @dp.message_handler(state=PersonalData.expected_meetings)
async def answer_expected_meetings(message: Message, state: FSMContext):
    expected_meetings = message.text
    data = await state.get_data()
    lang = data.get('language')
    lang = 'en'
    await state.update_data({'expected_meetings ': expected_meetings})
    if lang == 'en':
        await message.answer('<b>Enter Company Type:</b>', reply_markup=company_type_keyboard)
    else:
        await message.answer('<b>Введите адрес электронной почты:</b>')
    await PersonalData.company_type.set()


@dp.callback_query_handler(state=PersonalData.company_type)
async def answer_company_type(call: CallbackQuery, state: FSMContext):
    company_type = call.data
    data = await state.get_data()
    lang = data.get('language')
    lang = 'en'
    await state.update_data({'company_type ': company_type})
    if lang == 'en':
        await call.message.edit_text(
            text='Your Company Annual Turnover in USD', reply_markup=company_size_keyboard)

    else:
        await call.answer('<b>Введите адрес электронной почты:</b>')
    await PersonalData.company_size.set()


@dp.callback_query_handler(state=PersonalData.company_size)
async def answer_company_size(call: CallbackQuery, state: FSMContext):
    company_size = call.data
    data = await state.get_data()
    lang = data.get('language')
    lang = 'en'
    if lang == 'en':
        await call.message.edit_text(
            text='We are interested in following Matchmaking', reply_markup=business_type_keyboard)

    else:
        await call.answer('<b>Введите адрес электронной почты:</b>')
    await PersonalData.business_type.set()

# await call.message.edit_reply_markup(None)
# await call.message.edit_reply_markup(
#     reply_markup=company_size_keyboard)
# await call.answer('<b>Enter company size alert :</b>', show_alert=True)
# await bot.answer_callback_query(call.id, text='✅')
