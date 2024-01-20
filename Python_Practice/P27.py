def mergeTwoLists(list1,list2):
    result=[]
    # Start i1 and i2 at index 0, the start of list1 and list2:
    i1 = 0
    i2 = 0

    while i1< len(list1) and i2<len(list2):
        if list1[i1]< list2[i2]:
            result.append(list1[i1])
            i1+=1
        else:
            result.append(list2[i2])
            i2+=1   

    if i1<len(list1):
        for j in range(i1,len(list1)):
             result.append(list1[j])

    if i2<len(list2):
        for j in range(i2,len(list2)):
             result.append(list1[j])

    return result

l1 = [4,6,45,49,100] 
l2 = [4,6,12]   

print(f'the merged list is : {mergeTwoLists(l1,l2)}')


