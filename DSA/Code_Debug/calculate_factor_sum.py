def calculateFactorSum(n1: int, n2: int) -> int:
    fact = 1
    sum = 0

    while fact <= n1:
        if fact % n2 == 0:
            sum += fact

        fact += 1

    return sum



sum = calculateFactorSum(30, 7)

print(f"the factors sum is : {sum}")
