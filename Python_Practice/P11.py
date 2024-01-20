import random

# Create string constants that for each type of character:
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '1234567890'
SPECIAL = '~!@#$%^&*()_+'

ALL_CHARS = LOWER_LETTERS+ UPPER_LETTERS+ NUMBERS+SPECIAL

def generatePassword(length):
    #12 is the minimum length for passwords:
    if length<12:
        length=12

    password = []
    password.append(LOWER_LETTERS[random.randint(0,25)])
    password.append(UPPER_LETTERS[random.randint(0,25)])
    password.append(NUMBERS[random.randint(0,10)])
    password.append(SPECIAL[random.randint(0,14)])

    while len(password)< length:
        password.append(ALL_CHARS[random.randint(0,74)])

    random.shuffle(password)

    return ''.join(password)

print(f'generate password for length 15 : {generatePassword(15)}')
