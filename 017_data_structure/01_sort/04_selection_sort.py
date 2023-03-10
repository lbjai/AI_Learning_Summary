#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""
首先在未排序序列中找到最小元素，存放到排序序列的起始位置，
然后再从剩余未排序元素中继续寻找最小元素，然后放到已排序序列的末尾
"""


def selection_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


print(selection_sort(nums=[5, 4, 6, 3, 7, 2, 8, 1, 9]))
