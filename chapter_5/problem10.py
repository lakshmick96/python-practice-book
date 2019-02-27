#implement a function izip that works like itertools.izip.

def izip(l, m):
    return iter(zip(l, m))

