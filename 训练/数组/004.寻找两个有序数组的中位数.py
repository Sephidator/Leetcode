"""
https://leetcode-cn.com/problems/median-of-two-sorted-arrays/

给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        m = len(A)
        n = len(B)

        # 做出如上的设置，使得m = len(A), n = len(B), m <= n
        # 使用imin和imax是为了取得log(m)的时间复杂度
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i

            # A[i] 太小，必须调整i使得B[j - 1] <= A[i]
            # 增大i，j就会相应减小，有可能满足B[j-1] <= A[i]
            # 相反，减小i的话，j会增大，B[j-1] <= A[i]更加不可能满足
            if i < m and B[j - 1] > A[i]:
                imin = i + 1

            # A[i - 1]太大，必须减小i使得 A[i-1] <= B[j]
            # 和上一步相反的，缩小imax
            elif i > 0 and A[i - 1] > B[j]:
                imax = i - 1

            else:
                if i is 0:
                    max_of_left = B[j - 1]
                elif j is 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                # (m + n)为单数的场合，m + n + 1是双数，可以背2整除
                # 我们要找的是第 (m + n - 1) // 2 + 1 个数
                # 也就是第 (m + n + 1) // 2 = (i + j) 个数
                # 这个数前面有 (i + j - 1)个数
                # 这个数字就是max_of_left
                if (m + n) % 2 is 1:
                    return max_of_left

                # m + n 为双数，那么max_of_left和min_of_right的平均数就是我们要求的数
                if i is m:
                    min_of_right = B[j]
                elif j is n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2


