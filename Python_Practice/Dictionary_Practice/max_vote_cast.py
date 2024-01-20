
from collections import Counter

input =['john','johnny','jackie','johnny',
            'john','jackie','jamie','jamie',
            'john','johnny','jamie','johnny',
            'john']

# method 1
dict = {ele : input.count(ele) for ele in input}

max_key = max(dict, key=dict.get)

# method 2 
votes_count = Counter(input)

max_value = max(votes_count.values())

votes_list = [key for key,value in votes_count.items() if value == max_value ]

print(votes_count)
print(max_value)
print(votes_list)
print(sorted(votes_list)[0])