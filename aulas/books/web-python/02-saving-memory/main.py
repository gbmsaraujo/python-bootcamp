from functools import reduce

# Map

precos = [1000, 1500, 1250, 2500]


def dobrar_array(num):
    return num * 2


precos_dobrados = list(map(dobrar_array, precos))

print(precos_dobrados)


# Zip

x = [1, 2, 3]
y = [3, 4, 5]

z = list(zip(x, y))

print(z)

# Zip Com Map

a = [5, 9, 2, 4, 7]
b = [3, 7, 1, 9, 2]
c = [6, 8, 0, 5, 3]


def the_max(iterable_list):
    return max(iterable_list)


# quero calcular um array com o máximo entre os tres itens das listas

max_array = list(map(the_max, zip(a, b, c)))

print(max_array)

# Filter

numbers = [-2, -1, 0, 1, 2]

positive_numbers = list(filter(lambda number: number > 0, numbers))


# Reduce

numbers = [1, 2, 3]

def my_sum(num1, num2):
    return num1 + num2

sum_numbers = reduce(my_sum, numbers)

print(sum_numbers)
