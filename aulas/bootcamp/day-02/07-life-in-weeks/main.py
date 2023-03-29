age = input("What's your current age? ")

years_rest = 90 - int(age)

days_rest = years_rest * 365
weeks_rest = years_rest * 52
months_rest = years_rest * 12


print(f"You have {days_rest} days, {weeks_rest} weeks, and {months_rest} months left.")
