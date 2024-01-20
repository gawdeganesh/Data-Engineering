def getTitleCase(text):
    titleText=''

    for i in range(len(text)):
        if i==0:
            titleText+=text[i].upper()
        elif text[i].isalpha() and not text[i-1].isalpha():
            titleText+=text[i].upper()  
        else:
            titleText+=text[i].lower()

    return titleText

text = input("Enter Text : \n")

print(f'Title text is : {getTitleCase(text)}')              


