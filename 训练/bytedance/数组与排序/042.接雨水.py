# https://leetcode-cn.com/explore/interview/card/bytedance/243/array-and-sorting/1047/
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。
#
# 示例:
#
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 思路
        # 在接雨水的容器中，一定存在最大高度，设left_index和right_index
        # 是最左和最右的、具有最大高度的柱子（可能是同一根柱子）
        #
        # 在接完雨水后，这个「水 + 容器」的形状一定是一个"梯形"或者"三角形"
        # 从 0 到left_index，高度（水+柱子）一定是从左向右上升
        # 从 n-1 到right_index，高度（水+柱子）一定是从右向左上升
        # 中间部分的高度一定是全部相同的，都是max_height
        #
        # 这样就可以算出 水 + 容器的体积
        # 然后减去容器本身
        if len(height) < 3:
            return 0

        max_height = 0
        volume_no_water = 0
        volume_with_water = 0

        for h in height:
            volume_no_water += h
            max_height = max(max_height, h)

        left_max_index = 0
        h_left = height[left_max_index]
        right_max_index = len(height) - 1
        h_right = height[right_max_index]

        while height[left_max_index] < max_height:
            h_left = max(h_left, height[left_max_index])
            volume_with_water += h_left
            left_max_index += 1

        while height[right_max_index] < max_height:
            h_right = max(h_right, height[right_max_index])
            volume_with_water += h_right
            right_max_index -= 1

        volume_with_water += max_height * (right_max_index - left_max_index + 1)
        return volume_with_water - volume_no_water