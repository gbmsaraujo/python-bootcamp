from game_data import data
from art import logo, vs
import random


def format_data(option):
    """Takes the options data and returns the printable format"""
    return f"{option['name']}, {option['description']}, from {option['country']}"


def  (guess, a_followers, b_followers):
    """Take the user guess and followers counts and returns if they got it right"""

    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def higher_lower():
    print(logo)

    option_b = random.choice(data)

    score = 0

    game_over = False

    while not game_over:

        option_a = option_b
        option_b = random.choice(data)

        if option_a == option_a:
            option_b = random.choice(data)

        print(f"Compare A: {format_data(option_a)}")

        print(vs)

        print(f"Against B: {format_data(option_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_follower_count = option_a["follower_count"]
        b_follower_count = option_b["follower_count"]

        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        print(logo)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
            game_over = False
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True


higher_lower()
