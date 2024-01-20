def collatz(startingNumber):
    if startingNumber<1:
        return []
    sequence = [startingNumber]
    num = startingNumber

    while num!=1:
        if num%2==1:
            num = 3*num +1
        else:
            num=num//2  
        sequence.append(num)

    return sequence

num = int(input("Enter a starting number : "))

print(f'The Collatz sequence is : {collatz(num)}')            