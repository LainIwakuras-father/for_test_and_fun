from aiogram import Router, F
from aiogram.filters import StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State, default_state
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message


storage = MemoryStorage()
router = Router()
# Создаем "базу данных" пользователей
#user_dict: dict = {}

#Код состояний практика  отдельные хендлеры
class FIOform(StatesGroup):
    Familia = State()
    Name = State()
    otchestvo = State()


#Хендлер отказа сразу
@router.message(F.text == 'Нет')
async def no_command(message: Message):
    await message.answer(
        text='Ну и пошел нахуй',
    )


#хендлер задующий состояние
@router.message(F.text == 'Да', StateFilter(default_state))
async def family_command(message: Message, state: FSMContext):
    await message.answer(
        text='Пожалуйста Напиши Свою Фамилию',
    )
    await state.set_state(FIOform.Familia)


#хендлер задующий состояние ФАМИЛИИ
@router.message(StateFilter(FIOform.Familia))
async def family_command(message: Message, state: FSMContext):
    await state.update_data(familia=message.text)
    await message.answer(
        text='Пожалуйста Напиши Свое Имя',
    )
    await state.set_state(FIOform.Name)

#хендлер задующий состояние ИМЕНИ
@router.message(StateFilter(FIOform.Name))
async def name_command(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(
        text='Пожалуйста Напиши Свое Отчество',
    )
    await state.set_state(FIOform.otchestvo)


#хендлер задующий состояние ОТЧЕСТВА
@router.message(StateFilter(FIOform.otchestvo))
async def otch_command(message: Message, state: FSMContext):
    await state.update_data(otchestvo=message.text)
    await message.answer(text='анкета сделана!')
    data = await state.get_data()
    print(type(data))

    await message.answer(text=f'Фамилия: {data["familia"]}\n'
                              f"Имя: {data['name']}\n"
                               f"Отчество: {data['otchestvo']}"
                         )
    await state.clear()
'''
        @router.message(Command(commands='Showdata'),StateFilter(default_state))
        async def show_command(message: Message):
            if message.from_user.id in user_dict:
                 await message.answer(text='анкета сделана!')
                 await message.answer(user_dict)
            else:
                await message.answer(text='еще не написал анкету !!!!')
'''
# Этот хэндлер будет срабатывать на команду "/cancel" в любых состояниях,
# кроме состояния по умолчанию, и отключать машину состояний
@router.message(Command(commands='cancel'),~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(
        text='Вы вышли из машины состояний\n\n'
             'Чтобы снова перейти к заполнению анкеты - '
             'отправьте просто Да'
    )
    # Сбрасываем состояние и очищаем данные, полученные внутри состояний
    await state.clear()
