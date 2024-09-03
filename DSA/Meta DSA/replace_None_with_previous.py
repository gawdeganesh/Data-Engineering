def replace_none_with_previous(values):
    # Check if the input list is not empty or only contains None
    if not values:
        return values
    
    # Initialize the last seen non-None value
    last_non_none = None
    for i in range(len(values)):
        if not values[i]:
            # If the current value is None, replace it with the last seen non-None value
            values[i] = last_non_none
        else:
            # Update the last seen non-None value
            last_non_none = values[i]
    return values

# Example usage
example_list = [1, None, 1, 2, None]
print(replace_none_with_previous(example_list))

# Edge case with initial None values
edge_case_list = [None, 1, None]
print(replace_none_with_previous(edge_case_list))

# Case with only None in the list
only_none_list = [None]
print(replace_none_with_previous(only_none_list))
