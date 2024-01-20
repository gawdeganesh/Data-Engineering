def print_fact(num: int) -> int:
    fact = 1

    while num >= fact:
        if num % fact == 0:
            print(fact, end=" ")
        fact += 1

    print()


def countFact(num: int) -> int:
    fact = 1
    count_fact = 0

    while num >= fact:
        if num % fact == 0:
            count_fact += 1
        fact += 1

    return count_fact


def checkPrime(num: int) -> int:
    fact = 1
    count_fact = 0

    while num >= fact:
        if num % fact == 0:
            count_fact += 1
        fact += 1

    if count_fact == 2:
        print("the number is a prime number")
    else:
        print("the number is not a prime number")


print_fact(12)
checkPrime(7)
checkPrime(12)
