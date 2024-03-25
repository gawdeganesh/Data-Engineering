def fill_in_the_blanks(input_lst):
    # Write your code here
    last_value = input_lst[0]

    for i in range(len(input_lst)):

        if input_lst[i]:
            last_value = input_lst[i]

        else:
            input_lst[i] = last_value

    return input_lst

    # Testcase 1


input_lst_2 = [None, 8, None]
output_2 = fill_in_the_blanks(input_lst_2)
