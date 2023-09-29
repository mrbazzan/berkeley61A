
# 1) add a to the absolute value of b, without calling **abs**

from operator import add, sub, mul

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(1, -1)
    2
    >>> a_plus_abs_b(-1, 1)
    0
    >>> a_plus_abs_b(-1, -1)
    0
    >>> a_plus_abs_b(0, 0)
    0
    """

    if b < 0 :
        op = sub
    else:
        op = add

    return op(a, b)


# 2) Function that takes 3 positive numbers and returns the sum of
#    squares of the two larger numbers. Use a single expression for the body
#    of the function

def sum_of_squares_of_two_larger_numbers(a, b, c):
    """
    Return sum of squares of the two larger numbers between a, b and c.

    >>> sum_of_squares_of_two_larger_numbers(1, 2, 3)
    13
    >>> sum_of_squares_of_two_larger_numbers(3, 2, 4)
    25
    >>> sum_of_squares_of_two_larger_numbers(5, 4, 3)
    41
    >>> sum_of_squares_of_two_larger_numbers(3, 3, 3)
    18
    """
    return pow(max(a,b,c), 2) + pow(min(max(a,b),max(a,c),max(b,c)), 2)
