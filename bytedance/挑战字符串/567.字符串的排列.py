# https://leetcode-cn.com/explore/interview/card/bytedance/242/string/1016/
#
# 给定两个字符串s1和s2，写一个函数来判断s2是否包含s1的排列。
#
# 换句话说，第一个字符串的排列之一是第二个字符串的子串。
#
# 示例1:
#
# 输入: s1 = "ab"
# s2 = "eidbaooo"
# 输出: True
# 解释: s2
# 包含
# s1
# 的排列之一("ba").
#
# 示例2:
#
# 输入: s1 = "ab"
# s2 = "eidboaoo"
# 输出: False
#
# 注意：
#
# 输入的字符串只包含小写字母
# 两个字符串的长度都在[1, 10000]
# 之间

class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # 使用t1和t2分别保存"s1"和"s2子串"中各个字母的数量，相等的时候就可以返回True
        # t1可以直接得出，t2使用视窗的思想，不是对于每一个新的子串重新计算一遍，而是
        # 每次浏览一个新的字符，就看一下被抛弃的那个字符，只更新表中两个位置，而不是整张表
        # 这个方法还可以继续优化，比较两张表是否相等的时候不直接比，而用count保存相等字母的数量
        if len(s1) > len(s2):
            return False
        else:
            t1 = [0] * 26
            t2 = [0] * 26
            for index in range(len(s1)):
                t1[ord(s1[index]) - ord('a')] += 1
                t2[ord(s2[index]) - ord('a')] += 1

            count = 0
            for i in range(26):
                if t1[i] == t2[i]:
                    count += 1

            for i in range(len(s1), len(s2)):
                if count == 26:
                    return True
                else:
                    r = ord(s2[i]) - ord('a')
                    l = ord(s2[i - len(s1)]) - ord('a')
                    if l != r:
                        t2[r] += 1
                        if t2[r] == t1[r]:
                            count += 1
                        elif t2[r] == t1[r] + 1:
                            count -= 1

                        t2[l] -= 1
                        if t2[l] == t1[l]:
                            count += 1
                        elif t2[l] == t1[l] - 1:
                            count -= 1
            return count == 26

        # if len(s1) > len(s2):
        #     return False
        # else:
        #     t1 = [0] * 26
        #     t2 = [0] * 26
        #     for index in range(len(s1)):
        #         t1[ord(s1[index]) - 97] += 1
        #         t2[ord(s2[index]) - 97] += 1
        #
        #     for i in range(len(s1), len(s2)):
        #         if t1 == t2:
        #             return True
        #         else:
        #             t2[ord(s2[i]) - ord('a')] += 1
        #             t2[ord(s2[i - len(s1)]) - ord('a')] -= 1
        #     return t1 == t2


s = Solution()
# print(s.checkInclusion("hello", "ooolleoooleh"))


