from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from loader import dp, bot


@dp.message_handler(text="/start")
async def bot_echo(message: types.Message):
    chat_id = message.chat.id
    text = "Ты нажал старт/"
    await bot.send_message(chat_id=chat_id, text=text)
    await message.answer(text)
    await message.reply(text)


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(content_types=types.ContentTypes.VIDEO | types.ContentTypes.TEXT | types.ContentTypes.PHOTO




                    )
async def bot_echo(message: types.Message):
    chat_id = message.chat.id
    text = message.text
    # await bot.send_message(chat_id=chat_id,text=text)
    print(message.from_user.id)
    print(message.from_user.id in ADMINS)
    if str(message.from_user.id) in ADMINS:
        await message.answer('Так сказал повелитель')
    else:
        await message.answer('А подробней?')


# await message.reply(text)

@dp.channel_post_handler()  # hendler канала к которому подключен бот
async def bot_echo(message: types.Message):
    chat_id = message.sender_chat.id
    text = message.text
    await bot.send_message(chat_id=chat_id, text=text)
    await message.answer(text)
    await message.reply(text)

# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
# @dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
# async def bot_echo_all(message: types.Message, state: FSMContext):
#     state = await state.get_state()
#     await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
#                          f"\nСодержание сообщения:\n"
#                          f"<code>{message}</code>")
