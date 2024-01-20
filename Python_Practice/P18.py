def drawBorder(width, height):
    if width <3 or height<3:
        return None
    # Print the top row:
    print('+'+('-'*(width-2))+'+')

    # Loop for each row (except the top and bottom):

    for i in range(height-2):
        print('|'+(' '*(width-2))+'|')

    # Print the bottom row:
    print('+'+('-'*(width-2))+'+')        

width= int(input('enter width of the rectangle : \n'))
height = int(input('enter height of the rectangle: \n'))

print(f'the rectangle ( {width}, {height} ) is \n ')
drawBorder(width,height)

