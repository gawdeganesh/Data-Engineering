def OrdinalSuffix(number):
    if number[-2:] in ('11','12','13'):
        return number + 'th'
    elif number[-1:] == '1':
        return number + 'st'
    elif number[-1:] == '2':
        return number + 'nd'
    elif number[-1:] == '3':
        return number + 'rd'
    else :
        return number + 'th'


number = input("Enter the number \n")
print(f'the ordinal number of {number} is '+ OrdinalSuffix(number))