# Sort the given list so that its elements should be grouped and those groups end up in the decreasing frequency order

from collections.abc import Iterable

def frequency_sort(items: list[str | int]) -> Iterable[str | int]:

    frequency_list = []

    items.sort()

    for i in items:
        most_frequent = max(set(items), key=items.count)
        
        if i == most_frequent:
            frequency_list.append(i)
            items.pop(most_frequent)
    print(frequency_list)

    return items

print("Example:")
print(list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])))

# These "asserts" are used for self-checking
assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 2, 2, 2, 6, 6]
assert list(frequency_sort(["bob", "bob", "carl", "alex", "bob"])) == [
    "bob",
    "bob",
    "bob",
    "carl",
    "alex",
]
assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
assert list(frequency_sort([])) == []
assert list(frequency_sort([1])) == [1]

print("The mission is done! Click 'Check Solution' to earn rewards!")