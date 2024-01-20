def duplicate_characters(input):

    input_dict = {key : list(input).count(key) for key in list(input)}

    input_list = [key for key in input_dict.keys() if input_dict[key]>1]
    

    return input_list

print(duplicate_characters("geeksforgeeks"))
