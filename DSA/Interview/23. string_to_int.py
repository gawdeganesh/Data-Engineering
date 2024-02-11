def str_to_int(s: str) -> int:
    # remove the extra spaces
    s = s.strip()

    if not s:
        return 0

    sign = -1 if s[0] == "-" else 1

    # string without a sign
    if s[0] in ("-", "+"):
        s = s[1:]

    result = 0

    for char in s:
        if char.isdigit():
            result = result * 10 + int(char)
            if sign == 1 and result > 0x7FFFFFFF:  # handling overflow
                return 0x7FFFFFFF
            if sign == -1 and result > 0x8000000:  # handling negative overflow
                return -0x8000000
        else:
            return -1

    return sign * result


print(f"the string to int value of '1234' is {str_to_int('1234')}")
print(f"the string to int value of '-34634' is {str_to_int('-34634')}")
print(f"the string to int value of '1hi234' is {str_to_int('1hi234')}")
print(f"the string to int value of '3456 d asas ' is {str_to_int('3456')}")
print(f"the string to int value of ' 1234 ' is {str_to_int(' 1234 ')}")
print(f"the string to int value of ' ' is {str_to_int(' ')}")
print(
    f"the string to int value of '12345464564575676575' is {str_to_int('12345464564575676575')}"
)
