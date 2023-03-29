MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "ingredients":
    {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    },
    "money": 0
}

# TODO: 1. Print report of all coffee machine resources
# TODO: 2. Print Report
# TODO: 3. Check resources sufficient?
# TODO: 4. Process coins
# TODO: 5. Check transaction successful?
# TODO: 6. Make Coffee


def report_resources(resources_info):
    """Print the report info related of item quantity in the machine"""
    ingredients = resources_info["ingredients"]
    money = resources_info["money"]

    for ingredient in ingredients:
        print(f"{ingredient}: {ingredients[ingredient]}{'ml' if  ingredient != 'coffee' else 'g'}")
    print(f"money: ${money}")


def get_sufficient_resources(order, resources_info):
    """Create an object that contain the ingredient and
    if it has any quantity in the client order"""
    choice_ingredients = MENU[order]["ingredients"]
    has_ingredient = True
    resources_array = []

    for ingredient in resources_info:
        if ingredient in choice_ingredients:
            if choice_ingredients[ingredient] > resources_info[ingredient]:
                has_ingredient = False
                resources_array.append({"ingredient": ingredient, "has_ingredient": has_ingredient})
            else:
                resources_array.append({"ingredient": ingredient, "has_ingredient": has_ingredient})
    return resources_array


def calculate_coins(order):
    """
    Catch the coins values inserted by user and calculate the monetary value
    and the difference to the change.
    """

    product_price = MENU[order]["cost"]
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    monetary_value = round(0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies, 2)

    if monetary_value >= product_price:
        difference = monetary_value - product_price

        return round(difference,2)
    else:
        return 0


def resources_subtraction(menu_data, total_resources, sufficient_ingredient):

    """Update the resources values, where:
    menu_data: object Menu,
    total_resources: object resource
    and sufficient_ingredient are ingredients in the order client
    """

    ingredient = sufficient_ingredient["ingredient"]
    total_resources["ingredients"][ingredient] -= menu_data[user_order]["ingredients"][ingredient]


finish_order = False
coin_result = 0
coins_step = True
user_order = ""

while not finish_order:
    user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_order == 'report':
        report_resources(resources)
    elif user_order == 'off':
        print("Have a good day! :)")
        finish_order = True
    else:
        sufficient_resources = get_sufficient_resources(user_order, resources["ingredients"])

        for user_ingredient in sufficient_resources:
            if not user_ingredient["has_ingredient"]:
                print(f"Sorry there is not enough {user_ingredient['ingredient']}.")
                coins_step = False
                break
            else:
                resources_subtraction(MENU, resources, user_ingredient)
                coins_step = True

        if coins_step:
            coin_result = calculate_coins(user_order)
            if coin_result:
                print(f"Here is ${coin_result} in change.\nHere is your {user_order} ☕️. Enjoy!")
                coin_result = 0
                resources["money"] += MENU[user_order]["cost"]
            else:
                print("Sorry that's not enough money. Money refunded.")











