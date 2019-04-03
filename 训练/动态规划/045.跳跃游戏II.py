"""
https://leetcode-cn.com/problems/jump-game-ii/

45. 跳跃游戏 II

给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。

"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # if not nums:
        #     return False
        #
        # min_jump = 0
        # index = 0
        #
        # while index < len(nums):
        #     if index + nums[index] >= len(nums) - 1:
        #         if index is len(nums) - 1:
        #             return min_jump
        #         else:
        #             return min_jump + 1
        #
        #     farthest_next = 0
        #     for i in range(index + 1, index + 1 + nums[index]):
        #         if i + nums[i] > farthest_next:
        #             farthest_next = i + nums[i]
        #             index = i
        #     min_jump += 1
        #
        # return min_jump

        cur_max, count, length, next_max = 0, 0, len(nums), nums[0]

        if length <= 1:
            return 0

        for i in range(length):
            next_max = max(next_max, i + nums[i])

            if i == cur_max:
                cur_max = next_max
                count += 1
            if cur_max >= length - 1:
                return count

        return -1


s = Solution()
print(s.jump([2, 3, 1, 1, 4]))
