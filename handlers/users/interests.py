from aiogram.dispatcher import FSMContext

from keyboards.inline.hobbies_callback_button import make_hobbies_call
from loader import dp, bot
from aiogram.types import CallbackQuery, Message

from states.personal_data import PersonalData
from filters import IsPrivate


# Your Hobbies
@dp.callback_query_handler(state=PersonalData.hobbies)
async def answer_hobbies(call: CallbackQuery, state: FSMContext):
    callback_data_l = call.data.split(':')
    print("@@@@@@@@@@@@@@@@@", callback_data_l)
    data = await state.get_data()
    lang = data.get('language')
    call_button = callback_data_l[3]
    button_state = callback_data_l[2]
    print(call_button != "➡ Next ➡")
    if call_button != "➡ Next ➡":
        change_button = "" + call_button if button_state.startswith("✅ ") else "✅ " + call_button
        print('change_button', change_button)
        print(button_state)
        await state.update_data({call_button: change_button})

        print("data.get('business_type_button')b", await state.get_data())
        data = await state.get_data()
        sports = data.get('sports')
        mindfulness = data.get('mindfulness')
        outdoor = data.get('outdoor')
        health_wellness = data.get('health_wellness')
        startups = data.get('startups')
        entrepreneurship = data.get('entrepreneurship')
        investments = data.get('investments')
        business_breakfasts = data.get('business_breakfasts')
        b2b_meetings = data.get('b2b_meetings')
        business_traveling = data.get('business_traveling')
        self_development = data.get('self_development')
        international_relations = data.get('international_relations')
        professional_networking = data.get('professional_networking')
        business_games = data.get('business_games')
        other_hobbies = data.get('other_hobbies')
        keyboard = await make_hobbies_call(sports=sports, mindfulness=mindfulness, outdoor=outdoor,
                                           health_wellness=health_wellness, startups=startups,
                                           entrepreneurship=entrepreneurship,
                                           investments=investments, business_breakfasts=business_breakfasts,
                                           b2b_meetings=b2b_meetings,
                                           business_traveling=business_traveling, self_development=self_development,
                                           international_relations=international_relations,
                                           professional_networking=professional_networking,
                                           business_games=business_games,
                                           other_hobbies=other_hobbies, lang='en')
        await call.message.edit_reply_markup(reply_markup=keyboard)
    elif call_button == "➡ Next ➡":
        # await call.message.delete_reply_markup()
        await call.message.delete()
        if lang == 'en':
            await call.message.answer('<b>The reason that you joined to this chat:</b>')
        else:
            await call.message.answer('<b>Причина, по которой вы присоединились к этому чату:</b>')
        await PersonalData.reason_chat.set()


@dp.message_handler(IsPrivate(), state=PersonalData.reason_chat)
async def answer_reason_chat(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    reason_chat = message.text
    await state.update_data({'reason_chat': reason_chat})
    if lang == 'en':
        await message.answer('<b>What is your superpower:</b>')
    else:
        await message.answer('<b>В чем твоя суперсила:</b>')
    await PersonalData.your_superpower.set()


@dp.message_handler(IsPrivate(), state=PersonalData.your_superpower)
async def answer_your_superpower(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    your_superpower = message.text
    await state.update_data({'your_superpower': your_superpower})
    if lang == 'en':
        await message.answer('<b>How you can be helpful to this community?</b>')
    else:
        await message.answer('<b>Как вы можете быть полезны этому сообществу?</b>')
    await PersonalData.your_value.set()


@dp.message_handler(IsPrivate(), state=PersonalData.your_value)
async def answer_your_value(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    your_value = message.text
    await state.update_data({'your_value': your_value})
    if lang == 'en':
        await message.answer('<b>What kind of help you need from Business Community?</b>')
    else:
        await message.answer('<b>Какая помощь вам нужна от бизнес-сообщества?</b>')
    await PersonalData.help_community.set()


@dp.message_handler(IsPrivate(), state=PersonalData.help_community)
async def answer_help_community(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get('language')
    help_community = message.text
    await state.update_data({'help_community': help_community})
    if lang == 'en':
        await message.answer('<b>Web site of your company (optional):</b>')
    else:
        await message.answer('<b>Сайт вашей компании (необязательно):</b>')
    await PersonalData.company_website.set()
