def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


# Permite que seu módulo também seja executado como script
# facilitando testes unitários no teu módulo

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

