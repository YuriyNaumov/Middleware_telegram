from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("get_cat", "Прислать кота"),
            types.BotCommand("more_cats", "Прислать больше котов"),
            types.BotCommand("channels","Список каналов  на подписку"),
            types.BotCommand("create_post","Предложить пост в канале"),
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("set_photo","Установить фото в часте"),
            types.BotCommand("set_title","Установить название группы"),
            types.BotCommand("set_description", "Установить описание группы"),
            types.BotCommand("ro", "Режим Read Only"),
            types.BotCommand("unro", "Отключить RO"),
            types.BotCommand("ban", "Забанить"),
            types.BotCommand("unban", "Разбанить"),


        ]
    )
