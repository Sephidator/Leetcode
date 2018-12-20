# https://leetcode-cn.com/explore/interview/card/bytedance/246/dynamic-programming-or-greedy/1029/
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 进阶:
#
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 看看分治法吧
        # 我看了下自己的笔记，然后估摸着写出来了
        # 但是我不想写注释了
        if not nums:
            return 0

        max_sum = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            res = res + nums[i] if res > 0 else nums[i]
            max_sum = res if res > max_sum else max_sum

        return max_sum


        # def recursive_get_max(end_index):
        #     if end_index == 0:
        #         return nums[0], nums[0]
        #     else:
        #         res_before, max_sum_before = recursive_get_max(end_index - 1)
        #         res = res_before + nums[end_index] if res_before > 0 else nums[end_index]
        #         max_sum = max(max_sum_before, res)
        #         return res, max_sum
        #
        # result, max_sum_value = recursive_get_max(len(nums) - 1)
        # return max_sum_value


s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))