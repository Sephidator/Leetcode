"""
https://leetcode-cn.com/explore/interview/card/tencent/221/array-and-strings/913/

螺旋矩阵 II
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0] * n for _ in range(n)]

        def go(x, y, number, direction):
            result[y][x] = number
            if direction is "right":
                if x + 1 is n or result[y][x+1] is not 0:
                    return x, y + 1, "down"
                else:
                    return x + 1, y, "right"
            elif direction is 'down':
                if y + 1 is n or result[y+1][x] is not 0:
                    return x - 1, y, "left"
                else:
                    return x, y + 1, "down"
            elif direction is 'left':
                if x is 0 or result[y][x-1] is not 0:
                    return x, y - 1, "up"
                else:
                    return x - 1, y, "left"
            elif direction is 'up':
                if y is 0 or result[y-1][x] is not 0:
                    return x + 1, y, "right"
                else:
                    return x, y - 1, "up"

        x = 0
        y = 0
        direction = "right"
        for i in range(1, n**2 + 1):
            x, y, direction = go(x, y, i, direction)

        return result


s = Solution()
print(s.generateMatrix(4))
