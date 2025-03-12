# Find missing element in unsorted list of arithmetic progression

def missing_number(items: list[int]) -> int:
    list_diff = []
    most_occurring_diff = 0
    most_occurring_count = 0
    missing_value = 0


    items.sort()

    for i in range(len(items)):
        if i > 0:
            diff = items[i] - items[i-1] 
            list_diff.append(diff)
        
    if len(list_diff) > 2:
        for i in list_diff:
            count = list_diff.count(i)
            if count > most_occurring_count:
                most_occurring_diff = i
                most_occurring_count = count
    else:
        most_occurring_diff = min(list_diff)

    for i in items[::-1]:
        expected_value = i + most_occurring_diff
        if expected_value not in items:
            missing_value = expected_value

    return missing_value


print("Example:")
print(missing_number([2, 6, 8]))

# These "asserts" are used for self-checking
assert missing_number([1, 4, 2, 5]) == 3
assert missing_number([2, 6, 8]) == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")