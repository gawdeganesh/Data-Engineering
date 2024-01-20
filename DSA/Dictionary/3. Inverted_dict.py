def inverted_dict(dict: dict)->dict:

    inv_dict = { }

    for item,price in dict.items():
        if price not in inv_dict:
            inv_dict[price] = []
        
        inv_dict[price].append(item)

    return inv_dict



dict2 = {"item1": 4, "item2": 5, "item3": 4}

inverted = inverted_dict(dict2)

print(f"Inverted dictionary: {inverted}")