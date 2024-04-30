"""
If we take a closer look at examples, we can notice that the number of rotations is equal to the index of the minimum element. A simple linear solution is to find the minimum element and returns its index. 

"""


def countRotations(arr, n):

    # We basically find index
    # of minimum element
    min = arr[0]
    min_index = 0
    for i in range(0, n):

        if min > arr[i]:

            min = arr[i]
            min_index = i

    return min_index


# Driver code
arr = [15, 18, 2, 3, 6, 12]
n = len(arr)
print(countRotations(arr, n))

