def array_reversal(arr: list) -> list:

    if not arr:
        return "array is empty"

    first, last = 0, len(arr) - 1

    # for _ in range(0, len(arr) // 2):
    #     arr[first], arr[last] = arr[last], arr[first]
    #     first = first + 1
    #     last = last - 1

    while first < last:
        arr[first], arr[last] = arr[last], arr[first]
        first += 1
        last -= 1

    return arr


# use while because you are not using i in the loop

print(array_reversal([1, 2, 34, 5, 6, -9, 88888, 1]))
print(array_reversal([]))
print(array_reversal([-1, -2, -34, -5, -6, -9, -88888]))
