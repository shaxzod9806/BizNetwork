from aiogram.dispatcher.filters.state import StatesGroup, State


# Shaxsiy ma'lumotlarni yig'sih uchun PersonalData holatdan yaratamiz
class PersonalData(StatesGroup):
    language = State()
    fullname = State()
    address = State()
    age = State()
    workplace = State()
    job = State()
    phone_number = State()
    email = State()
    check = State()
