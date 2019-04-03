# https://leetcode-cn.com/explore/interview/card/bytedance/246/dynamic-programming-or-greedy/1028/
# https://leetcode.com/problems/maximal-square/discuss/197525/Python-easy-to-understand-DP.
#
# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
#
# 示例:
#
# 输入:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# 输出: 4


# 动态规划 Dynamic Plan
# dp[i][j]表示所在正方形的长度，越到后面越大
# 最终在dp中，一个正方形可以表示成类似：
#
# 1 1 1 1
# 1 2 2 2
# 1 2 3 3
# 1 2 3 4
#
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        n, m, max_length = len(matrix), len(matrix[0]), 0
        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                elif matrix[i][j] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_length = max(max_length, dp[i][j])

        return max_length ** 2