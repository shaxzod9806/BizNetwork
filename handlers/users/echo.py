from aiogram import types

from filters import IsPrivate
from loader import dp, bot


# Echo bot
# @dp.message_handler(state=None)
# @dp.message_handler(IsPrivate(),state=None)
# @dp.message_handler(state=None)
# async def bot_echo(message: types.Message):
#     # await message.answer(bot.get_me())
#     # await message.answer(bot.get_me())
#     await bot.send_message(chat_id=-1001895105606,text="-kj")
