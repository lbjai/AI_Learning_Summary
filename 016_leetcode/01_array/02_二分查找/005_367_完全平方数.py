#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。

进阶：不要 使用任何内置的库函数，如  sqrt 。
示例 1：
输入：num = 16
输出：true

示例 2：
输入：num = 14
输出：false

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/valid-perfect-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        ans = -1
        while left <= right:
            middle = (left + right) // 2
            if middle * middle <= num:
                ans = middle
                left = middle + 1
            else:
                right = middle - 1
        return int(ans * ans) == num

num = 16
s = Solution()
print(s.isPerfectSquare(num))
