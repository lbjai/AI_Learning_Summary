#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(n + 1):
            if i == 0:
                dp[0] = 0
            elif i == 1:
                dp[1] = 1
            elif i == 2:
                dp[2] = 2
            else:
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def climbStairs_v2(self, n: int) -> int:
        p = 0
        q = 0
        r = 1
        for i in range(1, n + 1):
            q = p  # 记录上一次p的值
            p = r  # 记录上一次r的值
            r = p + q  # 记录本次的值
        return r

    def climbStairs_v1(self, n: int) -> int:
        """
        递归超出时间限制
        :param n:
        :return:
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs_v1(n - 2) + self.climbStairs_v1(n - 1)

s =Solution()
print(s.climbStairs(n=3))
