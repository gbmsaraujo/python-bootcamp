programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that u can easily call many times",
    "Loop": "The action of doing something over and over again",
}

print(programming_dictionary["Bug"])

# Add new Items:

programming_dictionary["If"] = "Conditional used to solve problem"

print(programming_dictionary)

# Create an empty dictionary:

empty_dictionary = {}

# Wipe an existing dictionary:

# programming_dictionary = {}

# Edit an item in a dictionary

programming_dictionary["Bug"] = "A moth in your computer"

print(programming_dictionary)


# Loop through a dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

