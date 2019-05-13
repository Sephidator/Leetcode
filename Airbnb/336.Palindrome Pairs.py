# https://leetcode.com/problems/palindrome-pairs/
# https://leetcode.com/problems/palindrome-pairs/discuss/79219/Python-solution~
#
# Given a list of unique words, find all pairs of distinct indices (i, j) in the given list,
# so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.
#
# Example 1:
#
# Input: ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
# Example 2:
#
# Input: ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]

from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_set = {}
        result = []
        for i in range(len(words)):
            word_set[words[i]] = i
        for i in range(len(words)):
            for j in range(len(words[i]) + 1):
                prefix = words[i][:j]
                suffix = words[i][j:]
                if prefix[::-1] in word_set and word_set[prefix[::-1]] != i and suffix == suffix[::-1]:
                    result.append([i, word_set[prefix[::-1]]])
                # j = 0 的场合，必有"abcd"必配"dcba"
                # 我在自己这边匹配一次后，对面又会匹配一次，为了避免重复，做出判断
                if j>0 and suffix[::-1] in word_set and word_set[suffix[::-1]] != i and prefix == prefix[::-1]:
                    result.append([word_set[suffix[::-1]], i])
        return result


        # def isPalindrome(a: int, b: int) -> bool:
        #     word = words[a] + words[b]
        #     half_len = len(word) // 2
        #     return word[:half_len] == word[:-(half_len+1):-1]
        #
        # result = []
        # for i in range(len(words)):
        #     for j in range(i+1, len(words)):
        #         if isPalindrome(i, j):
        #             result.append([i, j])
        #         if isPalindrome(j, i):
        #             result.append([j, i])
        # return result