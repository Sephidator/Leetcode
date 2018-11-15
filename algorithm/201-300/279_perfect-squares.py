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
                    # i是逐渐减小的
                    # 对于result == 1的情况，只可能会是 i * i == number
                    # 而这种情况只会出现在第一次扫描i（i最大）的情况下，之后所有的情况都有result>=2
                    # 所以当检测到result<=2的情况就可以返回了
                    # （如果第一次是1，直接可以返回，之后的结果必定>=2，所以result==2也可以返回了）
                    if result <= 2:
                        break
                    # 根据观察结果发现，最终的result<=4必然成立
                    # 于是，如果i^2是完全平方数之一，必定存在j>=i，使得j^2也是完全平方数
                    # 而因为j比i大，所以j^2是完全平方数的情况已经被考虑过了
                    # 因为result<=4，所以不会存在i^2是最大的完全平方数的可能
                    # （和不够大，或者4 * i^2 = number的情况下(2*i)^2 = number）
                    elif 4*i*i <= number:
                        break
                record[number] = result
                return result

        return perfect_square(n)


s = Solution()
for i in range(1, 1000):
    print('i = ' + str(i) + ', ' + str(s.numSquares(i)))
