import re
import logging
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.deep_linking import get_start_link
from filters import IsPrivate
from filters.test_filter import SomeF
from loader import dp, bot
from utils.db_api.models import User
from utils.misc import rate_limit
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@dp.message_handler(CommandStart(deep_link=re.compile(r"\d\d\d"))) # проверка функции
async def bot_start(message: types.Message):
    referal = message.get_args()
    await message.answer(f"Привет {message.from_user.full_name} Ты нажал на старт и передал аргумент с 3мя цифрами - {referal}\n"
                         f"Вы находитесь в личной переписке\n"
                         f"Молодец!!!,")



@rate_limit(5, key="start")
@dp.message_handler(CommandStart(),SomeF())
async def bot_start(message: types.Message, middleware_data, from_filter, user:User):
    await message.answer(f"Привет, {message.from_user.full_name}!\n {middleware_data=} \n {from_filter=}",
                         reply_markup = InlineKeyboardMarkup(
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text="простая кнопка", callback_data="button")
                                    ]
                                ]
                            ))

    logging.info(f"6. Handler")
    logging.info(f"Следующая точка: Post Process Message")
    non_existing_user  = 666666
    try:
        await message.answer('не праваильно закрыт тег <b>тег<b>')
    except Exception as err:
        await message.answer(f"Ошибка: {err} ")

    #Не попадает в еррор хэндлер
    try:
        await bot.send_message(chat_id=non_existing_user,text="не существует пользователя")
    except Exception as err:
        await message.answer(f"Не попало в хендлер.Ошибка {err}")

    await message.answer(f"Какой-то странный тег <kek>вот</kek>")

    return {"from_handler":"Данные из хэндлера"} # Передаем в  мидлваре в месседж постпроцесс

    # deep_link  = await get_start_link(payload="123")
    # await message.answer(f"Ты нажал на старт и в Вашей команде нет диплинка \n"
    #                      f"Выша диплинк сыылка {deep_link} ")


@dp.callback_query_handler(text='button')
async def get_button(call: types.CallbackQuery):
    await call.message.answer("Вы нажали на кнопку")


@dp.message_handler(commands=['my_help'])
async def help_start(message: types.Message):
    await message.answer("Ты нажал help")



# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     await message.answer(f"Привет, {message.from_user.full_name}!")
