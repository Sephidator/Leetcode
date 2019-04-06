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
        if not nums:
            return 0

        """
        matrix[left][right]用来保存left～right的能够达到的最高点数
        left和right两个边界不能打，也就是说 left == right 或者 left + 1 == right时
        matrix[left][right] = 0
        nums是分值列表，只剩一个气球的时候分数乘1，为了方便讨论，添加左右两个假的1
        """
        n = len(nums)
        matrix = [[0] * (n + 2) for _ in range(n + 2)]
        nums = [1] + nums + [1]

        """
        https://www.cnblogs.com/grandyang/p/5006441.html
        对于本题，显然有如下状态转移方程（递归就是这个思路）：
        matrix[left][right] = matrix[left][k] + nums[left] * nums[k] * nums[right] + matrix[k][right]
        (left < k < right)
        
        最大的难点在于区间的遍历顺序。
        一般来说，我们遍历所有子区间的顺序都是i从0到n，然后j从i到n，然后得到的 [i, j] 就是子区间。
        但是这道题用这种遍历顺序就不对，
        在前面的分析中已经说了，我们需要先更新完所有的小区间，然后才能去更新大区间，
        而用这种一般的遍历子区间的顺序，会在更新完所有小区间之前就更新了大区间，从而不一定能算出正确的dp值，
        比如拿题目中的那个例子 [3, 1, 5, 8] 来说，一般的遍历顺序是：
            [3] -> [3, 1] -> [3, 1, 5] -> [3, 1, 5, 8] -> [1] -> [1, 5] -> [1, 5, 8] -> [5] -> [5, 8] -> [8] 
        显然不是我们需要的遍历顺序，正确的顺序应该是先遍历完所有长度为1的区间，再是长度为2的区间，再依次累加长度，直到最后才遍历整个区间：
            [3] -> [1] -> [5] -> [8] -> [3, 1] -> [1, 5] -> [5, 8] -> [3, 1, 5] -> [1, 5, 8] -> [3, 1, 5, 8]
        
        对于每个长度x，我们要遍历n-x次，每次又会讨论x次k和tmp
        所以时间复杂度为：
        sigma((n - x) * x) = sigma(x) * n - sigma(x^2) = n^2(n+1)/2 - n(n+1)(2n+1)/6 = O(n^3)   1 <= x <= n
        """
        for length in range(1, n + 1):
            for left in range(0, n - length + 1):
                right = left + length + 1
                for k in range(left + 1, right):
                    tmp = matrix[left][k] + nums[left] * nums[k] * nums[right] + matrix[k][right]
                    matrix[left][right] = max(matrix[left][right], tmp)

        return matrix[0][n + 1]

        # # 神奇的递归，显然会超时
        # if len(nums) is 0:
        #     return 0
        # elif len(nums) is 1:
        #     return nums[0]
        # elif len(nums) is 2:
        #     min_num, max_num = sorted(nums)
        #     return min_num * max_num + max_num
        # else:
        #     result = 0
        #     for i in range(1, len(nums) - 1):
        #         shoot_result = nums[i-1] * nums[i] * nums[i+1] + self.maxCoins(nums[:i] + nums[i+1:])
        #         if shoot_result > result:
        #             result = shoot_result
        #     if nums[0] * nums[1] + self.maxCoins(nums[1:]) > result:
        #         result = nums[0] * nums[1] + self.maxCoins(nums[1:])
        #     if nums[-1] * nums[-2] + self.maxCoins(nums[:-1]) > result:
        #         result = nums[-1] * nums[-2] + self.maxCoins(nums[:-1])
        #     return result


s = Solution()
print(s.maxCoins([3, 1, 5, 8]))
