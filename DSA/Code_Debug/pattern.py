# 1 3 6 8 11 13 16 18 21 23


def pattern(n: int):
    num = 1
    i = 1
    while i <= n:
        print(num, end=" ")

        i += 1

        if i % 2 == 0:
            num = num + 2
        else:
            num = num + 3

    print()


pattern(10)
