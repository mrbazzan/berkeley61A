def fact(n):
    """Find factorial of a number.

    >>> fact(5)
    120
    >>> fact(4)
    24
    >>> fact(3)
    6
    """
    if n == 0:
        return 1
    return n * fact(n-1)

def num_sevens(n):
    """Returns the number of times 7 appears as a digit of n.

    >>> num_sevens(3)
    0
    >>> num_sevens(7)
    1
    >>> num_sevens(7777777)
    7
    >>> num_sevens(2637)
    1
    >>> num_sevens(76370)
    2
    >>> num_sevens(12345)
    0
    """
    if n == 0:
        return 0
    elif n % 10 == 7:
        return 1 + num_sevens(n // 10)
    else:
        return num_sevens(n // 10)
