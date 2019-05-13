# https://leetcode.com/problems/trapping-rain-water/
#
# 42. Trapping Rain Water
#
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.
#
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped.
# Thanks Marcos for contributing this image!
#
# Example:
#
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        volume_no_water = 0
        max_height = 0
        for h in height:
            volume_no_water += h
            max_height = max(max_height, h)

        volume_with_water = 0
        height_with_water = 0
        left_index = 0
        while height[left_index] < max_height:
            height_with_water = max(height_with_water, height[left_index])
            volume_with_water += height_with_water
            left_index += 1

        height_with_water = 0
        right_index = len(height) - 1
        while height[right_index] < max_height:
            height_with_water = max(height_with_water, height[right_index])
            volume_with_water += height_with_water
            right_index -= 1

        volume_with_water += max_height * (right_index - left_index + 1)
        return volume_with_water - volume_no_water