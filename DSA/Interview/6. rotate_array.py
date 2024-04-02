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


def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    def reverse(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    n = len(nums)
    k %= n  # Handle cases where k > n

    # To rotate left by k, rotate right by n - k
    k = n - k

    reverse(0, n - 1)  # Reverse the entire array
    reverse(0, k - 1)  # Reverse the first k elements
    reverse(k, n - 1)  # Reverse the remaining elements

    return nums  # time complexity : O[n] and space complexity : O[1] because of in-place update


from typing import List

"""
Time complexity = O(r*n), where r is number of rotations
and n is number of elements in the array

Space complexity = O(1)
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Becuase if k = 8 and length = 7, means
        # we should only rotate 1 time instead of 8 times
        rotations = k % len(nums)

        for _ in range(rotations):
            last = nums.pop()
            nums.insert(0, last)


print(rotate([1, 2, 34, 5, 6, -9, 88888], 3))  # [5, 6, -9, 88888, 1, 2, 34]
# print(rotate_array_left([], 1))
print(rotate([-1, -2, -34, -5, -6, -9, -88888], 10))
