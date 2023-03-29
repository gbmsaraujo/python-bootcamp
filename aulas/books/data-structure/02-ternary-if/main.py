# count = 0
# btn = "y"
# while btn != "n":
#     btn = input("press button? 'y' or 'n': ")
#     count += 1 if btn == "y" else -1
#     print(f"value: {count}")

# print(f"final value: {count}")


# Traditional Sintax

def tabuada_tradicional(number):
    tab_arr = []
    for i in range(1,11):
        tab_arr.append(2*i)
    print(tab_arr)

tabuada_tradicional(2)

# Comprehension Sintax



def tab_comprehension_sintax(num):
    return [num*i for i in range(1,11)]

print(tab_comprehension_sintax(3))
