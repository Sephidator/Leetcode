# https://leetcode.com/problems/alien-dictionary/
#
# 269. Alien Dictionary
#
# There is a new alien language which uses the latin alphabet.
# However, the order among letters are unknown to you.
# You receive a list of non-empty words from the dictionary,
# where words are sorted lexicographically by the rules of this new language.
# Derive the order of letters in this language.
#
# Example 1:
#
# Input:
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
#
# Output: "wertf"
#
#
# Example 2:
#
# Input:
# [
#   "z",
#   "x"
# ]
#
# Output: "zx"
#
#
# Example 3:
#
# Input:
# [
#   "z",
#   "x",
#   "z"
# ]
#
# Output: ""
#
# Explanation: The order is invalid, so return "".
#
#
# Note:
#
# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.
from typing import List


class Node:
    def __init__(self, value, father):
        self.value = value
        self.father = father
        self.children = set()

# 拓扑排序
# https://www.cnblogs.com/lightwindy/p/8531872.html
# https://blog.csdn.net/qq508618087/article/details/50981000
# https://leetcode.com/problems/alien-dictionary/discuss/283823/Python-24ms-Topological-Sort-solution
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        in_degree, follow, res = {}, {}, ""

        # 使用拓扑排序
        # in_degree计算每个点的入度
        # follow计算每个点之后的点
        for word in words:
            for c in word:
                in_degree[c] = 0
                follow[c] = []

        # 因为是字典序排序，
        # 情况1：对于abc和abd两个单词，因为ac部分是一样的，而且abc在前，所以c在d的前面
        # 情况2：但是对于abc和abcde这两个单词，因为相同的abc去掉之后前一个单词没了，所以其实de可以是任何词，无法得到拓扑关系
        for i in range(1, len(words)):
            k, length = 0, min(len(words[i - 1]), len(words[i]))
            # 查找相同部分
            while k < length and words[i - 1][k] == words[i][k]:
                k += 1
            # 避免情况2
            if k != length:
                in_degree[words[i][k]] += 1
                follow[words[i - 1][k]].append(words[i][k])

        # 拓扑排序的最开头总是那些入度为0的点，zero_set保存入度为0的点
        # 找到一个入度为0的点之后，把它从in_degree中删掉
        zero_set = set()
        for char in in_degree:
            if in_degree[char] == 0:
                zero_set.add(char)
        for char in zero_set:
            in_degree.pop(char)

        # 对于某个入度为0的点，把它添加到结果中
        # 并且对于这个点后继的点，统统入度减少1
        # 当入度变成0的时候，这些后继的点也要从in_degree中移除，添加到zero_set中
        res = []
        while zero_set:
            char = zero_set.pop()
            res.append(char)
            for next_char in follow[char]:
                in_degree[next_char] -= 1
                if in_degree[next_char] == 0:
                    in_degree.pop(next_char)
                    zero_set.add(next_char)

        # 对于有环的情况，就会导致环上的所有点的入度均大于0
        # 这样在处理完所有入度为0的点之后，in_degree中仍然有点，但是无法移除
        # 这就像iOS中的循环饮用问题，ARC无法减小到0
        if in_degree:
            return ""
        else:
            return "".join(res)


s = Solution()
print(s.alienOrder([
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]))



