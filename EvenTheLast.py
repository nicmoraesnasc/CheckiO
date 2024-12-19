def checkio(array: list[int]) -> int:
    if array != []:
        even = []
        for i in range(len(array)):
            if i % 2 == 0:
                even.append(array[i])
        return sum(even) * array[-1]
    else:
        return 0

print("Example:")
print(checkio([0, 1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30
assert checkio([6]) == 36
assert checkio([]) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
