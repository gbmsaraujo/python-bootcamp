from art import logo
import os


def add_secret_auction_list(name_value, bid_value):
    secret_auction = {}
    secret_auction["name"] = name_value
    secret_auction["bid"] = bid_value

    auction_list.append(secret_auction)


clear = lambda: os.system("clear")
auction_list = []
other_bidders = "yes"
winner = {"max_bid": 0}

print(f"{logo}\nWelcome to the secret auction program")

while other_bidders == "yes":
    user_name = input("What's your name?: ")
    user_bid = int(input("What's your bid?: $"))

    add_secret_auction_list(name_value=user_name, bid_value=user_bid)

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    clear()

for secret in auction_list:
    if secret["bid"] > winner["max_bid"]:
        winner["name"] = secret["name"]
        winner["max_bid"] = secret["bid"]

print(f"The winner is {winner['name']}with a bid of ${winner['max_bid']}.")
