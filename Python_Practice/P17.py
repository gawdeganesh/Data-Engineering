def drawRectangle(width,height):
    if width<1 or height<1:
        return None
    # for row in range(0,height):
    #     for column in range(0,width):
    #         print('#', end='')
    #     print()    

    for i in range(height):
        print(('#'*width))

width= int(input('enter width of the rectangle : \n'))
height = int(input('enter height of the rectangle: \n'))

print(f'the rectangle ( {width}, {height} ) is \n ')
drawRectangle(width,height)