def reverseString(text):
    text = list(text)

    for i in range(len(text)//2):
        mirrorIndex = len(text)-i-1
        text[i],text[mirrorIndex] = text[mirrorIndex],text[i]

    return ''.join(text)

text = input("Enter a String : \n")

print(f'The reverse String is : {reverseString(text)}')      