def max_product_of_two(arr: list[int]):

    if not arr:
        return -1

    # assign max numbers with smallest value
    max_1 = max_2 = float("-inf")

    # assign min numbers with largest value
    min_1 = min_2 = float("inf")

    for num in arr:
        # update max values
        if num > max_1:
            max_2 = max_1
            max_1 = num
        elif num > max_2:
            max_2 = num

        # update min values
        if num < min_1:
            min_2 = min_1
            min_1 = num
        elif num < min_2:
            min_2 = num

    return max(max_1 * max_2, min_1 * min_2)


print(max_product_of_two([1, 2, 34, 5, 6, 2, 4, 34, 1, 1, 1, 1, 5, 6, 6]))
print(max_product_of_two([]))
print(max_product_of_two([1, 2, -40, 5, -6, 2, 4, 34, 1, 1, 1, 1, 5, 6, 6]))
