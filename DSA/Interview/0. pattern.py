"""
1. Check the number of rows (decide you need start with i = 1 or i = 5  )
2. Check how the each row is starting is, is it starting with 5 or 1 and determine j
"""

"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

def pattern1(n: int) -> None:
    for _ in range(1, n + 1):
        for j in range(1, 6):
            print(j, end=" ")
        print()


"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""


def pattern2(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


"""
5
4 5
3 4 5
2 3 4 5
1 2 3 4 5

starting element is changing so j shouldnt start with constant numbers like 1,n
"""


def pattern3(n: int):
    for i in range(n, 0, -1):
        for j in range(i, n + 1):
            print(j, end=" ")
        print()


"""
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
"""


def pattern4(n: int) -> None:
    for i in range(n, 0, -1):
        for j in range(n, i - 1, -1):
            print(j, end=" ")
        print()

"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""


def pattern5(n: int) -> None:
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


"""
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""


def pattern6(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(n, i - 1, -1):
            print(j, end=" ")
        print()

"""
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""


def pattern7(n: int) -> None:
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

"""
1 2 3 4 5
2 3 4 5
3 4 5
4 5
5
"""

def pattern8(n: int) -> None:
    for i in range(1, n+1):
        for j in range(i, n+1):
            print(j, end=" ")
        print()

"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""


def pattern9(n: int) -> None:
    count = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(count, end=" ")
            count += 1
        print()

"""
1 2 1 2 1
1 2 1 2
1 2 1
1 2
1
"""

def pattern10(n: int) -> None:
    for i in range(1,n+1):
        for j in range(n, i-1,-1):
            if j%2==0:
                print('2', end=" ")
            else:
                print('1', end=" ")
        print()



""" 

Difficult Patterns with Spaces 
https://online.codeanddebug.in/wp-content/uploads/2024/01/Week-3-Assignment-2.pdf

"""

def pattern11(n: int) -> None:
    for i in range(1,n+1):
        for j in range(1, (n-i)+1):
            print(' ', end=" ")
        for k in range(i, 0,-1):
            print(k, end=" ")       

        print()

def pattern12(n: int) -> None:
    for i in range(n, 0, -1):
        for j in range(i - 1):
            print(" ", end=" ")
        for k in range(n, i - 1, -1):
            print(k, end=" ")

        print()

def pattern13(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end=" ")
        for k in range(2 * i - 1):
            print(i, end=" ")
        print()

def pattern14(n: int) -> None:
    for i in range(1, n // 2 + 2):
        for j in range(n // 2 - i + 1):
            print(" ", end=" ")
        for k in range(2 * i - 1):
            print(i, end=" ")
        print()

    for i in range(n // 2, -1, -1):
        for j in range(n // 2 - i + 1):
            print(" ", end=" ")
        for k in range(2 * i - 1):
            print(i, end=" ")
        print()

def pattern15(n: int) -> None:
    for i in range(1, n // 2 + 2):
        for j in range(1,i+1):
            print(j, end=" ")
        print()

    for i in range(n // 2, 0, -1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()


def pattern16(n: int) -> None:
    for i in range(n // 2 + 1, 0,-1):
        for j in range(i,n//2+2):
            print(j, end=" ")
        print()

    for i in range(2, n // 2 + 2):
        for j in range(i, n // 2 + 2):
            print(j, end=" ")
        print()

def pattern17(n: int) -> None:
    for i in range(1, n // 2 + 2):
        for j in range(n // 2 - i + 1):
            print(" ", end=" ")
        for k in range(1, 2 * i):
            print(k, end=" ")
        print()
        
    for i in range(n // 2, -1, -1):
        for j in range(n // 2 - i + 1):
            print(" ", end=" ")
        for k in range(1, 2 * i):
            print(k, end=" ")
        print()


pattern16(9)
