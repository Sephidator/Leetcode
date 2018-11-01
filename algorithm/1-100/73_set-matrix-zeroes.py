# 73. 矩阵置零
#
# https://leetcode-cn.com/problems/set-matrix-zeroes/description/
# https://leetcode.com/problems/set-matrix-zeroes/
# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
#
# 示例 1:
#
# 输入:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# 输出:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# 示例 2:
#
# 输入:
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# 输出:
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
# 进阶:
#
# 一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个常数空间的解决方案吗？


class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row_num = len(matrix)
        column_num = len(matrix[0])
        is_col = False

        # ri = row_index, ci = column_index
        for ri in range(row_num):
            if matrix[ri][0] == 0:
                is_col = True
            for ci in range(1, column_num):
                if matrix[ri][ci] == 0:
                    matrix[ri][0] = 0
                    matrix[0][ci] = 0

        for ci in range(1, column_num):
            for ri in range(1, row_num):
                if matrix[ri][0] == 0 or matrix[0][ci] == 0:
                    matrix[ri][ci] = 0

        if matrix[0][0] == 0:
            for ci in range(column_num):
                matrix[0][ci] = 0

        if is_col:
            for ri in range(row_num):
                matrix[ri][0] = 0

        print(matrix)


s = Solution()
s.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
