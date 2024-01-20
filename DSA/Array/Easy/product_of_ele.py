def productOfElements(arr,n):

    if not arr:
        return None

    product=[]

    for i in range(n):
        prod = 1
        for j in range(n):
            if i != j:
                prod = prod* arr[j]

        product.append(prod)

    return product    


# Driver code
arr = [2,1, 9, 8]
n = len(arr)
print("Original Array:", arr)
prod= productOfElements(arr, n)
print("Final Array:", prod)


