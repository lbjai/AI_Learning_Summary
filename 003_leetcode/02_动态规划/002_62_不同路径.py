#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
思路:由于在每个位置只能向下或者向右， 所以每个坐标的路径和等于上一行相同位置和上一列相同位置不同路径的总和，
状态转移方程：f[i][j] = f[i - 1][j] + f[i][j - 1];
复杂度:时间复杂度O(mn)。空间复杂度O(mn)，优化后O(n)
"""
from pprint import pprint


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 制作棋盘
        flag = []
        for i in range(m):
            if i == 0:
                flag.append([1 for _ in range(n)])
            else:
                flag.append([1] + [i for i in range(n - 1)])
        # 找到状态方程
        for i in range(1, m):
            for j in range(1, n):
                flag[i][j] = flag[i - 1][j] + flag[i][j - 1]
        return flag[-1][-1]


s = Solution()
print(s.uniquePaths(m=3, n=2))
print(s.uniquePaths(m=3, n=7))
