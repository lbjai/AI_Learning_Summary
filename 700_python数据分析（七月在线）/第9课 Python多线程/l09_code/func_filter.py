def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

def my_filter(func, array):
    ret = []
    for i in array:
        if func(i):
            ret.append(i)
    return ret
    
print(my_filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))