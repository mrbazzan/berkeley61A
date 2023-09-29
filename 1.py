
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

# 3) Show that `with_if_function` doesn't work the same way as
#    `with_if_statement`

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value,
       and false_result otherwise.
    """

    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

num = 0

def c():
    return False

def t():
    global num
    num = 1

def f():
    return num

# 
print(with_if_statement())

# All expressions are evaluated before passed to the formal parameter
print(with_if_function())

