from util_alphabetic import alphabet

alphabet_len = len(alphabet) - 1


def ceasar(direction, text, shift):
    ceasar_word = ""
    for char in text.lower():
        if char in alphabet:
            char_index = alphabet.index(char)
            if direction == "encode":
                new_position = char_index + shift
                ceasar_word += alphabet[new_position]
            else:
                ceasar_word += alphabet[char_index - shift]
        else:
            ceasar_word += char
    print(f"The {direction}d text is: {ceasar_word}")
