""" 1. Calculate the cube of all numbers from 1 to a given number."""


def cube(num: int) -> int:
    for i in range(1, num + 1):
        print(i**3, end=" ")

    print()


# cube(5)

""" Write a function named notPrimeNumbers which accepts 2 integers n1 and n2. Print all the numbers from n1 to n2 which are not prime.
"""


def notPrime(n1: int, n2: int) -> list:
    num_dict = {}

    for i in range(n1, n2 + 1):
        cnt = 0
        for j in range(1, i + 1):
            if i % j == 0:
                cnt += 1
        num_dict[i] = cnt

    non_prime = [key for key, value in num_dict.items() if value > 2]

    return non_prime


print(f"non prime numbers are {notPrime(5,20)}")
