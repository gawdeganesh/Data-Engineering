def array_intersection(arr1:list[int], arr2:list[int])-> list[int]:

    if not arr1 or not arr2:
        return -1 
    
    # sort the array 
    arr1.sort()
    arr2.sort()

    i=j=0
    intersection = []

    while i< len(arr1) and j<len(arr2):

        if arr1[i]== arr2[j]:
            intersection.append(arr1[i])
            i+=1
            j+=1
        
        elif arr1[i]<arr2[j]:
            i+=1
        
        else:
            j+=1

    return intersection

def string_intersection (str1, str2):
    if not str1 or not str2 :
        return -1
    
    counter_str1 = {}

    for char in str1:
        if char in counter_str1:
            counter_str1[char]+=1
        else:
            counter_str1[char]=1
    
    intersection = ''

    for char in str2:
        if char in counter_str1 and counter_str1[char]>0:
            intersection+= char
            counter_str1[char]-=1

    return intersection

print(array_intersection([],[]))
print(array_intersection([1,2,3,5,67,7],[]))
print(array_intersection([1,2,3,3,5,67,7],[34,1,3,45,67,7,1,3,3,3]))
print(array_intersection([1,2,3,5,67,7],[0,0,-1,-2,-3]))

print(string_intersection('',''))
print(string_intersection('abcxyz','abcdefg'))
print(string_intersection('aaaaabbcccderdfs','aabbccddeer'))

