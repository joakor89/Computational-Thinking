# Let's calculate a factorial

def factorial(n):
    """ Calculate factorial of n.

    n int > 0
    returns n!

    """
    print(n)
    if n == 1:
        return 1

    return n * factorial(n - 1)


n = int(input('Write up an integer: '))

print(factorial(n))
