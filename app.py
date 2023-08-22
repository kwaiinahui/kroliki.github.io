try:
    from aiogram  import Bot, types
    from aiogram  import Dispatcher, executor
    from aiogram.types.web_app_info import WebAppInfo
except:
    print("Ошибка подключения библиотеки")


bot = Bot(token='5852154761:AAGSak29zotWI1ibuMxfxuk_o8fEFFIEBXA')
dp = Dispatcher(bot=bot)
web_app_info = WebAppInfo(url='https://itproger.com')


@dp.message_handler(commands=['start'])
async def process_start_command(msg: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Перейти", web_app=web_app_info))
    await msg.answer("Привет мой друг", reply_markup=markup)
    



if __name__ == '__main__':
    print('Bot is starting..')
    executor.start_polling(dp)