from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import CallbackQuery


class IsPrivate(BoundFilter):
    try:
        async def check(self, message: types.Message):
            return message.chat.type == types.ChatType.PRIVATE
    except:
        async def check_c(self, call: CallbackQuery):
            # return message.chat.type == types.ChatType.PRIVATE
            return True
