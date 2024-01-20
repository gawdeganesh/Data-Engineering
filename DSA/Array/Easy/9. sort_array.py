#https://www.geeksforgeeks.org/sort-array-contain-1-n-values/

# bubble sort 

def sort(arr,n):

    if (n==1):
        return print(arr)
    else:
        for i in range (0,n-1):
            for j in range(0,n-i-1):
                if (arr[j]>arr[j+1]):
                    arr[j],arr[j+1] = arr[j+1],arr[j]
    return print(arr)

# Driver Code
arr = [3, 2, 5, 6, 1, 4]
n = len(arr)
 
# function call
sort(arr, n)