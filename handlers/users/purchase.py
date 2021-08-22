import logging
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choice_buttons import choice, pear_keyboard

from loader import dp, bot

@dp.message_handler(Command("items"))
async def show_items(message: types.Message):
    await message.answer(text="У нас есть 5 яблок и 10 груш \n"
                              "Если Вам ничего не нужно, нажимите отмену",
                         reply_markup=choice)

@dp.callback_query_handler(buy_callback.filter(item_name="pear"))
async def buying_pear(call:CallbackQuery, callback_data:dict):
    await  call.answer(cache_time=60)
    logging.info(f"callback_data={call.data}")
    logging.info(f"callback_data_dict={callback_data}")
    quantity = callback_data.get("quantity")
    color = callback_data.get("color")
    await call.message.answer(f"Вы выбрать купить грушу. Груш всего {quantity}. Цвет {color}. Спасибо",
                              reply_markup=pear_keyboard)

@dp.callback_query_handler(buy_callback.filter(item_name="apple"))
async def buying_apple(call:CallbackQuery, callback_data:dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data={call.data}")
    logging.info(f"callback_data_dict={callback_data}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"Вы выбрать купить яблоки. Яблок всего {quantity}. Спасибо")

@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    # Ответим в окошке с уведомлением!
    logging.info(f"canceldata={call}")
    await call.answer("Вы отменили эту покупку!", show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)