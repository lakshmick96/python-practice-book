#The built-in function enumerate takes an iteratable and returns an iterator over pairs (index, value) for each value in the source.

def my_enumerate(l):
    x = range(len(l))
    return zip(x, l)




