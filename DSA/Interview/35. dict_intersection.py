def dict_intersection(dict1: dict, dict2: dict) -> dict:

    common_items = {}

    for k, v in dict1.items():
        if k in dict2 and dict2[k] == v:
            common_items[k] = v
    return common_items


print(
    dict_intersection(
        {"a": 2, "b": 3, "c": 3, "d": 9, "e": 0}, {"a": 2, "b": 2, "c": 3}
    )
)
print(dict_intersection({"a": 2, "b": 3, "c": 3, "d": 9, "e": 0}, {}))
