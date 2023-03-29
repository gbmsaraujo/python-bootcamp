def prime_number_checker(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    if is_prime == True:
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")

user_number = int(input("type a number: "))

prime_number_checker(user_number)
