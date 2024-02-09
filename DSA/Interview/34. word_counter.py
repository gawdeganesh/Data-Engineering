def word_counter(text: list[str]) -> dict:
    if not text:
        return {}

    word_counter = {}

    for char in text:
        if char in word_counter:
            word_counter[char] += 1
        else:
            word_counter[char] = 1
    return word_counter


print(word_counter(["hi", "helllo", "hello", "123", "hi", "12"]))
print(word_counter(["hi"]))
