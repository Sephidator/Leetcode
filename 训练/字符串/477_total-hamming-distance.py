# https://leetcode-cn.com/problems/total-hamming-distance/description/
#
#
# 477. 汉明距离总和
#
# 两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。
#
# 计算一个数组中，任意两个数之间汉明距离的总和。
#
# 示例:
#
# 输入: 4, 14, 2
#
# 输出: 6
#
# 解释: 在二进制表示中，4表示为0100，14表示为1110，2表示为0010。（这样表示是为了体现后四位之间关系）
# 所以答案为：
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
# 注意:
#
# 数组中元素的范围为从 0到 10^9。
# 数组的长度不超过 10^4。


class Solution:
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # log_2(10^9) = 29.9
        def binary(number):
            bin_num = bin(number)[2:]
            return (30-len(bin_num))*'0' + bin_num

        def hamming_in_digit(one_num, nums_len):
            zero_num = nums_len - one_num
            return int((nums_len*(nums_len-1) - one_num*(one_num-1) - zero_num*(zero_num-1)) / 2)

        dic = {}
        for i in range(0, 30):
            dic[i] = 0

        for num in nums:
            for i, digit in enumerate(binary(num)):
                dic[i] = dic[i] + int(digit)

        hamming_distance = 0
        for i in range(0, 30):
            hamming_distance = hamming_distance + hamming_in_digit(dic[i], len(nums))

        return hamming_distance


s = Solution()
print(s.totalHammingDistance([]))
