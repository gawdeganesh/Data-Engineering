def move_zeros_to_end(arr: list) -> list:
    new_counter = 0

    if not arr:
        return -1

    for ele in arr:
        if ele != 0:
            arr[new_counter] = ele
            new_counter += 1

    for i in range(new_counter, len(arr)):
        arr[i] = 0

    return arr


print(move_zeros_to_end([0, 0, 0, 1, 2, 34, 5, 0, 6, -9, 0, 0, 88888]))
print(move_zeros_to_end([1, 2, 34, 5, 6, -9, 88888]))  # no zeros
print(move_zeros_to_end([]))
