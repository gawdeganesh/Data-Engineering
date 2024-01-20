# https://www.geeksforgeeks.org/find-subarray-with-given-sum/#

# def subArraySum(arr, n, sum):

#     for i in range(0,n):
#         sub_array_sum=arr[i]
#         if(sub_array_sum == sum):
#             print("Sum found at indexes",i)
#             return
        
#         for j in range(i+1,n-1):
#             if(sub_array_sum!= sum and sub_array_sum<sum):
#                 sub_array_sum= sub_array_sum+arr[j]
#             elif(sub_array_sum== sum):
#                 print(f"the subarray indices are {i},{j-1}")
#                 return   
#             else:
#                 break   
#     print("No Subarray Found")        


def subArraySum(arr, n, sum):

    seen_pairs = set()
    unique_pair = []

    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==sum and (i,j) not in seen_pairs:
                unique_pair.append([i,j])
                seen_pairs.add((i,j))
    
    return unique_pair
     

# Driver Code
if __name__ == "__main__":
    arr = [15,2,4,8,9,5,10,23,21,2,4]
    n = len(arr)
    sum = 23
    print(subArraySum(arr, n, sum))