import random

def rollDice(numberOfDIce):
    total = 0

    for i in range(numberOfDIce):
        total+=random.randint(1,6)
    return total

print(rollDice(5))    