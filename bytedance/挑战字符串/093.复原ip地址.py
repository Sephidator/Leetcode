# https://leetcode-cn.com/explore/interview/card/bytedance/242/string/1044/
#
# 复原IP地址
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
#
# 示例:
#
# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid(s):
            if int(s) > 255:
                return False
            elif len(s) > len(str(int(s))):
                return False
            else:
                return True

        length = len(s)
        result = []
        if length <= 3:
            return result

        for cut1 in range(1, 4):
            for cut3 in range(length-1, length-4, -1):
                if cut3 - cut1 <= 1:
                    continue
                elif not is_valid(s[0:cut1]) or not is_valid(s[cut3:length]):
                    continue
                elif cut3 - cut1 >= 7:
                    continue
                else:
                    for cut2 in range(cut1 + 1, cut3):
                        if is_valid(s[cut1:cut2]) and is_valid(s[cut2:cut3]):
                            ip1 = s[0:cut1]
                            ip2 = s[cut1:cut2]
                            ip3 = s[cut2:cut3]
                            ip4 = s[cut3:length]
                            result.append(".".join([ip1, ip2, ip3, ip4]))
        return sorted(result)


s = Solution()
print(s.restoreIpAddresses("101023"))
