def missing_number(arr: list[int], start: int, end: int) -> int:

    if not arr or (start == 0 and end == 0):
        return -1

    if len(arr) != (end - start):
        return "more than one numbers are missing"

    total_number = len(arr) + 1

    sum_of_n_numbers = ((start + end) * total_number) // 2
    missing_number = sum_of_n_numbers - sum(arr)

    return missing_number


print(missing_number([0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11], 0, 11))
print(missing_number([], 0, 11))
print(missing_number([3, 4, 5, 6, 8, 9, 10, 11, 12, 13], 3, 13))
print(missing_number([4, 5, 6, 8, 9, 10, 12], 4, 12))
