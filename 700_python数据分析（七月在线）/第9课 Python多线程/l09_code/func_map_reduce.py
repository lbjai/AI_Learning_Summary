# map sample

a = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * x, a)))

from functools import reduce

def add(x, y):
    return x + y
print(reduce(add, [1, 3, 5, 7, 9]))