import rich

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Confirm, IntPrompt
from rich.columns import Columns

console = Console()


def display_cash_register():
    total_amount = 0

    while True:
        console.print(Panel(Text(f"Total amount: ${total_amount}", style="bold green")))
        action = Confirm.ask("Do you want to add an item to the cash register?")

        if not action:
            break

        item_price = IntPrompt.ask("Enter the price of the item:")
        total_amount += item_price

    console.print(Panel(Text(f"Final total amount: ${total_amount}", style="bold green")))


display_cash_register()
print()
print()



const_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
const_lower = 'abcdefghijklmnopqrstuvwxyz'

def caesar_cipher(word, shift):
    result = ""
    for char in word:
        if char.isupper():
            index = const_upper.index(char)
            new_index = (index + shift) % 26
            result += const_upper[new_index]
        elif char.islower():
            index = const_lower.index(char)
            new_index = (index + shift) % 26
            result += const_lower[new_index]
        else:
            result += char
    return result

def encrypt_text(text):
    words = text.split()
    encrypted_words = []
    for word in words:
        shift = len(word)
        encrypted_word = caesar_cipher(word, shift)
        encrypted_words.append(encrypted_word)
    return ' '.join(encrypted_words)

input_text = 'Okey, Google!'
output_text = encrypt_text(input_text)
print(output_text)