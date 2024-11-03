import logging
import time

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)

from new_config import *
from new_keyboard import *
import new_text

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)



class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer(new_text.start,reply_markup=kb)

@dp.message_handler(lambda message: message.text == 'Информация')
async def help_message(message: types.Message):
    # await message.answer(new_text.Информация, reply_markup=kb)
    with open('files_new/Продукт1.png', "rb") as img:
        await message.answer_photo(img, new_text.Информация, reply_markup=kb)

@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    await message.answer(new_text.Рассчитать, reply_markup=inline_kb)

@dp.message_handler(lambda message: message.text == 'Купить')
async def buy_menu(message: types.Message):
    await message.answer("Выберите продукт для покупки:", reply_markup=inline_kb_products)

@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer(new_text.formulas)
    await call.answer()  # Убираем индикатор загрузки

@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await UserState.age.set()
    await call.message.answer(new_text.calories)
    await call.answer()  # Убираем индикатор загрузки

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

    # Вычисление BMR (для женщин)
    bmr = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.answer(f"Ваша норма калорий: {bmr:.2f} калорий в день.")
    await state.finish()


@dp.callback_query_handler(lambda call: call.data == 'buy_product1')
async def buy_product1(call: types.CallbackQuery):
    await call.message.answer(new_text.buy_product1)
    time.sleep(1)
    await call.message.answer("Товар добавлен в корзину.")
    time.sleep(1)
    await call.message.answer_photo(photo=open('files_new/Продукт1.png', "rb"),
                                    caption="Вы успешно приобрели продукт! Спасибо за покупку!")
    await call.answer()


@dp.callback_query_handler(lambda call: call.data == 'buy_product2')
async def buy_product2(call: types.CallbackQuery):
    await call.message.answer(new_text.buy_product2)
    time.sleep(1)
    await call.message.answer("Товар добавлен в корзину.")
    time.sleep(1)
    await call.message.answer_photo(photo=open('files_new/Продукт2.png', "rb"),
                                    caption="Вы успешно приобрели продукт! Спасибо за покупку!")
    await call.answer()

@dp.callback_query_handler(lambda call: call.data == 'buy_product3')
async def buy_product3(call: types.CallbackQuery):
    await call.message.answer(new_text.buy_product3)
    time.sleep(1)
    await call.message.answer("Товар добавлен в корзину.")
    time.sleep(1)
    await call.message.answer_photo(photo=open('files_new/Продукт3.png', "rb"),
                                    caption="Вы успешно приобрели продукт! Спасибо за покупку!")
    await call.answer()


@dp.callback_query_handler(lambda call: call.data == 'buy_product4')
async def buy_product4(call: types.CallbackQuery):
    await call.message.answer(new_text.buy_product4)
    time.sleep(1)
    await call.message.answer("Товар добавлен в корзину.")
    time.sleep(1)
    await call.message.answer_photo(photo=open('files_new/Продукт4.png', "rb"),
                                    caption="Вы успешно приобрелипродукт! Спасибо за покупку!")
    await call.answer()



@dp.callback_query_handler(lambda call: call.data == 'back_to_main_menu')
async def back_to_main_menu(call: types.CallbackQuery):
    await call.message.answer("Возвращаемся в главное меню...", reply_markup=kb)
    await call.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
