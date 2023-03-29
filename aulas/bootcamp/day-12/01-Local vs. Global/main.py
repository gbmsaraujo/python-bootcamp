enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")


# Modify global scope

def increase_enemies():
    global enemies
    enemies += 1

# increase_enemies()
print(f"enemies outside function: {enemies}")

"""Porém, n é tão trivial alterar variáveis globais, para resolver esse problema: """


def new_increase_enemies():
    return enemies + 2

enemies = new_increase_enemies()

print(f"new enemies outside function: {enemies}")
