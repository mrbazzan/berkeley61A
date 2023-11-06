
"""
Recursive List function definition
"""

empty_rlist = None

def make_rlist(first, rest):
    return first, rest

def first(s):
    return s[0]

def rest(s):
    return s[1]

def get_length(rlist):
    count = 0
    while rlist != empty_rlist:
        rlist = rest(rlist)
        count += 1
    return count

def get_item(rlist, index):
    assert index < get_length(rlist), "rlist out of range"
    while index > 0:
        rlist = rest(rlist)
        index -= 1
    return first(rlist)

rlist = make_rlist(1, make_rlist(3, make_rlist(5, make_rlist(4, empty_rlist))))
