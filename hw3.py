"""CS 61A Homework 3: Due online by 5pm on Friday, September 23.

This interval arithmetic example is based on Structure and Interpretation of
Computer Programs, Section 2.1.4:
http://mitpress.mit.edu/sicp/full_text/book/book_Z_H-14.html#%_sec_2.1.4

Alyssa P. Hacker is designing a system to help people solve engineering
problems. One feature she wants to provide in her system is the ability to
manipulate inexact quantities (such as measured parameters of physical devices)
with known precision, so that when computations are done with such approximate
quantities the results will be numbers of known precision.

Alyssa's idea is to implement interval arithmetic as a set of arithmetic
operations for combining "intervals" (objects that represent the range of
possible values of an inexact quantity). The result of adding, subracting,
multiplying, or dividing two intervals is itself an interval, representing the
range of the result.

Alyssa postulates the existence of an abstract object called an "interval" that
has two endpoints: a lower bound and an upper bound. She also presumes that,
given the endpoints of an interval, she can construct the interval using the
data constructor make_interval.   Using the constructor and selectors, she
defines the following operations.
"""

def str_interval(x):
    """Return a string representation of interval x.

    >>> str_interval(make_interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.

    >>> str_interval(add_interval(make_interval(-1, 2), make_interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return make_interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y.

    >>> str_interval(mul_interval(make_interval(-1, 2), make_interval(4, 8)))
    '-8 to 16'
    >>> str_interval(mul_interval(make_interval(4, 8), make_interval(-1, 2)))
    '-8 to 16'
    >>> str_interval(mul_interval(make_interval(-3, -1), make_interval(4, 8)))
    '-24 to -4'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return make_interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))



"""Alyssa's program is incomplete because she has not specified the
implementation of the interval abstraction. Define the constructor and selectors
in terms of two_element tuples.
"""

def make_interval(a, b):
    """Construct an interval from a to b."""
    return (a, b)

def lower_bound(x):
    """Return the lower bound of interval x."""
    return min(x)

def upper_bound(x):
    """Return the upper bound of interval x."""
    return max(x)

"""Alyssa implements division below, by multiplying by the reciprocal of y. Ben
Bitdiddle, an expert systems programmer, looks over Alyssa's shoulder and
comments that it is not clear what it means to divide by an interval that spans
zero. Add an assert statement to Alyssa's code to ensure that no such interval
is used as a divisor.
"""

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided
    by any value in y.

    Division is implemented as the multiplication of x by the reciprocal of y.

    >>> str_interval(div_interval(make_interval(-1, 2), make_interval(4, 8)))
    '-0.25 to 0.5'
    """
    assert lower_bound(y) and upper_bound(y), "Dividing by an interval containing zero"
    reciprocal_y = make_interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

"""Using reasoning analogous to Alyssa's, define a subtraction function for
intervals.  Add a doctest.
"""

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y.

    >>> str_interval(sub_interval(make_interval(-1, 2), make_interval(4, 8)))
    '-9 to -2'
    """
    # (4, 8) - (2, 3) = ((x1 - y2), (x2 - y1))
    lower = lower_bound(x) - upper_bound(y)
    upper = upper_bound(x) - lower_bound(y)
    return make_interval(lower, upper)

"""In passing, Ben also cryptically comments, "By testing the signs of the
endpoints of the intervals, it is possible to break mul_interval into nine
cases, only one of which requires more than two multiplications."  Write a
fast multiplication function using Ben's suggestion.  Add a doctest.
"""

def mul_interval_fast(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y, using as few multiplications as possible.

    >>> str_interval(mul_interval_fast(make_interval(-1, 2), make_interval(4, 8)))
    '-8 to 16'
    >>> str_interval(mul_interval_fast(make_interval(4, 8), make_interval(-1, 2)))
    '-8 to 16'
    >>> str_interval(mul_interval_fast(make_interval(4, 8), make_interval(0, 2)))
    '0 to 16'
    >>> str_interval(mul_interval_fast(make_interval(4, 8), make_interval(-3, -1)))
    '-24 to -4'
    >>> str_interval(mul_interval_fast(make_interval(-3, -1), make_interval(4, 8)))
    '-24 to -4'
    >>> str_interval(mul_interval_fast(make_interval(1, 2), make_interval(4, 5)))
    '4 to 10'
    >>> str_interval(mul_interval_fast(make_interval(-7, 2), make_interval(-4, 5)))
    '-35 to 28'
    """
    if lower_bound(x) >= 0 and upper_bound(x) >= 0:
        # [+ +] [+ +]
        if lower_bound(y) >= 0 and upper_bound(y) >= 0:
            lower = lower_bound(x) * lower_bound(y)
            upper = upper_bound(x) * upper_bound(y)

        # [+ +] [- +]
        elif lower_bound(y) < 0 and upper_bound(y) >= 0:
            lower = upper_bound(x) * lower_bound(y)
            upper = upper_bound(x) * upper_bound(y)

        # [+ +] [- -]
        elif lower_bound(y) < 0 and upper_bound(y) < 0:
            lower = upper_bound(x) * lower_bound(y)
            upper = lower_bound(x) * upper_bound(y)

    elif lower_bound(x) < 0 and upper_bound(x) < 0:
        # [- -] [+ +]
        if lower_bound(y) >= 0 and upper_bound(y) >= 0:
            lower = lower_bound(x) * upper_bound(y)
            upper = upper_bound(x) * lower_bound(y)

        # [- -] [- +]
        elif lower_bound(y) < 0 and upper_bound(y) >= 0:
            lower = lower_bound(x) * upper_bound(y)
            upper = lower_bound(x) * lower_bound(y)

        # [- -] [- -]
        elif lower_bound(y) < 0 and upper_bound(y) < 0:
            lower = upper_bound(x) * upper_bound(y)
            upper = lower_bound(x) * lower_bound(y)

    elif lower_bound(x) < 0 and upper_bound(x) >= 0:
        # [- +] [+ +]
        if lower_bound(y) >= 0 and upper_bound(y) >= 0:
            lower = lower_bound(x) * upper_bound(y)
            upper = upper_bound(x) * upper_bound(y)

        # [- +] [- -]
        elif lower_bound(y) < 0 and upper_bound(y) < 0:
            lower = upper_bound(x) * lower_bound(y)
            upper = lower_bound(x) * lower_bound(y)

        # [- +] [- +]
        elif lower_bound(y) < 0 and upper_bound(y) >= 0:
            lower = min(lower_bound(x) * upper_bound(y),
                        upper_bound(x) * lower_bound(y))
            upper = max(lower_bound(x) * lower_bound(y),
                        upper_bound(x) * upper_bound(x))

    return make_interval(lower, upper)


"""After debugging her program, Alyssa shows it to a potential user, who
complains that her program solves the wrong problem. He wants a program that can
deal with numbers represented as a center value and an additive tolerance; for
example, he wants to work with intervals such as 3.5 +/- 0.15 rather than 3.35
to 3.65. Alyssa returns to her desk and fixes this problem by supplying an
alternate constructor and alternate selectors in terms of the existing ones:
"""

def make_center_width(c, w):
    """Construct an interval from center and width."""
    return make_interval(c - w, c + w)

def center(x):
    """Return the center of interval x."""
    return (upper_bound(x) + lower_bound(x)) / 2

def width(x):
    """Return the width of interval x."""
    return (upper_bound(x) - lower_bound(x)) / 2

"""Unfortunately, most of Alyssa's users are engineers. Real engineering
situations usually involve measurements with only a small uncertainty, measured
as the ratio of the width of the interval to the midpoint of the interval.
Engineers usually specify percentage tolerances on the parameters of devices.

Define a constructor make_center_percent that takes a center and a percentage
tolerance and produces the desired interval. You must also define a selector
percent that produces the percentage tolerance for a given interval. The center
selector is the same as the one shown above.
"""

def make_center_percent(c, p):
    """Construct an interval from center and percentage tolerance.

    >>> str_interval(make_center_percent(2, 50))
    '1.0 to 3.0'
    >>> str_interval(make_center_percent(3, 50))
    '1.5 to 4.5'
    >>> str_interval(make_center_percent(5, 20))
    '4.0 to 6.0'
    """
    return make_center_width(c, (p/100)*c)


def percent(x):
    """Return the percentage tolerance of interval x.

    >>> percent(make_interval(1, 3))
    50.0
    >>> percent(make_interval(1, 11))
    83.33333333333334
    >>> percent(make_interval(4, 6))
    20.0
    """
    return 100 * (width(x) / center(x))


"""After considerable work, Alyssa P. Hacker delivers her finished system.
Several years later, after she has forgotten all about it, she gets a frenzied
call from an irate user, Lem E. Tweakit. It seems that Lem has noticed that the
formula for parallel resistors can be written in two algebraically equivalent
ways:

    (r1 * r2) / (r1 + r2)

    and

    1 / (1/r1 + 1/r2)

He has written the following two programs, each of which computes the
parallel_resistors formula differently:
"""

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = make_interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

"""Lem complains that Alyssa's program gives different answers for the two ways
of computing. This is a serious complaint.

Demonstrate that Lem is right. Investigate the behavior of the system on a
variety of arithmetic expressions. Make some intervals A and B, and use them in
computing the expressions A/A and A/B. You will get the most insight by using
intervals whose width is a small percentage of the center value.
"""

def test_one():
    """
    >>> a = make_center_percent(4, 0.4)
    >>> b = make_center_percent(2, 0.2)
    >>> div_interval(a, a)
    (0.9920318725099602, 1.0080321285140563)
    >>> div_interval(a, b)
    (1.9880239520958083, 2.012024048096192)

    >>> par1(a, b) != par2(a, b)
    True
    """
    pass

"""
Solution
--------

The test above shows that dividing an interval by itself does not result
to unity,it returns a value close to it.

Also, executing par1 and par2 with the same arguments does not result
to the same value. Hence, Lem's observation is right.
"""


"""Eva Lu Ator, another user, has also noticed the different intervals computed
by different but algebraically equivalent expressions. She says that the problem
is multiple references to the same interval.

The Multiple References Problem: a formula to compute with intervals using
Alyssa's system will produce tighter error bounds if it can be written in such a
form that no variable that represents an uncertain number is repeated.

Thus, she says, par2 is a better program for parallel resistances than par1. Is
she right? Why? Write an explanation as a string below.
"""

"""
Solution
-------
Yes, Eva is right.

Given that both formulas are algebraically equivalent, they can also be derived
from each other. par1 is a condensed form of par2

Deriving par1 from par2 involves multiplying through by r1r2
(i.e (1*r1r2) / ((1/r1)*r1r2 + (1/r2)*r1r2) ). This assumes that (1/r1)*r1r2
returns 1/r2 (i.e r1/r1 equals one, this is not the case as proved
previously -- dividing an interval by itself does not return unity), and that
(1/r2)*r1r2 also returns 1/r1.

This also follows Eva's analysis of reference to the same interval
(i.e r1/r1 equalling one)

par1 deviates from par2 because it requires divison which will
accumulate debt (introduce error?).
"""

"""Write a function quadratic that returns the interval of all values f(t) such
that t is in the argument interval x and

f(t) = a * t * t + b * t + c

Make sure that your implementation returns the smallest such interval, one that
does not suffer from the multiple references problem.

Hint: the derivative f'(t) = 2 * a * t + b, and so the extreme point of the
quadratic is -b/(2*a).
"""

def quadratic(x, a, b, c):
    """Return the interval that is the range the quadratic defined by a, b, and
    c, for domain interval x.

    >>> str_interval(quadratic(make_interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(make_interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"

"""Write three similar functions, each of which takes as an argument a sequence
of intervals and returns the sum of the square of each interval that does not
contain 0.

    1. Using a for statement containing an if statement.
    2. Using map and filter and reduce.
    3. Using generator expression and reduce.

Hint: Square is a special case of quadratic, but you can also use the simpler
square_interval function below for intervals that do not contain 0.
"""

def non_zero(x):
    """Return whether x contains 0."""
    return lower_bound(x) > 0 or upper_bound(x) < 0

def square_interval(x):
    """Return the interval that contains all squares of values in x, where x
    does not contain 0.
    """
    assert non_zero(x), 'square_interval is incorrect for x containing 0'
    return mul_interval(x, x)

# The first two of these intervals contain 0, but the third does not.
seq = (make_interval(-1, 2), make_center_width(-1, 2), make_center_percent(-1, 50))

zero = make_interval(0, 0)

def sum_nonzero_with_for(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using a for statement.

    >>> str_interval(sum_nonzero_with_for(seq))
    '0.25 to 2.25'
    """
    "*** YOUR CODE HERE ***"

from functools import reduce
def sum_nonzero_with_map_filter_reduce(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using using map, filter, and reduce.

    >>> str_interval(sum_nonzero_with_map_filter_reduce(seq))
    '0.25 to 2.25'
    """
    "*** YOUR CODE HERE ***"

def sum_nonzero_with_generator_reduce(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using using reduce and a generator expression.

    >>> str_interval(sum_nonzero_with_generator_reduce(seq))
    '0.25 to 2.25'
    """
    "*** YOUR CODE HERE ***"


"""Extra for experts: Write a function polynomial that takes an interval x and a
tuple of coefficients c, and returns the (possibly approximate) interval
containing all values of f(t) for t in interval x, where:

  f(t) = c[k-1] * pow(t, k-1) + c[k-2] * pow(t, k-2) + ... + c[0] * 1

Like quadratic, your polynomial function should return the smallest such
interval, one that does not suffer from the multiple references problem.

Hint: You can approximate this result. Consider using Newton's method.
"""

def polynomial(x, c):
    """Return the interval that is the range the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(make_interval(0, 2), (-1, 3, -2)))
    '-3 to 0.125'
    >>> str_interval(polynomial(make_interval(1, 3), (1, -3, 2)))
    '0 to 10'
    >>> r = polynomial(make_interval(0.5, 2.25), (10, 24, -6, -8, 3))
    >>> round(lower_bound(r), 5)
    18.0
    >>> round(upper_bound(r), 5)
    23.0
    """
    "*** YOUR CODE HERE ***"

