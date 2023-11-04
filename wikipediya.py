import wikipedia
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message


bot_token = '6727540928:AAGo66K-sHJvcSdC2uAbIExeO8pLlUeAXA8'
bot = Bot(token=bot_token)
dp = Dispatcher(bot)
wikipedia.set_lang('uz')

@dp.message_handler(commands=['start', ])
async def startfun(message: Message):
    await message.reply(f"Wikipediya botga xush kelibsiz {message.from_user.full_name}")

@dp.message_handler()
async def wikifun(msg: Message):
    try:
        respon = wikipedia.summary(msg.text)
        await msg.reply(respon)
    except:
        await msg.reply("Bunday maqola yoq")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
