
def arrayEvenAndOdd(arr, n):
    even_array=[]
    odd_array=[]

    if(n==1):
        return print(arr)
    else:
        for i in range(n):
            if arr[i]%2==0:
               even_array.append(arr[i]) 
            else:
                odd_array.append(arr[i])  

        return  print(even_array+odd_array)        


arr = [1, 3, 2, 4, 7, 6, 9, 10]
n = len(arr)
arrayEvenAndOdd(arr, n)




def arrayEvenAndOdd(arr, n):
    even_array = [i for i in arr if i % 2 == 0]
    odd_array = [i for i in arr if i % 2 == 1]

    return even_array + odd_array