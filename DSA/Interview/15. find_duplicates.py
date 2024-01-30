def find_duplicates(arr: list[int]) -> list[int]:
    dict_count = {ele: arr.count(ele) for ele in arr}
    unique_ele = [key for key, values in dict_count.items() if values == 1]

    return unique_ele


print(find_duplicates([1, 2, 34, 5, 6, 2, 4, 34, 1, 1, 1, 1, 5, 6, 6]))
print(find_duplicates([]))
print(find_duplicates([1, 2, -40, 5, -6, 2, 4, 34, 1, 1, 1, 1, 5, 6, 6]))
