def move_negatives(arr: list[int]) -> list:
    if not arr:
        return -1

    index = 0

    for i in range(len(arr)):
        if arr[i] < 0:
            arr[index] = arr[i]
            index += 1

    for i in range(index, len(arr)):
        if arr[i] >= 0:
            arr[index] = arr[i]
            index += 1

    return arr


print(move_negatives([]))
print(move_negatives([1, 2, 34, 5, 6, 2, 4, 34, 1, 1, 1, 1, 5, 6, 6]))
print(move_negatives([1, 2, -40, 5, -6, 2, 4, 34, 1, 1, 1, 1, 5, 6, 6]))
