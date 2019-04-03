"""

https://leetcode-cn.com/explore/interview/card/tencent/221/array-and-strings/903/

给定n个非负整数a1，a2，...，an，每个数代表坐标中的一个点(i, ai) 。
在坐标内画n条垂直线，垂直线i 的两个端点分别为(i, ai) 和(i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

图中垂直线代表输入数组[1, 8, 6, 2, 5, 4, 8, 3, 7]。
在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例:
输入: [1, 8, 6, 2, 5, 4, 8, 3, 7] 输出: 49

"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        解答：https://zhuanlan.zhihu.com/p/40616691
        """
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = (right - left) * min(height[right], height[left])
            if area > max_area:
                max_area = area
            if height[left] <= height[right]:
                left += 1
            else:
                right -=1
        return max_area
