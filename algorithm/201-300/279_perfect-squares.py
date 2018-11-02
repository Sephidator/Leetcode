# 279. 完全平方数
# https://leetcode-cn.com/problems/perfect-squares/description/
#
# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
#
# 示例 1:
# 输入: n = 12
# 输出: 3
# 解释: 12 = 4 + 4 + 4.
#
# 示例 2:
# 输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9.


class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import sqrt
        record = {}

        def perfect_square(number):
            if number in record:
                return record[number]
            elif number == 0:
                return 0
            else:
                result = 10000
                i = int(sqrt(number))
                while i >= 1:
                    result = min(result, 1 + perfect_square(number - i*i))
                    i = i - 1
                    if result <= 2:
                        break
                    elif 4*i*i <= number:  # 奇技淫巧，观察知道最终结果不会大于4，所以有这一句...
                        break
                record[number] = result
                return result

        return perfect_square(n)


s = Solution()
for i in range(1, 1000):
    print('i = ' + str(i) + ', ' + str(s.numSquares(i)))
