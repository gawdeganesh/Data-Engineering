def moveNumbers(arr,n):

    if not arr:
        return None

    product=[]

    for ele in arr:
        if ele <0:
            product.append(ele)

    for ele in arr:
        if ele >=0:
            product.append(ele)
            
    return product    


# Driver code
arr = [2,1, 9, 8,0,-4,5,-34,-44]
n = len(arr)
print("Original Array:", arr)
prod= moveNumbers(arr, n)
print("Final Array:", prod)
