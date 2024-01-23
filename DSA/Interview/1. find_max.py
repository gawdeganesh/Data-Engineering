def find_max_element(arr: list) -> int:
    if not arr:
        return None
    max_element = arr[0]
    for ele in arr:
        if ele > max_element:
            max_element = ele
    return max_element


print(find_max_element([1, 2, 34, 5, 6, -9, 88888]))
print(find_max_element([]))
print(find_max_element([-1, -2, -34, -5, -6, -9, -88888]))
