from aiogram import Dispatcher


from .throttling import ThrottlingMiddleware
from .big_brother import BigBrother
from  .acl import ACLMiddleWare
from .sentinel import Sentinel

from loader import dp


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(ACLMiddleWare())
    dp.middleware.setup(BigBrother())
    dp.middleware.setup(Sentinel())

