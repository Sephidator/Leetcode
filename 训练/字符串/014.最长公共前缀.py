# https://leetcode-cn.com/explore/interview/card/bytedance/242/string/1014/
#
# 最长公共前缀
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
#
# 所有输入只包含小写字母 a-z 。


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        try:
            for i in range(len(strs[0])):
                char = strs[0][i]
                for string in strs:
                    if char is not string[i]:
                        return prefix
                prefix = prefix + char
        except IndexError:
            return prefix
        else:
            return prefix

        # if len(strs) == 0:
        #     return ""
        #
        # prefix = strs[0]
        #
        # for s in strs:
        #     while s.find(prefix) != 0:
        #         prefix = prefix[0:len(prefix) - 1]
        #         if prefix == "":
        #             return prefix
        # return prefix


s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))


