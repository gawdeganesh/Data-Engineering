def merge_dictionary(dict1: dict[str, int], dict2: dict[str, int]) -> dict:
    merged_dict = dict2.copy()
    for key, value in dict1.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value

    return merged_dict


# Example usage
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "d": 5, "e": 6}

merged_dict = merge_dictionary(dict1, dict2)

print(f"Merged dictionary: {merged_dict}")
