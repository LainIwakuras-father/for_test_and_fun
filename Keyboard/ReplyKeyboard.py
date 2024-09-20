from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
kb = [
          [KeyboardButton(text='Да'),KeyboardButton(text='Нет')]
      ]

keyboard1 = ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='нажми на ссылки дебил'
)