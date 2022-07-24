class Solution:
    def twoSum1(self, nums, target):
        num = len(nums)
        for index, ele in enumerate(nums):
            for next in range(index + 1, num, 1):
                if nums[index] + nums[next] == target:
                    return [index, next]

    def twoSum2(self, nums, target):
        for index, ele in enumerate(nums):
            if target - ele in nums[index + 1:]:
                return [index, nums.index(target - ele, index + 1)]
        else:
            # 如果没有该分支，则执行耗时568ms，有该分支执行时间为440ms
            return []

    def twoSum(self, nums, target):
        # 执行耗时28ms
        hashmap = dict()
        for index, num in enumerate(nums):
            if target-num in hashmap:
                return [hashmap[target-num],index]
            hashmap[num] = index




nums = [3, 2, 4]
target = 6
result = Solution().twoSum(nums, target)
print(result)

nums = [2, 7, 11, 15]
target = 9
result = Solution().twoSum(nums, target)
print(result)

nums = [3, 3]
target = 6
result = Solution().twoSum(nums, target)
print(result)
