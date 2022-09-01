#!/user/bin/env python3
# -*- coding: utf-8 -*-
import random
"""
快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为两个子序列（sub-lists）。
"""

# 快速排序通过分治法和递归原理来实现，分治法的主要作用是把一个序列分成两个序列，
# 等递归到底部时，数列的大小是1，也就排序好了

def quick_sort(nums):
    """
    ① 从数列中挑出一个元素，称为 “基准”（pivot），
    ② 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
        在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
    ③ 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
    :param nums:
    :return:
    """
    if len(nums) <= 1:
        return nums
    index = random.randint(0, len(nums) - 1)
    value = nums.pop(index)
    left = [i for i in nums if i < value]
    right = [i for i in nums if i >= value]
    return quick_sort(left) + [value] + quick_sort(right)


print(quick_sort([4, 5, 6, 3, 7, 7, 8, 1, 9]))
