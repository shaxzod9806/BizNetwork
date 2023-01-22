from aiogram.dispatcher.filters.state import StatesGroup, State


# Shaxsiy ma'lumotlarni yig'sih uchun PersonalData holatdan yaratamiz
class PersonalData(StatesGroup):
    language = State()
    photo = State()
    fullname = State()
    born_address = State()
    live_address = State()
    company_name = State()
    company_position = State()
    company_address = State()
    hobbies = State()
    reason_chat = State()
    your_superpower = State()
    your_value = State()
    help_community = State()
    instagram_link = State()
    linkedin_link = State()
    company_website = State()
    check = State()
    can_private = State()


class PersonalDataPrivate(StatesGroup):
    company_type = State()
    company_website = State()
    email = State()
    birthday = State()
    phone_number = State()
    company_size = State()
    business_type = State()
    industries = State()
    we_would_meet = State()
    meeting_formats = State()
    meeting_times = State()
    expected_meetings = State()
    check = State()
