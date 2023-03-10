print("Welcome to the tip calculator!")

total_bill = input("What was the total bill?\n$ ")
tip_bill = input("How much tip would you like to give? 10, 12, or 15?\n")
total_people = input("How many people to split the bill?\n")

total_with_tip = (1 + (float(tip_bill) / 100)) * float(total_bill)
each_person_value = total_with_tip / int(total_people)

print(f"Each person should pay: ${round(each_person_value, 2)}")
