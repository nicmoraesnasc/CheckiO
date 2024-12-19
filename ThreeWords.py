def checkio(words: str) -> bool:
    counter = 0
    word = words.split()

    for i in word:
        if i.isalpha():
            counter += 1
            if counter >= 3:
                return True
            print(counter)
        elif i.isdecimal():
            (print(counter))
            counter = 0
    if counter >= 3:
        return True
    else:
        return False

print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))

# print("Example:")
# print(checkio("Hello World hello"))

# # These "asserts" are used for self-checking
# assert checkio("Hello World hello") == True
# assert checkio("He is 123 man") == False
# assert checkio("1 2 3 4") == False
# assert checkio("bla bla bla bla") == True
# assert checkio("Hi") == False

# print("The mission is done! Click 'Check Solution' to earn rewards!")