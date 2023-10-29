"""
Tree Abstract Implementation
"""

def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)

    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False

    for t in branches(tree):
        if not is_tree(t):
            return False

    return True

def is_leaf(tree):
    return not branches(tree)

def count_nodes(tree):
    total = 1
    if is_leaf(tree):
        return 1
    for branch in branches(tree):
        total = total + count_nodes(branch)
    return total

def collect_leaves(tree):
    if is_leaf(tree):
        return tree
    total = []
    for branch in branches(tree):
        total = total + collect_leaves(branch)
    return total

    # list comprehension
    # total = [collect_leaves(b) for b in branches(tree)]
    # return sum(total, start=tree if is_leaf(tree) else [])

def str_tree(tree, indent=0):
    t = str(label(tree))
    for b in branches(tree):
        t += "\n" + " " * indent + str_tree(b, indent*2)
    return t

def print_tree(tree, indent=0):
    if is_leaf(tree):
        print(" "*indent, label(tree))
        return

    print(" "*indent, label(tree))
    for b in branches(tree):
        print_tree(b, indent+1)

def print_calls(name, fn):
    def inner(tree):
        print("function name: ", name)
        print_tree(tree)
        input()
        ret = fn(tree)
        print("Returned: ", ret)
        return ret
    return inner

collect_leaves = print_calls('collect_leaves', collect_leaves)


t = tree(3, [tree(1),
             tree(2, [tree(1),
                      tree(1)])])
print(t)
print(label(t))
print(branches(t))
print(count_nodes(t))
print(collect_leaves(t))
print(str_tree(t, 1))
print_tree(t)
