def product_except_self(nums):
    # The length of the input array
    length = len(nums)

    # The answer array to hold the products
    answer = [0] * length

    # answer[i] contains the product of all the elements to the left
    # Note: for the element at index '0', there are no elements to the left,
    # so the answer[0] would be 1
    answer[0] = 1
    for i in range(1, length):
        answer[i] = nums[i - 1] * answer[i - 1]

    # R contains the product of all the elements to the right
    # Note: for the element at index 'length - 1', there are no elements to the right,
    # so the R would be 1
    R = 1
    for i in reversed(range(length)):
        # For the index 'i', R would contain the
        # product of all elements to the right. We update R accordingly
        answer[i] = answer[i] * R
        R *= nums[i]

    return answer


# Example usage:
example_array = [1, 2, 3, 4]
product_except_self(example_array)
