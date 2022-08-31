#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。

示例 1:
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]

示例 2:
输入: nums = [0]
输出: [0]
 
提示:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

进阶：你能尽量减少完成的操作次数吗？

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/move-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        一次遍历
        时间复杂度: O(n)
        空间复杂度: O(1)
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            # 当前第i个元素不等于0，就换到左边；等于0就换到右边
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1

    def moveZeroes_v1(self, nums: List[int]) -> None:
        """
        两次遍历
        时间复杂度: O(n)
        空间复杂度: O(1)
        Do not return anything, modify nums in-place instead.
        """
        # 记录非零的个数
        left = 0
        n_nums = len(nums)
        for index, num in enumerate(nums):
            if nums[index] != 0:
                nums[left] = nums[index]
                left += 1
        for i in range(left, n_nums):
            nums[i] = 0

    def moveZeroes_v2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums = sorted(nums, key=bool, reverse=True)


nums = [0, 1, 0, 3, 12]
s = Solution()
s.moveZeroes_v2(nums=nums)
