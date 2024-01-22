def reverse(num:int)->int:
    n = num
    reverse_number = 0

    while n>0:
        last_digit = n % 10
        reverse_number= (reverse_number * 10) + last_digit
        n=n//10

    print(f'reversed number of {num} is  : {reverse_number}' )

reverse(123)
reverse(1000)