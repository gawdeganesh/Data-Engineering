#https://www.geeksforgeeks.org/find-the-largest-three-elements-in-an-array/
import sys

def print3largest(arr,arrSize):
    first= second=third= -sys.maxsize

    if(arrSize<3):
        return print("Size of the array is less than 3")

    for element in arr:
        if (element>first):
            third= second  # this sequence is important 
            second=first
            first=element

        elif (element>second and element != first):
            third= second
            second=element

        elif(element>third and element != second and element != first) :
            third=element     

    print("The three largest element are", first,second,third)    


# Driver program to test above function

# note if we want to send distinct top 3 numbers then add this condition in the if block elif (element>second and element != first):
arr = [12, 13, 1, 34, 34, 1]
n = len(arr)
print3largest(arr, n)

