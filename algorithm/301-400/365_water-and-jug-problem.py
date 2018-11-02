# 365. 水壶问题
# https://leetcode-cn.com/problems/water-and-jug-problem/description/
#
#
# 有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？
#
# 如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。
#
# 你允许：
#
# 装满任意一个水壶
# 清空任意一个水壶
# 从一个水壶向另外一个水壶倒水，直到装满或者倒空
# 示例 1: (From the famous "Die Hard" example)
#
# 输入: x = 3, y = 5, z = 4
# 输出: True
# 示例 2:
#
# 输入: x = 2, y = 6, z = 5
# 输出: False


class Solution:
    def canMeasureWater_mySolution_TOE(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        from math import gcd
        # sb: how much water small bottle can contain
        # bb: how much water big bottle can contain
        sb = min(x, y)
        bb = max(x, y)
        records = {}

        # sw: how much water in the small bottle
        # bw: how much water in the big bottle
        # occurred: whether the (sw, bw) situation occurred
        def dfs(sw, bw, occurred):
            if (sw, bw) in records:
                return records[sw, bw]
            elif (sw, bw) in occurred:
                records[sw, bw] = False
                return False
            elif sw == z or bw == z or sw + bw == z:
                records[sw, bw] = True
                # print(sw, bw)
                return True
            else:
                occurred.append((sw, bw))
                big_to_small = min(sb - sw, bw)
                small_to_big = min(sw, bb - bw)
                result = dfs(0, bw, occurred) or dfs(sw, 0, occurred) or \
                         dfs(sb, bw, occurred) or dfs(sw, bb, occurred) or \
                         dfs(sw + big_to_small, bw - big_to_small, occurred) or \
                         dfs(sw - small_to_big, bw + small_to_big, occurred)
                occurred.pop()
                records[sw, bw] = result
                # if result:
                #     print(sw, bw)
                return result

        if z == 0:
            return True
        elif sb == 0:
            return z == bb
        elif z > sb + bb:
            return False
        else:
            return dfs(0, 0, [])

    # 我发现：水壶问题可以转换成"是否存在整数解n1和n2，使得 n1*x + n2*y = z"
    # 这个规律是我发现的，具体的数学解释不知道，233
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        def have_integer_solution(num1, num2, result):
            from math import gcd
            return result % gcd(num1, num2) == 0

        if z == 0:
            return True
        elif x == 0 or y == 0:
            return z == max(x, y)
        elif z > x + y:
            return False
        else:
            return have_integer_solution(x, y, z)


s = Solution()
print(s.canMeasureWater(2, 6, 5))
