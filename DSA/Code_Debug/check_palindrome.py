def check_palindrome(num:int)->bool:
    n = num
    reverse_number = 0

    while n>0:
        last_digit = n % 10
        reverse_number= (reverse_number * 10) + last_digit
        n=n//10

    return num==reverse_number

print(check_palindrome(1221))
print(check_palindrome(9854))
print(check_palindrome(91))
print(check_palindrome(123454321))