def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }

    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher.get(argument, "nothing")


teste = input("Teste: ")

# Driver program
if teste == "oi":
    argument = 0
    print(numbers_to_strings(argument))
