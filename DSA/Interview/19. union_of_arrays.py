def union_of_array(arr1: list, arr2: list) -> list:
    set1 = set(arr1)
    set2 = set(arr2)

    return list(set1.union(set2))  # time : O(N + M) space : O(N + M)


print(union_of_array([], []))
print(union_of_array([1, 2, 3, 4], []))
print(union_of_array([1, 2, 3, 4], [-1, 2, 4, 56, 67, 4]))


def union_of_array_brute_force(arr1: list, arr2: list) -> list:
    union_array = []

    for ele in arr1:
        if ele not in union_array:
            union_array.append(ele)

    for ele in arr2:
        if ele not in union_array:
            union_array.append(ele)

    return union_array  # time : O((N+M)^2) space : O(N + M)


print(union_of_array_brute_force([], []))
print(union_of_array_brute_force([1, 2, 3, 4], []))
print(union_of_array_brute_force([1, 2, 3, 4], [-1, 2, 4, 56, 67, 4]))

# two pointers method

"""
Sort both arrays if they are not sorted.
Initialize two pointers, one for each array.
Iterate through both arrays and compare the elements at the pointers.
Add the smaller element to the union array and move the corresponding pointer.
If both elements are the same, add any one of them to the union array and move both pointers.
Continue this process until you reach the end of one or both arrays.
Add any remaining elements from either array to the union array.

"""


def union_of_arrays(array1, array2):
    # Sort both arrays
    array1.sort()
    array2.sort()

    union_array = []
    i, j = 0, 0

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            union_array.append(array1[i])
            i += 1
        elif array1[i] > array2[j]:
            union_array.append(array2[j])
            j += 1
        else:
            union_array.append(array1[i])
            i += 1
            j += 1

    # Add any remaining elements
    while i < len(array1):
        union_array.append(array1[i])
        i += 1

    while j < len(array2):
        union_array.append(array2[j])
        j += 1

    return union_array  # time : O(NlogN + MlogM) space : O(N + M)


# Example usage
array1 = [1, 2, 3, 4]
array2 = [3, 4, 5, 6]
result = union_of_arrays(array1, array2)
print("Union of the two arrays:", result)
