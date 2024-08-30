from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, state
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor




API_TOKEN = ''
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)



class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start_message(message):
     await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler(Command("Calories"))
async def start_command(message: types.Message):
    await message.answer("Введите 'Calories' для начала.")


@dp.message_handler(Command("help"))
async def help_command(message: types.Message):
    await message.answer("Введите 'Calories' для начала процесса расчета нормы калорий. "
                         "Следуйте инструкциям, чтобы ввести свой возраст, рост и вес.")


@dp.message_handler(lambda message: message.text == 'Calories')
async def set_age(message: types.Message):
    await UserState.age.set()
    await message.answer("Введите свой возраст:")


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пожалуйста, введите корректный возраст (число).")
        return

    await state.update_data(age=message.text)
    await UserState.growth.set()
    await message.answer("Введите свой рост:")


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пожалуйста, введите корректный рост (число).")
        return

    await state.update_data(growth=message.text)
    await UserState.weight.set()
    await message.answer("Введите свой вес:")


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пожалуйста, введите корректный вес (число).")
        return

    await state.update_data(weight=message.text)


    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])


    bmr = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.answer(f"Ваша норма калорий: {bmr:.2f} калорий в день.")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
