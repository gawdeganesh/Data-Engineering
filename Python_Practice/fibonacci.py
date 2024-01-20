def fibonacci(n):
    fib_series = [0, 1]  # Starting with the first two numbers of the series

    if n <= 1:
        return fib_series[:n + 1]

    while len(fib_series) <= n:
        next_number = fib_series[-1] + fib_series[-2]  # Sum of the last two numbers
        fib_series.append(next_number)

    return fib_series

# Example usage
num_terms = 10  # Change this value to generate more or fewer terms
fibonacci_series = fibonacci(num_terms)

print(f"Fibonacci series up to {num_terms} terms:")
print(fibonacci_series)
