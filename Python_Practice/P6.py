def writeToFile(filename, text):
# Open the file in write mode:
    with open(filename, 'w') as fileObj:
    # Write the text to the file:
        fileObj.write(text)

def appendToFile(filename, text):
# Open the file in append mode:
    with open(filename, 'a') as fileObj:
    # Write the text to the end of the file:
        fileObj.write(text)

def readFromFile(filename):
    # Open the file in read mode:
    with open(filename) as fileObj:
    # Read all of the text in the file and return it as a string:
        return fileObj.read()

writeToFile('test.txt','Hi testing \n')
appendToFile('test.txt', ' append testing')
print(readFromFile('test.txt'))
