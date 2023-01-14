# Let's calculate fibonacci number
def fibonacci(n):
    """ Calculate fibonacci's recursion
    n int > 0 
    returns n!
    """
    print(n)
    if n == 0 or n == 1:
        return 1
    print(n)

    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input('Write up an integer: '))
print(f'Fibonacci number for {n} is {fibonacci(n)}')