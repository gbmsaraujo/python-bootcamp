def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")

def newGreeting(name):
    print(f"Hello, {name}")
    print(f"How do you do? {name}")
    print(f"Isn't the weather nice today, {name}?")

# newGreeting('Gabriel')


#  Functions with more than 1 input

def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")


greet_with(location="Nowhere", name="Gabs araujo")


