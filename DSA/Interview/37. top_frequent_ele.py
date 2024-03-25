""" 
Given a list of elements, find the top N most frequent elements and return them in a dictionary.
"""


def top_frequent(ele_list: list[int], n: int) -> dict[int, int]:
    count_dict = {}

    for ele in ele_list:
        count_dict[ele] = count_dict.get(ele, 0) + 1

    if len(count_dict) < n:
        return -1

    print(count_dict)

    print (sorted(count_dict.items(), key=lambda items: items[1], reverse=True)[n][1])
    sorted_dict = dict(
        sorted(count_dict.items(), key=lambda items: items[1], reverse=True)[:n]
    )

    # count = 0
    # top_dict = {}

    # for k,v in sorted_dict.items():
    #     if count<n :
    #         count+=1
    #         top_dict[k] = v
    #     else :
    #         return top_dict

    return sorted_dict


print(top_frequent([1, 3, 45, 656, 1, 3, 3, 4, 56, 45, 1656, 656, 0, 0, 0, 0, 0, 0, 1], 3 ))
print(top_frequent([1, 3, 45, 0, 1], 6))
