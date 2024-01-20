def camel_to_snake(word: str) -> str:
    new_word = ""

    for i in range(len(word)):
        if word[i].isupper():
            new_word = new_word + "_"
        new_word = new_word + word[i]

    return new_word


word = "camelToSnakeProgram"
print(f"original word : {word} and the snake case is", camel_to_snake(word))
a = int(input("Enter a number"))