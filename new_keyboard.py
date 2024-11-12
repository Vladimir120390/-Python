from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Создание клавиатуры меню
def main_menu_keyboards ():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button_register = KeyboardButton(text="Регистрация")
    button_calculate = KeyboardButton(text='Рассчитать')
    button_info = KeyboardButton(text='Информация')
    button_buy = KeyboardButton(text="Купить")

    kb.add(button_register, button_info,button_calculate, button_buy)
    return kb


# Создание Inline-клавиатуры расчёта
def inline_keyboards():
    inline_kb = InlineKeyboardMarkup()
    button_calories = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
    button_formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
    inline_kb.add(button_calories, button_formulas)
    return inline_kb

# создание inline-клавиатуры продуктов
def inline_products_keyboard():
    inline_kb_products = InlineKeyboardMarkup()
    button_product1 = InlineKeyboardButton(text='Продукт 1', callback_data='buy_product1')
    button_product2 = InlineKeyboardButton(text='Продукт 2', callback_data='buy_product2')
    button_product3 = InlineKeyboardButton(text='Продукт 3', callback_data='buy_product3')
    button_product4 = InlineKeyboardButton(text='Продукт 4', callback_data='buy_product4')
    button_back_to_products = InlineKeyboardButton(text='Назад', callback_data='back_to_products')  # Кнопка "Назад"
    button_back_to_main_menu = InlineKeyboardButton(text='Вернуться в главное меню', callback_data='back_to_main_menu')  # Кнопка "Назад в главное меню"
    inline_kb_products.add(button_product1, button_product2, button_product3, button_product4, button_back_to_products)
    return inline_kb_products


# Создаем кнопку для каждого продукта
def create_product_keyboard(products):
    inline_kb = InlineKeyboardMarkup()
    for index, product in enumerate(products):
        button = InlineKeyboardButton(text=product[1], callback_data=f'buy_product_{index + 1}')
        inline_kb.add(button)
    return inline_kb





