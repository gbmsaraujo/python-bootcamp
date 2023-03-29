def sqrt(number):
    if not isinstance(number, (int, float)):
        raise TypeError("Number must be numeric")
    elif number < 0:
        raise ValueError("Number can't be negative")
    else:
        return (number) ** (1 / 2)


# print(sqrt("4"))


# Catching Exception


# def testCatch(num1, num2):
#     try:
#         divide = num1 / num2
#         print(divide)
#     except ZeroDivisionError:
#         raise ValueError("Impossible Calculate")


# testCatch(2, 0)


# Example 2:

age=-1

while age <= 0:
    try:
        age = int(input("Enter with your age: "))
        if age <= 0:
            print("Your age must be positive!")
    except ValueError:
        print("Invalid response")
    except EOFError:
        raise

