"""Submission for 61A Homework 2.

Name:
Login:
Collaborators:
"""
from operator import add, mul, sub

square = lambda x: x * x
identity = lambda x: x
triple = lambda x: 3 * x
increment = lambda x: x + 1

def summation(n, term):
    """Return the sum of the first n terms in a sequence.

    term -- a function that takes one argument
    >>> summation(5, lambda x: x)
    15
    >>> summation(10, lambda x: x)
    55
    >>> summation(100, lambda x: x)
    5050
    >>> summation(5, lambda x: x + 1)
    20
    """

    total, k = 0, 1
    while k <= n:
        total = total + term(k)
        k = k + 1
    return total


# Q1
def product(n, term):
    """Return the product of the first n terms in a sequence.

    term -- a function that takes one argument
    >>> product(3, lambda x: x*x)
    36
    >>> product(2, lambda x: x*x*x)
    8
    """

    total, i = 1, 1
    while i <= n:
        total = total * term(i)
        i = i + 1
    return total

def factorial(n):
    """Return n factorial by calling product.

    >>> factorial(4)
    24
    """
    def identity(x):
        return x

    return product(n, identity)

# Q2
def accumulate(combiner, start, n, term):
    """Return the result of combining the first n terms in a sequence.

    combiner -- a function that takes two arguments. It defines how
                the current term is combined with the previous total.

    start -- base value for starting the accumulation.

    n -- the number of terms of the sequence.

    term -- a function that takes one argument. It defines the value at
            each term.

    >>> accumulate(mul, 2, 3, lambda x: x*x)
    72
    """

    total, i = start, 1
    while i <= n:
        total = combiner(total, term(i))
        i = i + 1
    return total

def summation_using_accumulate(n, term):
    """An implementation of summation using accumulate.

    >>> summation_using_accumulate(100, lambda x: x)
    5050
    >>> summation_using_accumulate(5, lambda x: x)
    15
    >>> summation_using_accumulate(10, lambda x: x)
    55
    """
    return accumulate(add, 0, n, term)

def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, lambda x: x)
    24
    >>> product_using_accumulate(5, lambda x: x)
    120
    >>> product_using_accumulate(3, lambda x: x*x)
    36
    """
    return accumulate(mul, 1, n, term)



# Q3
def double(f):
    """Return a function that applies f twice.

    f -- a function that takes one argument

    >>> double(lambda x: x + 1)(3)
    5
    """
    def inner(x):
        return f(f(x))
    return inner


# Q4
def repeated(f, n):
    """Return the function that computes the nth application of f.

    f -- a function that takes one argument
    n -- a positive integer

    >>> repeated(square, 2)(5)  # square(square(5))
    625
    >>> repeated(square, 1)(5)
    25
    >>> repeated(square, 0)(5)
    5
    >>> repeated(lambda x: x + 1, 3)(5)  # 1 + 1 + 1 + 5
    8
    >>> repeated(lambda x: 3*x, 5)(1)  # 3 * 3 * 3 * 3 * 3 * 1
    243

    """

    def inner(num):
        count = n
        while count > 0:
            num = f(num)
            count = count - 1
        return num
    return inner

def square(x):
    """Return x squared."""
    return x * x

def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h
