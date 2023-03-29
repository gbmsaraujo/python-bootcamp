# Number Guessing Game Objectives:

# Include an ASCII art logo.
from art import logo
import random

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


def message_attempts(attempts):
    return f"You have {attempts} attempts remaining to guess the number"

def compare(guess, random_number, turns):

    if guess == random_number:
        print(f"You got it! The answer was {guess}")
    elif guess > random_number:
        print("Too high.\nGuess again.")
        print(message_attempts(turns))
    else:
        print("Too slow.\nGuess again.")
        print(message_attempts(turns))

def guess_game():

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    random_number = random.randint(1, 100)

    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    turns = 10 if level == 'easy' else 5

    guess = 0

    while guess != random_number:
        guess = int(input("Make a Guess: "))
        turns -= 1
        compare(guess=guess, random_number=random_number, turns=turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return

guess_game()

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
