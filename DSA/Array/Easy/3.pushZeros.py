# https://www.geeksforgeeks.org/move-zeroes-end-array/#

# def pushZerosToEnd(arr, arraySize):
#     count_zeros= 0
#     array_without_zeros = []

#     for element in arr:
#         if element == 0:
#             count_zeros+=1
#         else :
#             array_without_zeros.append(element)    

#     if count_zeros==0:
#         return print(arr)
#     else :
#         return(print(array_without_zeros+[0]*count_zeros))


# # Driver code
# arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
# n = len(arr)
# print("Array after pushing all zeros to end of array:")
# pushZerosToEnd(arr, n)

# ###### time and space complexity is O(n)

# def pushZerosToEnd(arr, n):
#     count_zeros = 0

#     for i in range(n):
#         if arr[i] != 0:
#             arr[count_zeros] = arr[i]
#             count_zeros += 1   # load all the non zero element in the arr[] and count_zeros has the array length without zeros 

#     for i in range(count_zeros, n):
#         arr[i] = 0



def pushZerosToEnd(arr, n):
    non_zero_counter = 0

    for i in range(n):
        if arr[i]!=0:
            arr[non_zero_counter] = arr[i]
            non_zero_counter+=1


    for i in range(non_zero_counter, n):
        arr[i]=0
        



# Driver code
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
n = len(arr)
print("Array after pushing all zeros to end of array:")
pushZerosToEnd(arr, n)
print(arr)
