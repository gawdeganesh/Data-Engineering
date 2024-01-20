def list_reverse(arr,size):
 
    #if only one element present, then return the array
    if(size==1):
        return arr
     
    #if only two elements present, then swap both the numbers.
    elif(size==2):
        arr[0],arr[1],=arr[1],arr[0]
        return arr
     
    #if more than two elements presents, then swap first and last numbers.
    else:
        for i in range(size//2):
            arr[i],arr[size-i-1]=arr[size-i-1],arr[i]
        return arr
    
#    left = 0
#     right = len(arr)-1
#     while (left < right):
#         # Swap
#         temp = arr[left]
#         arr[left] = arr[right]
#         arr[right] = temp
#         left += 1
#         right -= 1   


# # Reversing a list using slicing technique
# def Reverse(lst):
#     new_lst = lst[::-1]
#     return new_lst
 
arr=[1,2,3,4,5]
size=5
print('Original list: ',arr)
print("Reversed list: ",list_reverse(arr,size))