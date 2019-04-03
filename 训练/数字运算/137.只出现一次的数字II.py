"""
137. 只出现一次的数字 II

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,3,2]
输出: 3
示例 2:

输入: [0,1,0,1,0,1,99]
输出: 99
"""
from typing import List

"""
实现一个数据结构来记录每一位上1的个数，当1的个数为3的时候清零
这个数据结构就是「one_digit, zero_digit」这个组合
两位数，每一位可以是1和0，于是可以表示4个结果0、1、2、3
137.只出现一次的数字I中，因为多出现的元素是出现2次，只需要一位，所以直接异或就可以，但是本题不行
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        one_digit = 0
        zero_digit = 0
        # one_digit, zero_digit表示了每一位有多少个1
        # 如果one_digit = 1, zero_digit = 0，那么就表示这一位上有2个1
        for num in nums:
            # 从第0位到第1位的进位
            carrier = zero_digit & num

            # 第0位加上新的数字后的结果
            zero_digit = zero_digit ^ num

            # 根据进位计算新的one_digit
            one_digit = one_digit ^ carrier

            # 如果某一位上one_digit和zero_digit都是1，那么其mask位就是0，否则就是1
            # 这意味着如果某一位上1的个数为3（one_digit = 1, zero_digit = 1）
            # 那么就要把这一位上的数字清零（用mask和zero_digit、one_digit进行与操作）
            mask = ~(one_digit & zero_digit)
            one_digit = one_digit & mask
            zero_digit = zero_digit & mask

        return zero_digit
