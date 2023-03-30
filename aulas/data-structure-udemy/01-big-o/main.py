"""
- Code 1 and Code 2: Cronômetro em que code 1 roda em 15s
e code 2 em 60s: Time Complexity, pelo tempo, Code 1 melhor que 2

- Porém, medimos tb space complexity, ou seja, por mais que code 1 rode
mais rápido, porém ele pode ocupar mais slots de memória q o code 2 que roda em mais tempo!

- Omega, Theta e Omicron(conhecido como O);
- Big O - Omicron;


Imagina percorrer uma lista = [1, 2, 3, 4, 5, 6, 7]

- Se quero achar o 1, melhor cenário, chamamos de Omega;
- Se queremos o 4, cenário mediano, chamamos de theta;
- Se queremos o 7, pior cenário, chamamos de omicron ou Big O

"""

"""
* 1o Caso : O(n)

- Caso mais simples:
Passamos um numero n como parâmetros e rodamos n vezes, por isso O(n), n opera n vezes
"""


def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)


"""
* 2o Caso : O(n²)

"""


def print_items_2(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

print_items_2(10)



"""
* Drop Non-Dominants:

Se tenho:

def print_items_2(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

    for k in range(n):
        print(k)


Vou n² + n = 100 + 10

se aumento meu numero, meu n se torna desprezível, podendo ser descartado
e considerando apenas como n²

print_items_2(10)


"""

"""
3o Caso: O(1)

Imagine a seguinte função:
"""

def add_items(n):
    return n + n

"""
Temos apenas uma operação mesmo tendo n + n + n + n, temos uma operação, considerado constante;
"""



"""
4o Caso: O(log n):

Vamos supor que eu tenho uma lista

[1, 2, 3, 4, 5, 6, 7, 8]

precisamos achar um número, vamos supor 1

1o: Dividimos na metade, e vemos q ele está presente na primeira metade;
[1, 2 ,3, 4]

2o Dividimos na segunda metade, vimos q ele esta presente na 1a dessa segunda divisão

[1, 2], descartamos [3,4]

3o Investigamos no array q sobrou

[1,3]

em 3 etapas conseguimos achar um numero:

2³ = 8

que é a mesma coisa que

    8
Log  =3
    2


agora imagina uma lista de 1 bi de items em que precisamos iterar sobre, iteraríamos 1 bi de vezes, porém O(log n) precisaríamos operar cerca de 31 passos

Um dos mais eficientes modos!
"""


# Big O em listas

"""
Se temos uma lista = [0, 3, 23, 7]


se adiciono ou removo um item na lista, nada muda, teríamos O(1)

porem se eu tiro o primeiro, no caso, 0, preciso rearranjar os index, que vira um O(n)
"""


# O² = Loop dentro de um loop
# O(n) = Proporcional
#  O(log n) = Divide and Conquer
#  O(1) = Constante
