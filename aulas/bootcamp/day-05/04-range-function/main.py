total = 0
total_impar = 0

for number in range(1, 101):
    total += number

print(total)

# soma dos números impares
for number in range(1, 101, 2):
    total_impar += number

print(total_impar)
