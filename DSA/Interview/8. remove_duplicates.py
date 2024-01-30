def remove_duplicates(arr: list) -> list:
    if not arr:
        return -1

    dict = {}
    for ele in arr:
        if ele not in dict.keys():
            dict[ele] = 1
        else:
            dict[ele] += 1

    unique_list = [keys for keys in dict.keys()]

    return unique_list  # time and space : O(N)


print(
    remove_duplicates([1, 2, 34, 5, 6, -9, 88888, 2, 4, 34, 88888, 1, 1, 1, 1, 5, 6, 6])
)
print(remove_duplicates([]))
