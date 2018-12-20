# https://leetcode-cn.com/explore/interview/card/bytedance/243/array-and-sorting/1019/
# https://leetcode.com/problems/longest-consecutive-sequence/solution/
#
# 最长连续序列
# 给定一个未排序的整数数组，找出最长连续序列的长度。
#
# 要求算法的时间复杂度为 O(n)。
#
# 示例:
#
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。


# the numbers are stored in a HashSet (or Set, in Python) to allow O(1) lookups, O(1) 的查找
# 我们只需要从那些"不是一个更长序列的开头"的数字开始来构建序列就可以了
# （也就是说用来构建序列的数字必须是序列的开头，最小的数字）
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_streak = 0
        num_set = set(nums)

        # HashSet(or Set, in Python) 有O(1)的查找时间复杂度
        # 如果不使用set集合的话，下面这两个打标注的地方都会是O(n)的时间复杂度
        # 算法的关键在于找到每个序列的头（序列中最小的数字），然后计算序列的长度
        # 如果num in num_set不是序列的头，则这个num不会被用来计算长度
        for num in num_set:
            if num - 1 not in num_set:   #:::::
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:   #:::::
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak





