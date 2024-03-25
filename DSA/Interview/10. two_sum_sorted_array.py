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


def twoSum(nums, target):
    n = len(nums)

    """ brute force complexity = o(n^2) 

        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+ nums[j] == target:
                    return [i,j]
    """
    hashmap = {}

    for i in range(n):
        hashmap[nums[i]] = i

    for i in range(n):
        complement = target - nums[i]

        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]

    # Approach 3: One-pass Hash Table

    """
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i
    """


# Example usage:
# Assuming the array is sorted and may contain multiple pairs adding up to the target.
example_array = [1, 2, 4, 5, 5, -1, 7]
target_sum = 10
# print(two_sum_sorted_array(example_array, target_sum))
print(twoSum(example_array, target_sum))
