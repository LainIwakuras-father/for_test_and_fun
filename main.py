import asyncio
import logging
from aiogram import Bot, Dispatcher

from handlers import stars_comand,id
from FSMachine import states
from confing import myconfig


async def main():
#Объект бота
  bot = Bot(token=myconfig.bot_token.get_secret_value())
# Диспетчер
  dp = Dispatcher()

  dp.include_routers(
      states.router,
      stars_comand.router,
      id.router
  )
  await bot.delete_webhook(drop_pending_updates=True)
  await dp.start_polling(bot)

if __name__ == '__main__':
   logging.basicConfig(level=logging.INFO)
   asyncio.run(main())