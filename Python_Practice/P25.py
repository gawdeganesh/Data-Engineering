import random
def shuffle(values):
    for i in range(len(values)):

        swapindex = random.randint(0,len(values)-1)
        values[i],values[swapindex] = values[swapindex],values[i]

    return values

values =[]

n = int(input("Enter number of elements : "))

for i in range(0, n):
	ele = int(input())
	values.append(ele)

print (values)
print(f'the shuffle list of values : {shuffle(values)}')


