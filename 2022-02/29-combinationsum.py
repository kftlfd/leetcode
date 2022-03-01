'''
Leetcode
39. Combination Sum (medium)
2022-02-17

Given an array of distinct integers candidates and a target integer 
target, return a list of all unique combinations of candidates where 
the chosen numbers sum to target. You may return the combinations in 
any order.

The same number may be chosen from candidates an unlimited number of 
times. Two combinations are unique if the frequency of at least one 
of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up 
to target is less than 150 combinations for the given input.
'''

from typing import List



# recursion and backtrack
# taken from
# https://leetcode.com/problems/combination-sum/discuss/1777309/Python-3-DFS-Recursion-Solution-and-Explanation

# Runtime: 71 ms, faster than 87.39% of Python3 online submissions for Combination Sum.
# Memory Usage: 13.9 MB, less than 87.78% of Python3 online submissions for Combination Sum.
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(candidates, target, start, curr_list, res):
            if target == 0:
                res.append(curr_list)
                return
            for i in range(start, len(candidates)):
                n = candidates[i]
                if n <= target:
                    backtrack(candidates, target-n, i, curr_list+[n], res)
                else: break
        
        candidates.sort()
        res = []
        backtrack(candidates, target, 0, [], res)        
        return res



tests = [
    [[2,3,6,7], 7],
    [[2,3,5], 8],
    [[2], 1]
]
solution = Solution()
for test in tests:
    print('test:', *test)
    print('out: ', solution.combinationSum(test[0], test[1]), '\n')
