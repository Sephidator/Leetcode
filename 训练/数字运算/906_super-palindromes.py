# https://leetcode-cn.com/problems/super-palindromes/description/
#
# 906.超级回文数
#
#
# 如果一个正整数自身是回文数，而且它也是一个回文数的平方，那么我们称这个数为超级回文数。
#
# 现在，给定两个正整数
# L
# 和
# R （以字符串形式表示），返回包含在范围[L, R]
# 中的超级回文数的数目。
#
#
#
# 示例：
#
# 输入：L = "4", R = "1000"
# 输出：4
# 解释：
# 4，9，121，以及
# 484
# 是超级回文数。
# 注意
# 676
# 不是一个超级回文数： 26 * 26 = 676，但是
# 26
# 不是回文数。
#
#
# 提示：
#
# 1 <= len(L) <= 18
# 1 <= len(R) <= 18
# L
# 和
# R
# 是表示[1, 10 ^ 18) 范围的整数的字符串。
# int(L) <= int(R)


# TMD 讨论区的家伙们都是打表的
class Solution:
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        # table = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004,
        #          100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004,
        #          404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004,
        #          1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201,
        #          1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321,
        #          1234567654321, 4000008000004, 4004009004004, 100000020000001, 100220141022001,
        #          102012040210201, 102234363432201, 121000242000121, 121242363242121, 123212464212321,
        #          123456787654321, 400000080000004, 10000000200000001, 10002000300020001, 10004000600040001,
        #          10020210401202001, 10022212521222001, 10024214841242001, 10201020402010201,
        #          10203040504030201, 10205060806050201, 10221432623412201, 10223454745432201,
        #          12100002420000121, 12102202520220121, 12104402820440121, 12122232623222121,
        #          12124434743442121, 12321024642012321, 12323244744232321, 12343456865434321,
        #          12345678987654321, 40000000800000004, 40004000900040004]
        # l_num = int(L)
        # r_num = int(R)
        # n = 0
        # for i in table:
        #     if i < l_num:
        #         continue
        #     elif i > r_num:
        #         break
        #     else:
        #         n = n + 1
        # return n

        from math import sqrt, floor, ceil

        def is_palindrome(number):
            string = str(number)
            return string == string[::-1]

        def set_to_palindrome(number):
            string = str(number)
            replace_len = len(string) // 2
            preserved_len = len(string) - replace_len
            palindrome = int(string[:preserved_len] + string[:replace_len][::-1])
            return palindrome

        def next_palindrome(number, is_palin):
            if is_palin:
                string = str(number)
                replace_len = len(string) // 2
                preserved_len = len(string) - replace_len
                new_number = int(string[:preserved_len] + replace_len * "9") + 1
                return set_to_palindrome(new_number)
            else:
                palin_num = set_to_palindrome(number)
                if palin_num < number:
                    palin_num = next_palindrome(palin_num, True)
                return palin_num

        l_num = int(L)
        r_num = int(R)
        n = 0
        k = int(ceil(sqrt(l_num)))
        while k <= int(floor(sqrt(r_num))):
            if is_palindrome(k):
                if is_palindrome(k * k):
                    n = n + 1
                    print(k*k)
                k = next_palindrome(k, True)
            else:
                k = next_palindrome(k, False)
        return n


import time
start = (int(round(time.time() * 1000)))  # 毫秒级时间戳
so = Solution()
print(so.superpalindromesInRange("1", "999999999999999999"))
end = (int(round(time.time() * 1000)))
print(end - start)
