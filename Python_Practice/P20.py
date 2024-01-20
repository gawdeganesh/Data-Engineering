def commaFormat(number):
    number = str(number)

    if '.'in number:
        fractionalPart = number[number.index('.'):]
        number = number[:number.index('.')]
    else:
        fractionalPart=''

    triplet = ''
    commaNumbar = ''

    for i in range(len(number)-1,-1,-1):
        triplet= number[i]+triplet

        if len(triplet)==3:
            commaNumbar=triplet+','+commaNumbar
            triplet= ''

    if triplet!= '':
        commaNumbar= triplet + ',' + commaNumbar

    return commaNumbar[:-1]+ fractionalPart    


