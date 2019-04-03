"""
55. 跳跃游戏

https://leetcode-cn.com/problems/jump-game/

给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # 我的写法是，对于某一个点，查找他能跳到的"能达到最远位置的点"
        # 然后跳转到这个点之后重复同样操作...
        # 算法正确，但是不够简洁

        # if not nums:
        #     return False
        #
        # index = 0
        #
        # while index < len(nums):
        #     if index + nums[index] >= len(nums) - 1:
        #         return True
        #     elif nums[index] is 0:
        #         return False
        #
        #     farthest_next = 0
        #     for i in range(index + 1, index + 1 + nums[index]):
        #         if i + nums[i] > farthest_next:
        #             farthest_next = i + nums[i]
        #             index = i
        # return False

        # 这个方法是，far保存能够到达的最远的点的索引
        # 如果某个点更新这个值之后，发现far小于等于自己（虽然实际上只有等于一种情况）
        # 这就说明，无法再向前进了，如果这个点不是最后一个点，就反悔false
        far = 0
        for k, v in enumerate(nums):
            far = max(far, k + v)
            if far <= k != len(nums) - 1:
                return False
        return True


s = Solution()
print(s.canJump([3,2,1,0,4]))
