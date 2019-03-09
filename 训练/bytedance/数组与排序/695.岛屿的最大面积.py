# https://leetcode-cn.com/explore/interview/card/bytedance/243/array-and-sorting/1034/
# 岛屿的最大面积
# 给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。
#
# 找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)
#
# 示例 1:
#
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。
#
# 示例 2:
#
# [[0,0,0,0,0,0,0,0]]
# 对于上面这个给定的矩阵, 返回 0。
#
# 注意: 给定的矩阵grid 的长度和宽度都不超过 50。


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        m = len(grid)
        n = len(grid[0])

        def count_island_area(i, j):
            grid[i][j] = -1
            count = 1
            if i > 0 and grid[i - 1][j] == 1:
                count += count_island_area(i - 1, j)
            if i < m - 1 and grid[i + 1][j] == 1:
                count += count_island_area(i + 1, j)
            if j > 0 and grid[i][j - 1] == 1:
                count += count_island_area(i, j - 1)
            if j < n - 1 and grid[i][j + 1] == 1:
                count += count_island_area(i, j + 1)
            return count

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 1:
                    island_area = count_island_area(row, column)
                    max_area = max(max_area, island_area)

        return max_area


s = Solution()
print(s.maxAreaOfIsland([
    [1, 1],
    [1, 0],
]))
