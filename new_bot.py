import asyncio
import logging


from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import initiate_db, get_all_products, populate_db

logging.basicConfig(level=logging.INFO)

from new_config import *
from new_keyboard import *
import new_text
from new_admin import *
from crud_functions import *


bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)



class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer(new_text.start,reply_markup=main_menu_keyboards())

@dp.message_handler(lambda message: message.text == 'Информация')
async def help_message(message: types.Message):
    with open('files_update/bot.png', "rb") as img:
        await message.answer_photo(img, new_text.Информация, reply_markup=main_menu_keyboards())



@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    await message.answer(new_text.Рассчитать, reply_markup=inline_keyboards())


@dp.message_handler(lambda message: message.text == 'Купить')
async def buy_menu(message: types.Message):
    products = get_all_products()
    await message.answer("Доступные товары:")
    for product in products:
        caption = f"Название: {product[1]}\nОписание: {product[2]}\nЦена: {product[3]} р."
        await message.answer_photo(photo=open(product[4], "rb"), caption=caption)
    inline_kb = create_product_keyboard(products)
    await message.answer("Выберите продукт, нажав на кнопку ниже:", reply_markup=inline_kb)


@dp.callback_query_handler(lambda call: call.data.startswith('buy_product'))
async def show_product_details(call: types.CallbackQuery):
    product_id = int(call.data.split('_')[-1])
    product = get_all_products()[product_id - 1]

    # Отправляем изображение и описание продукта
    await call.message.answer_photo(photo=open(product[4], "rb"),
                                    caption=f"Название: {product[1]}\nОписание: {product[2]}\nЦена: {product[3]} р.")
    await call.message.answer("Товар добавлен в корзину.")
    await call.message.answer("Вы успешно приобрели продукт! Спасибо за покупку!")
    await call.answer()



@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer(new_text.formulas)
    await call.answer()

@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await UserState.age.set()
    await call.message.answer(new_text.calories)
    await call.answer()

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


if __name__ == '__main__':
    initiate_db()
    populate_db()
    executor.start_polling(dp, skip_updates=True)
