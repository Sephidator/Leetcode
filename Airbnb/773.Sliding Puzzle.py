# https://leetcode.com/problems/sliding-puzzle/
import collections
from typing import List


class Solution:
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        goal = '123450'
        start = self.board2str(board)

        bfs = collections.deque()
        bfs.append((start, 0))
        visited = set()
        visited.add(start)

        # 使用广度优先搜索
        # 这就像一个不断扩大的圆，step较少的情况永远被先访问到
        # 也就是说第一次匹配goal成功的时候，一定是所有可能匹配中最少step数的
        while bfs:
            shape, step = bfs.popleft()
            if shape == goal:
                return step

            zero_index = shape.index('0')
            x, y = zero_index // 3, zero_index % 3

            moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for (mx, my) in moves:
                nx, ny = x + mx, y + my
                if nx < 0 or nx >= 2 or ny < 0 or ny >= 3:
                    continue

                new_shape = self.swap(shape, x, y, nx, ny)
                if new_shape not in visited:
                    bfs.append((new_shape, step + 1))
                    visited.add(new_shape)
        return -1


    def swap(self, shape, x, y, nx, ny) -> str:
        shape_list = list(shape)
        shape_list[x * 3 + y], shape_list[nx * 3 + ny] = shape_list[nx * 3 + ny], shape_list[x * 3 + y]
        return "".join(shape_list)


    def board2str(self, board):
        bstr = ""
        for i in range(2):
            for j in range(3):
                bstr += str(board[i][j])
        return bstr


s = Solution()
print(s.slidingPuzzle([[1,2,3],[4,0,5]]))
