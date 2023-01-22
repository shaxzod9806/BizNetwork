import aiogram.types
from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.check_keyboard import check_private_en, check_private_ru
from keyboards.inline.business_type_call import make_business_type_call
from keyboards.inline.industries_inline_button import make_industries_call
from keyboards.inline.meeting_formats_call_button import make_menu_meeting_formats_call
from keyboards.inline.meeting_times_call_button import make_menu_meeting_times_call
from keyboards.inline.we_would_meet_callback import make_menu_we_would_meet_call
from loader import dp
from aiogram.types import CallbackQuery, Message
from states.personal_data import PersonalDataPrivate


@dp.callback_query_handler(state=PersonalDataPrivate.business_type)
async def answer_business_type(call: CallbackQuery, state: FSMContext):
    callback_data_l = call.data.split(':')
    print("@@@@@@@@@@@@@@@@@", callback_data_l)
    data = await state.get_data()
    lang = data.get('language')
    call_button = callback_data_l[3]
    button_state = callback_data_l[2]
    print(call_button != "➡ Next ➡")
    # if call_button != "➡ Next ➡":
    if call_button != "➡ Next ➡" and call_button != "➡ Далее ➡":
        change_button = "" + call_button if button_state.startswith("✅ ") else "✅ " + call_button
        print('change_button', change_button)
        print(button_state)
        await state.update_data({call_button: change_button})

        print("data.get('business_type_button')b", await state.get_data())
        data = await state.get_data()
        b2b = data.get('B2B')
        b2g = data.get('B2G')
        b2c = data.get('B2C')
        print(b2c, b2g, b2b)
        keyboard = await make_business_type_call(b2b, b2g, b2c, lang)
        await call.message.edit_reply_markup(reply_markup=keyboard)
    elif call_button == "➡ Next ➡" or call_button == "➡ Далее ➡":
        await call.message.edit_text("<b>Industries</b>")
        keyboard = await make_industries_call(lang=lang)
        await call.message.edit_reply_markup(reply_markup=keyboard)
        await PersonalDataPrivate.industries.set()
    await state.update_data({'accommodation': '',
                             'administrative': '',
                             'construction': '',
                             'consumer': '',
                             'education': '',
                             'entertainment': '',
                             'farming': '',
                             'financial': '',
                             'government': '',
                             'holding': '',
                             'hospitals': '',
                             'manufacturing': '',
                             'oil': '',
                             'professional': '',
                             'real': '',
                             'retail': '',
                             'technology': '',
                             'transportation': '',
                             'utilities': '',
                             'wholesale': '',
                             'other_industries': ''
                             })


@dp.callback_query_handler(state=PersonalDataPrivate.industries)
async def answer_industries(call: CallbackQuery, state: FSMContext):
    callback_data_l = call.data.split(':')
    s = ['show', 'level', 'False', 'accommodation', 'k']
    print("@@@@answer_industries@@@@@@@@@@@@@", callback_data_l)
    data = await state.get_data()
    call_button = callback_data_l[3]
    if call_button != "➡ Next ➡":
        state_button = data.get(call_button)
        change_button = "" if state_button.startswith("✅ ") else "✅ "
        await state.update_data({call_button: change_button})
        data = await state.get_data()
        lang = data.get('language')

        accommodation = data.get('accommodation')
        administrative = data.get('administrative')
        construction = data.get('construction')
        consumer = data.get('consumer')
        education = data.get('education')
        entertainment = data.get('entertainment')
        farming = data.get('farming')
        financial = data.get('financial')
        government = data.get('government')
        holding = data.get('holding')
        hospitals = data.get('hospitals')
        manufacturing = data.get('manufacturing')
        oil = data.get('oil')
        professional = data.get('professional')
        real = data.get('real')
        retail = data.get('retail')
        technology = data.get('technology')
        transportation = data.get('transportation')
        utilities = data.get('utilities')
        wholesale = data.get('wholesale')
        other_industries = data.get('other_industries')
        if lang == 'en':
            keyboard = await make_industries_call(accommodation, administrative, construction,
                                                  consumer, education, entertainment,
                                                  farming, financial, government,
                                                  holding, hospitals,
                                                  manufacturing, oil, professional, real,
                                                  retail, technology, transportation,
                                                  utilities, wholesale, other_industries, lang)
            await call.message.edit_reply_markup(
                reply_markup=keyboard)
        else:
            keyboard = await make_industries_call(accommodation, administrative, construction,
                                                  consumer, education, entertainment,
                                                  farming, financial, government,
                                                  holding, hospitals,
                                                  manufacturing, oil, professional, real,
                                                  retail, technology, transportation,
                                                  utilities, wholesale, other_industries, lang)
            await call.message.edit_reply_markup(
                reply_markup=keyboard)
    elif call_button == "➡ Next ➡":
        lang = data.get('language')
        if lang == 'en':
            await call.message.edit_text("<b>We would like to meet</b>")
        else:
            await call.message.edit_text("<b>мы хотели бы встретиться</b>")
        await PersonalDataPrivate.we_would_meet.set()
        await state.update_data({'owners': '',
                                 'chairman': '',
                                 'ceo': '',
                                 'c_level': '',
                                 'departament': '',
                                 'mid_level': '',
                                 'other_we_would_meet': ''
                                 })
        keyboard = await make_menu_we_would_meet_call(lang=lang)
        await call.message.edit_reply_markup(reply_markup=keyboard)


@dp.callback_query_handler(state=PersonalDataPrivate.we_would_meet)
async def answer_we_would_meet(call: CallbackQuery, state: FSMContext):
    callback_data_l = call.data.split(':')
    # s = ['show', 'level', 'False', 'accommodation', 'k']
    # s = ['show', 'level', '', 'chairman', '']
    print("@@@@ we_would_meet @@@@@@@@@@@@@", callback_data_l)
    data = await state.get_data()

    call_button = callback_data_l[3]
    # button_state = callback_data_l[2]
    print("call_button = callback_data_l[3]", call_button)

    if call_button != "➡ Next ➡":
        state_button = data.get(call_button)
        change_button = "" if state_button.startswith("✅ ") else "✅ "
        await state.update_data({call_button: change_button})
        data = await state.get_data()
        lang = data.get('language')

        owners = data.get('owners')
        chairman = data.get('chairman')
        ceo = data.get('ceo')
        c_level = data.get('c_level')
        departament = data.get('departament')
        mid_level = data.get('mid_level')
        other_we_would_meet = data.get('other_we_would_meet')
        if lang == 'en':
            keyboard = await make_menu_we_would_meet_call(owners=owners, chairman=chairman, ceo=ceo,
                                                          c_level=c_level, departament=departament,
                                                          mid_level=mid_level, other_we_would_meet=other_we_would_meet,
                                                          lang=lang)
            await call.message.edit_reply_markup(reply_markup=keyboard)
        else:
            keyboard = await make_menu_we_would_meet_call(owners=owners, chairman=chairman, ceo=ceo,
                                                          c_level=c_level, departament=departament,
                                                          mid_level=mid_level, other_we_would_meet=other_we_would_meet,
                                                          lang=lang)

            await call.message.edit_reply_markup(reply_markup=keyboard)
    elif call_button == "➡ Next ➡":
        print("Please elif call_button == ➡ Next ➡")
        lang = data.get('language')
        if lang == "en":
            await call.message.edit_text("<b>Preferable meeting formats</b>")
        else:
            await call.message.edit_text("<b>Предпочтительные форматы встречи</b>")

        await PersonalDataPrivate.meeting_formats.set()
        await state.update_data({'offline': '',
                                 'online': '',
                                 'combined': '',
                                 'other_meeting_formats': ''
                                 })
        keyboard = await make_menu_meeting_formats_call(lang=lang)
        await call.message.edit_reply_markup(reply_markup=keyboard)


@dp.callback_query_handler(state=PersonalDataPrivate.meeting_formats)
async def answer_meeting_formats(call: CallbackQuery, state: FSMContext):
    callback_data_l = call.data.split(':')
    # s = ['show', 'level', 'False', 'accommodation', 'k']
    # s = ['show', 'level', '', 'chairman', '']
    print("@@@@ meeting_formats @@@@@@@@@@@@@", callback_data_l)
    data = await state.get_data()

    call_button = callback_data_l[3]
    print("call_button = callback_data_l[3]", call_button)

    if call_button != "➡ Next ➡":
        state_button = data.get(call_button)
        change_button = "" if state_button.startswith("✅ ") else "✅ "
        await state.update_data({call_button: change_button})
        data = await state.get_data()
        lang = data.get('language')
        offline = data.get('offline')
        online = data.get('online')
        combined = data.get('combined')
        other_meeting_formats = data.get('other_meeting_formats')
        if lang == 'en':
            keyboard = await make_menu_meeting_formats_call(offline=offline, online=online, combined=combined,
                                                            other_meeting_formats=other_meeting_formats, lang=lang)
            await call.message.edit_reply_markup(reply_markup=keyboard)
        else:
            keyboard = await make_menu_meeting_formats_call(offline=offline, online=online, combined=combined,
                                                            other_meeting_formats=other_meeting_formats, lang=lang)

            await call.message.edit_reply_markup(reply_markup=keyboard)
    elif call_button == "➡ Next ➡":
        print("Please elif call_button == ➡ Next ➡")
        lang = data.get('language')
        if lang == "en":

            await call.message.edit_text("<b>Preferable Timing for Meetings</b>")
        else:
            await call.message.edit_text("<b>Предпочтительное время для встреч</b>")

        await PersonalDataPrivate.meeting_times.set()
        await state.update_data({'january': '',
                                 'february': '',
                                 'march': '',
                                 'april': '',
                                 'may': '',
                                 'june': '',
                                 'july': '',
                                 'august': '',
                                 'september': '',
                                 'october': '',
                                 'november': '',
                                 'december': '',
                                 'soonest_time': '',
                                 'other_meeting_times': ''
                                 })
        keyboard = await make_menu_meeting_times_call(lang=lang)
        await call.message.edit_reply_markup(reply_markup=keyboard)


@dp.callback_query_handler(state=PersonalDataPrivate.meeting_times)
async def answer_meeting_times(call: CallbackQuery, state: FSMContext):
    callback_data_l = call.data.split(':')
    # s = ['show', 'level', 'False', 'accommodation', 'k']
    # s = ['show', 'level', '', 'chairman', '']
    print("@@@@ meeting_formats @@@@@@@@@@@@@", callback_data_l)
    data = await state.get_data()

    call_button = callback_data_l[3]
    # button_state = callback_data_l[2]
    print("call_button = callback_data_l[3]", call_button)

    if call_button != "➡ Next ➡":
        state_button = data.get(call_button)
        change_button = "" if state_button.startswith("✅ ") else "✅ "
        await state.update_data({call_button: change_button})
        data = await state.get_data()
        lang = data.get('language')

        january = data.get('january')
        february = data.get('february')
        march = data.get('march')
        april = data.get('april')
        may = data.get('may')
        june = data.get('june')
        july = data.get('july')
        august = data.get('august')
        september = data.get('september')
        october = data.get('october')
        november = data.get('november')
        december = data.get('december')
        soonest_time = data.get('soonest_time')
        other_meeting_times = data.get('other_meeting_times')
        if lang == 'en':
            keyboard = await make_menu_meeting_times_call(january=january, february=february, march=march,
                                                          april=april,
                                                          may=may, june=june, july=july, august=august,
                                                          september=september, october=october, november=november,
                                                          december=december, soonest_time=soonest_time,
                                                          other_meeting_times=other_meeting_times, lang=lang
                                                          )
            await call.message.edit_reply_markup(reply_markup=keyboard)
        else:
            keyboard = await make_menu_meeting_times_call(january=january, february=february, march=march,
                                                          april=april,
                                                          may=may, june=june, july=july, august=august,
                                                          september=september, october=october, november=november,
                                                          december=december, soonest_time=soonest_time,
                                                          other_meeting_times=other_meeting_times, lang=lang)

            await call.message.edit_reply_markup(reply_markup=keyboard)
    elif call_button == "➡ Next ➡":
        print("Please elif call_button == ➡ Next ➡")
        lang = data.get('language')
        text = "<b>Number of expected meetings</b>" if lang == "en" else "<b>Количество ожидаемых встреч</b>"
        await call.message.answer(text)
        await PersonalDataPrivate.expected_meetings.set()


@dp.message_handler(state=PersonalDataPrivate.expected_meetings)
async def answer_expected_meetings(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    expected_meetings = message.text
    await state.update_data({
        "expected_meetings": expected_meetings
    })
    if lang == "en":
        await message.answer("<b>Hereby I confirm above mentioned data and "
                             "by submitting this form, "
                             "consent to the processing of personal data</b>",
                             reply_markup=check_private_en
                             )
    else:
        await message.answer("<b>Настоящим подтверждаю вышеуказанные данные и"
                             "отправив эту форму,"
                             "согласие на обработку персональных данных</b>",
                             reply_markup=check_private_ru
                             )
    await PersonalDataPrivate.check.set()


@dp.message_handler(state=PersonalDataPrivate.check)
async def answer_check(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    check = message.text
    # await message.delete()
    if lang == 'en':
        if check == 'I agree':
            await message.answer("Thanks", reply_markup=types.ReplyKeyboardMarkup())
        else:
            await message.answer("You are Refused", reply_markup=types.ReplyKeyboardMarkup())
    else:
        if check == 'Я согласен':
            await message.answer("Спасибо", reply_markup=types.ReplyKeyboardMarkup())
        else:
            await message.answer("Вам отказали", reply_markup=types.ReplyKeyboardMarkup())
    await state.finish()
