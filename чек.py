import tkinter as tk
from tkinter import messagebox

list_items = []
amount = []


def add_cas():
    items = item_entry.get()
    price = price_entry.get()

    list_items.append(items)
    amount.append(price)

    item_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

    messagebox.showinfo("Успешно", "Товар добавлен в корзину!")


def check_cart():
    cart_text = ""
    for i in range(len(list_items)):
        cart_text += f"{list_items[i]} - {amount[i]} .руб \n "

    messagebox.showinfo("Содержимое корзины", cart_text)


def clear_cart():
    list_items.clear()
    amount.clear()
    messagebox.showinfo("Корзина очищена", "Ваша корзина теперь пуста")


def create_check():
    total_price = sum([int(i) for i in amount])
    len_items = len(list_items)
    name_saller = 'Владимир Геращенко'
    name_of_shop = '"ВСЁ, ЧТО НУЖНО!"'
    street_shop = 'г.о. Тольятти Южное шоссе 155б'

    check_text = f'''  
        
             Название магазина:
             
                  {name_of_shop}
                
             Адрес магазина:
             
            {street_shop}
                  
            Продавец: {name_saller}
                
            ___________________________
            Кол-во товаров:  {len_items}
            Общая стоимость: {total_price}.руб
            
                ____________________________
                
         Большое спасибо за покупку!
            Будем ждать вас еще!
    '''


    messagebox.showinfo("Чек", check_text)


root = tk.Tk()
root.title("Печать чека")
root.geometry("250x250")
root.resizable( False, False)
item_label = tk.Label(root, text="Введите название товара:")
item_label.pack()

item_entry = tk.Entry(root)
item_entry.pack()

price_label = tk.Label(root, text="Введите цену товара:")
price_label.pack()

price_entry = tk.Entry(root)
price_entry.pack()

add_button = tk.Button(root, text="Добавить товар", command=add_cas)
add_button.pack()
# add_button.place(x=80, y=160)
check_button = tk.Button(root, text="Что в корзине", command=check_cart)
check_button.pack()

clear_button = tk.Button(root, text="Очистить корзину", command=clear_cart)
clear_button.pack()

create_button = tk.Button(root, text="Создать чек", command=create_check)
create_button.pack()

root.mainloop()
