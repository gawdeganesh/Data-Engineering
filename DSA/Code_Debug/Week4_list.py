""" 
Q1. Write a Python code to check if a given list is sorted in ascending order.
You don’t have to change the list. Just output YES if list is sorted else NO. 
"""

def is_sorted(arr:list[int])->str:
    if not arr or len(arr) ==1:
        return 'List is empty or has length 1'
    
    i = 0
    while i < len(arr)-1:
        if arr[i]> arr[i+1]:
            return 'No'
        i+=1

    return 'Yes'

# print(is_sorted([1,2,3,4,45,47,56]))
# print(is_sorted([1,2,3,5,47,44,56]))
# print(is_sorted([]))

""" 
Q2. Given two sorted lists, write a Python code to merge them into a single
sorted list.
Don’t use SORT() method.
"""

def merge_sorted_list(arr1:list[int], arr2:list[int])->list[int]:

    if not arr1 and arr2:
        return arr2
    elif not arr2 and arr1:
        return arr1

    i=j=0
    merge_sorted_list = []

    while i<len(arr1) and j< len(arr2):
        if arr1[i]<arr2[j]:
            merge_sorted_list.append(arr1[i])
            i+=1
        else: 
            merge_sorted_list.append(arr2[j])
            j+=1
    
    if i<len(arr1):
        while i <len(arr1):
            merge_sorted_list.append(arr1[i])
            i+=1

    if j<len(arr2):
        while j <len(arr2):
            merge_sorted_list.append(arr2[j])
            j+=1
    return merge_sorted_list

arr1 = []
arr2 = [1,2,3,4,8,9]
arr3 = [-2,-1,0,1,2,6,7,10,11,12]

# print(f"the merged and sorted array is : {merge_sorted_list(arr2, arr3)}")
# print(f"the merged and sorted array is : {merge_sorted_list(arr1, arr3)}")

""" 
Q3. Write a python program to check if the list contains three consecutive
common numbers in Python.
"""

def find_all_consecutive_common_numbers(lst):
    # Early return if the list has fewer than 3 elements
    if len(lst) < 3:
        return []
    
    results = []  # To store all sets of three consecutive common numbers
    current_count = 1  # To count the occurrences of the current number
    
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            current_count += 1
            # Check if the count is 3 and the number is not already added
            if current_count == 3:
                if results and results[-1] != lst[i]:
                    results.append(lst[i])
                elif not results:
                    results.append(lst[i])
        else:
            current_count = 1  # Reset count for a new number
    
    return results

# Example usage
example_list = [1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 2,2,2]
print("Distinct sets of three consecutive common numbers:", find_all_consecutive_common_numbers(example_list))

"""
Q4. Write a Python code to check if a list is a palindrome 
(reads the same forwards and backwards). Just print “YES” or “NO”
"""

from typing import List


def isPalindrome(lst: List) -> bool:
    for i in range(0, len(lst)):
        if lst[i] != lst[len(lst) - i - 1]:
            return False
    return True


print(isPalindrome([1, 2, 3, 4, 4, 3, 2, 1]))
print(isPalindrome([1, 2, 3, 4, 3, 2, 1]))
print(isPalindrome([1, 2, 3, 4, 3, 4, 1]))


"""
Q5. Write a Python code to find the occurrence of each element in a list 
and print the element with the highest occurrence.
"""
my_list = ["Anirudh", 1, 1, 1, 2, 3, 154, 65, 2, 2, 1, 44, 5, 154, 154, "Anirudh"]

unique_elements = []

for i in my_list:
    if i not in unique_elements:
        unique_elements.append(i)

# Print the frequencies and keep track of the largest frequency and that element
highest_frequency = 0
highest_frequency_element = 0

for i in unique_elements:
    freq = my_list.count(i)
    print(f"{i} occurs {freq} times")
    if freq > highest_frequency:
        highest_frequency = freq
        highest_frequency_element = i

print(f"Highest frequency = {highest_frequency}")
print(f"Highest frequency element = {highest_frequency_element}")


def secondLargest(nums: List[int]):
    if len(nums) < 2:
        return "Not enough elements"

    largest = second_largest = float("-inf")  # -inf means the most negative value
    # Can take as the smallest value

    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float("-inf"):
        return "There is no second largest element"
    else:
        return second_largest


nums = [12, 74, -89, 96, -98, -96, 52]
result = secondLargest(nums)
print(f"Second largest element = {result}")