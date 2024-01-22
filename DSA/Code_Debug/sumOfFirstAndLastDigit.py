def sumOfFirstAndLast(num:int)->int:
    last_digit  = num%10
    first_digit = num// (10**(len(str(num))-1))

    sum = last_digit+ first_digit

    print(f'the sum of the first and last digit of {num} is {sum}')


sumOfFirstAndLast(1234)
sumOfFirstAndLast(91)
sumOfFirstAndLast(124)
sumOfFirstAndLast(999293)