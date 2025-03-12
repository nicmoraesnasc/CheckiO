# Determine the words' popularity

def popular_words(text: str, words: list) -> dict:
    dictionary = {}
    list_counter = []
    text_words = text.split()
    for index in range(len(text_words)):
        text_words[index] = text_words[index].lower()
    for word in words:
        counter = text_words.count(word)
        list_counter.append(counter)
    for index in range(len(words)):
        dictionary[words[index]] = list_counter[index]
    return dictionary
    
print("Example:")
print(
    popular_words(
        """
When I was One
I had just begun
When I was Two
I was nearly new
""",
        ["i", "was", "three", "near"],
    )
)

# These "asserts" are used for self-checking
assert popular_words(
    "\nWhen I was One\nI had just begun\nWhen I was Two\nI was nearly new\n",
    ["i", "was", "three", "near"],
) == {"i": 4, "was": 3, "three": 0, "near": 0}

print("The mission is done! Click 'Check Solution' to earn rewards!")