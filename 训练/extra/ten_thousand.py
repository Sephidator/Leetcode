"""
有1、5、10、20、50、100
有多少种组合得到10000元

https://www.zhihu.com/question/315108379
"""


class Solution:
    def ten_thousand(self):
        money_list = [1, 5, 10, 20, 50, 100]
        amount = 10000

        result = [money_list[0]] * (amount + 1)

        for money in money_list[1::]:
            for j in range(money, len(result)):
                result[j] += result[j - money]
        return result[amount]


s = Solution()
print(s.ten_thousand())
