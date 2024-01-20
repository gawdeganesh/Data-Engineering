def swapList(newlist):
    newlist[0],newlist[-1]= newlist[-1],newlist[0]

    # size= len(newList)
    # temp = newList[0]
    # newList[0]= newList[size-1]
    # newList[size-1]= temp


    return newlist


newList= [1,3,4,6,7,8]

print(f'Swapped list is :{swapList(newList)}')