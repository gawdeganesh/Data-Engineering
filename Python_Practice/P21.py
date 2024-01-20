# Map the lowercase letters to uppercase letters.
LOWER_TO_UPPER = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g':
'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O',
'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x':
'X', 'y': 'Y', 'z': 'Z'}

def getUppercase(text):
    uppercaseText=''

    for character in text:
        if character in LOWER_TO_UPPER:
            uppercaseText += LOWER_TO_UPPER[character]
        else:
            uppercaseText += character    

    return uppercaseText

text = input("Enter Text : \n")

print(f'Upper text is : {getUppercase(text)}')