from aiogram.dispatcher import FSMContext
from keyboards.inline.callback_buttons import company_type_keyboard
from keyboards.inline.company_size import company_size_keyboard
from loader import dp, bot
from aiogram import types
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from states.personal_data import PersonalData


@dp.callback_query_handler(state=PersonalData.business_type)
async def answer_business_type(call: CallbackQuery, state: FSMContext):
    business_type = call.data
    data = await state.get_data()
    lang = data.get('language')
    # lang = 'en'
    if lang == 'en':
        await call.message.edit_text(text='Enter industries ', reply_markup=company_size_keyboard)

    else:
        await call.answer('<b>Введите адрес электронной почты:</b>')
    await PersonalData.company_size.set()
# await call.message.edit_reply_markup(None)
# await call.message.edit_reply_markup(
#     reply_markup=company_size_keyboard)
# await call.answer('<b>Enter company size alert :</b>', show_alert=True)
# await bot.answer_callback_query(call.id, text='✅')
