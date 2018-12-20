# https://leetcode-cn.com/explore/interview/card/bytedance/246/dynamic-programming-or-greedy/1042/
#
# 买卖股票的最佳时机
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
#
# 注意你不能在买入股票前卖出股票。
#
# 示例 1:
#
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
# 示例 2:
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # max必然是「最高点 - 最低点」
        # 当出现比现有最低点还低的点的时候，有可能出现比现有的max更长的新的max，要重新求max
        # 如果不是上述情况，则只是现有的max不断变大而已
        if len(prices) <= 1:
            return 0

        max_profit = 0
        low = prices[0]
        high = prices[0]

        for p in prices:
            if p < low:
                low = p
                high = p
            elif p > high:
                high = p
                max_profit = max(max_profit, high - low)

        return max_profit
