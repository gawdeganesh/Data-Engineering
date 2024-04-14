# https://www.geeksforgeeks.org/leaders-in-an-array/
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/submissions/1224333268/


def superiorElements(arr: list[int]) -> list[int]:
    result = [0]* len(arr)
    maxi = -1
    n = len(arr)
    for i in range(n - 1, -1, -1):
        result[i] = maxi
        maxi = max(maxi, arr[i])     
        
    return result


# Driver function
arr = [16, 17, 4, 3, 5, 2]
print(superiorElements(arr))

