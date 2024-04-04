# https://www.geeksforgeeks.org/rearrange-array-such-that-even-positioned-are-greater-than-odd/
# https://leetcode.com/problems/sort-array-by-parity/description/


def assign(A, size):
    i, j = 0, len(A) - 1
    while i < j:
        if A[i] % 2 > A[j] % 2:
            A[i], A[j] = A[j], A[i]
        if A[i] % 2 == 0:
            i += 1
        if A[j] % 2 == 1:
            j -= 1
    return A


# Driver Code
arr = [1, 3, 2, 2, 5]
n = len(arr)
assign(arr, n)
for i in range(n):
    print(arr[i], end=" ")
print()
