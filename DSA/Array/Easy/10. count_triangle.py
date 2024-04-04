# Python3 code to count the number of possible triangles using brute force approach

# Function to count all possible
# triangles with arr[] elements


# def findNumberOfTriangles(arr, n):

# 	# Count of triangles
# 	count = 0

# 	# The three loops select three
# 	# different values from array
# 	for i in range(n):
# 		for j in range(i + 1, n):

# 			# The innermost loop checks for
# 			# the triangle property
# 			for k in range(j + 1, n):

# 				# Sum of two sides is greater
# 				# than the third
# 				if (arr[i] + arr[j] > arr[k] and
# 					arr[i] + arr[k] > arr[j] and
# 						arr[k] + arr[j] > arr[i]):
# 					count += 1
# 	return count


# # Driver code
# if __name__ == "__main__":
# 	arr = [10, 21, 22, 100, 101, 200, 300]
# 	size = len(arr)

# 	# Function call
# 	print("Total number of triangles possible is",
# 		findNumberOfTriangles(arr, size))


# approach 2 : First sort the array in ascending order. Then use two loops. The outer loop to fix the first side and the inner loop to fix the second side and then find the farthest index of the third side (greater than indices of both sides) whose length is less than the sum of the other two sides. So a range of values third side can be found, where it is guaranteed that its length is greater than the other individual sides but less than the sum of both sides.


def findNumberOfTriangles1(arr, size):

    # Sort array and initialize count as 0
    n = size
    arr.sort()
    count = 0

    # Fix the first element. We need to run till n-3 as
    # the other two elements are selected from arr[i + 1...n-1]
    for i in range(0, n - 2):

        # Initialize index of the rightmost third element
        k = i + 2  # pointer used to calcualte the sum

        # Fix the second element
        for j in range(i + 1, n):

            # Find the rightmost element which is smaller
            # than the sum of two fixed elements
            # The important thing to note here is, we use
            # the previous value of k. If value of arr[i] +
            # arr[j-1] was greater than arr[k], then arr[i] +
            # arr[j] must be greater than k, because the array
            # is sorted.
            while k < n and arr[i] + arr[j] > arr[k]:
                k += 1

            # Total number of possible triangles that can be
            # formed with the two fixed elements is k - j - 1.
            # The two fixed elements are arr[i] and arr[j]. All
            # elements between arr[j + 1] to arr[k-1] can form a
            # triangle with arr[i] and arr[j]. One is subtracted
            # from k because k is incremented one extra in above
            # while loop. k will always be greater than j. If j
            # becomes equal to k, then above loop will increment k,
            # because arr[k] + arr[i] is always greater than arr[k]
            if k > j:
                count += k - j - 1

    return count


# Driver code
if __name__ == "__main__":
    arr = [10, 21, 22, 100, 101, 200, 300]
    size = len(arr)

    # Function call
    print("Total number of triangles possible is", findNumberOfTriangles1(arr, size))

    # approach 3 : Follow the given steps to solve the problem:

# Sort the array and then take three variables l, r, and i, pointing to start, end-1, and array element starting from the end of the array.
# Traverse the array from the end (n-1 to 1), and for each iteration keep the value of l = 0 and r = i-1
# Now if a triangle can be formed using arr[l] and arr[r] then triangles can obviously be formed
# from a[l+1], a[l+2]…..a[r-1], arr[r] and a[i], because the array is sorted , which can be directly calculated using (r-l). and then decrement the value of r and continue the loop till l is less than r
# If a triangle cannot be formed using arr[l] and arr[r] then increment the value of l and continue the loop till l is less than r


# Python implementation of the above approach
def CountTriangles(A):

    n = len(A)

    A.sort()

    count = 0

    for i in range(n - 1, 0, -1):
        l = 0
        r = i - 1
        while l < r:
            if A[l] + A[r] > A[i]:

                # If it is possible with a[l], a[r]
                # and a[i] then it is also possible
                # with a[l + 1]..a[r-1], a[r] and a[i]
                count += r - l

                # checking for more possible solutions
                r -= 1

            else:

                # if not possible check for
                # higher values of arr[l]
                l += 1
    print("No of possible solutions: ", count)


# Driver Code
if __name__ == "__main__":

    A = [10, 21, 22, 100, 101, 200, 300]

    # Function call
    CountTriangles(A)

# This code is contributed by PrinciRaj1992
