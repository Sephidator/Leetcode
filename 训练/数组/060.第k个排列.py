# https://leetcode-cn.com/explore/interview/card/bytedance/243/array-and-sorting/1021/
#
# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 给定 n 和 k，返回第 k 个排列。
#
# 说明：
#
# 给定 n 的范围是 [1, 9]。
# 给定 k 的范围是[1,  n!]。
# 示例 1:
#
# 输入: n = 3, k = 3
# 输出: "213"
# 示例 2:
#
# 输入: n = 4, k = 9
# 输出: "2314"
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def ceil_division(dividend, divisor):
            return dividend // divisor + (dividend % divisor > 0)

        def ceil_mod(dividend, divisor):
            res = dividend % divisor
            return divisor if res == 0 else res

        num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        factorial_record = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        result = ''

        for index in range(n - 1, 0, -1):
            digit = ceil_division(k, factorial_record[index])
            result += str(num_list[digit - 1])
            num_list.pop(digit - 1)
            k = ceil_mod(k, factorial_record[index])

        result += str(num_list[0])
        return result


s = Solution()
print(s.getPermutation(4, 9))

print(23 // 6 + (23 % 5 > 0))
