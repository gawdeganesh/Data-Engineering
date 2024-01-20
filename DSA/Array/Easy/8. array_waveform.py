# https://www.geeksforgeeks.org/sort-array-wave-form-2/

# Follow the steps mentioned below to implement the idea:

# Traverse all even positioned elements of the input array, and do the following. 
# If the current element is smaller than the previous odd element, swap the previous and current. 
# If the current element is smaller than the next odd element, swap next and current.

def sortInWave(arr, n):

    for i in range (0,n-1,2):
        # If the current element is smaller than the previous odd element, swap the previous and current. 
        if (i>0 and arr[i]<arr[i-1]):
            arr[i],arr[i-1] = arr[i-1],arr[i]

        # If the current element is smaller than the next odd element, swap next and current.
        if (arr[i]<arr[i+1]):
            arr[i],arr[i+1] = arr[i+1],arr[i]

    return arr


# Driver program
arr = [10, 90, 49, 2, 1, 5, 23]
print(sortInWave(arr, len(arr)))



# another approch

# Sort the array.
# Traverse the array from index 0 to N-1, and increase the value of the index by 2.
# While traversing the array swap arr[i] with arr[i+1].
# Print the final array. 

def sortInWave(arr, n):
     
    #sort the array
    arr.sort()
    
    # Swap adjacent elements
    for i in range(0,n-1,2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
