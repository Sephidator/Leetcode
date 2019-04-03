"""
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

示例 :

输入: [1,2,1,3,2,5]
输出: [3,5]
注意：

结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
"""
from functools import reduce
from operator import xor
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # https://blog.csdn.net/qq_17550379/article/details/83929138
        # mask = reduce(lambda x, y: x ^ y, nums)
        mask = reduce(xor, nums)
        mask &= -mask
        result = [0, 0]
        for num in nums:
            if num ^ mask:
                result[0] ^= num
            else:
                result ^= num
        return result
