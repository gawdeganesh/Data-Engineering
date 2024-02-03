def compressed_string(input_string: str) -> str:

    if not input_string.isalpha():
        return "the string does not contain all characters"

    cnt_char = 1
    previous_char = input_string[0]
    compressed_list = []

    for i in range(1, len(input_string)):
        if input_string[i] == previous_char:
            cnt_char += 1
        else:
            compressed_list.append(previous_char + str(cnt_char))
            previous_char = input_string[i]
            cnt_char = 1

    # to add the last character
    compressed_list.append(previous_char + str(cnt_char))

    compressed_string = "".join(compressed_list)

    return (
        compressed_string
        if len(compressed_string) < len(input_string)
        else input_string
    )


print(compressed_string("asadsddadffas"))
print(compressed_string("12112332"))
print(compressed_string("wwwwwwdasdAABBssdsfeqq"))
print(compressed_string(""))
