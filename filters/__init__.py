from aiogram import Dispatcher

from .private_chat import IsPrivate
from .test_filter import SomeF


from loader import dp
# from .is_admin import AdminFilter


if __name__ == "filters":

    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(SomeF)

