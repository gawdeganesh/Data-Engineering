def linear_search(arr: list, element: int) -> bool:
    if not arr:
        return "Array is empty"

    for ele in arr:
        if ele == element:
            return True
    return False


print(linear_search([1, 2, 34, 5, 6, -9, 88888], -9))
print(linear_search([1, 2, 34, 5, 6, -9, 88888], 234))
print(linear_search([], -9))
