valores = [1, 2, 3, 4]

def func(*args):
    print(args)

func(*valores)

def func_2(**kwargs):
    print(kwargs)

func_2(a=1, b=2)
