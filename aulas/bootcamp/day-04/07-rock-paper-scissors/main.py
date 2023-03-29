import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

the_game = [rock, paper, scissors]

computer_choice = random.randint(0,2)

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if user_choice > 2 or user_choice<0:
    print("You type an invalid number, you lose!\n")
elif user_choice > computer_choice:
    if user_choice == 2 and computer_choice == 0:
        print(f"You choose:\n{the_game[user_choice]}\nComputer choice:\n{the_game[computer_choice]}\n You Lose!")
    else:
        print(f"You choose:\n{the_game[user_choice]}\nComputer choice:\n{the_game[computer_choice]}\n You Win!")
elif computer_choice>user_choice:
    if user_choice == 0 and computer_choice == 2:
      print(f"You choose:\n{the_game[user_choice]}\nComputer choice:\n{the_game[computer_choice]}\n You win!")
    else:
        print(f"You choose:\n{the_game[user_choice]}\nComputer choice:\n{the_game[computer_choice]}\n You Lose!")
else:
    print(f"You choose:\n{the_game[user_choice]}\nComputer choice:\n{the_game[computer_choice]}\n it was a draw :o")
