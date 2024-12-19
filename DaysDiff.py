from datetime import datetime

def days_diff(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:

    date_a = datetime(a[0], a[1], a[2]).date()
    date_b = datetime(b[0], b[1], b[2]).date()
    if date_a > date_b:
        diff_days = date_a - date_b
    else:
        diff_days = date_b - date_a
    return diff_days.days



print("Example:")
print(days_diff((1982, 4, 19), (1982, 4, 22)))

assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238

print("The mission is done! Click 'Check Solution' to earn rewards!")