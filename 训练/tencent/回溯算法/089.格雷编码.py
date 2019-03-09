"""
https://leetcode-cn.com/explore/interview/card/tencent/227/hui-su-suan-fa/946/

格雷编码
格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。

给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。格雷编码序列必须以 0 开头。

示例 1:

输入: 2
输出: [0,1,3,2]
解释:
00 - 0
01 - 1
11 - 3
10 - 2

对于给定的 n，其格雷编码序列并不唯一。
例如，[0,2,3,1] 也是一个有效的格雷编码序列。

00 - 0
10 - 2
11 - 3
01 - 1
示例 2:

输入: 0
输出: [0]
解释: 我们定义格雷编码序列必须以 0 开头。
     给定编码总位数为 n 的格雷编码序列，其长度为 2n。当 n = 0 时，长度为 20 = 1。
     因此，当 n = 0 时，其格雷编码序列为 [0]。
"""
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [i ^ (i >> 1) for i in range(1 << n)]
        
        # if n is 0:
        #     return [0]
        # elif n is 1:
        #     return [0, 1]
        #
        # def code_to_num(code: str):
        #     num = 0
        #     for digit in code:
        #         num = (num << 1) + (ord(digit) - ord('0'))
        #     return num
        #
        # def num_to_code(num: int):
        #     code = ""
        #     for i in range(n):
        #         code = str(num % 2) + code
        #         num = num >> 1
        #     return code
        #
        # def get_next_gray_code_list(code: str):
        #     result = []
        #     for i in range(len(code)):
        #         result.append(code[:i] + str(ord('1') - ord(code[i])) + code[i+1:])
        #     return result
        #
        # record = []
        # used_set = set()
        #
        # def search(code: str):
        #     if code in used_set:
        #         return
        #     else:
        #         used_set.add(code)
        #         record.append(code_to_num(code))
        #         for next_code in get_next_gray_code_list(code):
        #             search(next_code)
        #
        # search(num_to_code(0))
        # return record


print(Solution().grayCode(3))

