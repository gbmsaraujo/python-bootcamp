import os
import random
from hangman_art import stages, logo
from hangman_words import word_list

clear = lambda: os.system('clear')
random_word = random.choice(word_list)
display = []
chances = 6
end_game = False

print(logo)

# debug
# print(f"The word is {random_word}")

for _ in range(len(random_word)):
    display.append("_")

while not end_game:
    user_letter = input("Guess a letter: ")
    print(stages[chances])
    if user_letter in display:
        print(f"You've already guessed {user_letter}")

    if not user_letter in random_word:
        chances -= 1
        print(f"you gessed {user_letter}, that's not in the word. You lose a life.")
        print(stages[chances])
    else:
        for index, letter in enumerate(random_word):
            if user_letter == letter:
                display[index] = letter

    print("".join(display))

    if "_" not in display:
        end_game = True
        print("You Won!")
    elif chances == 0:
        end_game = True
        print("You Lost!")
