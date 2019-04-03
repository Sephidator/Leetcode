# https://leetcode-cn.com/explore/interview/card/bytedance/243/array-and-sorting/1046/
# 给出一个区间的集合，请合并所有重叠的区间。
#
# 示例 1:
#
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2:
#
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

# Definition for an interval.


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # 把list按照start从小到大的顺序排好
        # 然后把前后项合并即可
        if not intervals:
            return []
        intervals.sort(key=lambda r: r.start)

        result = [intervals[0]]
        for v in intervals[1:]:
            if v.start <= result[-1].end:
                if v.end > result[-1].end:
                    result[-1].end = v.end
            else:
                result.append(v)
        return result

        # 我算法的思路是，对于result中原有的一个项old，和我新的一项new
        # 如果old和new发生重叠的场合，都会把old移除并且更改new的内容（将old和new合并）
        # 如果new = [2, 4]是old= [1, 5]的一部分，则不插入new，否则一般都会插入new
        # 不够优雅
        # result = []
        # for new in intervals:
        #     new_result = []
        #     need_to_append = True
        #
        #     while result:
        #         old = result.pop()
        #         if old.start <= new.start and new.end <= old.end:
        #             new_result.append(old)
        #             need_to_append = False
        #         elif new.start <= old.start and old.end <= new.end:
        #             continue
        #         elif old.start <= new.start <= old.end or old.start <= new.end <= old.end:
        #             new = Interval(min(old.start, new.start), max(old.end, new.end))
        #         else:
        #             new_result.append(old)
        #
        #     if need_to_append:
        #         new_result.append(new)
        #     result = new_result
        #
        # return result


s = Solution()
print(s.merge([Interval(2,3), Interval(4,7), Interval(3,4)]))
