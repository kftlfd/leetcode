"""
Leetcode
40. Combination Sum II
Medium
2024-08-13

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

 

Constraints:

    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30
"""

from typing import List


class Solution:
    """
    Time Limit Exceeded
    """

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        n = len(candidates)
        ans = []
        seen = set()

        def add(nums: List[int]):
            nums_hash = str(nums)
            if nums_hash not in seen:
                ans.append(nums[:])
                seen.add(nums_hash)

        def dfs(idx: int, nums: List[int], cur_sum: int):
            if cur_sum == target:
                add(nums)
                return

            if cur_sum > target or idx >= n:
                return

            # pick
            cur_num = candidates[idx]
            nums.append(cur_num)
            dfs(idx + 1, nums, cur_sum + cur_num)
            nums.pop()

            # omit
            dfs(idx + 1, nums, cur_sum)

        dfs(0, [], 0)
        return ans


class Solution1:
    """
    leetcode solution: Backtracking
    Runtime: 69 ms, faster than 34.85% of Python3 online submissions for Combination Sum II.
    Memory Usage: 16.5 MB, less than 92.14% of Python3 online submissions for Combination Sum II.
    """

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()
        self.backtrack(candidates, target, 0, [], answer)
        return answer

    def backtrack(self, candidates, target, totalIdx, path, answer):
        if target < 0:
            return  # backtracking
        if target == 0:
            answer.append(path)
            return  # end
        for i in range(totalIdx, len(candidates)):
            if i > totalIdx and candidates[i] == candidates[i - 1]:
                continue
            self.backtrack(
                candidates,
                target - candidates[i],
                i + 1,
                path + [candidates[i]],
                answer,
            )
