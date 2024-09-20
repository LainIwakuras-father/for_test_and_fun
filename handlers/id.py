
from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters import StateFilter, Command
from aiogram.fsm.state import  default_state


router = Router()


@router.message(Command('id'),StateFilter(default_state))
async def start_command(message: Message):
      await message.answer(text=message.from_user.id)
