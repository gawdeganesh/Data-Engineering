# https://leetcode.com/problems/product-of-array-except-self/description/


def productExceptSelf(nums: list[int]) -> list[int]:
    cur_ele = 1
    l_prod = 1
    left_prod = []
    for i in range(len(nums)):
        l_prod = l_prod * cur_ele
        left_prod.append(l_prod)
        cur_ele = nums[i]

    last_ele = 1
    right_prod = [0] * len(nums)
    r_prod = 1
    for i in range(len(nums) - 1, -1, -1):
        r_prod = r_prod * last_ele
        right_prod[i] = r_prod
        last_ele = nums[i]

    answer = [0] * len(nums)
    for i in range(len(nums)):
        answer[i] = left_prod[i] * right_prod[i]
    return answer


# Driver code
arr = [2, 1, 9, 8]
n = len(arr)
print("Original Array:", arr)
prod = productExceptSelf(arr)
print("Final Array:", prod)
