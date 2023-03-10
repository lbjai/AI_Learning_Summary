#!/user/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + ((right - left) // 2)
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1

    def search1(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        return -1


nums = [-1, 0, 3, 5, 9]
target = 9
s = Solution()
print(s.search(nums, target))
