# 1 3 6 8 11 13 16 18 21 23


def pattern1(n: int):
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


#pattern1(10)


"""
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""


def pattern(n: int) -> None:
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


pattern(5)