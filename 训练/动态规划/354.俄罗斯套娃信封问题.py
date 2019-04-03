# https://leetcode-cn.com/explore/interview/card/bytedance/246/dynamic-programming-or-greedy/1031/
#
# 俄罗斯套娃信封问题
# 给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
#
# 请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
#
# 说明:
# 不允许旋转信封。
#
# 示例:
#
# 输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# 输出: 3
# 解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。


class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        from bisect import bisect_left
        r = []
        for env in sorted(envelopes, key=lambda x: (x[0], -x[1])):
            pos = bisect_left(r, env[1])
            if pos == len(r):
                r.append(env[1])
            elif env[1] < r[pos]:
                r[pos] = env[1]
        return len(r)

        # 算法正确，但是TOE
        # 淦，我跟一个人的java实现的算法一样，但是我跑不过
        #
        # if len(envelopes) <= 1:
        #     return len(envelopes)
        #
        # e_list = sorted(envelopes)
        # max_depth = [1] * len(e_list)
        # max_result = 1
        #
        # for i in range(1, len(e_list)):
        #     envelope = e_list[i]
        #     for i_before in range(0, i):
        #         envelope_before = e_list[i_before]
        #         if envelope[0] > envelope_before[0] and envelope[1] > envelope_before[1]:
        #             if max_depth[i_before] + 1 > max_depth[i]:
        #                 max_depth[i] = max_depth[i_before] + 1
        #     if max_depth[i] > max_result:
        #         max_result = max_depth[i]
        #
        # return max_result


s = Solution()
print(sorted([[2, 3], [2, 4], [1, 3]]))
print({23, 4})