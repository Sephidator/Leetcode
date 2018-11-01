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
