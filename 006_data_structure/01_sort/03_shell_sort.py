#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""
希尔排序的实质就是分组插入排序
先将整个待排元素序列分割成若干个子序列（由相隔某个“增量”的元素组成的）分别进行直接插入排序，
然后依次缩减增量再进行排序，待整个序列中的元素基本有序（增量足够小）时，再对全体元素进行一次直接插入排序。
因为直接插入排序在元素基本有序的情况下（接近最好情况），效率是很高的，因此希尔排序在时间效率上比前两种方法有较大提高。
"""


def shell_sort(nums):
    """
    ① 先取一个小于n的整数step作为第一个增量，把文件的全部记录分成step个组。
    ② 所有距离为step的倍数的记录放在同一个组中，在各组内进行直接插入排序。
    ③ 取第二个增量d2小于d1重复上述的分组和排序，直至所取的增量dt=1(dt小于dt-l小于…小于d2小于d1)，
    即所有记录放在同一组中进行直接插入排序为止。
    :param nums:
    :return:
    """
    step = len(nums) // 2
    while step >= 1:
        for i in range(step, len(nums)):
            cur = i
            while nums[cur - step] > nums[cur] and cur - step >= 0:
                nums[cur], nums[cur - step] = nums[cur - step], nums[cur]
                cur -= 1
        step //= 2
    return nums


print(shell_sort([4, 5, 3, 6, 7, 2, 1, 8]))
