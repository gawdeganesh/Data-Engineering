#https://www.geeksforgeeks.org/find-element-appears-array-every-element-appears-twice/

def findSingle(arr, n):

    dict ={key: arr.count(key) for key in arr}
    arr =[key for key,value in dict.items() if value == 1]
    return print(arr)


# Driver program to test above function
arr = [6, 10, 5, 4, 9, 120, 4, 6, 10]
n = len(arr)
findSingle(arr, n)