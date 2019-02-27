# Write a function tree_reverse to reverse elements of a nested-list recursively.

def tree_reverse(l):
    result = []
    for i in l[::-1]:
        if isinstance(i, list):
            result.append(tree_reverse(i))
        else:
            result.append(i)
    return result


