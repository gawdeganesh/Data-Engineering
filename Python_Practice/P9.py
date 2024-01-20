def average(numbers):
    if len(numbers)==0:
        return None
    total = 0

    for number in numbers:
        total+= number

    return total/len(numbers)

def median(numbers):
    if len(numbers)==0:
        return None
    numbers.sort()

    if len(numbers) % 2 == 0:
        return (numbers[len(numbers)//2]+ numbers[(len(numbers)//2) - 1]) /2
    else:
        return numbers[len(numbers)//2] 
    
def mode(numbers):
# Special case: If the numbers list is empty, return None:
    if len(numbers) == 0:
       return None
# Dictionary with keys of numbers and values of how often they appear:
    numberCount = {}
# Track the most frequent number and how often it appears:
    mostFreqNumber = None
    mostFreqNumberCount = 0
# Loop through all the numbers, counting how often they appear:
    for number in numbers:
        if number not in numberCount:
            numberCount[number] = 0
        numberCount[number] += 1

        if numberCount[number] > mostFreqNumberCount:
            mostFreqNumber = number
            mostFreqNumberCount = numberCount[number]

    return mostFreqNumber    

numbers =[1,23,45,56]

print(f'the average is {average(numbers)}')
print(f'the median is {median(numbers)}')



