# https://www.geeksforgeeks.org/leaders-in-an-array/

def printLeaders(arr, n):

    for i in range(1,n):
        if (arr[i]>arr[i-1] or i==(n-1)):
            print(arr[i], end=' ')   
        else:
            continue    

# Driver function
arr=[16, 17, 4, 3, 5, 2]
printLeaders(arr, len(arr))