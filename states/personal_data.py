from aiogram.dispatcher.filters.state import StatesGroup, State


# Shaxsiy ma'lumotlarni yig'sih uchun PersonalData holatdan yaratamiz
class PersonalData(StatesGroup):
    language = State()
    fullname = State()
    company_name = State()
    company_address = State()
    company_website = State()
    email = State()
    phone_number = State()
    expected_meetings = State()
    company_type = State()
    company_size = State()
    business_type = State()
    industries = State()
    we_would_meet = State()
    meeting_formats = State()
    meeting_times = State()
    check = State()
