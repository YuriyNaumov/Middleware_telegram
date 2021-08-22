import logging

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from data.config import banned_users

class BigBrother(BaseMiddleware):
    #1
    async def on_pre_process_update(self, update:types.Update, data:dict):
        logging.info("[-----------------новый апдейт-----------------------]")
        logging.info("1. Pre Process Update")
        logging.info("Следущая  точка: Process Update")
        data["middleware_data"] = "Это пойдет до on_post_process_update"
        if update.message:
            user = update.message.from_user.id
        elif update.callback_query:
            user = update.callback_query.from_user.id
        else:
            return

        if user in banned_users:
            raise CancelHandler()

    #2
    async def on_process_update(self, update:types.Update, data:dict):
        logging.info(f"2. Process Update {data=}")
        logging.info("Следующая точка: Pre Process Message")
    #3
    async def on_pre_process_message(self, message:types.Message, data:dict):
        logging.info(f"3. Preprocess Message {data=}")
        logging.info(f"Следующая точка filters, process Message")
        data['middleware_data'] = "Это пройдет в on_process_message"
    # 4 Filers

    # 5.
    async def on_process_message(self, message: types.Message, data:dict):
        logging.info(f"5.Process Message")
        logging.info("Следующая точка: Handler")
        data["middleware_data"] = "Это попадет в хендлер"

    #6.  Handler

    #7.
    async def on_post_process_message(self, message:types.Message, data_from_handler:list, data:dict):
        logging.info(f"7. Post process Message, {data=}, {data_from_handler=}")
        logging.info("Следующая точка: Post Proces Update")

    #8
    async def on_post_process_update(self, update:types.Update, data:dict, data_from_handler:list):
        logging.info(f"8. Post Process Update, {data=}, {data_from_handler=}")
        logging.info("__________________Конец_______________________")

