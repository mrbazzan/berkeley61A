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


t = tree(3, [tree(1),
             tree(2, [tree(1),
                      tree(1)])])
print(t)
print(label(t))
print(branches(t))
print(count_nodes(t))
