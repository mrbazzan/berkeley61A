
square = lambda x: x*x

def logarithm(a, base=2):
     return find_root(lambda x: pow(base, x) - a)

def approx_eq(x, y, delta=1e-5):
    return abs(x - y) < delta

def approx_derivative(f, x, delta=1e-5):
    df = f(x + delta) - f(x)
    return df/delta

def newton_update(f):
    def update(x):
        return x - f(x) / approx_derivative(f, x)
    return update

def iter_improve(update, test, guess):
    while not test(guess):
        guess = update(guess)
    return guess

def find_root(f, initial_guess=10):
    def test(x):
        return approx_eq(f(x), 0)
    return iter_improve(newton_update(f), test, initial_guess)
 
def square_root(a):
    """
    >>> square_root(16)
    4.000000000026422
    """
    return find_root(lambda x: square(x) - a)