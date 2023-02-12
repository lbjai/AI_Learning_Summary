def print_line():
    """打印一条横线"""
    print("-"*50)


def print_lines(num):
    """打印 num 条横线"""
    i = 0
    while i < num:
        print_line()
        i += 1

print_lines(5)
