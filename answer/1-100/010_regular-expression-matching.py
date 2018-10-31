# https://leetcode-cn.com/problems/regular-expression-matching/description/
# https://leetcode.com/problems/regular-expression-matching/
#
# 给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。
#
# '.' 匹配任意单个字符。
# '*' 匹配零个或多个前面的元素。
# 匹配应该覆盖整个字符串 (s) ，而不是部分字符串。
#
# 说明:
#
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
# 示例 1:
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 示例 2:
#
# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: '*' 代表可匹配零个或多个前面的元素, 即可以匹配 'a' 。因此, 重复 'a' 一次, 字符串可变为 "aa"。
# 示例 3:
#
# 输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个('*')任意字符('.')。
# 示例 4:
#
# 输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 'c' 可以不被重复, 'a' 可以被重复一次。因此可以匹配字符串 "aab"。
# 示例 5:
#
# 输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memory = {}

        def dp(s_index, p_index):
            if (s_index, p_index) not in memory:
                if p_index == len(p):
                    ans = s_index == len(s)
                else:
                    first_match = (s_index < len(s)) and (p[p_index] in {s[s_index], '.'})
                    if p_index + 1 < len(p) and p[p_index + 1] == '*':
                        ans = dp(s_index, p_index + 2) or first_match and dp(s_index + 1, p_index)
                    else:
                        ans = first_match and dp(s_index + 1, p_index + 1)
                memory[s_index, p_index] = ans
            return memory[s_index, p_index]

        return dp(0, 0)



    def isMatch_recursive(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype: bool
        """
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return self.isMatch(text, pattern[2:]) or \
                   first_match and self.isMatch(text[1:], pattern)
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])




s = Solution()
print(s.isMatch('aa', 'a*'))

