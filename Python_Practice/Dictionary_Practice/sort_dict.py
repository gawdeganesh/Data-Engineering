from collections import OrderedDict
import numpy as np
myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}

sorted_list_key = list(myDict.keys())
sorted_list_key.sort()
sorted_list_values = list(myDict.values())
sorted_value_index = np.argsort(sorted_list_values)

sorted_dict_key = {key : myDict[key] for key in sorted_list_key}
sorted_dict_value = {sorted_list_key[i] : sorted_list_values[i] for i in sorted_value_index}
print(sorted_dict_key)
print(sorted_dict_value)