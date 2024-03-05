def fibonacci(num: int):
    # initialize first two numbers
    series = [0, 1]

    if num <= 2:
        return series[:num]
    else:
        while len(series) < num:
            sum_of_last_two_elements = series[-1] + series[-2]
            series.append(sum_of_last_two_elements)

    return series


# print(fibonacci(10))
print(fibonacci(2))
