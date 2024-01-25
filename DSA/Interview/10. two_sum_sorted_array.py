def two_sum_sorted_array(arr: list, target: int) -> list:
    # if array is not sorted
    arr.sort()

    left, right = 0, len(arr) - 1
    results = []
    results_data = []

    while left < right:
        current_sum = arr[left] + arr[right]

        if target == current_sum:
            results.append((left, right))
            results_data.append((arr[left], arr[right]))
            left += 1
            right -= 1
            # return left, right  if there is only single pair expected

        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return results


# Example usage:
# Assuming the array is sorted and may contain multiple pairs adding up to the target.
example_array = [1, 2, 3, 4, 5, 5, 6, 7]
target_sum = 10
print(two_sum_sorted_array(example_array, target_sum))
