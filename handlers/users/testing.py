from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types
from states import Test

@dp.message_handler(Command("test"), state=None)
async def enter_test(message:types.Message, state:FSMContext):
    await message.answer("Вы начали тестирование .\n"
                         "Вопрос №1. \n\n"
                         "Часто ли Вы занимаетесь бессмысленными делами?")


    await Test.Q1.set() # состояние на 1-ый вопрос. записываем 1-ый ответ (1-ое состояние)


@dp.message_handler(state=Test.Q1)
async def answer_q1(message:types.Message, state:FSMContext):

    answer = message.text
    await state.update_data({
        "answer1": answer
    })

    await message.answer("Вопрос №2. \n\n"
                         "Ухудшилась ли у Вас память?")

    await Test.Q2.set() # Устанавливаем 2-ое состояние  await Test.next()



@dp.message_handler(state=Test.Q2)
async def answer_q1(message:types.Message, state:FSMContext):

    answer = message.text
    await state.update_data({
        "answer2": answer
    })

    data = await state.get_data()

    answer1 = data.get("answer1")
    answer2 = data.get("answer2")

    if (answer1 == 'да') and (answer2 == 'да'):
        await message.answer("Спасибо за Ваши ответы. Все правильно")
        await message.answer(f"Ответ 1: {answer1}")
        await message.answer(f"Ответ 2: {answer2}")
    elif answer1 == 'нет':
        await message.answer("Спасибо за Ваши ответы")
        await message.answer(f"Ответ на 1-ый вопрос не верный")
    else:
        await message.answer("Спасибо за Ваши ответы")
        await message.answer(f"Все не верно")

    await state.finish() #сбрасываем состояния await state.reset_state() or state.reset_state(with_data=False) оставит данные


