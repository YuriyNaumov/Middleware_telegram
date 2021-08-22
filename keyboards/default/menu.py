from aiogram.types import reply_keyboard, KeyboardButton, ReplyKeyboardMarkup

menu = ReplyKeyboardMarkup([
    [
        KeyboardButton(text="Котлетки")
    ],
    [
        KeyboardButton(text="Макарошки"),
        KeyboardButton(text="Пюрешка")
    ]


], resize_keyboard = True
)

