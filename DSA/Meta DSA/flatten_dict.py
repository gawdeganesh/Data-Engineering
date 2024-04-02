def flatten_dict(d, parent_key="", sep="."):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


nested_dict = {"a": 1, "b": {"c": 2, "d": {"e": 3, "f": 4}}}
print(flatten_dict(nested_dict))
