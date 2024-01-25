def two_sum(arr: list, sum: int) -> list:
    seen_pairs = set()
    seen_pairs_data = []  # to store the array data
    unique_pairs = []

    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j]) == sum and [arr[i], arr[j]] not in seen_pairs_data:
                # checking if 2,9 is not getting calculated multiple times
                unique_pairs.append([i, j])
                seen_pairs.add((i, j))
                seen_pairs_data.append([arr[i], arr[j]])

    # print(seen_pairs_data)

    return unique_pairs  # time complexity : O(N^2) and Space = O(N)


print(two_sum([1, 2, 34, 5, 6, -9, 9, 2, 11, 0, 2, 9], 11))
# print(two_sum([1, 2, 34, 5, 6, -9, 88888], 200))
# print(two_sum([], -9))
