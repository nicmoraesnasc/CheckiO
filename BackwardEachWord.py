def backward_string_by_word(text: str) -> str:
    words = text.split(' ')
    lista = []
    if len(words) > 0:
        for i in words:
            word = i[::-1]
            lista.append(word)
        backwards_words = ' '.join(lista)
        return (backwards_words)
    else:
        return ''

print("Example:")
print(backward_string_by_word("hello   world"))

# These "asserts" are used for self-checking
assert backward_string_by_word("") == ""
assert backward_string_by_word("world") == "dlrow"
assert backward_string_by_word("hello world") == "olleh dlrow"
assert backward_string_by_word("hello   world") == "olleh   dlrow"
assert backward_string_by_word("welcome to a game") == "emoclew ot a emag"

print("The mission is done! Click 'Check Solution' to earn rewards!")