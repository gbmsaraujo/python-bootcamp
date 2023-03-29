print("Leap Year")

year = float(input("Which year do you want to check? "))

if not year%4 == 0:
    print("Not leap Year")
elif not year%100 == 0:
    print("Leap year")
elif year%400 == 0:
    print("Leap year")
else:
    print("Not Leap year")
