
def insertElement(arr, n, x, pos):

    if n >= len(arr):
        print("Array is already full. Cannot insert more elements.")
        return

    for i in range(n-1, pos-1, -1):
        arr[i+1]= arr[i]

    arr[pos] = x    

def deleteElement(arr,n,value):
    valueFound = False
    index=0
    # search the index of the value
    for i in range(n):
        if value == arr[i]:
            index = i
            valueFound= True
            break

    if index==n and valueFound:
        return arr.pop()
    elif valueFound and index<n:
        for i in range(index,n-1):
            arr[i]=arr[i+1]

        arr[:]= arr[:n-1] 
        return arr
    else:
        return 'value not found'   
        


# # Driver's code
# if __name__ == '__main__':
#     # Declaring array and key to delete
#     # here -1 is for empty space
#     arr = [2, 4, 1, 8, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
#     n = 5
     
#     print("Before insertion : ")
#     for i in range(0,n) :
#         print(arr[i],end=' ')
 
#     print("\n")
 
#     x = 10;
#     pos = 2;
   
#     # Function call
#     insertElement(arr, n, x, pos)
#     n+=1
 
#     print("After insertion : ")
#     for i in range(0,n) :
#         print(arr[i],end=' ')


# Driver's code
if __name__ == '__main__':
    # Declaring array and key to delete
    arr = [10, 50, 30, 40, 20]
    key = 100
  
    print("Array before deletion:")
    print (arr)
  
    # deletes key if found in the array 
    # otherwise shows error not in list
   
    print("Array after deletion", deleteElement(arr,len(arr),key))