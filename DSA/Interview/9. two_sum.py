def two_sum(arr: list, sum: int) -> list:
    seen_pairs = set()
    unique_pairs = []

    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j]) == sum and (i, j) not in unique_pairs:
                unique_pairs.append([i, j])
                seen_pairs.add((i, j))
    return unique_pairs


print(two_sum([1, 2, 34, 5, 6, -9, 9, 2, 11, 0, 2, 9], 11))
print(two_sum([1, 2, 34, 5, 6, -9, 88888], 200))
print(two_sum([], -9))
