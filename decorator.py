
def check_range(x, y):
    def wrapped(fn):
        def wrap(param):
            soln = fn(param)
            if (soln >= x) and (soln <= y):
                print(f"Integer is between {x} and {y}")
            else:
                print(f"Integer is not between {x} and {y}")
        return wrap
    return wrapped

@check_range(1,10)
def triple(x):
    return 3 * x

triple(17)

# check_range(1, 10)(triple)(2)
# >> wrapped(fn=triple)(2)
# >> wrap(fn=triple)(x=2)
# >> triple(2)

# check_range(1, 10)(triple(2))(2)
# >> wrapped(fn=triple(x:triple=2))(x:wrap=2)
# >> wrapped(fn=6)(x:wrap=2)
# >> wrap(fn=6)(x=2)
# >> 6(2)
