#Write a function permute to compute all possible permutations of elements of a given list.

import itertools
def permute(data):
    return list(itertools.permutations(data))

print permute([1,2,3,4])

