def first_ocr_substring(s:str, sub:str)->int:

    # length of substring must be less than actual string
    if len(sub) > len(s):
        return -1
    
    for i in range(len(s) - len(sub)+1):
        if s[i: i+len(sub)] == sub:
            return i
        
    return -1

print(first_ocr_substring('abcabcabbcbabca', 'abc'))
print(first_ocr_substring('caasscasda', 'abc'))
print(first_ocr_substring('', 'abc'))
print(first_ocr_substring('cdfaseabc', 'abc'))
