from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Создание клавиатуры
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton(text='Рассчитать')
button_info = KeyboardButton(text='Информация')
button_buy = KeyboardButton(text="Купить")
kb.add(button_calculate, button_info, button_buy)

# Создание Inline-клавиатуры
inline_kb = InlineKeyboardMarkup()
button_calories = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_kb.add(button_calories, button_formulas)

inline_kb_products = InlineKeyboardMarkup()
button_product1 = InlineKeyboardButton(text='Продукт 1', callback_data='buy_product1')
button_product2 = InlineKeyboardButton(text='Продукт 2', callback_data='buy_product2')
button_product3 = InlineKeyboardButton(text='Продукт 3', callback_data='buy_product3')
button_product4 = InlineKeyboardButton(text='Продукт 4', callback_data='buy_product4')
button_back = InlineKeyboardButton(text='Назад', callback_data='back_to_main_menu')
inline_kb_products.add(button_product1, button_product2, button_product3, button_product4, button_back)