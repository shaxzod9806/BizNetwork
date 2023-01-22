from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

check_keyboard_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✅ YES'),
            KeyboardButton(text='❌ NO'),
        ],
    ],
    resize_keyboard=True
)
check_keyboard_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✅ ДА'),
            KeyboardButton(text='❌ НЕТ'),
        ],
    ],
    resize_keyboard=True
)
start_private_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="I'm Interested"),
            KeyboardButton(text="Not Interested"),
        ],
    ],
    resize_keyboard=True
)
start_private_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Мне это интересно'),
            KeyboardButton(text="Не интересует"),
        ],
    ],
    resize_keyboard=True
)
check_private_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='I agree'),
            KeyboardButton(text="Refuse"),
        ],
    ],
    resize_keyboard=True
)
check_private_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Я согласен'),
            KeyboardButton(text="Отказаться"),
        ],
    ],
    resize_keyboard=True
)



add_company_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✅ YES'),
            KeyboardButton(text='❌ NO'),
        ],
    ],
    resize_keyboard=True
)

add_company_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✅ ДА'),
            KeyboardButton(text='❌ НЕТ'),
        ],
    ],
    resize_keyboard=True
)
