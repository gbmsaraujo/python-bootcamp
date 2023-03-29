from collections import namedtuple

ex_tuples = (10, 20, 30)
dez, vinte, trinta = ex_tuples

print(dez)
# print(vinte)
# print(trinta)


print(ex_tuples[-2])


# accessing tuple elements using slicing
my_tuple = ("p", "r", "o", "g", "r", "a", "m", "i", "z")


Estados = namedtuple("Estados", ["nome", "sigla"])

estado_1 = Estados("Rio De Janeiro", "RJ")


print(estado_1)
print(estado_1.nome)

x = "global"


def f():
    x = "enclosing"

    def g():
        x = "local"
        print(x)

    g()


f()
