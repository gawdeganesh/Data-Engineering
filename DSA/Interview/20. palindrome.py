def palindrome(arr: list[int]) -> bool:
    if not arr:
        return -1

    left, right = 0, len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1

    return True


print(palindrome([]))
print(palindrome([1, 2, 2, 1]))
print(palindrome([1, 2, 3, 2, 1]))
print(palindrome([1, 2, 3, 4, 56, 7, 2, 1]))
