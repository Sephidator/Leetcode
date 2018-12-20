# https://leetcode-cn.com/explore/interview/card/bytedance/246/dynamic-programming-or-greedy/1030/
#
# 三角形最小路径和
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
#
# 例如，给定三角形：
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
#
# 说明：
#
# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # 动态规划 + 原地算法
        # 比深搜 + 保存高到不知道哪里去
        if not triangle:
            return 0
        elif len(triangle) == 1:
            return triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(i + 1):
                if j == 0:
                    triangle[i][j] += triangle[i-1][0]
                elif j == i:
                    triangle[i][j] += triangle[i-1][i-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[-1])

        # max_depth = len(triangle) - 1
        # record = {}
        #
        # def min_total(i, j):
        #     if i == max_depth:
        #         return triangle[i][j]
        #     elif (i, j) in record.keys():
        #         result = record[i, j]
        #         record.pop((i, j))
        #         return result
        #     else:
        #         result = triangle[i][j] + min(min_total(i+1, j), min_total(i+1, j+1))
        #         record[i, j] = result
        #         return result
        #
        # return min_total(0, 0)


s = Solution()
print(s.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))
