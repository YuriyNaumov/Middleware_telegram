from aiogram import types
from io import BytesIO
from loader import dp
from  pathlib import Path



# @dp.message_handler(content_types=types.ContentType.DOCUMENT)
# async def get_audio(message:types.Message):
#     if message.audio:
#         file_id = message.audio.file_id
#     elif message.document:
#         file_id = message.document.file_id
#     await dp.bot.send_document(message.from_user.id, document=file_id)

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_audio(message:types.Message):
    save_to_io = BytesIO()
    await message.photo[-1].download(destination=save_to_io) # загружает  документ в байты
    await message.answer_document(types.InputFile(save_to_io, filename="Photo.jpg"))

@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def download_document(message:types.Message):
    path_to_download = Path().joinpath("items","categories","subcategories","photos")
    path_to_download.mkdir(parents=True, exist_ok=True)
    path_to_download = path_to_download.joinpath(message.document.file_name)

    await message.document.download(destination=path_to_download)
    await message.answer(f"Документ был сохранен в путь: {path_to_download}")