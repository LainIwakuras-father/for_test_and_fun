from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters import StateFilter, Command
from aiogram.fsm.state import  default_state
from Keyboard.ReplyKeyboard import keyboard1

router = Router()


@router.message(Command('start'),StateFilter(default_state))
async def start_command(message: Message):
      await message.answer(
          text="Приветствую! Это Тестовый Бот для практики!")
      await message.answer(
          text='Для начала. Я могу просить твое ФИО?',
          reply_markup = keyboard1
      )