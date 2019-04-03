# https://leetcode-cn.com/explore/interview/card/tencent/227/hui-su-suan-fa/935/
#
# 括号生成
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]



class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []

        def generate(string: str, left_parenthesis_num: int):
            right_parenthesis_num = len(string) - left_parenthesis_num
            if left_parenthesis_num is n:
                self.result.append(string + ')' * (n - right_parenthesis_num))
            else:
                generate(string + '(', left_parenthesis_num + 1)
                if left_parenthesis_num > right_parenthesis_num:
                    generate(string + ')', left_parenthesis_num)

        generate('', 0)
        return self.result
