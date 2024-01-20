
def rearrange(arr, n):
    arr.sort()
    modified_array=[0]*(n)  #empty array will throw an error because you cannot assign value size error

    if (n==0):
        return print("Array is empty")
    elif (n==1):
        return print(arr)
    else :
        for i in range(0,n//2): # in range we need int value, so no floating always use //
            modified_array[2*i],modified_array[2*i+1]= arr[n-i-1],arr[i] # multiply by 2 for the next run

    if(n%2==0):
        return modified_array
    else:        
        modified_array[n - 1]= arr[(n//2)]   
        return modified_array



# Driver code
arr = [4, 2, 1, 7, 5,6]
n = len(arr)
print("Original Array")
print(arr)
print("Modified Array")
print(rearrange(arr, n))



# # Swap adjacent elements
#     for i in range(0,n-1,2):
#         arr[i], arr[i+1] = arr[i+1], arr[i]