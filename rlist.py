
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

"""
Local State
"""
def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return "Insufficient funds"
        balance = balance - amount
        return balance
    return withdraw

wd = make_withdraw(100)

"""
Mutable Recursive List
"""

def make_mutable_rlist():
    contents = empty_rlist
    def dispatch(message, value=None):
        nonlocal contents
        if message == "len":
            return get_length(contents)
        elif message == "get":
            return get_item(contents, value)
        elif message == "add_top":
            contents = make_rlist(value, contents)
        elif message == "pop_top":
            top = first(contents)
            contents = rest(contents)
            return top
        elif message == "str":
            print(contents)

    return dispatch

def example():
    m_list = make_mutable_rlist()
    m_list("add_top", 1)
    m_list("add_top", 3)
    m_list("add_top", 8)

    m_list("str")

    print(m_list("len"))
    print(m_list("get", 2))

    print(m_list("pop_top"))

    m_list("str")


"""
Functional Implementation of a Dictionary
"""

def make_dict():
    records = []

    def getitem(key):
        for k, v in records:
            if k == key:
                return v
    def setitem(key, value):
        for record in records:
            if record[0] == key:
                record[1] = value
                return
        records.append([key, value])

    def dispatch(message, key=None, value=None):
        if message == 'setitem':
            return setitem(key, value)
        elif message == 'getitem':
            return getitem(key)
        elif message == 'keys':
            return tuple(k for k, _ in records)
        elif message == 'values':
            return tuple(v for _, v in records)
    return dispatch

def dict_example():
    d = make_dict()
    d('setitem', 3, 9)
    d('setitem', 4, 16)
    print(d('getitem', 3))
    print(d('keys'))
    print(d('values'))
