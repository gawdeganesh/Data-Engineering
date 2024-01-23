def sum_of_elements(arr: list) -> int:
    if not arr:
        return 0

    sum = 0
    for ele in arr:
        sum = sum + ele
    return sum


print(sum_of_elements([1, 2, 34, 5, 6, -9, 88888]))
print(sum_of_elements([]))
print(sum_of_elements([-1, -2, -34, -5, -6, -9, -88888]))
