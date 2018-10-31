"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # name = nums[i], value = i
        # 注意key值是nums里面的数字，而value值是索引，而不是相反
        dictionary = {}
        for i in range(len(nums)):
            num_j = target - nums[i]
            if num_j in dictionary:  # key in dict, return true of false
                return [dictionary[num_j], i]
            dictionary[nums[i]] = i


s = Solution()
nums = [2, 7, 11, 15]
target = 9
print(s.twoSum(nums, target))
