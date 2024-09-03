def printMaximum(inum):
    hash_set = [0] * 10

    result = ""
    for num in str(inum):
        hash_set[int(num)] += 1

    for num in range(9, -1, -1):
        if hash_set[num] > 0:
            result += str(num) * hash_set[num]

    return int(result)


# Driver code
num = 38293367
print(printMaximum(num))
