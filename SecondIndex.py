# Find the second index in a string

def second_index(text: str, symbol: str) -> int | None:
    if symbol in text:
        counter = 0
        for i in range(len(text)):
            if text[i] == symbol:
                counter += 1
                if counter > 1:
                    return i
        return None
    else:
        return None
                    

print("Example:")
print(second_index("find the river", "e"))

# These "asserts" are used for self-checking
assert second_index("sims", "s") == 3
assert second_index("find the river", "e") == 12
assert second_index("hi", " ") == None
assert second_index("hi mayor", " ") == None
assert second_index("hi mr Mayor", " ") == 5

print("The mission is done! Click 'Check Solution' to earn rewards!")
