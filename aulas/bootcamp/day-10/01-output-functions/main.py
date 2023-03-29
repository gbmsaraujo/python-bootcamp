# Functions with output

# def first_upper_letter(word):
#     first_upper_name = ""
#     for index, letter in enumerate(word):
#         if index == 0:
#             first_upper_name += letter.upper()
#         else:
#             first_upper_name += letter
#     return first_upper_name


def format_name(first_name, last_name):
    """ Take a first and last name and format it to return the title case version of the name. """
    f_name = first_name.title()
    l_name = last_name.title()

    return f"{f_name} {l_name}"


full_name = format_name("gaBrIEl", "ARAUJO")

print(full_name)
