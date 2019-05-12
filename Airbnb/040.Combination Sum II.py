# https://leetcode.com/problems/combination-sum-ii/
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def combinations(candidates: List[int], target: int, pre_combination: List[int]) -> List[List[int]]:
            if not target:
                return [pre_combination]

            solutions = []
            for i, num in enumerate(candidates):
                # 重复的场合直接跳过， 这意味着对于[1, 1, 6, 7]匹配8的场合
                # 对于[1, 1, 6], 显然两个1都要用来匹配
                # 但是对于[1, 7]的场合，因为前一个1已经用过一次了，第二个1不必重复使用
                if i > 0 and num == candidates[i-1]:
                    continue
                if target >= num:
                    solutions.extend(combinations(candidates[i+1:], target - num, pre_combination + [num]))
                else:
                    break
            return solutions

        candidates.sort()
        return combinations(candidates, target, [])


s = Solution()
print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
