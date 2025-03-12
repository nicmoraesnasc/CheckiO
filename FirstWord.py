# Find the first word in a string

def first_word(text: str) -> str:
    just_words = "".join(i if i.isalpha() or i == "'" else " " for i in text)
    print(just_words)
    first_word = just_words.split()
    return first_word[0]


print(first_word("don't touch"))

print("Example:")
print(first_word("Hello world"))

# These "asserts" are used for self-checking
assert first_word("Hello world") == "Hello"
assert first_word(" a word ") == "a"
assert first_word("don't touch it") == "don't"
assert first_word("greetings, friends") == "greetings"
assert first_word("... and so on ...") == "and"
assert first_word("hi") == "hi"

print("The mission is done! Click 'Check Solution' to earn rewards!")
