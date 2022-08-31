#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

 

示例 1：

输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]
示例 2：

输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]
 

提示：

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 已按 非递减顺序 排序


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/squares-of-a-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        复杂度分析

        时间复杂度：O(n)O(n)，其中 nn 是数组 \textit{nums}nums 的长度。
        空间复杂度：O(1)O(1)。除了存储答案的数组以外，我们只需要维护常量空间。
        :param nums:
        :return: 
        """
        n = len(nums)
        ans = [-1] * n
        i, j, pos = 0, n - 1, n - 1
        while i <= j:
            i2 = nums[i]*nums[i]
            j2 = nums[j]*nums[j]
            if i2 > j2:
                ans[pos] = i2
                i += 1
            else:
                ans[pos] = j2
                j -= 1
            pos -= 1
        return ans

    def sortedSquares_v1(self, nums: List[int]) -> List[int]:
        return sorted(list(map(lambda x: x * x, nums)))


nums = [-4, -1, 0, 3, 10]
s = Solution()
print(s.sortedSquares(nums))
"""
def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j, k = 0, n-1, n-1
        ans = [-1] * n
        while i <= j:
            lm = nums[i] * nums[i]
            rm = nums[j] * nums[j]
            if lm > rm:
                ans[k] = lm
                i += 1
            else:
                ans[k] = rm
                j -= 1
            k -= 1
        return ans
"""
