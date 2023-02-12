
def pow1(n,i):
    """
    幂运算
    :param n: 底数
    :param i: 幂数
    :return:
    """
    if i > 1:
        res = n*pow(n,i-1)
        # i -= 1
        return res
    else:
        res = n
        return res


# print(pow1(2, 3))

def hui_wen(s):
    """
    判断指定字符串是否是回文
    先检查第一个和最后一个，一致则看剩余部分，不一致则不是
    参数：
        s ：指定字符串
    :return:
    """
    if len(s) < 2:
        # 字符串的长度小于2则一定是回文
        return True
    elif s[0] != s[-1]:
        return False
    # 递归条件
    return hui_wen(s[1:-1])




# s = "12345654321"
s = 'abc'
print(hui_wen(s))