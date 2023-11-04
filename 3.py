"""
Taxicab Distance
"""

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    return abs(street(a) - street(b)) + abs(avenue(a) - avenue(b))

"""
Flatten
"""

def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x # Ensure x is not mutated
    [1, [2, 3], 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> x
    [[1, [1, 1]], 1, [1, 1]]
    """
    flattened = []
    for item in lst:
        if type(item) is list:
            flattened += flatten(item)
        else:
            flattened += [item]
    return flattened

"""
Replace Leaf
"""

from tree import tree, print_tree, is_leaf, label, branches

def copy_tree(t):
    return t

def replace_leaf(t, old, new):
    """Returns a new tree where every leaf value equal to old has
    been replaced with new.

    >>> yggdrasil = tree('odin',
    ...                  [tree('balder',
    ...                        [tree('thor'),
    ...                         tree('freya')]),
    ...                   tree('frigg',
    ...                        [tree('thor')]),
    ...                   tree('thor',
    ...                        [tree('sif'),
    ...                         tree('thor')]),
    ...                   tree('thor')])
    >>> laerad = copy_tree(yggdrasil) # copy yggdrasil for testing purposes
    >>> print_tree(replace_leaf(yggdrasil, 'thor', 'freya'))
     odin
      balder
       freya
       freya
      frigg
       freya
      thor
       sif
       freya
      freya
    >>> laerad == yggdrasil # Make sure original tree is unmodified
    True
    """
    if is_leaf(t):
        if label(t) == old:
            return tree(new)
        return t

    lst = []
    for branch in branches(t):
        lst += [replace_leaf(branch, old, new)]

    return tree(label(t), lst)

"""
Mobiles
"""

def mobile(left, right):
    """Construct a mobile from a left side and a right side."""
    assert is_side(left), "left must be a side"
    assert is_side(right), "right must be a side"
    return ['mobile', left, right]

def is_mobile(m):
    """Return whether m is a mobile."""
    return type(m) == list and len(m) == 3 and m[0] == 'mobile'

def left(m):
    """Select the left side of a mobile."""
    assert is_mobile(m), "must call left on a mobile"
    return m[1]

def right(m):
    """Select the right side of a mobile."""
    assert is_mobile(m), "must call right on a mobile"
    return m[2]

def side(length, mobile_or_weight):
    """Construct a side: a length of rod with a mobile or weight at the end."""
    assert is_mobile(mobile_or_weight) or is_weight(mobile_or_weight)
    return ['side', length, mobile_or_weight]

def is_side(s):
    """Return whether s is a side."""
    return type(s) == list and len(s) == 3 and s[0] == 'side'

def length(s):
    """Select the length of a side."""
    assert is_side(s), "must call length on a side"
    return s[1]

def end(s):
    """Select the mobile or weight hanging at the end of a side."""
    assert is_side(s), "must call end on a side"
    return s[2]

def weight(size):
    """Construct a weight of some size."""
    assert size > 0
    return ['weight', size]

def size(w):
    """Select the size of a weight."""
    assert is_weight(w), 'must call size on a weight'
    return w[1]

def is_weight(w):
    """Whether w is a weight."""
    return type(w) == list and len(w) == 2 and w[0] == 'weight'

"""
Total weight of a mobile
"""

def total_weight(m):
    """
    >>> w1 = weight(3)
    >>> w2 = weight(2)
    >>> t = mobile(side(2, w1), side(4, w2))
    >>> v = mobile(side(5, w2), side(5, w1))
    >>> total_weight(mobile(side(3, w1), side(4, v)))
    8
    >>> total_weight(mobile(side(6, w2), side(4, t)))
    7
    >>> total_weight(mobile(side(2, t), side(1, v)))
    10
    """
    if is_weight(m):
        return size(m)

    return total_weight(end(left(m))) + total_weight(end(right(m)))

"""
Balanced

A mobile is balanced if two conditions are met:

i) The torque applied by its left side is equal to that applied by its right side.
Torque of the left side is the length of the left rod multiplied by the total
weight hanging from that rod. Likewise for the right.

ii) Each of the mobiles hanging at the end of its sides is balanced.
"""

def balanced(m):
    """Return whether m is balanced.

    >>> s = mobile(side(2, weight(3)), side(4, weight(2)))
    >>> balanced(s)
    False
    >>> t = mobile(side(2, weight(3)), side(2, weight(3)))
    >>> balanced(t)
    True
    >>> u = mobile(side(10, weight(2)), side(4, s))
    >>> balanced(u)
    False
    >>> v = mobile(side(5, weight(4)), side(10, weight(2)))
    >>> balanced(v)
    True
    >>> w = mobile(side(3, t), side(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(side(1, v), side(1, w)))
    False
    >>> balanced(mobile(side(1, w), side(1, v)))
    False
    """

    if is_weight(m):
        return True

    left_side = left(m)
    right_side = right(m)

    end_left_side = end(left_side)
    end_right_side = end(right_side)

    left_torque = length(left_side) * total_weight(end_left_side)
    right_torque = length(right_side) * total_weight(end_right_side)

    return (balanced(end_left_side) == balanced(end_right_side)) \
            and (left_torque == right_torque)

"""
Totals
"""

def totals_tree(m):
    """Return a tree representing the mobile with its total weight at the root.

    >>> totals_tree(weight(3))
    [3]
    >>> s = mobile(side(2, weight(3)), side(4, weight(2)))
    >>> totals_tree(s)
    [5, [3], [2]]
    >>> u = mobile(side(10, weight(2)), side(4, s))
    >>> totals_tree(u)
    [7, [2], [5, [3], [2]]]
    >>> v = mobile(side(5, weight(4)), side(10, weight(2)))
    >>> totals_tree(v)
    [6, [4], [2]]
    >>> x = mobile(side(1, weight(2)), side(1, weight(1)))
    >>> print_tree(totals_tree(x))
     3
      2
      1
    >>> y = mobile(side(2, weight(1)), side(2, s))
    >>> print_tree(totals_tree(y))
     6
      1
      5
       3
       2
    >>> print_tree(totals_tree(mobile(side(2, x), side(3, y))))
     9
      3
       2
       1
      6
       1
       5
        3
        2
    """
    if is_weight(m):
        return tree(size(m))

    lst = []
    for side in [end(left(m)), end(right(m))]:
        lst = lst + [totals_tree(side)]

    return tree(total_weight(m), lst)
