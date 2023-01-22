# from aiogram.dispatcher import FSMContext
#
# from keyboards.inline.industries_inline_button import make_industries_call
# from loader import dp, bot
# from aiogram import types
# from aiogram.types import CallbackQuery, Message
# from states.personal_data import PersonalDataPrivate
#
#
# @dp.callback_query_handler(state=PersonalDataPrivate.industries)
# async def answer_industries(call: CallbackQuery, state: FSMContext):
#     callback_data_l = call.data.split(':')
#     s = ['show', 'level', 'False', 'accommodation', 'k']
#     print("@@@@answer_industries@@@@@@@@@@@@@", callback_data_l)
#     data = await state.get_data()
#
#     call_button = callback_data_l[3]
#     # button_state = callback_data_l[2]
#
#     if call_button != "➡ Next ➡":
#         state_button = data.get(call_button)
#         change_button = "" if state_button.startswith("✅ ") else "✅ "
#         await state.update_data({call_button: change_button})
#         data = await state.get_data()
#         lang = data.get('language')
#
#         accommodation = data.get('accommodation')
#         administrative = data.get('administrative')
#         construction = data.get('construction')
#         consumer = data.get('consumer')
#         education = data.get('education')
#         entertainment = data.get('entertainment')
#         farming = data.get('farming')
#         financial = data.get('financial')
#         government = data.get('government')
#         holding = data.get('holding')
#         hospitals = data.get('hospitals')
#         manufacturing = data.get('manufacturing')
#         oil = data.get('oil')
#         professional = data.get('professional')
#         real = data.get('real')
#         retail = data.get('retail')
#         technology = data.get('technology')
#         transportation = data.get('transportation')
#         utilities = data.get('utilities')
#         wholesale = data.get('wholesale')
#         other = data.get('other')
#         if lang == 'en':
#             await call.message.edit_reply_markup(
#                 reply_markup=make_industries_call(accommodation, administrative, construction,
#                                                   consumer, education, entertainment,
#                                                   farming, financial, government,
#                                                   holding, hospitals,
#                                                   manufacturing, oil, professional, real,
#                                                   retail, technology, transportation,
#                                                   utilities, wholesale, other, lang))
#         else:
#             await call.message.edit_reply_markup(
#                 reply_markup=make_industries_call(accommodation, administrative, construction,
#                                                   consumer, education, entertainment,
#                                                   farming, financial, government,
#                                                   holding, hospitals,
#                                                   manufacturing, oil, professional, real,
#                                                   retail, technology, transportation,
#                                                   utilities, wholesale, other, lang))
#     elif call_button == "➡ Next ➡":
#         await call.message.answer("next step")
#         await PersonalDataPrivate.we_would_meet.set()
#         await state.update_data({'owners': '',
#                                  'chairman': '',
#                                  'ceo': '',
#                                  'c_level': '',
#                                  'departament': '',
#                                  'mid_level': '',
#                                  'other': ''
#                                  })
#
