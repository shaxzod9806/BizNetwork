from aiogram import types

from filters import IsGroup
from loader import dp


@dp.message_handler(IsGroup(), text='/start')
async def bot_start(message: types.Message):
    # await message.answer(f"Salom, {message.from_user.full_name}!")
    lang = await message.from_user.language_code
    text = f"""
            {lang} Ro'yxatdan o'ting
    """
    await message.answer(text)
