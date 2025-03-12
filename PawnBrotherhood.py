# You are given a set of square coordinates where we have placed white pawns
# You should count how many pawns are safe

def safe_pawns(pawns: set) -> int:
    listc = ["a", "b", "c", "d", "e", "f", "g", "h"]
    
    safe_list = []

    for pawn in pawns:
        character = pawn[0]
        number = int(pawn[1])
        shield_pawns = set()

        if number > 1:
            index = listc.index(character)
            previous_num = number-1

            if character != "a":
                previous_char = listc[index-1]
                shield_pawns.add(previous_char + str(previous_num))

            if character != "h":
                next_char = listc[index+1]
                shield_pawns.add(next_char + str(previous_num))

            intersection = pawns.intersection(shield_pawns)
            
            if intersection != set():
                safe_list.append(pawn)

        else:
            continue

    return len(safe_list)


print("Example:")
print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))


# These "asserts" are used for self-checking
assert safe_pawns({"f4", "g5", "c3", "d2", "b4", "e3", "d4"}) == 6
assert safe_pawns({"f4", "e5", "g4", "e4", "b4", "d4", "c4"}) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")
