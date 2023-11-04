from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

bot_token = '6917688542:AAG8OAMuI6bmxpuBp62o2ALzFgR2o2QLtvA'
bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', ])
async def startfun(message: Message):
    await message.reply(f"To'ti botga xush kelibsiz {message.from_user.full_name}")


@dp.message_handler()
async def totifunc(msg: Message):
    await msg.answer(msg.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)