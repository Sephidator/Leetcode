# https://leetcode-cn.com/explore/interview/card/tencent/226/dynamic-programming/937/
# 子集
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for i in range(2 ** len(nums)):
            subset = []
            num = i
            index = 0
            while num > 0:
                if num & 1:
                    subset.append(nums[index])
                index += 1
                num = num >> 1
            result.append(subset)
        return result

s = Solution()
print(s.subsets([1, 2, 3]))