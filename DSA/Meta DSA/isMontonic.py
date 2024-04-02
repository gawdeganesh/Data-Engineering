# https://leetcode.com/problems/monotonic-array/description/


def is_monotonic(array):
    # Check for the trivial cases where the array length is less than 2
    if len(array) < 2:
        return True

    # Flags to keep track of the array's monotonicity
    non_decreasing = True
    non_increasing = True

    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            non_increasing = False
        elif array[i] < array[i - 1]:
            non_decreasing = False

    # The array is monotonic if it is either non-decreasing or non-increasing
    return non_decreasing or non_increasing


# Example usage
print(is_monotonic([1, 2, 5, 5, 8]))  # True
print(is_monotonic([9, 4, 4, 2, 2]))  # True
print(is_monotonic([1, 4, 6, 3]))  # False
print(is_monotonic([1, 1, 1, 1, 1, 1]))  # True
