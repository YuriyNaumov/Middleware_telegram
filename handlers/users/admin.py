from aiogram import types
from filters import IsPrivate
from loader import dp

@dp.message_handler(user_id=[170719594], text=['admin'])
@dp.message_handler(user_id=[170719594], text=['secret'])  ##admin or secret логическое ИЛИ в фильтре
async def admin_chat_secret (message:types.Message):
    await message.answer("Это секретное сообщение администратор в личной переписке")

