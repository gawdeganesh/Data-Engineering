def word_count(text: list[str]) -> dict:
    dict = {words: text.count(words) for words in text}

    return dict


list = ["hello", "hi", "hello", "hi", "zero", "five", "zero"]
print(word_count(list))
