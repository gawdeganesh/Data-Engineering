def binary_search(arr:list, target:int)->int:
    if not arr:
        return 'array is empty'

    arr[:] = sorted(arr) # binary search needs a sorted array

    #define the range 
    left, right = 0, len(arr)-1

    while left<=right:
        mid = (left+right)//2
        mid_value = arr[mid]

        if mid_value== target:
            return mid         # target found
        elif mid_value<target:
            left = mid + 1       # discard left
        else:
            right = mid - 1      # discard right

    return None
    

print(binary_search([1, 2, 34, 5, 6, -9, 88888], -9))
print(binary_search([1, 2, 34, 5, 6, -9, 88888], 234))
print(binary_search([], -9))