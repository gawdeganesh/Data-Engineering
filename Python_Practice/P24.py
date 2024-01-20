def makeChange(amount):
    change={}

    if amount>=25:
        change['quarters'] = amount//25
        amount = amount%25

    if amount>=10:
        change['dimes'] = amount//10
        amount = amount%10

    if amount>=5:
        change['nickels'] = amount//5
        amount = amount%5

    if amount>=1:
        change['pennies'] = amount

    return change

amount = int(input("Enter Amount : \n"))

print(f'change : {makeChange(amount)}')         

