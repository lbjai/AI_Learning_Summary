#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：

输入：nums = [], target = 0
输出：[-1,-1]
 

提示：
来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index_s = self.binary_search(nums, target)
        if index_s == -1:
            return [-1, -1]
        left, right = index_s, index_s
        # 向左边寻找
        while left - 1 >= 0 and nums[left - 1] == target: left -= 1
        # 向右边查找
        while right + 1 < len(nums) and nums[right + 1] == target: right += 1
        return [left, right]

    def binary_search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return -1

    def searchRange1(self, nums: List[int], target: int) -> List[int]:
        # 暴力求解方式1
        f1, f2 = -1, -1
        for index, num in enumerate(nums):
            if num == target:
                f2 = index
        if target in nums:
            f1 = nums.index(target)
        return [f1, f2]

    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        # 暴力求解方式2
        f1, f2 = -1, -1
        for index, num in enumerate(nums):
            # 获取第一个下标位置,规则就是
            if target - 1 < num <= target:
                f1 = index - 1
            # 获取最后一个下标位置
            if num == target:
                f2 = index

        return [f1, f2]

    def searchRange3(self, nums: List[int], target: int) -> List[int]:
        # 暴力求解方式3
        f1 = -1
        n_len = len(nums)
        for index in range(0, n_len, 1):
            # 获取第一个下标位置
            if nums[index] == target:
                f1 = index
                break
        # 获取第2个下标位置
        for i in range(f1 + 1, n_len, 1):
            if nums[i] == target:
                return [f1, i]
        return [f1, f1]


nums = [5, 6, 7, 9, 9, 11]
target = 9
s = Solution()
print(s.searchRange(nums, target))
