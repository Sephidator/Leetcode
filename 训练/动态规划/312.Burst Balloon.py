"""
Given n balloons, indexed from 0 to n-1.
Each balloon is painted with a number on it represented by array nums.
You are asked to burst all the balloons.
If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins.
Here left and right are adjacent indices of i.
After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

"""
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 神奇的递归，显然会超时
        if len(nums) is 0:
            return 0
        elif len(nums) is 1:
            return nums[0]
        elif len(nums) is 2:
            min_num, max_num = sorted(nums)
            return min_num * max_num + max_num
        else:
            result = 0
            for i in range(1, len(nums) - 1):
                shoot_result = nums[i-1] * nums[i] * nums[i+1] + self.maxCoins(nums[:i] + nums[i+1:])
                if shoot_result > result:
                    result = shoot_result
            if nums[0] * nums[1] + self.maxCoins(nums[1:]) > result:
                result = nums[0] * nums[1] + self.maxCoins(nums[1:])
            if nums[-1] * nums[-2] + self.maxCoins(nums[:-1]) > result:
                result = nums[-1] * nums[-2] + self.maxCoins(nums[:-1])
            return result


s = Solution()
print(s.maxCoins([3, 2, 5, 4]))
