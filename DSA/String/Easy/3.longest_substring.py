def longest_substring(text: list[str]) -> str:
    if len(text)==0: return ''

    text = sorted(text)

    result = ''

    for ch in text[0]:
        if text[-1].startswith(result+ch):
            result+=ch
        else:
            break
    
    return result



list = ["flower", "flow", "flight"]

print(f"longest substring: ", longest_substring(list))
