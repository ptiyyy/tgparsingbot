import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from parser import get_anekdot


bot = Bot(token="7381384322:AAEpdlq3l4gerrr1I3zq8ib6q7qK4VRSeo8")
dp = Dispatcher()
tgkeyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="выслать говна")]
],
    resize_keyboard=True,
    input_field_placeholder='меню снизу если чё')


@dp.message(CommandStart())
async def cmd_sart(message: Message):
    with open("anekdot.txt") as file:
        anekdot = file.read()
    await message.answer(anekdot, reply_markup=tgkeyboard)
    get_anekdot()


@dp.message(F.text == 'выслать говна')
async def govna(message: Message):
    get_anekdot()
    with open("anekdot.txt") as file:
        anekdot = file.read()
    await message.answer(anekdot, reply_markup=tgkeyboard)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
