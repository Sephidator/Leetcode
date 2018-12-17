# https://leetcode-cn.com/explore/interview/card/bytedance/242/string/1012/
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        sub_str = ''

        for index, char in enumerate(s):
            if char in sub_str:
                # i是sub_str中没有char的"尾巴"的开始字符串
                # find方法会查找某个字符在字符串中第一次出现的index
                # 但是因为只要char在sub_str中就会触发，所以sub_str中不会出现重复的字符
                #
                # 注意：陈俊达使用了一个list[128]来保存各个字符"之前所在的index"
                # 也就是说，可以用静态的数据结构来保存位置，而不是用find动态查找

                max_len = max(max_len, len(sub_str))
                i = sub_str.find(char) + 1
                sub_str = sub_str[i:len(sub_str)] + char
            else:
                sub_str = sub_str + char

        max_len = max(max_len, len(sub_str))
        return max_len


s = Solution()
print(s.lengthOfLongestSubstring('dvddsadsaffdsfaddsdfsf'))
