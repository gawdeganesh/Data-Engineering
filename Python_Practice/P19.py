def drawPyramid(height):
    for rowNumber in range(height):
        # Create a string of spaces for the left side of the pyramid:
        leftSideSpaces = ' '*(height - (rowNumber+1))
        # Create the string of hashtags for this row of the pyramid:
        pyramidRow = '#' * (rowNumber*2 +1)

        # Print the left side spaces and the row of the pyramid:

        print(leftSideSpaces + pyramidRow)

drawPyramid(4)

