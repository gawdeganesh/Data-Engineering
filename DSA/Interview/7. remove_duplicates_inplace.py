def remove_duplicates_sorted_array(arr: list) -> list:
    """
    This function takes a sorted array and removes the duplicates in place.
    It returns the length of the array with unique elements.
    """

    arr.sort()

    if not arr:
        return "array is empty"

    # Initialize the index of the next non-duplicate element
    write_index = 1

    # Go through the array starting from the second element

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[write_index] = arr[i]
            write_index += 1
    return (
        write_index,
        arr[:write_index],
    )  # Return the new length and the array without duplicates space : O(1) and  time : O(N)


print(
    remove_duplicates_sorted_array(
        [1, 2, 34, 5, 6, -9, 88888, 2, 4, 34, 88888, 1, 1, 1, 1, 5, 6, 6]
    )
)
print(remove_duplicates_sorted_array([]))
