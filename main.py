import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message

from FSMachine import handlers
from FSMachine.handlers import storage
from Keyboard.ReplyKeyboard import keyboard1
from confing import myconfig


async def main():
  print("ЗАРАБОТАЛО ЖИЕСТЬ")
#Объект бота
#6604848876: AAEmg5hfZPjzUNbFAkJ3BfrpkZyFN3wwF3M
  bot = Bot(token=myconfig.bot_token.get_secret_value())
# Диспетчер
  dp = Dispatcher(storage=storage)

  @dp.message(Command('start'),StateFilter(default_state))
  async def start_command(message: Message):
      await message.answer(
          text="Приветствую! Это Тестовый Бот для практики!")
      await message.answer(
          text='Для начала. Я могу просить твое ФИО?',
          reply_markup = keyboard1
      )

  dp.include_routers(
      handlers.router
  )
  await bot.delete_webhook(drop_pending_updates=True)
  await dp.start_polling(bot)

if __name__ == '__main__':
   logging.basicConfig(level=logging.INFO)
   asyncio.run(main())