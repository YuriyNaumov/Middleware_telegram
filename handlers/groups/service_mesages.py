from filters import IsGroup
from loader import types, bot
from loader import dp
import logging


@dp.message_handler(IsGroup(), content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def new_member(message: types.Message):
    members = ", ".join([m.get_mention(as_html=True) for m in message.new_chat_members])
    logging.info(members)
    logging.info(message)
    await message.reply(f"Привет, {members}.")
    # await message.reply(f"Привет, {message.new_chat_members[0].last_name}.")


@dp.message_handler(IsGroup(), content_types=types.ContentTypes.LEFT_CHAT_MEMBER)
async def banned_member(message: types.Message):
    if message.left_chat_member.id == message.from_user.id:
        await message.answer(f"{message.left_chat_member.get_mention(as_html=True)} вышел из чата")
    elif message.from_user.id == (await bot.me).id:
        return
    else:
        await message.answer(f"{message.left_chat_member.full_name} был удален из чата"
                             f"пользователем {message.from_user.full_name}.")
