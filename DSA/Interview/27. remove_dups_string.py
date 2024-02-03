def remove_duplicates(input_string: str) -> str:

    if not input_string:
        return "-1"

    seen = set()
    unique_str = ""

    for char in input_string:
        if char not in seen:
            seen.add(char)
            unique_str += char
    return unique_str


print(remove_duplicates("asadsddadffas"))
print(remove_duplicates("12112332"))
print(remove_duplicates("sdas,,,@@@,esAssfas5##+"))
print(remove_duplicates(""))

# Method 2 : Use a dictionary and then check the keys when value is 1
