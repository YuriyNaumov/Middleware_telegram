from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import menu
from loader import dp

@dp.message_handler(Command("menu"))
async def show_menu(message:types.Message):
    await message.answer("Выберите товар из меню ниже", reply_markup=menu)


@dp.message_handler(text="Котлетки")
async def get_cotletki(message:types.Message):
    await message.answer("Вы выбрали котлектки.")


@dp.message_handler(Text(equals=["Пюрешка", "Макарошки"]))
async def get_food(message: types.Message):
    await message.answer(f"Вы выбрали: {message.text}", reply_markup=ReplyKeyboardRemove())