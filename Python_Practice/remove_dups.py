def removeDupWithoutOrder(str):
 
    # set() --> A Set is an unordered collection
    #         data type that is iterable, mutable,
    #         and has no duplicate elements.
    # "".join() --> It joins two adjacent elements in
    #             iterable with any symbol defined in
    #             "" ( double quotes ) and returns a
    #             single string
    return "".join(set(str))

def removeDupWithOrder(str):

    t=''
    for char in str:
        if char in t:
            pass
        else:
            t=t+char
    return t

# Driver program
if __name__ == "__main__":
    str = "geeksforgeeks"
    print ("Without Order = ",removeDupWithoutOrder(str))
    print ("With Order = ",removeDupWithOrder(str))