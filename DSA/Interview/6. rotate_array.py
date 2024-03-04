def rotate_array_aux(arr: list, k: int) -> list:

    k %= len(arr)  # normalize k

    left_part = arr[-k:]  # [6, -9, 88888]
    right_part = arr[:-k]  # [1, 2, 34, 5]

    return left_part + right_part  # time complexity : O[n] and space complexity : O[n]


def rotate_array(arr: list, k: int) -> list:

    def reverse(start, end):

        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    n = len(arr)

    if k == 0 or n == 0 or k % n == 0:
        return -1  # no rotation required

    k = k % n  # normalize k

    reverse(0, n - 1)  # [88888, -9, 6, 5, 34, 2, 1]
    reverse(0, k - 1)  # [6, -9, 88888, 5, 34, 2, 1]
    reverse(k, n - 1)  # [6, -9, 88888, 1, 2, 34, 5]

    return arr  # time complexity : O[n] and space complexity : O[1] because of in-place update


# print(rotate_array([1, 2, 34, 5, 6, -9, 88888], 3))
# print(rotate_array([], 1))
# print(rotate_array([-1, -2, -34, -5, -6, -9, -88888], 10))


def rotate_array_left_aux(arr: list, k: int) -> list:

    k %= len(arr)  # normalize k

    right_part = arr[:k]  # [1, 2, 34]
    left_part = arr[k:]  # [5, 6, -9, 88888]

    return left_part + right_part


def rotate_array_left(arr: list, k: int) -> list:

    def reverse(start, end):

        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    n = len(arr)

    if k == 0 or n == 0 or k % n == 0:
        return -1  # no rotation required

    k = k % n  # normalize k

    reverse(0, n - 1)  # [88888, -9, 6, 5, 34, 2, 1]
    reverse(0, n - k - 1)  # [5, 6, -9 ,88888, 34, 2, 1]
    reverse(n - k, n - 1)  # [5, 6, -9, 88888, 1, 2, 34]

    return arr  # time complexity : O[n] and space complexity : O[1] because of in-place update


print(rotate_array_left([1, 2, 34, 5, 6, -9, 88888], 3))  # [5, 6, -9, 88888, 1, 2, 34]
# print(rotate_array_left([], 1))
print(rotate_array_left([-1, -2, -34, -5, -6, -9, -88888], 10))
