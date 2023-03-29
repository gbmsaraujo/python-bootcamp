from util_functions import ceasar
from art import logo
import os

continue_or_not = "yes"
clear = lambda: os.system('clear')

print(logo)

while continue_or_not.lower() == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    ceasar(direction=direction, text=text, shift=shift)

    continue_or_not = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    clear()

print("Goodbye! ")

