def remove_duplicates_sorted_array(arr: list) -> list:
    """
    This function takes a sorted array and removes the duplicates in place.
    It returns the length of the array with unique elements.
    """

    arr.sort()

    if not arr:
        return "array is empty"

    # Initialize the index of the next non-duplicate element
    write_index = 0

    # Go through the array starting from the second element

    for i in range(0, len(arr) - 1):
        if arr[i] != arr[i + 1]:
            arr[write_index] = arr[i]
            write_index += 1

    # Handle the last element: always add it as it is not checked in the loop
    arr[write_index] = arr[-1]
    write_index += 1

    return write_index, arr[:write_index]
    # Return the new length and the array without duplicates space : O(1) and  time : O(N)


print(
    remove_duplicates_sorted_array(
        [1, 2, 34, 5, 6, -9, 88888, 2, 4, 34, 1, 1, 1, 1, 5, 6, 6]
    )
)
print(remove_duplicates_sorted_array([]))


class Solution:
    def removeDuplicates(nums: list[int]) -> int:
        if len(nums) == 1:
            return 1
        i = 0
        j = i + 1
        while j < len(nums):
            if nums[j] != nums[i]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
            j += 1
        return i + 1


def remove_duplicates_sorted_array(arr: list) -> tuple:
    """
    This function takes a sorted array and removes the duplicates in place.
    It returns the length of the unique array and the array itself up to the unique elements.
    """

    if not arr:
        return 0, "array is empty"

    # Initialize the index for writing unique elements
    write_index = (
        1  # Start from 1 because the first element is always unique in its position
    )

    # Start from the second element and compare with the previous
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[write_index] = arr[i]
            write_index += 1

    return write_index, arr[:write_index]
