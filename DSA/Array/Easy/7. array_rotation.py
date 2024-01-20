# https://www.geeksforgeeks.org/array-rotation/

def rotate(arr, d, n):

    # if the value of k ever exceeds the length of the array
    rotate = d % n

    cnt_of_rotation = 1

    while (cnt_of_rotation <= rotate):
        last_element = arr[0]
        for i in range(0, n - 1):
            arr[i] = arr[i + 1]
        arr[n - 1] = last_element
        cnt_of_rotation += 1

    return arr

# Driver code
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2
 
# Function calling
result = rotate(arr, d, n)
print(result)


# approach 2

def rotate(L, d, n):
    k = L.index(d)
    new_lis = []
    new_lis = L[k+1:]+L[0:k+1]
    return new_lis

# approach 3 

def rotate_effcient(arr_new, d, n):

    # step 1 : create a temp array and store the arr_new twice and then perform the slicing

    temp_array = [0]*2*n

    for i in range(n):
        temp_array[i]=temp_array[i+n]=arr_new[i]    

    # if the value of k ever exceeds the length of the array
    rotate = d % n

    return temp_array[rotate:rotate+n]

# Driver code
arr_new = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2
 
# Function calling
result = rotate_effcient(arr_new, d, n)
print(result)