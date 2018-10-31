# 72_编辑距离
# https://leetcode-cn.com/problems/edit-distance/description/
# https://github.com/youngwind/blog/issues/106
# http://www.cnblogs.com/ivanyb/archive/2011/11/25/2263356.html
#
# 给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
#
# 你可以对一个单词进行如下三种操作：
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
# 示例 1:
#
# 输入: word1 = "horse", word2 = "ros"
# 输出: 3
# 解释:
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 示例 2:
#
# 输入: word1 = "intention", word2 = "execution"
# 输出: 5
# 解释:
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        d = {(0, 0): 0}
        for a in range(len(word1)):
            d[a + 1, 0] = a + 1
        for b in range(len(word2)):
            d[0, b + 1] = b + 1

        for i in range(len(word1)):
            for j in range(len(word2)):
                temp = 0 if word1[i] == word2[j] else 1
                m1 = d[i, j + 1] + 1
                m2 = d[i + 1, j] + 1
                m3 = d[i, j] + temp
                d[i + 1, j + 1] = min(m1, m2, m3)

        return d[len(word1), len(word2)]

    def minDistance_recursion(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        def recursion(word1, word2, len1, len2):
            if len1 == 0:
                return len2
            elif len2 == 0:
                return len1
            else:
                temp = 0 if word1[len1-1] == word2[len2-1] else 1
                m1 = recursion(word1, word2, len1 - 1, len2) + 1
                m2 = recursion(word1, word2, len1, len2 - 1) + 1
                m3 = recursion(word1, word2, len1 - 1, len2 - 1) + temp
                return min(m1, m2, m3)

        return recursion(word1, word2, len(word1), len(word2))


s = Solution()
print(s.minDistance('123213', 'rewr123'))