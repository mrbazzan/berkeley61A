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

from operator import add, sub

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    op = add
    count, index = 0, 0
    while index < n:
        count = op(count, 1)

        if ((index+1) % 7 == 0) or num_sevens(index+1) > 0:
            op = sub if op is add else add

        index += 1

    return count
