def isValid(input: str) -> bool:
    bracket_hash_map = {")": "(", "]": "[", "}": "{"}  # use closing brackets as keys

    stack = []

    for char in input:
        if char in bracket_hash_map.values():
            stack.append(char)
        elif char in bracket_hash_map:
            if (
                stack and stack[-1] == bracket_hash_map[char]
            ):  # if we use opening brackets as keys, difficult to get the keys to match
                stack.pop()
            else:
                return False
        else:  # anything onther than those brackets
            continue
    return len(stack) == 0


# Example usage:
print(isValid("()"))  # True
print(isValid("(2+3141)[cdsads]x{x}"))  # True
print(isValid("(]"))  # False
print(isValid("([)]"))  # False
print(isValid("{[]}}"))  # True
