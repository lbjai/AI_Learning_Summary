#!/user/bin/env python3
# -*- coding: utf-8 -*-

def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


print(bubble_sort([4, 5, 3, 6, 2, 7, 1, 8]))
