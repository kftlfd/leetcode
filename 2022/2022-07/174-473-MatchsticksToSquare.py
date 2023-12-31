"""
Leetcode
473. Matchsticks to Square (medium)
2022-07-12

You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

Example 1:
Input: matchsticks = [1,1,2,2,2]
Output: true

Example 2:
Input: matchsticks = [3,3,3,3,4]
Output: false
"""

from typing import List


# https://leetcode.com/problems/matchsticks-to-square/discuss/1273708/Python-dp-on-subsets-explained
# Runtime: 1537 ms, faster than 60.00% of Python3 online submissions for Matchsticks to Square.
# Memory Usage: 64.9 MB, less than 6.78% of Python3 online submissions for Matchsticks to Square.
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        nums = matchsticks
        N = len(nums)
        basket, rem = divmod(sum(nums), 4)
        if rem or max(nums) > basket:
            return False

        @lru_cache(None)
        def dfs(mask):
            if mask == 0:
                return 0
            for j in range(N):
                if mask & 1 << j:
                    neib = dfs(mask ^ 1 << j)
                    if neib >= 0 and neib + nums[j] <= basket:
                        return (neib + nums[j]) % basket
            return -1

        return dfs((1 << N) - 1) == 0


s = Solution()
tests = [
    [1, 1, 2, 2, 2],
    [3, 3, 3, 3, 4],
]
for t in tests:
    print(t)
    print(s.makesquare(t))
    print()
