# https://leetcode.com/problems/combination-sum-ii/
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def combinations(candidates: List[int], target: int, pre_combination: List[int]) -> List[List[int]]:
            if not target:
                return [pre_combination]

            solutions = []
            for i, num in enumerate(candidates):
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
