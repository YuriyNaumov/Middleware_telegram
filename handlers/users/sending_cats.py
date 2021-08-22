from aiogram.dispatcher.filters import Command
from aiogram.types import ContentType, Message, InputFile, MediaGroup

from loader import dp, bot


@dp.message_handler(content_types=ContentType.PHOTO)
async def get_file_id_p(message: Message):
    await message.reply(message.photo[-1].file_id)

@dp.message_handler(content_types=ContentType.VIDEO)
async def get_file_id_v(message: Message):
    await message.reply(message.video.file_id)


@dp.message_handler(Command("get_cat"))
async def send_cat(message: Message):
    photo_file_id = "AgACAgQAAxkBAAIEfmEZO9Y8SWqCSxPrBSUIf_QqkJGZAALhqzEb1ki1UE04cxPNn7lcAQADAgADdwADIAQ"
    photo_url = "https://www.culture.ru/storage/images/b5b7e5309630181835c39a7b11a26f06/4c7803a96c5a95f7e913a8ba7a523940.jpeg"
    photo_bytes = InputFile(path_or_bytesio="photos/cat.jpg")

    await message.answer_photo(photo=photo_url, caption="Вот тебе фото кота  /more_cats")


@dp.message_handler(Command("more_cats"))
async def more_cats(message:Message):
    album = MediaGroup()
    photo_file_id = "AgACAgQAAxkBAAIEfmEZO9Y8SWqCSxPrBSUIf_QqkJGZAALhqzEb1ki1UE04cxPNn7lcAQADAgADdwADIAQ"
    photo_url = "https://www.culture.ru/storage/images/b5b7e5309630181835c39a7b11a26f06/4c7803a96c5a95f7e913a8ba7a523940.jpeg"
    photo_url2 = 'https://mnogo-krolikov.ru/wp-content/uploads/2019/12/word-image-10.jpeg'
    photo_bytes = InputFile(path_or_bytesio="photos/cat.jpg")
    video_file_id = "BAACAgIAAxkBAAIEgmEZPTcXR4Zlm3QTq7jv-eE0F-y_AAKQDQACaiTQSOAqz8XwrU17IAQ"
    album.attach_photo(photo_file_id)
    album.attach_photo(photo_bytes)
    album.attach_photo(photo_url)
    album.attach_photo(photo_url2)
    album.attach_video(video_file_id, caption="видео с котиком")

    # await bot.send_media_group(chat_id=message.from_user.id, media=album)
    await message.answer_media_group(media=album)


