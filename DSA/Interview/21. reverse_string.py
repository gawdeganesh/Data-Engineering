def reverse_string(word)->str:
    if not word:
        return ''
    
    reverse_string = ''

    for char in word:
        reverse_string = char + reverse_string

    return reverse_string


print(f"reverse string of abcd is  {reverse_string('abcd')} ")
print(f"reverse string of aaaa is  {reverse_string('aaaa')} ")
print(f"reverse string of '' is  {reverse_string(' ')} ")
print(f"reverse string of 12345 is  {reverse_string('12345')} ")


# other ways 

def reverse_string(word):
    return word[::-1]

def reverse_string(word):
    return ''.join(reversed(word))

from functools import reduce

def reverse_string(word):
    return reduce(lambda x, y: y + x, word)

# time and space complexity for all the program : O(N)