from art import logo


def realize_operation(num1, num2, operation):
    switcher = {"+": num1 + num2, "-": num2 - num2, "*": num1 * num2, "/": num1 / num2}

    return switcher.get(operation)


def calculator():
    print(logo)
    result = 0
    first_number = float(input("What's the first number? "))
    continue_calc = True
    try:
        while continue_calc == True:
            operation = input("+\n-\n*\n/\nPick an operation: ")

            next_number = float(input("What's the next number? "))

            result = realize_operation(first_number, next_number, operation)

            if result == None:
                print("Operação incorreta, tente novamente!")
                calculator()

            print(f"{first_number} {operation} {next_number} = {result}")

            yes_new_no = input(
                "Type 'y' to continue calculating, type 'new' to start a new calculation or 'e' to exit: "
            )

            if yes_new_no == "y":
                first_number = result
            elif yes_new_no == "new":
                calculator()
            else:
                break

    except ValueError:
        print("Valores digitados estão incorretos, tente novamente!")
        calculator()

calculator()
