print("Welcome to Python Pizza Deliveries!")
bill = 0
pizza_size = input("What size pizza do you want? S, M or L? ")
add_pepperoni = input("Do you wanna add pepperoni? Y or N? ")
extra_cheese = input("Do you wanna add extra cheese? Y or N? ")

if pizza_size == "S":
    bill += 15
elif pizza_size == "M":
    bill += 20
else:
    bill += 25
if add_pepperoni == "Y":
    if pizza_size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")
