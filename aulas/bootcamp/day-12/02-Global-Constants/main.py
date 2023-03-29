PI = 3.14159
URL = "https://www.google.com"


def modify_var():
    global PI
    PI += 2
    print(PI)

modify_var()
