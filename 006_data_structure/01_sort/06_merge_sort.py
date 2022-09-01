#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""
归并排序是用分治思想，分治模式在每一层递归上有三个步骤：

分解（Divide）：将n个元素分成个含n//2个元素的子序列。
解决（Conquer）：用合并排序法对两个子序列递归的排序。
合并（Combine）：合并两个已排序的子序列已得到排序结果。
"""


def merge(left, right):
    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    res += left
    res += right
    return res


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


print(merge_sort([5, 4, 2, 1, 6, 9, 8, 7, 3]))
# 排序分析
# 分割1 [5, 4, 2, 1, 6], [9, 8, 7, 3]
# 分割2 [5, 4, 2], [1, 6], [9, 8] [7, 3]
# 分割3 [5],[4,2],[1],[6],[9],[8],[7],[3]
# 分割4 [5],[4],[2],[1],[6],[9],[8],[7],[3]
# 合并1  [5],[2,4],[1,6],  [8,9],[3,7]
# 合并2  [2,4,5],[1,6],    [8,9],[3,7]
# 合并3  [1,2,4,5,6],      [3,7,8,9]
# 合并4  [1,2,3,4,5,6,7,8,9]
