print("Welcome to the Love Calculator!")
your_name = input("What's your name? ").lower()
their_name = input("What's their name? ").lower()
combined_names = your_name + their_name
score = 0

true_score = (
    combined_names.count("t")
    + combined_names.count("r")
    + combined_names.count("u")
    + combined_names.count("e")
)

love_score = (
    combined_names.count("l")
    + combined_names.count("o")
    + combined_names.count("v")
    + combined_names.count("e")
)

score = str(true_score) + str(love_score)

if int(score) < 10 or int(score) > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score) > 40 and int(score) < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")
