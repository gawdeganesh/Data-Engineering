def longest_substring(text: list[str]) -> str:
    if not text:
        return "substring cannot be possible"
    if len(text) == 1:
        return list[0]

    smallest_length = min(len(ele) for ele in list)
    prefix = ""

    for i in range(smallest_length):
        current_char = text[0][i]
        match = True

        for ele in text:
            if current_char != ele[i]:
                match = False
                return prefix

        prefix += current_char

    if match:
        return prefix


list = ["flower", "flow", "flight"]

print(f"longest substring: ", longest_substring(list))
