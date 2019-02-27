# Write a function peep, that takes an iterator as argument and returns the first element and an equivalant iterator.

def peep(it):
    x = it.next()
    y = list(it)
    y.insert(x, 0)
    return x, y

it = iter(range(5))
x, it1 = peep(it)
print x, list(it1)

