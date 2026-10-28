
def fibonacci_iterative(n):
    series = []
    a, b = 0, 1
    additions = 0

    for i in range(n):
        series.append(a)

        if i < n - 1:
            a, b = b, a + b
            additions += 1

    return series, additions


def fibonacci_recursive(n, calls):
    calls[0] += 1

    if n <= 1:
        return n

    return (fibonacci_recursive(n - 1, calls)
            + fibonacci_recursive(n - 2, calls))


# Main program
n = int(input("Enter the number of terms: "))

if n < 0:
    print("Please enter a non-negative integer.")
else:
    series, additions = fibonacci_iterative(n)

    calls = [0]
    if n == 0:
        last_term = None
    else:
        last_term = fibonacci_recursive(n - 1, calls)

    print("Fibonacci series:", series)
    print("Addition count:", additions)
    print("Recursive call count:", calls[0])
    print("Last Fibonacci term:", last_term)
