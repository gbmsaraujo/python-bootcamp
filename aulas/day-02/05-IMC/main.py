height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

imc = int(weight) / (float(height) ** 2)

imc_as_int = int(imc)
print(imc_as_int)
