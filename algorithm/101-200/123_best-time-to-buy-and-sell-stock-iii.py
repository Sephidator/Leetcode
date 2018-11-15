# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/description/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39611/Is-it-Best-Solution-with-O(n)-O(1).
#
# 123. 买卖股票的最佳时机 III
#
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
#
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
# 示例 1:
#
# 输入: [3,3,5,0,0,3,1,4]
# 输出: 6
# 解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
#      随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
# 示例 2:
#
# 输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
#      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
# 示例 3:
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hold1 = -10000000000000000
        hold2 = -10000000000000000
        release1 = 0
        release2 = 0
        for p in prices:  # Assume we only have 0 money at first
            release2 = max(release2, hold2 + p)  # The maximum if we've just sold 2nd stock so far.
            hold2 = max(hold2, release1 - p)     # The maximum if we've just buy  2nd stock so far.
            release1 = max(release1, hold1 + p)  # The maximum if we've just sold 1nd stock so far.
            hold1 = max(hold1, - p)              # The maximum if we've just buy  1st stock so far.
        return release2  # Since release1 is initiated as 0, so release2 will always higher than release1


s = Solution()
print(s.maxProfit([2, 1, 4, 5, 2, 9, 7]))
